# 05 · Development & Tech Stack

How to build a fast, secure, compliant, conversion-ready healthcare/wellness website.
Choices here must support compliance (doc 04) and the conversion paths (doc 02–03).

---

## 1. Choosing the platform

| Option | Best for | Notes for healthcare/wellness |
|--------|----------|-------------------------------|
| **WordPress** | Content-heavy clinics, SEO blogs, budget builds | Huge plugin ecosystem; must harden security & pick HIPAA-aware form/host if PHI |
| **Webflow** | Design-led brand sites, marketing sites (no PHI) | Fast to build, clean code; not for storing PHI |
| **Headless (Next.js + CMS)** | Performance, scale, custom UX, health-tech | Best Core Web Vitals; more dev cost; full control over tracking/PHI |
| **Shopify** | Wellness e-commerce (supplements, programs) | Strong commerce; check health-claim & supplement policies |
| **Squarespace/Wix** | Small practices, fast/cheap | Limited compliance control; fine for simple no-PHI sites |

**Decision drivers:** Does it handle PHI? Content volume/SEO needs? Booking/EHR
integrations? Budget? In-house maintenance ability? Performance targets?

> If PHI is collected, the host/form/booking vendors must support **BAAs** and HIPAA-eligible
> configurations (see doc 04). Many mainstream builders do **not** — design around this.

---

## 2. Key integrations

- **Booking/scheduling:** Calendly, NexHealth, Jane, SimplePractice, Acuity, Zocdoc, or
  EHR-native booking. Prioritize online self-scheduling — it's the top conversion lever.
- **EHR/EMR / practice management:** integrate or hand off cleanly (Epic, athenahealth,
  Dentrix, etc.). Avoid duplicate data entry for staff.
- **Telehealth:** HIPAA-compliant video (Zoom for Healthcare, Doxy.me) if applicable.
- **CRM / marketing automation:** HubSpot, GoHighLevel, or HIPAA-compliant alternatives;
  ensure BAA if health data flows in.
- **Payments:** Stripe/Square/PayPal; PCI-DSS compliant; surface insurance/financing.
- **Forms/chat:** use HIPAA-eligible form & chat tools on any PHI-collecting page.
- **Reviews:** Google Business Profile, Birdeye/Podium for review generation (compliant).

---

## 3. Performance (directly affects conversions & SEO)

Targets — **Core Web Vitals** (Google ranking + UX signals):
- **LCP** < 2.5s · **INP** < 200ms · **CLS** < 0.1
- Mobile load: aim < 3s on 4G.

How:
- Optimize/compress images (WebP/AVIF), lazy-load, responsive sizes.
- Minimize JS; defer non-critical scripts; limit heavy third-party tags.
- CDN + good hosting; caching; modern image/font loading.
- Avoid bloated page builders where they hurt speed.

---

## 4. Technical SEO (build it in)

- Crawlable, logical URL structure; XML sitemap; clean robots.txt.
- **Structured data (schema.org):** `MedicalClinic`/`Physician`/`LocalBusiness`,
  `MedicalWebPage`, `FAQPage`, `Review`/`AggregateRating` (only if compliant), `BreadcrumbList`.
- Unique titles/meta per page; canonical tags; no duplicate content.
- Per-location pages with `LocalBusiness` + NAP consistency for local SEO.
- Mobile-first, HTTPS everywhere, proper redirects, 404 handling.
- Open Graph / Twitter cards for sharing.

---

## 5. Security & reliability

- HTTPS/TLS sitewide; HSTS; secure headers (CSP, X-Frame-Options).
- Keep CMS/plugins/dependencies patched; least-privilege access; MFA for admins.
- WAF + bot protection; rate-limit forms; spam protection that's accessible.
- Encrypted backups; tested restore; uptime monitoring.
- For PHI: access logs, session timeouts, strong auth on portals (see doc 04).

---

## 6. QA & launch

- Cross-browser + device testing (iOS/Android, Safari/Chrome/Firefox/Edge).
- Accessibility audit (axe/Lighthouse + manual + screen reader) — WCAG 2.2 AA.
- Test every conversion path: booking, call tracking, forms, payments.
- Verify analytics/consent firing correctly (and NOT leaking PHI).
- Performance test (PageSpeed/WebPageTest); fix regressions.
- 301 redirect map if migrating; preserve SEO equity.
- Staging sign-off → launch checklist → post-launch smoke test.

---

## Deliverable: Tech Spec
- Platform + hosting choice (+ BAA status if PHI):
- Integrations list (booking, EHR, CRM, payments, telehealth):
- Performance budget & CWV targets:
- Schema & technical-SEO plan:
- Security baseline:
- QA + launch checklist owner & date:
