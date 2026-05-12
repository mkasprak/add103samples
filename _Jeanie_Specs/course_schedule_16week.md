#  ADD-103: Fundamental Web Development  16-Week Course Schedule
**Term:** Fall 2026 (16 Weeks)
**Cadence:** 2 Days/Week (e.g., Mon/Wed or Tue/Thu)
**Total Sessions:** 30 Lessons + Finals Week

> **Philosophy**: Teach by Example. "Watch one, Do one."
> **Toolchain Ramp-Up**: Students build real pages *before* learning professional tools. Tools are introduced just-in-time, when students have something meaningful to use them for.
> **Last 4 Weeks**: Dedicated solely to the Final Portfolio Project.

---

##  Phase 1: Just Build  No Toolchain Anxiety (Weeks 13)
*Students write real HTML and see it in a browser before touching a terminal, account login, or Git.*

### Week 1: The Environment & First Page
- **Day 1 (1A): Welcome + File Organization + First HTML Page**
  - Syllabus review. File naming rules (no spaces, lowercase, underscores).
  - Folder structure: `ADD103/week_01/index.html`.
  - VS Code: install, open folder, create file, save  nothing else.
  - Write a complete boilerplate HTML page. Double-click to open in browser.
  - Assignment: `about-me.html`  a personal page with headings and paragraphs.
- **Day 2 (1B): HTML Deep Dive  Structure & Text**
  - `<!doctype html>`, `<html>`, `<head>`, `<body>` explained.
  - Headings (h1h6), paragraphs, `<strong>`, `<em>`, HTML comments, `<title>`.
  - Assignment: Expand `about-me.html` with proper heading hierarchy and formatted text.

### Week 2: Content Structure (HTML5 Semantics)
- **Day 3 (2A): Semantic HTML**
  - VS Code: split view, Emmet, format on save.
  - `<header>`, `<nav>`, `<main>`, `<footer>`, `<article>`, `<section>`, `<aside>`.
  - Why semantics matter: SEO + accessibility intro. Alt text basics.
  - Assignment: Rebuild `about-me.html` using full semantic structure.
- **Day 4 (2B): Content Elements  Links, Images, Lists, Tables**
  - Anchor tags, absolute vs. relative paths. Images, image file types.
  - Lists (`<ul>`, `<ol>`). Tables for data (`<table>`, `<thead>`, `<tbody>`).
  - Assignment: Add navigation, an image, and a data table to your site.

### Week 3: Content Creation & Web Writing
- **Day 5 (3A): Writing for the Web + SEO + Metadata**
  - How people read on screens. `<meta>` tags: description, charset, viewport.
  - Heading hierarchy for SEO. Open Graph basics.
  - Assignment: Add proper `<head>` SEO metadata to all pages.
- **Day 6 (3B): Editing Images for the Web**
  - Image formats: JPG, PNG, WebP. Optimizing with Squoosh.app (no install).
  - Sizing images correctly. Writing descriptive, accessible alt text.
  - Assignment: Optimize and add a properly sized hero image to your site.

---

##  Phase 2: Make It Look Good  CSS Core (Weeks 46)
*Students learn CSS. GitHub is introduced via the web UI. No terminal yet.*

### Week 4: CSS Fundamentals + Version Control Intro
- **Day 7 (4A): Intro to CSS  Selectors, Properties, External Stylesheets**
  - Install VS Code Live Server extension (first extension install).
  - Tag, class, and ID selectors. The cascade and specificity basics.
  - `color`, `background-color`, `font-size`, `text-align`.
  - Assignment: Create `style.css` and style your site.
- **Day 8 (4B): GitHub  Version Control Concepts + Web UI Upload**
  - What is version control? Why developers use it.
  - Create a GitHub account. Create a repo via the web UI.
  - Upload existing project files via drag & drop (no terminal).
  - Assignment: Get your Week 13 work into GitHub. Share the link.

### Week 5: CSS Typography & Color
- **Day 9 (5A): Web Typography**
  - Google Fonts (link tag method). `font-family`, `font-size` (rem vs px), `line-height`.
  - Typographic hierarchy.
  - Assignment: Apply a Google Font and typographic system to your site.
- **Day 10 (5B): CSS Color + Usability + WCAG Basics**
  - Hex, RGB, RGBA, HSL. Color theory for UI.
  - WCAG 2.1 contrast standards (AA minimum). WebAIM Contrast Checker.
  - Assignment: Define a color palette and verify all text meets AA contrast.

### Week 6: The Box Model & Positioning
- **Day 11 (6A): The Box Model**
  - Content  Padding  Border  Margin. `box-sizing: border-box`.
  - Using Chrome DevTools to inspect and debug box model live.
  - Assignment: Diagnose and fix spacing issues on your site using DevTools.
- **Day 12 (6B): CSS Positioning**
  - Normal flow. `position`: static, relative, absolute, fixed, sticky.
  - When to use positioning vs. layout (foreshadowing Flexbox).
  - Assignment: Build a page with a sticky nav and an absolute-positioned badge.

---

##  Phase 3: Go Live  Deployment & Accessibility (Weeks 78)
*Students now have a real project worth deploying. Git terminal and cPanel introduced here.*

### Week 7: File Management, FTP & Git Terminal
- **Day 13 (7A): File Management + FTP + cPanel**
  - InMotion cPanel login and orientation. `public_html` directory.
  - File Manager: upload, rename, permissions, troubleshoot 403/404.
  - FTP concepts and when to use an FTP client.
  - Assignment: Upload project via File Manager. Confirm live URL.
- **Day 14 (7B): Git Terminal + GitHub  cPanel Deployment Pipeline**
  - First terminal use: `git init`, `git add`, `git commit`, `git push`.
  - Connect GitHub repo to cPanel Git Version Control.
  - The full pipeline: VS Code  push  GitHub  cPanel pull  live URL.
  - Assignment: Re-deploy via Git pipeline. Never drag files again.

### Week 8: Accessibility + Midterm Lab
- **Day 15 (8A): Accessibility  WCAG, WAVE, ARIA**
  - WCAG 2.1 explained. Running and reading a WAVE audit.
  - ARIA landmarks and roles basics. Keyboard navigation testing.
  - **Policy**: Midterm must pass WAVE with zero errors for grade above C.
  - Assignment: Run WAVE on your live site. Fix all errors. Document changes.
- **Day 16 (8B): Midterm Open Lab**
  - In-class studio + peer feedback session.
  - **Midterm Project Due**: live, deployed, WAVE-clean, multi-page site.

---

##  Phase 4: Modern Layout  Flexbox & Grid (Weeks 911)
*Students have tools confidence. Time for the design phase.*

### Week 9: Flexbox
- **Day 17 (9A): Flexbox Container**
  - `display: flex`, main + cross axes. `justify-content`, `align-items`, `gap`.
  - Assignment: Rebuild site navigation as a Flexbox row.
- **Day 18 (9B): Flexbox Items**
  - `flex-grow`, `flex-shrink`, `flex-basis`. `align-self`, `order`. Nesting.
  - Assignment: Build a card grid using Flexbox wrapping.

### Week 10: CSS Grid
- **Day 19 (10A): CSS Grid Basics**
  - `display: grid`, `grid-template-columns` (fr units, `repeat()`), `gap`.
  - Assignment: Create a photo gallery with CSS Grid.
- **Day 20 (10B): Grid Areas**
  - `grid-template-areas`. Holy Grail layout. Grid vs. Flexbox  when to use which.
  - Assignment: Rebuild main page layout using Grid Areas.

### Week 11: Responsive Design
- **Day 21 (11A): Media Queries & Breakpoints**
  - `@media` rule. Breakpoints: 480px / 768px / 1024px. Mobile-first approach.
  - Assignment: Add media queries to make card grid stack on mobile.
- **Day 22 (11B): Responsive Images & Media**
  - `srcset` and `sizes`. `<picture>` element. WebP format.
  - Native HTML5 `<video>` and `<audio>`.
  - Assignment: Add a responsive hero image with `srcset`.

---

##  Phase 5: Pro Tools  Frameworks & AI (Weeks 1213)

### Week 12: Web Frameworks (Bootstrap 5)
- **Day 23 (12A): Framework Concepts + Bootstrap Grid**
  - Why frameworks exist. Bootstrap CDN. 12-column grid: `container`, `row`, `col-*`.
  - Assignment: Rebuild card grid using Bootstrap grid system.
- **Day 24 (12B): Bootstrap Components**
  - Navbars (responsive + hamburger). Cards, Badges, Alerts. Utility classes.
  - Assignment: Add Bootstrap Navbar and Cards to a page.

### Week 13: AI in Web Development
- **Day 25 (13A): Using AI for Scaffolding & Debugging**
  - What AI tools can and cannot do. Prompting strategies.
  - The "Show Your Work" rule: explain every line you submit.
  - Assignment: Use AI to scaffold a Bootstrap page. Annotate every section.
- **Day 26 (13B): AI Output Audit & Refactor**
  - Lighthouse + WAVE on AI-generated code. Common AI mistakes.
  - Refactoring AI output to meet course standards.
  - Assignment: Audit and fix the AI page from 13A. Document every change.

---

##  Phase 6: Final Portfolio Project (Weeks 1416)

### Week 14: Project Planning & Structure
- **Day 27 (14A): Concept, Wireframe & Proposal**
  - Portfolio needs: About, Work/Projects, Contact.
  - Paper or Figma wireframes. Content outline.
  - Assignment: Submit written proposal + wireframe.
- **Day 28 (14B): HTML Skeleton Build**
  - Translate wireframe to semantic HTML. Create and link all pages.
  - Set up GitHub repo + cPanel pipeline for final project.
  - Assignment: Push skeleton to GitHub. Confirm live URL.

### Week 15: Layout, Polish & QA
- **Day 29 (15A): Layout + Styling + Mobile-First**
  - Grid/Flexbox from wireframe. Typography + color palette. Mobile-first build.
  - Assignment: Full layout implemented, responsive at mobile + desktop.
- **Day 30 (15B): Final QA + Peer Review**
  - WAVE audit (zero errors required). Lighthouse (target 90+ Perf, 100 A11y).
  - Peer review against the rubric. Deploy final fixes.

### Week 16: Finals
- **Final Presentations**: Demo your live portfolio to the class.
  - Walk through design decisions, challenges solved, what you'd do next.
  - Graded on: live deployment, WAVE clean, responsive design, presentation clarity.
