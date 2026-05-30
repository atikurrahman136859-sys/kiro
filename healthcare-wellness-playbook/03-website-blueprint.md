# 03 · Website Blueprint (IA, Content & UI/UX)

The architecture, page-by-page outline, content plan, and UI/UX strategy that turn the
positioning (02) into a buildable, conversion-focused website.

---

## Part A — Information Architecture (Sitemap)

Recommended baseline sitemap for a healthcare/wellness site:

```
Home
About
  ├─ Our Team / Providers (with credentials)
  ├─ Our Approach / Philosophy
  └─ Facility / Tour
Services (hub)
  ├─ Service A (detail page)
  ├─ Service B (detail page)
  └─ Service C (detail page)
Conditions / Treatments (optional hub for SEO)
Locations (one page per location — local SEO)
Pricing / Insurance & Financing
Patient/Client Resources
  ├─ New Patient Info / What to Expect
  ├─ FAQs
  ├─ Forms / Patient Portal
  └─ Blog / Articles (SEO engine)
Reviews / Testimonials (if compliant)
Contact / Book Appointment
Legal: Privacy Policy · Terms · Accessibility Statement · HIPAA Notice (as applicable)
```

**URL & nav rules**
- Clean, keyword-relevant URLs (`/services/physical-therapy`, `/locations/austin`)
- Primary nav: max 5–7 items; keep "Book"/"Call" as a persistent button.
- Footer: locations, services, legal, trust badges, social, NAP (Name/Address/Phone).

---

## Part B — Page-by-Page Outlines (conversion blocks)

### Homepage
1. **Hero:** primary promise + 1 CTA (Book) + trust line (e.g., "4.9★ from 600+ patients")
2. **Trust bar:** credentials, affiliations, insurance/badges, review stars
3. **Services overview:** 3–6 cards linking to detail pages
4. **Why us / differentiators:** proof pillars
5. **How it works:** 3-step "what to expect" (reduces anxiety)
6. **Social proof:** testimonials / outcomes (compliant)
7. **Meet the team:** human faces + credentials
8. **FAQ snapshot** + insurance note
9. **Final CTA band:** book/call + location/hours/map

### Service detail page (template)
- H1 = service + benefit · who it's for · symptoms/conditions addressed
- What to expect (steps) · risks/safety (honest) · pricing/insurance note
- Provider(s) for this service · related FAQs · proof · **CTA: book this service**

### Location page (local SEO)
- NAP, embedded map, hours, parking/accessibility, services at this location,
  local reviews, photos, location-specific CTA, structured data (LocalBusiness/MedicalClinic).

### Booking / Contact page
- Online booking widget first; phone (click-to-call) second; form third.
- Privacy reassurance near the form; expected response time; what happens next.

### About / Team
- Mission + approach; named providers with photos, credentials, specialties, languages.

### Blog / Article (YMYL-grade)
- Author byline + credentials + medical-reviewer note + last-updated date.
- Clear, cited, non-promotional; internal links to services; soft CTA.

---

## Part C — Content Strategy

### C1. Conversion copy framework (per page)
- **Headline:** outcome-focused, specific, human (not jargon).
- **Subhead:** who it's for + the promise.
- **Body:** benefits → proof → process → objection handling.
- **CTA:** action + value ("Book your free consult", not just "Submit").
- **Microcopy:** privacy, reassurance, and "what happens next."

### C2. Content pillars & SEO clusters
- **Pillar pages:** each core service (broad, authoritative).
- **Clusters:** conditions, symptoms, "how to", cost, comparisons, prevention.
- **Local content:** "[service] in [city]", insurance accepted, community involvement.
- **Map intent:** informational (blog) → commercial (service) → transactional (book).

### C3. Trust content (essential in health)
- Provider credentials & bios · certifications/affiliations · facility photos
- Patient stories/testimonials (compliant) · outcomes/data (substantiated)
- FAQs addressing safety, privacy, pain, cost, time.

### C4. Content production workflow
Draft → **medical/clinical accuracy review** → SEO optimization → legal/compliance check →
publish → schedule periodic review (YMYL freshness). Track who reviewed and when.

---

## Part D — UI/UX Strategy

### D1. UX principles
- **Clarity over cleverness:** anxious or unwell users need calm, obvious paths.
- **Reduce cognitive load:** short sections, scannable, plain language.
- **Accessibility is core, not optional:** WCAG 2.2 AA (see doc 04). This is also law (ADA).
- **Mobile-first:** thumb-friendly CTAs, click-to-call, fast.
- **Trust through design:** real imagery, clean layout, no clutter, secure feel.

### D2. Design system
- **Color:** calming, accessible palette; check contrast ratios (≥4.5:1 text).
- **Typography:** highly legible; min 16px body; clear hierarchy.
- **Components:** buttons, cards, forms, accordions (FAQ), booking widget, alerts.
- **Imagery:** authentic photography of real staff/space; diverse, respectful representation.
- **Iconography & spacing:** generous whitespace = perceived professionalism/safety.

### D3. Key UX flows to design
- Find a service → understand it → book (≤3 clicks)
- Find a location → hours/contact → call or book
- New patient → "what to expect" → forms/portal
- Emergency/urgent path → immediate click-to-call (prominent)

### D4. Deliverables
- User flows → low-fi wireframes → design system → hi-fi mockups (desktop + mobile)
- Prototype for the booking flow (test for friction before build)

---

## Deliverable checklist
- [ ] Approved sitemap
- [ ] Page outlines for all priority pages
- [ ] Content plan + keyword map + production workflow
- [ ] Design system + hi-fi mockups (home, service, location, booking)
- [ ] Accessibility requirements attached (link doc 04)
