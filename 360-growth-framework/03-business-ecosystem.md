# 03 — The Visual Business Ecosystem

This document visualizes the whole company as a connected ecosystem: the client at
the center, service lines orbiting them, a shared data core binding everything, and
the lifecycle flywheel driving recurring growth.

> All diagrams use Mermaid, which renders natively on GitHub. View this file on
> GitHub (or any Mermaid-enabled viewer) to see the visuals.

---

## 3.1 The Ecosystem Overview — Client at the Center

```mermaid
flowchart TB
    subgraph CORE[" "]
        CLIENT(("CLIENT\nGrowth Partner\nRelationship"))
        DATA[["Shared Data & CRM Core\n(single source of truth)"]]
        CLIENT --- DATA
    end

    STRAT["Strategy &\nConsulting"]
    BRAND["Branding &\nCreative"]
    WEB["Web &\nTechnology"]
    MKT["Marketing &\nGrowth"]
    SALES["Sales & CRM"]
    CX["Customer\nExperience"]
    OPS["Operations"]
    FIN["Finance &\nLegal"]
    INNO["Innovation\n& AI"]

    CLIENT --- STRAT
    CLIENT --- BRAND
    CLIENT --- WEB
    CLIENT --- MKT
    CLIENT --- SALES
    CLIENT --- CX
    CLIENT --- OPS
    CLIENT --- FIN
    CLIENT --- INNO

    STRAT -.feeds.-> DATA
    BRAND -.feeds.-> DATA
    WEB -.feeds.-> DATA
    MKT -.feeds.-> DATA
    SALES -.feeds.-> DATA
    CX -.feeds.-> DATA
    OPS -.feeds.-> DATA
    FIN -.feeds.-> DATA
    INNO -.feeds.-> DATA
```

**Reading it:** the client is the hub. Nine service lines orbit and serve them. A
shared data + CRM core sits beneath the relationship — every service both feeds it
and draws from it. That core is what makes us *integrated*, not just *full-service*.

---

## 3.2 The Growth Flywheel

The ecosystem is powered by a flywheel: each turn makes the next turn easier and
cheaper, because data, brand equity, and trust compound.

```mermaid
flowchart LR
    A["Insight\n(research + data)"] --> B["Brand & Presence\n(identity + digital)"]
    B --> C["Demand\n(marketing + sales)"]
    C --> D["Experience\n(CX + operations)"]
    D --> E["Retention & LTV\n(loyalty + analytics)"]
    E --> F["Scale & Expansion\n(growth + finance)"]
    F --> G["Reinvestment\n(innovation + new ventures)"]
    G --> A
```

> Each stage produces an asset the next stage consumes: insight → assets → customers
> → data → loyalty → capital → new insight. **Momentum is the moat.**

---

## 3.3 The Three Layers of the Ecosystem

```mermaid
flowchart TB
    subgraph L1["LAYER 1 — Client Experience (front stage)"]
        ACC["Single Account Team / Growth Partner Lead"]
        ROADMAP["360° Growth Roadmap"]
        DASH["One Client Dashboard"]
    end
    subgraph L2["LAYER 2 — Service Delivery (back stage)"]
        SVC["9 Service Lines\nStrategy · Brand · Web/Tech · Marketing · Sales · CX · Ops · Finance/Legal · Innovation"]
    end
    subgraph L3["LAYER 3 — Shared Infrastructure (foundation)"]
        CRM["CRM + Data Warehouse"]
        PM["Project & Workflow System"]
        KB["Knowledge Base / SOP Library"]
        AUTO["Automation & AI Layer"]
    end
    L1 --> L2 --> L3
    L3 -. powers .-> L1
```

| Layer | Purpose | Owner |
|-------|---------|-------|
| **1 — Client Experience** | The single, seamless relationship the client feels | Account / Growth Partner Lead |
| **2 — Service Delivery** | The specialist teams that do the work | Service-line directors |
| **3 — Shared Infrastructure** | The data, tools, automation, and SOPs that connect everything | Operations / RevOps |

---

## 3.4 The Unified Digital Funnel as One Ecosystem

```mermaid
flowchart LR
    subgraph AWARE["Awareness"]
        SEO["SEO / Content"]
        PAIDS["Paid Social"]
        PAIDSEARCH["Paid Search"]
        VIDEO["Video / YouTube"]
        SOCIAL["Organic Social"]
        DPR["Digital PR / Influencer"]
    end
    subgraph CONSIDER["Consideration"]
        W["Website / App"]
        REVIEWS["Reviews / Reputation"]
        RETARGET["Retargeting"]
    end
    subgraph CONVERT["Conversion"]
        ECOM["E-commerce checkout"]
        LP["Landing pages / CRO"]
        MKTPLACE["Marketplaces"]
    end
    subgraph KEEP["Retention & Advocacy"]
        EMAIL["Email / SMS"]
        LOYALTY["Loyalty / referrals"]
        SUPPORT["Support / CX"]
        COMMUNITY["Online community"]
    end
    AWARE --> CONSIDER --> CONVERT --> KEEP
    KEEP -.advocacy fuels awareness.-> AWARE
    W -. data .-> HUB[["Unified Customer Profile"]]
    ECOM -. data .-> HUB
    EMAIL -. data .-> HUB
    MKTPLACE -. data .-> HUB
```

The point: **every digital channel writes into the same customer profile**, tied
together by pixels, UTMs, and CRM IDs. One funnel, one profile, one attribution
model — no channel runs in a silo. Full detail in
[`05`](05-digital-channel-strategy.md).

---

## 3.5 The Service Constellation (what we sell, grouped)

```mermaid
mindmap
  root((360° Partner))
    Strategy
      Business consulting
      Feasibility & research
      Growth & expansion strategy
      Transformation
    Brand & Creative
      Identity & guidelines
      Social & ad creative
      Photography & video
      UI/UX
    Web & Technology
      Websites & e-commerce
      Apps
      Hosting & maintenance
      Scalable infrastructure
    Marketing
      SEO & content
      Paid media
      Influencer & digital PR
      Email & lifecycle
    Revenue
      Sales enablement
      CRM & pipeline
      CRO
    Customer & Ops
      Helpdesk & loyalty
      ERP & inventory
      SOPs & training
    Data & AI
      Analytics & dashboards
      Predictive intelligence
      Automation
      AI integration
    Finance & Legal
      Registration & compliance
      Budgeting & forecasting
      Fundraising
```

---

## 3.6 How the Ecosystem Creates Lock-In (Healthy, Value-Based)

```mermaid
flowchart LR
    MORE_SERVICES["More connected services"] --> MORE_DATA["More shared data"]
    MORE_DATA --> BETTER_RESULTS["Better, faster results"]
    BETTER_RESULTS --> MORE_TRUST["More trust"]
    MORE_TRUST --> MORE_SERVICES
    BETTER_RESULTS --> HIGHER_LTV["Higher client LTV"]
```

Lock-in here is *earned*, not contractual: the more of the ecosystem a client uses,
the richer their shared data, the better our results, the deeper the trust — which
naturally pulls in more services. This loop is the commercial heart of the model and
is operationalized in [`06 — Client Retention Model`](06-client-retention-model.md).
