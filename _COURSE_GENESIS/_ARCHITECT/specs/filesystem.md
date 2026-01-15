# 📂 Filesystem & Naming Standards

## 1. Directory Structure
The workspace must contain these core folders:
*   `Canvas Lessons/`: Stores the HTML files for the LMS.
*   `notebook_files/`: Stores the Markdown specs for the AI Tutor.
*   `_Jeanie_Specs/`: Stores the project tracking files (`project_status.md`).

## 2. Naming Conventions (Strict)
We use a **Chronological Prefix** system to keep files sorted.

### HTML Lessons
*   **Format**: `[Sequential_ID]_assignment[Number][Track]_[Topic].html`
*   *Example*: `28_assignment9a_functions.html`
*   *Why*: The `28_` ensures it sits in the correct order in the folder, regardless of the assignment name.

### Jeanie Specs (Markdown)
*   **Format**: `official_[Number][Track]_[Topic].md`
*   *Example*: `official_9a_functions.md`
*   *Why*: "Official" groups them all together, easy to find.

### Project Files
*   **Format**: `snake_case` or language specific standard.
*   *Example*: `coffee_shop.py`, `dashboard_layout.pbix`.

## 3. The "Copy-Paste" Rule
If you need to create a new file, **DO NOT** generate it from memory.
1.  Read `_ARCHITECT/templates/[File_Type]`.
2.  Copy the content.
3.  Fill in the blanks.
