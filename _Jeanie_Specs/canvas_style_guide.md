# ADD 103: Canvas Lesson Style Guide & Specs

**Last Updated:** Spring 2026
**Course:** ADD 103 - Introduction to Web Design
**Role:** Jeanie (Course Architect)

This document defines the strict requirements for generating lesson pages that are compatible with **Instructure Canvas** and meet the **Quality Matters (QM)** rigor requested by the user.

---

## 🎨 1. Technical Constraints (Canvas Compatibility)
Canvas is finicky. We must adhere to these rules to prevent layout breakage.

*   **⚠️ INLINE STYLES ONLY**: Never use `<style>` blocks in the `<head>` or `<body>`. Canvas strips them. Every single visual property must be in `style="..."`.
*   **Container Width**: All content must be wrapped in a main `<div>` with `max-width: 800px; margin: 0 auto;`.
*   **Code Blocks**: Must use `<pre>` tags with `white-space: pre-wrap;` to preserve indentation.
    *   *Bad:* `<div class="code">...</div>`
    *   *Good:* `<pre style="background: #282c34; color: #abb2bf; ...">...</pre>`
*   **Images**: All `<img>` tags **MUST** have an `alt="..."` attribute for accessibility.

---

## 🖌️ 2. Visual Identity (MCC Branding)
We use the McHenry County College palette.

| Element | Color | Hex Code | Usage |
| :--- | :--- | :--- | :--- |
| **Primary** | MCC Purple | `#582C83` | Headers, Rubric Table Headers, Links |
| **Accent** | MCC Gold | `#FFC629` | Top Border, Bullet Points, Highlights |
| **Text** | Dark Grey | `#333333` | Body Text (Never use pure black #000) |
| **Background** | Off-White | `#f9f9f9` | Page Background |
| **Code Bg** | Atom Dark | `#282c34` | Code Blocks |

---

## 📝 3. Page Structure (The Template)
Every Lesson Page MUST follow this exact sequence:

### A. The Container
```html
<div style="max-width: 800px; margin: 0 auto; ... border-top: 10px solid #FFC629;">
```

### B. Header
*   Purple Background (`#582C83`).
*   **H1**: "Week X: [Topic]"
*   **Subtitle**: "ADD 103: Introduction to Web Design | Spring 2026"

### C. QM Alignment Strip
*   Light Blue Background (`#f0f7ff`).
*   **Icon**: 🎯
*   **Text**: "Learning Objective Alignment: [LO Name] — '[Description]'"

### D. Overview ("Why This Matters")
*   **H2**: "Overview" (Purple text, Gold left-border).
*   **Content**: High-level intro. "Why are we learning this?"
*   **Accessibility Note**: Green box (`#e8f5e9`) explaining the A11y implication of the topic.

### D2. Required Video (The Lecture)
*   **H2**: "🎥 Watch the Lesson"
*   **Content**: A placeholder for the Panopto embed.
*   **Snippet**:
    ```html
    <div style="background-color: #f4f4f4; padding: 20px; border: 1px dashed #ccc; text-align: center; color: #666; margin: 20px 0;">
        <strong>[VIDEO PLACEHOLDER]</strong><br>
        Topic: Lesson Walkthrough<br>
        <em>(User to embed Panopto/YouTube Iframe here)</em>
    </div>
    ```

### E. The Textbook (Deep Dive)
*   **H2**: "📖 The Textbook: [Topic Title]"
*   **Function**: Expandable `<details>` sections for theory.
*   **Style**: `<summary>` with bold text and `+` icon logic (via CSS content if possible, but standard arrow is fine).

### F. Teach by Example (Look & Learn)
*   **H2**: "👀 Look & Learn"
*   **Content**: A realistic code scenario.
*   **The Code Block**:
    ```html
    <div style="background-color: #fff; border: 2px solid #eee; ...">
        <pre style="background-color: #282c34; color: #abb2bf; padding: 20px; font-family: 'Consolas', monospace; overflow-x: auto; white-space: pre-wrap;">
        <!-- CODE GOES HERE -->
        </pre>
    </div>
    ```
*   **Observation**: A bulleted list explaining *what* to look at in the code.

### G. Guided Practice (The Project)
*   **H2**: "💻 Project: [Creative Title]"
    *   *Examples:* "The Developer Manifesto", "The Multimedia Resume", "The Semantic Biography".
*   **Rigor**: Assignments must be multi-step and college-level.
    *   *Step 1*: Setup/Files.
    *   *Step 2*: The Code/Implementation.
    *   *Step 3*: Verification/Publishing.

### H. Dig Deeper (Resources & Extra Credit)
*   **Style**: Yellow tint background (`#fff8e1`).
*   **H2**: "⛏️ Dig Deeper (Resources)"
*   **Links**: List of MDN/W3Schools links.
*   **⭐ Extra Credit Challenge**: A specific, optional task worth 5pts (e.g., "The Favicon Challenge").

### I. Grading Rubric
*   **H2**: "🏆 Grading Rubric"
*   **Table**: Full HTML table.
    *   **Headers**: Criteria (60%), Points (20%), Notes (20%).
    *   **Style**: Purple header cells, zebra-striped body rows.
    *   **Content**: Specific criteria (e.g., "Semantics: Correct use of `<header>`...").

### J. Footer
*   Dark Background (`#333`).
*   Text: `&copy; 2026 Dr. Meri Kasprak in collaboration with Gemini`

---

## 🧠 4. Pedagogy & Tone
*   **Tone**: Professional but encouraging. "We are building reality."
*   **Emojis**: Use them as wayfinding icons (🎯, 📖, 👀, 💻, ⛏️, 🏆).
*   **Reciprocity**: If applicable, include a "Discussion" block where students share an analogy or critique.
*   **Google Fonts**: In Week 3+, enforce the use of Google Fonts.

---

## 🛠️ 5. Implementation Rules
1.  **Strict File Naming**: `week_X_topic.html` (lowercase, underscores).
2.  **Comments**: Code examples must be heavily commented (`<!-- Like this -->` or `/* Like this */`).
3.  **Validation**: Always "Inspect" the code mentally to ensure tags are closed.
