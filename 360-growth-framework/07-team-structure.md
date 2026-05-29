# 07 — Internal Team Structure by Phase

A 360° firm needs an org design that delivers a *single relationship* to the client
while keeping *deep specialist capability* inside. The answer is a **pod + practice
matrix**: client-facing pods own the relationship; specialist practices own the craft.

---

## 7.1 The Operating Model: Pods × Practices

```mermaid
flowchart TB
    subgraph PODS["CLIENT PODS (own the relationship & outcomes)"]
        POD1["Growth Pod A"]
        POD2["Growth Pod B"]
        POD3["Growth Pod C"]
    end
    subgraph PRACTICES["SPECIALIST PRACTICES (own the craft & quality)"]
        PR1["Strategy"]
        PR2["Brand & Creative"]
        PR3["Web & Tech"]
        PR4["Marketing"]
        PR5["Sales/CRM"]
        PR6["CX & Ops"]
        PR7["Data & AI"]
        PR8["Finance & Legal"]
    end
    subgraph SHARED["SHARED SERVICES (run the firm)"]
        REVOPS["RevOps / PMO"]
        TALENT["Talent / L&D"]
        FINOPS["Finance / Admin"]
    end
    PODS <--> PRACTICES
    PRACTICES --> SHARED
    PODS --> SHARED
```

- **Pods** are cross-functional, client-facing teams led by a Growth Partner Lead.
  They own the client roadmap, retention, and results across all phases.
- **Practices** are the centers of excellence. Specialists "live" in a practice
  (for craft, standards, and career growth) and are "deployed" into pods.
- **Shared services** (RevOps/PMO, Talent, Finance) keep the machine running.

> This is how firms stay integrated *and* deep: the client feels one team (the pod),
> while quality is guaranteed by the practices behind it.

---

## 7.2 Core Roles

| Role | Owns | Sits in |
|------|------|---------|
| **Growth Partner Lead (Account Lead)** | The client relationship, roadmap, retention, revenue | Pod |
| **Project / Delivery Manager** | Timelines, scope, resourcing, quality of delivery | Pod / PMO |
| **Strategist** | Insight, positioning, roadmap logic | Strategy practice |
| **Creative Director + designers** | Brand, creative, UX | Brand practice |
| **Web/Tech leads + developers** | Sites, apps, infrastructure, automation | Web/Tech practice |
| **Marketing leads + specialists** | SEO, paid, content, social, offline | Marketing practice |
| **Sales/CRM specialist (RevOps)** | Funnels, CRM, pipeline, CRO | Sales practice |
| **CX / Ops specialist** | Support, loyalty, SOPs, ERP | CX & Ops practice |
| **Data analyst / engineer** | Dashboards, attribution, insight, AI | Data practice |
| **Finance/Legal partners** | Compliance, budgeting, fundraising | Finance practice (often partly external) |

---

## 7.3 Which Team Leads Each Phase

The pod is constant; the **lead practice rotates** as the client moves through phases.

```mermaid
flowchart LR
    P1["P1 Discovery\nLEAD: Strategy"] --> P2["P2 Foundation\nLEAD: Brand + Legal/Ops"]
    P2 --> P3["P3 Digital\nLEAD: Web/Tech"]
    P3 --> P4["P4 Launch\nLEAD: Marketing + Sales"]
    P4 --> P5["P5 Operate\nLEAD: CX + Ops + Data"]
    P5 --> P6["P6 Scale\nLEAD: Growth + Perf + Finance"]
    P6 --> P7["P7 Transform\nLEAD: Innovation + Strategy + Data"]
```

| Phase | Lead practice | Heavily involved | On standby |
|-------|---------------|------------------|------------|
| 1 Discovery | Strategy | Data, Finance, Brand | — |
| 2 Foundation | Brand + Legal/Ops | Web/Tech, Strategy | Marketing |
| 3 Digital | Web/Tech | Brand, Marketing, Automation | Sales |
| 4 Launch | Marketing + Sales | Brand, PR, Web/Tech, Data | CX |
| 5 Operate/Retain | CX + Ops + Data | Marketing, Automation, Tech | Strategy |
| 6 Scale | Strategy/Growth + Performance Mktg + Finance | Tech, Data, Ops | Brand |
| 7 Transform | Innovation + Strategy + Data | All practices | — |

> Throughout, the **Growth Partner Lead stays the same person**. Continuity of
> relationship is the asset; specialist leadership rotates underneath it.

---

## 7.4 The RACI for Cross-Functional Work

To prevent the classic "who owns this?" failure in integrated delivery:

| Activity | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Client roadmap & retention | Growth Partner Lead | Pod Director | Practice leads | Client |
| Project delivery | Delivery Manager | Growth Partner Lead | Specialists | Client |
| Craft quality / standards | Specialists | Practice lead | Delivery Manager | Pod |
| Data integrity / reporting | Data analyst | RevOps lead | All practices | Client |
| Cross-sell / new proposals | Growth Partner Lead | Pod Director | Strategy + Finance | — |

---

## 7.5 Scaling the Org (how headcount grows with the firm)

```mermaid
flowchart LR
    S1["Stage 1: Boutique\nGeneralists + freelancers\n1 blended pod"] --> S2["Stage 2: Growing\nDefined practices\n2-3 pods + PMO"]
    S2 --> S3["Stage 3: Established\nFull practices\nMultiple pods + RevOps"]
    S3 --> S4["Stage 4: Scaled\nPractice P&Ls\nPods by segment/industry\nPartner network"]
```

| Stage | Team shape | Capacity model |
|-------|-----------|----------------|
| **Boutique** | Generalists wear multiple hats; partners for legal/specialist gaps | Freelance + contractor flex |
| **Growing** | Practices forming; first dedicated PMO/RevOps | Core team + vetted freelancer bench |
| **Established** | Full practices, multiple pods, defined career ladders | Mostly in-house + specialist partners |
| **Scaled** | Practices run as P&Ls; pods specialized by industry/segment | In-house core + partner network + offshore delivery |

---

## 7.6 The Partner / Vendor Network (the "virtual" 360°)

No firm builds *everything* in-house on day one. A managed partner network lets you
offer the full 360° immediately while protecting margin and quality:

| Capability | Build in-house when… | Partner when… |
|---|---|---|
| Legal / compliance | Rarely (regulated) | Almost always — white-label legal partners |
| Specialized dev (apps, AI) | Recurring demand justifies it | Spiky / niche demand |
| Production (video, print, OOH) | High volume | Project-based |
| Niche marketing (PR, influencers) | Core to your positioning | Long-tail needs |

> **Rule:** the client always experiences *one firm*. Whether a capability is
> in-house or partner is our operational concern, never their problem. The Growth
> Partner Lead and shared systems (`08`, `09`) make the seams invisible.
