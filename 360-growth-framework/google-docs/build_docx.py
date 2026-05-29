#!/usr/bin/env python3
"""
Convert the consolidated framework Markdown into a native .docx file using only
the Python standard library. A .docx is an OOXML zip package, so we write the
XML parts by hand. Supports: Title/H1/H2/H3 headings, paragraphs, bold runs,
bullet lists, and bordered tables with shaded header rows.

Usage: python3 build_docx.py input.md output.docx
"""
import sys
import re
import zipfile

# ----------------------------- helpers -----------------------------------

def esc(text):
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;")
                .replace('"', "&quot;"))

LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def resolve_links(text):
    def repl(m):
        label, url = m.group(1), m.group(2)
        if url.startswith("http"):
            return f"{label} ({url})"
        return label
    return LINK_RE.sub(repl, text)

def make_runs(text):
    """Return run XML for inline text, handling **bold** and links/backticks."""
    text = resolve_links(text).replace("`", "")
    parts = text.split("**")
    out = []
    for i, part in enumerate(parts):
        if part == "":
            continue
        bold = (i % 2 == 1)
        rpr = "<w:rPr><w:b/></w:rPr>" if bold else ""
        out.append(f'<w:r>{rpr}<w:t xml:space="preserve">{esc(part)}</w:t></w:r>')
    if not out:
        out.append('<w:r><w:t xml:space="preserve"></w:t></w:r>')
    return "".join(out)

def para(text, style=None):
    ppr = f'<w:pPr><w:pStyle w:val="{style}"/></w:pPr>' if style else ""
    return f"<w:p>{ppr}{make_runs(text)}</w:p>"

def bullet(text):
    ppr = ('<w:pPr><w:numPr><w:ilvl w:val="0"/><w:numId w:val="1"/></w:numPr>'
           '<w:spacing w:after="60"/></w:pPr>')
    return f"<w:p>{ppr}{make_runs(text)}</w:p>"

def empty():
    return '<w:p/>'

# ----------------------------- table --------------------------------------

PAGE_WIDTH = 9360  # usable width in dxa (Letter, 1in margins)

def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip() for c in line.split("|")]

def is_separator(line):
    cells = split_row(line)
    if not cells:
        return False
    return all(re.fullmatch(r":?-{2,}:?", c.strip()) for c in cells if c.strip() != "") and any(
        set(c.strip()) <= set(":-") and "-" in c for c in cells)

def table_xml(rows):
    ncols = max(len(r) for r in rows)
    colw = PAGE_WIDTH // ncols
    grid = "".join(f'<w:gridCol w:w="{colw}"/>' for _ in range(ncols))
    borders = ("<w:tblBorders>"
               '<w:top w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
               '<w:left w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
               '<w:bottom w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
               '<w:right w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
               '<w:insideH w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
               '<w:insideV w:val="single" w:sz="4" w:space="0" w:color="BFBFBF"/>'
               "</w:tblBorders>")
    tblpr = (f'<w:tblPr><w:tblW w:w="{PAGE_WIDTH}" w:type="dxa"/>'
             f'<w:tblLayout w:type="fixed"/>{borders}'
             '<w:tblLook w:val="04A0" w:firstRow="1" w:lastRow="0" '
             'w:firstColumn="0" w:lastColumn="0" w:noHBand="0" w:noVBand="1"/></w:tblPr>')
    out = [f"<w:tbl>{tblpr}<w:tblGrid>{grid}</w:tblGrid>"]
    for ri, row in enumerate(rows):
        cells = list(row) + [""] * (ncols - len(row))
        out.append("<w:tr>")
        for c in cells:
            shd = '<w:shd w:val="clear" w:color="auto" w:fill="D9E2F3"/>' if ri == 0 else ""
            tcpr = f'<w:tcPr><w:tcW w:w="{colw}" w:type="dxa"/>{shd}</w:tcPr>'
            # header cells bold
            cell_text = f"**{c}**" if (ri == 0 and c) else c
            pcontent = make_runs(cell_text) if c != "" else '<w:r><w:t></w:t></w:r>'
            ppr = '<w:pPr><w:spacing w:after="0"/></w:pPr>'
            out.append(f"<w:tc>{tcpr}<w:p>{ppr}{pcontent}</w:p></w:tc>")
        out.append("</w:tr>")
    out.append("</w:tbl>")
    out.append(empty())
    return "".join(out)

# ----------------------------- parser -------------------------------------

def parse(md):
    lines = md.split("\n")
    body = []
    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]
        stripped = line.strip()
        if stripped == "":
            i += 1
            continue
        # tables
        if stripped.startswith("|"):
            tbl = [line]
            j = i + 1
            while j < n and lines[j].strip().startswith("|"):
                tbl.append(lines[j])
                j += 1
            rows = [split_row(t) for t in tbl]
            # drop separator row(s)
            rows = [r for t, r in zip(tbl, rows) if not is_separator(t)]
            body.append(table_xml(rows))
            i = j
            continue
        # headings
        if stripped.startswith("#### "):
            body.append(para(stripped[5:], "Heading3"))
            i += 1; continue
        if stripped.startswith("### "):
            body.append(para(stripped[4:], "Heading2"))
            i += 1; continue
        if stripped.startswith("## "):
            body.append(para(stripped[3:], "Heading1"))
            i += 1; continue
        if stripped.startswith("# "):
            body.append(para(stripped[2:], "Title"))
            i += 1; continue
        # blockquote
        if stripped.startswith("> "):
            body.append(para(stripped[2:], "Quote"))
            i += 1; continue
        # bullets
        if stripped.startswith("- ") or stripped.startswith("* "):
            body.append(bullet(stripped[2:]))
            i += 1; continue
        # paragraph: gather consecutive plain lines
        buf = [stripped]
        j = i + 1
        while j < n:
            s = lines[j].strip()
            if (s == "" or s.startswith("|") or s.startswith("#")
                    or s.startswith("- ") or s.startswith("* ") or s.startswith("> ")):
                break
            buf.append(s)
            j += 1
        body.append(para(" ".join(buf)))
        i = j
    return "".join(body)

# ----------------------------- package parts ------------------------------

CONTENT_TYPES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
<Default Extension="xml" ContentType="application/xml"/>
<Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
<Override PartName="/word/styles.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.styles+xml"/>
<Override PartName="/word/numbering.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.numbering+xml"/>
</Types>'''

RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
</Relationships>'''

DOC_RELS = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/styles" Target="styles.xml"/>
<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/numbering" Target="numbering.xml"/>
</Relationships>'''

STYLES = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:styles xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:docDefaults><w:rPrDefault><w:rPr><w:rFonts w:ascii="Calibri" w:hAnsi="Calibri" w:cs="Calibri"/><w:sz w:val="22"/><w:szCs w:val="22"/></w:rPr></w:rPrDefault>
<w:pPrDefault><w:pPr><w:spacing w:after="140" w:line="276" w:lineRule="auto"/></w:pPr></w:pPrDefault></w:docDefaults>
<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>
<w:style w:type="paragraph" w:styleId="Title"><w:name w:val="Title"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:before="240" w:after="240"/></w:pPr><w:rPr><w:b/><w:sz w:val="52"/><w:szCs w:val="52"/><w:color w:val="1F3864"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading1"><w:name w:val="heading 1"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="360" w:after="120"/><w:outlineLvl w:val="0"/></w:pPr><w:rPr><w:b/><w:sz w:val="32"/><w:szCs w:val="32"/><w:color w:val="2F5496"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading2"><w:name w:val="heading 2"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="240" w:after="80"/><w:outlineLvl w:val="1"/></w:pPr><w:rPr><w:b/><w:sz w:val="26"/><w:szCs w:val="26"/><w:color w:val="2F5496"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Heading3"><w:name w:val="heading 3"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:keepNext/><w:spacing w:before="200" w:after="60"/><w:outlineLvl w:val="2"/></w:pPr><w:rPr><w:b/><w:sz w:val="24"/><w:szCs w:val="24"/><w:color w:val="1F3864"/></w:rPr></w:style>
<w:style w:type="paragraph" w:styleId="Quote"><w:name w:val="Quote"/><w:basedOn w:val="Normal"/><w:next w:val="Normal"/><w:qFormat/><w:pPr><w:spacing w:before="120" w:after="120"/><w:ind w:left="720"/></w:pPr><w:rPr><w:i/><w:color w:val="595959"/></w:rPr></w:style>
</w:styles>'''

NUMBERING = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:numbering xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
<w:abstractNum w:abstractNumId="0"><w:multiLevelType w:val="hybridMultilevel"/>
<w:lvl w:ilvl="0"><w:start w:val="1"/><w:numFmt w:val="bullet"/><w:lvlText w:val="&#8226;"/><w:lvlJc w:val="left"/><w:pPr><w:ind w:left="720" w:hanging="360"/></w:pPr><w:rPr><w:rFonts w:ascii="Symbol" w:hAnsi="Symbol" w:hint="default"/></w:rPr></w:lvl>
</w:abstractNum>
<w:num w:numId="1"><w:abstractNumId w:val="0"/></w:num>
</w:numbering>'''

DOC_OPEN = ('<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
            '<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">'
            '<w:body>')
SECTPR = ('<w:sectPr><w:pgSz w:w="12240" w:h="15840"/>'
          '<w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" '
          'w:header="720" w:footer="720" w:gutter="0"/></w:sectPr>')
DOC_CLOSE = "</w:body></w:document>"


def main():
    src, dst = sys.argv[1], sys.argv[2]
    with open(src, "r", encoding="utf-8") as f:
        md = f.read()
    body = parse(md)
    document = DOC_OPEN + body + SECTPR + DOC_CLOSE
    with zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("[Content_Types].xml", CONTENT_TYPES)
        z.writestr("_rels/.rels", RELS)
        z.writestr("word/_rels/document.xml.rels", DOC_RELS)
        z.writestr("word/styles.xml", STYLES)
        z.writestr("word/numbering.xml", NUMBERING)
        z.writestr("word/document.xml", document)
    print(f"Wrote {dst}")


if __name__ == "__main__":
    main()
