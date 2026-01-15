# Canvas Lesson Style Checklist & Guide

Use this checklist to validate all new Canvas pages.

## 🎨 Visual Identity
- [ ] **Container**: Max-width `800px`, centered margin, font-family `'Segoe UI', Tahoma, ...`.
- [ ] **Colors**:
    -   Primary Purple: `#4b3190` (Headers, buttons, borders)
    -   Accent Yellow/Gold: `#fdbb30` (Key term borders, underlines)
    -   Backgrounds: `#ffffff` (Main), `#f9f9f9` (Sections), `#bcbcbc` (Code block bg - wait, check exact hex). *Correction: Code bg is `#282c34` or `#2d3748`.*
- [ ] **Headers**:
    -   `<h2>` with purple background (`#4b3190`) and white text. Rounded corners (`10px`).
    -   `<h3>` with purple text and yellow bottom border (`#fdbb30`).
- [ ] **Icons/Emojis**: Use consistent emojis in headers (e.g., ℹ️, 🎤, 🔑, 🚀).

## 🦆 "Monty Pyduck" Narrative Elements
- [ ] **The Mascot**: Include an image of the "Duck in a hoodie/glasses" where appropriate (e.g., "Welcome", "Beyond the Index").
- [ ] **The Voice**:
    -   Professional but accessible.
    -   Use "Mallard" puns regarding security or rules (e.g., "Mallard Security Rule", "Mallard Guard").
    -   **User Warnings**: Any note/warning from "You" (the Professor) gets a Duck emoji (🦆).
    -   **Jeanie Notes**: Any note from "Me" (Jeanie/AI) gets a Star emoji (✨, 🌟).
    -   Reference "Jeanie" (the AI tutor) if relevant.
- [ ] **Signature**:
    -   Footer must include: `&copy; 2026 Meri Kasprak, Ph.D. 🦆`
    -   Line 2: `In collaboration with Gemini ✨`

## 📄 Structure: Lessons (Assignments)
Every lesson page should follow this flow:
1.  **Header Topic**: `[Emoji] Assignment [Num][Letter]: [Topic]`
2.  **Introduction Block**:
    -   White background.
    -   Hooks the student (Why is "Hello World" boring?).
    -   Duck image float-right.
    -   **Stats Badge**: `[Time Estimate]` `[Points]` (Light purple bg `#efeaf6`).
3.  **"The Mission" / "The Challenge"**:
    -   Grey/Off-white background box.
    -   Clear Goal, Challenge, and Requirements.
    -   **Extra Credit**: Highlighted in light blue/yellow.
4.  **Instructions & Videos**:
    -   **Mandatory**: Two videos per page.
        1.  **Overview Video**: "Watch: [Topic] Overview"
        2.  **Coding Sample**: "Watch: [Me] Coding the Solution/Example"
    -   Use `<details>` block or inline frames as appropriate.
    -   Step-by-step headers (Step 1, Step 2...).
5.  **Code Examples**:
    -   Dark theme block (`#282c34`).
    -   Font: `'Courier New', monospace`.
    -   **Note**: Ensure syntax highlighting is applied (colored spans) if possible, or consistent distinct color.
6.  **Dig Deeper** (Optional):
    -   `<details>` element.
    -   Summary style: `#fff3e0` (orange tint) or `#efeaf6` (purple tint).
7.  **Submission**:
    -   Clear file naming requirement (e.g., `joke.py`).
    -   "Can't find your file?" help block.
8.  **Grading Rubric**:
    -   **Standard**: Detailed Grid format (Criteria | Distinguished | Proficient | Emerging).
    -   **ADA Compliance**:
        -   Must include a `<caption>` or table note identifying it as a "Grading Rubric".
        -   Use proper column spans (`colspan`) and scope attributes (`scope="col"`, `scope="row"`) for headers.
    -   Header: Purple background, white text.

## 📄 Structure: Modules
1.  **Header**: `[Emoji] Module [Num]: [Title]`
2.  **Overview**: "Before You Begin" / Context.
3.  **Key Terms**: Yellow/Gold accent box (`#fff8e1` bg, `#fdbb30` border-left).
4.  **Content**: Sections defined by `<h3>` with under-borders.
5.  **Deliverables Checklist**: Boxed summary at the bottom.

## ⚠️ Resolved Standards
-   **Rubric Style**: **Detailed Grid** is the standard (unless a very minor check).
-   **Code Block Theme**: **Dark Theme (`#282c34`)** with syntax coloring.
-   **Title Format**: "Assignment [Num][Letter]: [Topic]" (e.g., "Assignment 8A: Dictionaries").

## 🧱 HTML Components Snippets
**Standard Header:**
```html
<h2 style="color: #ffffff; background-color: #4b3190; margin: 0; padding: 15px; border-radius: 10px;">
    🚀 Title Here
</h2>
```

**Code Block (Dark):**
```html
<pre style="background-color: #282c34; color: #ffffff; padding: 15px; border-radius: 5px; font-family: 'Courier New', monospace;">
print("Hello World")
</pre>
```

**Mallard Security Rule (Alert):**
```html
<h4 style="color: #c62828;">🛡️ Mallard Security Rule: [Rule Name]</h4>
<p>Description...</p>
```
