# 04 · Compliance & Trust (Healthcare/Wellness)

This is the document that separates a credible health agency from a generalist. Compliance
isn't a checkbox — it's a competitive advantage and a legal necessity. **Always confirm
specifics with the client's legal counsel and compliance officer before launch.**

> Disclaimer: This is practical guidance for web/marketing teams, not legal advice.

---

## 1. Data privacy & PHI

### HIPAA (US) — when it applies
HIPAA applies if the client is a "covered entity" (or business associate) and the site
handles **Protected Health Information (PHI)** — e.g., appointment requests with health
details, patient portals, intake forms, chat that collects symptoms.

Practical web requirements when PHI is involved:
- **Sign a BAA** (Business Associate Agreement) with every vendor touching PHI: hosting,
  forms, booking, analytics, email, chat, CRM. No BAA → don't send PHI there.
- **Encrypt** data in transit (HTTPS/TLS) and at rest.
- **Avoid leaking PHI to ad/analytics trackers.** Standard Google Analytics, Meta Pixel,
  etc. on pages that collect PHI is a known HIPAA risk. Use HIPAA-eligible/compliant
  configurations, server-side tagging, or keep trackers off PHI pages.
- **Access controls & audit logs** for portals; strong auth.
- **Minimum necessary:** only collect what you need on forms.
- **Breach plan & retention policy** documented.

### GDPR / UK GDPR (EU/UK)
- Health data is "special category" data → needs explicit, granular consent + lawful basis.
- Cookie consent **before** non-essential trackers fire (true opt-in, not pre-ticked).
- Data subject rights (access, erasure), DPA with processors, records of processing.

### Other regimes
- **CCPA/CPRA** (California), **PIPEDA** (Canada), **Australian Privacy Act**, plus
  local/state medical privacy laws. Confirm jurisdictions during discovery (doc 00).

### Required legal pages
- Privacy Policy · Terms of Use · Cookie/consent notice · Accessibility Statement
- HIPAA Notice of Privacy Practices (US covered entities) · medical disclaimer

---

## 2. Accessibility (ADA / WCAG) — legal + ethical

Healthcare serves people with disabilities, older adults, and people in distress.
Accessibility is **required** (ADA in the US; EN 301 549/European Accessibility Act in EU)
and is a frequent source of lawsuits.

**Target: WCAG 2.2 Level AA.** Core requirements:
- Color contrast ≥ 4.5:1 (text); don't rely on color alone.
- Full keyboard navigation; visible focus states.
- Alt text for informative images; proper heading structure.
- Labeled, accessible forms with clear error messages.
- Captions/transcripts for video; no auto-playing audio.
- Accessible booking flow (critical conversion path).
- Test with screen readers (NVDA/VoiceOver) + automated tools (axe, Lighthouse).
- Publish an **Accessibility Statement** with a contact for issues.

---

## 3. E-E-A-T & YMYL (Google quality + SEO)

Health sites are **YMYL — "Your Money or Your Life"** — held to Google's highest quality
bar. Rankings and trust depend on **E-E-A-T** (Experience, Expertise, Authoritativeness,
Trustworthiness):

- **Named authors with real credentials** on health content (no anonymous articles).
- **Medical review** byline ("Medically reviewed by Dr. X, [credentials], [date]").
- **Cite reputable sources** (peer-reviewed, .gov/.edu, major health bodies).
- **Last-updated dates** + periodic content review (freshness for YMYL).
- **Accurate, non-sensational** claims; clear separation of fact vs. opinion.
- Strong **About**, contact, and organizational transparency.

---

## 4. Advertising & marketing claims

### Truthful claims (FTC / ASA / local equivalents)
- Health claims must be **truthful and substantiated** by competent evidence.
- **No guaranteed cures or outcomes.** Avoid "miracle", "cure", "100% effective".
- Disclose material connections (sponsorships, affiliate, paid endorsements).
- Testimonials must be genuine, typical (or disclosed as atypical), and verifiable.

### Platform ad-policy restrictions (plan for these in doc 06)
- **Google Ads:** healthcare & medicines policies; certification/restrictions for some
  categories; limits on personalized/health-audience targeting.
- **Meta Ads:** restricts targeting based on health conditions; bans certain claims and
  before/after framing in some health/wellness verticals; landing-page review.
- **TikTok/others:** strict on health/medical and supplement claims.
> Build ads + landing pages knowing these limits up front to avoid disapprovals.

### Testimonials & reviews (profession-specific)
- Some professions/jurisdictions **restrict or ban** patient testimonials (e.g., certain
  medical/dental boards, GDC in the UK historically limited some uses). Confirm in discovery.
- Get **written consent** + (where relevant) HIPAA authorization to use patient stories,
  photos, or before/after images. Never expose PHI without authorization.

---

## 5. Trust signals to build in (turns compliance into conversion)
- Credentials, licenses, board certifications (verifiable)
- Affiliations/accreditations (hospitals, associations) + logos (with permission)
- Security/trust badges, HTTPS, clear privacy reassurance near forms
- Real staff/facility photography; transparent pricing & process
- Visible reviews/ratings (compliant) and a clear complaints/contact path

---

## Pre-launch compliance checklist
- [ ] Jurisdictions & regimes confirmed (HIPAA/GDPR/CCPA/local)
- [ ] BAAs signed with all PHI-touching vendors (if applicable)
- [ ] No PHI leaking to non-compliant trackers; consent gating in place
- [ ] Legal pages live (privacy, terms, cookie, accessibility, HIPAA notice, disclaimers)
- [ ] WCAG 2.2 AA audit passed (automated + manual + screen reader)
- [ ] Health content has authors + medical review + sources + dates
- [ ] Ad claims reviewed; testimonial consents obtained
- [ ] Legal/compliance sign-off recorded (who + date)
