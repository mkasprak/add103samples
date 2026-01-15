# Project Documentation

## Process Log

1. **Initial Setup**: I exported the canvas file renamed .zip and extracted then brought the folder in here as an import
2. **Analysis**: Analyzed the Canvas Export (`add-103-001n-export/imsmanifest.xml`) and identified the previous course as a Web Design course (HTML/CSS/Bootstrap).
3. **Architect Setup**: Identified the "Genesis/Jeanie" system in the workspace. Found that `_Jeanie_Specs` contained placeholder ADD 100 (Python) material.
4. **Planning**: Created an Implementation Plan to rewrite ADD 103 with a modern Web Development curriculum, replacing the ADD 100 placeholders.
5. **Execution**: Overwrote `official_syllabus.md` with the new Web Design curriculum and reset `project_status.md` with the new Module map.
6. **Refinement Requirement**: User requested a specific 16-week structure (2 days/week), a "Digital Deeper" section, and a template based on McHenry County College styles.
    *   **Constraints**: 16 Weeks, Last 4 weeks = Final Project, "Teach by Example" philosophy.
    *   **Legacy Content**: Must preserve CPanel and GitHub setup instructions.
7.  **Quality Matters Refinement**: User emphasized adherence to Quality Matters (QM) standards.
    *   **Action**: Updating template to explicitly state Learning Objective Alignment (QM Standard 2.1 and 2.2).
    *   **Action**: Ensuring accessibility info is prominent (QM Standard 8).
8.  **Content Generation**: Generated Week 1 Content.
    *   `week_1a_welcome.html`: Welcome + VS Code Setup.
    *   `week_1b_git.html`: GitHub + cPanel Pipeline setup (using recovered steps).
9.  **Guideline Integration**: Added `documentation/teaching_bravely.md`.
    *   **Action**: Will use the 7 Principles (Contact, Cooperation, Active Learning, Feedback, Time on Task, High Expectations, Diversity) as a checklist for all future modules.
10. **Refinement**: Updated Template and Week 1 files with:
    *   **Footer**: "Copyright 2026 Dr. Meri Kasprak in collaboration with Gemini".
    *   **Code Quality**: Added extensive comments to code examples ("Teach by Example").
11. **Content Generation**: Generated Week 2 Content using the new **Interactive Textbook** format (Collapsible Details).
    *   `week_2a_semantics.html`: Deep dive into Header/Main/Footer and SEO.
    *   `week_2b_content.html`: Deep dive into Absolute vs Relative paths and Accessibility.
12. **Rubric Integration**: Retroactively added **Grading Rubrics** to the template and all 4 generated lessons.
    *   Features: `<caption>`, `<th scope="col">`, and specific criteria for each lesson.
13. **Engagement Integration**: Added **Discussion & Peer Review** sections to the template.
    *   **Reciprocity**: "Part 1 (Post) + Part 2 (Review 2 Peers)" standard added to Week 3B (Box Model Project).
14. **Refactor for Canvas Compatibility**:
    *   **Strict Inline Styles**: Removed all `<style>` tags. All styles are now `style="..."` attributes.
    *   **Preformatted Code**: Converted all code blocks to `<pre style="white-space: pre-wrap;">` to preserve line breaks and indentation.
    *   **Regenerated**: Template, Week 1A, 1B, 2A, 2B, 3A, 3B.
