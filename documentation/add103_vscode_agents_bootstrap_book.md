# ADD 103 Course Book
## VS Code First, GitHub in Week 3, Agents + Bootstrap in Week 12

Term: Spring 2026  
Author: Dr. Meri Kasprak (working draft for Canvas and lecture adaptation)

---

## How To Use This Book

This book is written for a Watch One, Do One teaching style.

- Each section explains core ideas in plain language.
- Each section includes fully commented code examples.
- Every code example is followed by a video placeholder where you can embed your lecture walkthrough.
- Students should copy, run, and modify each example before moving on.

### Standard Video Placeholder Block

Use this block after every example when you adapt content into Canvas pages.

- Video Title: [Add title]
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 4 to 8 minutes
- Instructor Notes: [What to emphasize live]

---

## Week 1: Hosting and cPanel Foundations

### Learning Goal
Students can log into cPanel, create a web directory, upload a file, and verify a live URL.

### Concept: Local vs Live
A file on a student laptop is private. A file in public_html is publicly reachable by URL.

### Example 1.1: First Published Page

```html
<!doctype html>
<html lang="en">
<head>
  <!-- The browser needs charset to render emoji and symbols correctly -->
  <meta charset="UTF-8">
  <!-- Mobile-friendly viewport settings -->
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Week 1 - First Live Page</title>
</head>
<body>
  <!-- Main heading tells users and screen readers what this page is about -->
  <h1>Hello from my live site</h1>

  <!-- This paragraph confirms successful deployment -->
  <p>I uploaded this file to public_html/ADD103/week_01/</p>

  <!-- Add date manually so students prove they edited and republished -->
  <p>Deployment timestamp: 2026-05-11</p>
</body>
</html>
```

- Video Title: Week 1.1 Uploading the first page with cPanel File Manager
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 6 minutes
- Instructor Notes: Emphasize path accuracy and why 404 errors happen

### Example 1.2: Common Deployment Mistake and Fix

```text
# Broken URL pattern
https://studentdomain.com/ADD103/week01/index.html

# Correct URL pattern
# Note the underscore in week_01 to match the actual folder name
https://studentdomain.com/ADD103/week_01/index.html
```

- Video Title: Week 1.2 Fixing path mismatches and 404 errors
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 5 minutes
- Instructor Notes: Show side-by-side folder names and URL path segments

---

## Week 2: VS Code Workflow and Semantic HTML

### Learning Goal
Students can use VS Code productively and write semantic page structure.

### Concept: Why VS Code Now
VS Code gives students real developer habits early: file tree awareness, extensions, formatting, and autocomplete.

### Example 2.1: Semantic Skeleton

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Semantic Starter</title>
</head>
<body>
  <!-- Header introduces site identity and primary nav -->
  <header>
    <h1>Birdwatcher Journal</h1>
    <nav>
      <!-- Real links would point to actual pages -->
      <a href="index.html">Home</a>
      <a href="log.html">Field Log</a>
      <a href="about.html">About</a>
    </nav>
  </header>

  <!-- Main should appear once and contain unique page content -->
  <main>
    <article>
      <h2>Morning Observation</h2>
      <p>Spotted a red-tailed hawk near the north trail.</p>
    </article>

    <section>
      <h3>Gear Checklist</h3>
      <ul>
        <li>Binoculars</li>
        <li>Notebook</li>
        <li>Camera</li>
      </ul>
    </section>
  </main>

  <!-- Footer contains legal or contact details -->
  <footer>
    <p>Copyright 2026 Birdwatcher Journal</p>
  </footer>
</body>
</html>
```

- Video Title: Week 2.1 Semantic structure and screen reader landmarks
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 8 minutes
- Instructor Notes: Explain why div-only pages hurt accessibility

### Example 2.2: Useful VS Code Habits

```text
1) Use format document after writing a draft.
2) Keep Explorer panel open to avoid wrong file edits.
3) Use split editor for HTML and browser preview notes.
4) Rename files carefully and update matching links.
5) Save frequently and test after each small change.
```

- Video Title: Week 2.2 VS Code workflow habits for beginners
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 5 minutes
- Instructor Notes: Demo one clean workflow and stick to it

---

## Week 3: GitHub Kickoff and CSS Foundations

### Learning Goal
Students can create a repository, commit meaningful snapshots, and apply basic CSS.

### Concept: Why Version Control Matters
GitHub protects student progress and teaches professional collaboration patterns.

### Example 3.1: First HTML + CSS Pair

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Style Guide Starter</title>
  <!-- Link external stylesheet so styles are reusable -->
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <h1>My Brand Styles</h1>
  <p>This paragraph should show my base typography settings.</p>
</body>
</html>
```

- Video Title: Week 3.1 Connecting HTML and CSS files
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 6 minutes
- Instructor Notes: Show what breaks when href path is wrong

### Example 3.2: Commented CSS Basics

```css
/* Global page defaults improve consistency */
body {
  background-color: #f5f7fb; /* Light background for readability */
  color: #1f2937;            /* Dark neutral text */
  font-family: Arial, sans-serif;
  line-height: 1.7;
  margin: 0;
  padding: 2rem;
}

/* Main title style */
h1 {
  color: #1d4ed8;            /* Blue accent */
  font-size: 2rem;
  margin-bottom: 1rem;
}

/* Paragraph style */
p {
  max-width: 60ch;           /* Limits line length for better readability */
}
```

- Video Title: Week 3.2 Reading CSS declarations line by line
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 7 minutes
- Instructor Notes: Explain each property as a design decision

### Example 3.3: Beginner Git Command Flow

```bash
# Check current file status before staging
git status

# Add all changed files
git add .

# Create a meaningful snapshot message
git commit -m "Week 3 style guide draft with base typography"

# Publish local commits to GitHub
git push
```

- Video Title: Week 3.3 First commit and push walkthrough
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 6 minutes
- Instructor Notes: Stress commit message quality, not just command memorization

---

## Week 4: Color Systems and CSS Variables

### Learning Goal
Students can define a visual palette and apply variables across components.

### Example 4.1: Color Tokens in :root

```css
/* Design tokens live in :root for global reuse */
:root {
  --color-bg: #f8fafc;        /* Page background */
  --color-surface: #ffffff;   /* Card or panel background */
  --color-text: #0f172a;      /* Primary text */
  --color-accent: #7c3aed;    /* Accent color */
  --color-warn: #b91c1c;      /* Error or warning color */
}

body {
  background: var(--color-bg); /* Pull value from token */
  color: var(--color-text);
}

.card {
  background: var(--color-surface);
  border-left: 6px solid var(--color-accent);
  padding: 1rem;
}
```

- Video Title: Week 4.1 Building reusable color tokens
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 7 minutes
- Instructor Notes: Show one-token update and whole-page impact

---

## Week 5: Flexbox Layout Patterns

### Learning Goal
Students can create one-dimensional responsive layouts using Flexbox.

### Example 5.1: Flex Container with Cards

```html
<section class="cards">
  <article class="card">Card 1</article>
  <article class="card">Card 2</article>
  <article class="card">Card 3</article>
</section>
```

```css
.cards {
  display: flex;          /* Turns children into flex items */
  gap: 1rem;              /* Space between cards */
  flex-wrap: wrap;        /* Allows wrapping on small screens */
}

.card {
  flex: 1 1 220px;        /* Grow, shrink, and ideal width */
  background: #ffffff;
  border: 1px solid #d1d5db;
  padding: 1rem;
}
```

- Video Title: Week 5.1 Flexbox growth, shrink, and wrap
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 8 minutes
- Instructor Notes: Explain one-dimensional layout vs Grid

---

## Week 6: CSS Grid Essentials

### Learning Goal
Students can design two-dimensional layouts with explicit columns and rows.

### Example 6.1: Basic Grid Dashboard

```html
<div class="dashboard">
  <header class="panel header">Header</header>
  <aside class="panel sidebar">Sidebar</aside>
  <main class="panel content">Main Content</main>
  <footer class="panel footer">Footer</footer>
</div>
```

```css
.dashboard {
  display: grid;                         /* Activate grid layout */
  grid-template-columns: 220px 1fr;      /* Sidebar + content */
  grid-template-rows: auto 1fr auto;     /* Header, body, footer */
  gap: 1rem;
  min-height: 100vh;
}

.header { grid-column: 1 / -1; }         /* Span full width */
.sidebar { grid-column: 1; }
.content { grid-column: 2; }
.footer { grid-column: 1 / -1; }

.panel {
  padding: 1rem;
  background: #ffffff;
  border: 1px solid #d1d5db;
}
```

- Video Title: Week 6.1 Grid tracks, spanning, and page framing
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 9 minutes
- Instructor Notes: Compare line-based placement with visual output

---

## Week 7: Responsive Design and Media Queries

### Learning Goal
Students can adapt layouts and typography for mobile, tablet, and desktop.

### Example 7.1: Mobile First Navigation

```css
/* Base: mobile styles first */
.nav {
  display: flex;
  flex-direction: column;   /* Vertical stack on phones */
  gap: 0.5rem;
}

/* Tablet and up */
@media (min-width: 768px) {
  .nav {
    flex-direction: row;    /* Horizontal nav on larger screens */
    justify-content: space-between;
  }
}
```

- Video Title: Week 7.1 Mobile-first thinking with one breakpoint
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 7 minutes
- Instructor Notes: Show why starting desktop-first often causes regressions

---

## Week 8: Midterm Build Studio

### Learning Goal
Students can integrate semantic HTML, CSS styling, and responsive behavior into a coherent mini-site.

### Example 8.1: Midterm Self-Check Block

```text
Before submitting:
- Validate all links.
- Test on a narrow viewport.
- Confirm alt text on every meaningful image.
- Remove unused CSS rules.
- Confirm page title is unique.
```

- Video Title: Week 8.1 Midterm QA checklist in action
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 5 minutes
- Instructor Notes: Model professional QA discipline

---

## Week 9: Bootstrap Fundamentals

### Learning Goal
Students can use the Bootstrap grid and components intentionally, not blindly.

### Example 9.1: Bootstrap Grid Starter

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Bootstrap Grid Starter</title>
  <!-- Bootstrap CSS from CDN -->
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
  <main class="container py-4">
    <h1 class="mb-4">Bootstrap Grid Demo</h1>

    <div class="row g-3">
      <!-- On md+ screens each card gets 4 columns, full width on mobile -->
      <article class="col-12 col-md-4">
        <div class="p-3 border rounded">Card A</div>
      </article>
      <article class="col-12 col-md-4">
        <div class="p-3 border rounded">Card B</div>
      </article>
      <article class="col-12 col-md-4">
        <div class="p-3 border rounded">Card C</div>
      </article>
    </div>
  </main>
</body>
</html>
```

- Video Title: Week 9.1 Bootstrap container, row, and column logic
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 8 minutes
- Instructor Notes: Explain col-12 and col-md-4 behavior clearly

---

## Week 10: Media Optimization

### Learning Goal
Students can deliver responsive images and accessible media.

### Example 10.1: Responsive Image with srcset

```html
<img
  src="images/campus-800.jpg"
  srcset="
    images/campus-400.jpg 400w,
    images/campus-800.jpg 800w,
    images/campus-1200.jpg 1200w
  "
  sizes="(max-width: 600px) 100vw, 800px"
  alt="Students working in a campus design lab"
>
```

- Video Title: Week 10.1 Choosing image sizes with srcset
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 7 minutes
- Instructor Notes: Connect file size to performance scores

---

## Week 11: Interactivity Basics

### Learning Goal
Students can attach simple behavior to page elements using JavaScript.

### Example 11.1: Accessible Toggle Pattern

```html
<button id="menuBtn" aria-expanded="false" aria-controls="mainMenu">
  Open Menu
</button>

<nav id="mainMenu" hidden>
  <a href="#">Home</a>
  <a href="#">Projects</a>
  <a href="#">Contact</a>
</nav>

<script>
  // Grab button and menu once so we can reuse references
  const menuBtn = document.getElementById('menuBtn');
  const mainMenu = document.getElementById('mainMenu');

  // Toggle menu visibility and keep ARIA in sync
  menuBtn.addEventListener('click', () => {
    const isExpanded = menuBtn.getAttribute('aria-expanded') === 'true';

    // Flip aria-expanded value
    menuBtn.setAttribute('aria-expanded', String(!isExpanded));

    // hidden=true hides menu, hidden=false shows it
    mainMenu.hidden = isExpanded;

    // Update visible button label to match new state
    menuBtn.textContent = isExpanded ? 'Open Menu' : 'Close Menu';
  });
</script>
```

- Video Title: Week 11.1 DOM event handling with accessibility attributes
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 9 minutes
- Instructor Notes: Explain state sync between UI text and ARIA

---

## Week 12: Agents + Bootstrap Programming Studio

### Learning Goal
Students can use coding agents to scaffold Bootstrap pages, then evaluate and improve output.

### Concept: Agent as Pair Programmer, Not Autopilot
Students must critique every generated block for semantics, accessibility, and maintainability.

### Example 12.1: Structured Prompt Template

```text
Build a Bootstrap 5 landing page with:
- sticky navbar
- hero section with one primary call-to-action
- three feature cards
- contact form

Constraints:
- semantic HTML landmarks
- accessible labels and alt text
- mobile-first responsive behavior
- no inline styles

Output format:
- one complete HTML file
- brief notes explaining major section choices
```

- Video Title: Week 12.1 Prompt design for predictable agent output
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 8 minutes
- Instructor Notes: Show that constraints improve code quality

### Example 12.2: Refactoring Agent Output

```html
<!-- Before: generated button text is vague -->
<button class="btn btn-primary">Click Here</button>

<!-- After: clearer intent and improved accessibility -->
<button class="btn btn-primary" aria-label="Submit contact form">
  Send Message
</button>
```

- Video Title: Week 12.2 Improving agent-generated UI text and semantics
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 5 minutes
- Instructor Notes: Teach students to justify each refactor decision

### Example 12.3: Agent Reflection Log Format

```text
Prompt used:
[Paste exact prompt]

Suggestion accepted:
- Bootstrap navbar scaffold because structure was clean.

Suggestion rejected:
- Replaced generic button labels with action-specific labels.

Changes made:
- Added form labels and input ids.
- Fixed heading hierarchy from h1 to h2 in nested sections.
- Simplified redundant utility classes.
```

- Video Title: Week 12.3 Writing a professional accept-reject reflection log
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 6 minutes
- Instructor Notes: Reflection quality is part of assessment quality

---

## Appendix A: Debugging Playbook

### Example A.1: Fast Triage Sequence

```text
1) Read the error message fully.
2) Confirm the correct file is open.
3) Check paths and spelling first.
4) Validate HTML nesting and missing closing tags.
5) Use browser DevTools Elements and Console tabs.
6) Test one small fix at a time.
```

- Video Title: Appendix A.1 Debugging rhythm for beginners
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 6 minutes
- Instructor Notes: Normalize debugging as a core developer skill

---

## Appendix B: Assessment Language for Agent Era

### Rubric anchors

- Technical correctness: Code runs and matches requirements.
- Accessibility quality: Semantic structure, labels, contrast.
- Design intent: Visual hierarchy and responsive behavior.
- Version discipline: Meaningful commits and revision flow.
- Agent literacy: Student can explain why code was accepted or changed.

### Example B.1: Strong Submission Note

```text
I accepted the generated card layout because it respected Bootstrap grid conventions.
I rewrote the form section to include labels and ids for accessibility.
I removed duplicate margin utility classes to make spacing consistent.
My final version passed mobile checks at 375px and 768px widths.
```

- Video Title: Appendix B.1 What a strong technical reflection sounds like
- Video Embed Link: [Paste Panopto or YouTube link]
- Video Length Target: 4 minutes
- Instructor Notes: Use this as a grading calibration sample

---

## Next Build Step

When you are ready, this book can be split into:

- one Canvas lesson page per weekly section,
- one instructor script per code example,
- one student lab sheet per week,
- one quick-check quiz bank per chapter.
