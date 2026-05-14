# 1A Video 3: File Organization Rules & Your First HTML Page

| Field | Value |
|-------|-------|
| **Week** | Week 1A |
| **Video** | Video 3 of 3 |
| **Type** | Gemini (AI-generated avatar) |
| **Target Length** | 5 min |
| **LO Alignment** | LO1 Files + LO2 Hand Code HTML |
| **Status** | Not Started |
| **Evergreen?** | YES — no semester dates, no instructor name |

---

## Student Takeaway

> Students can create a properly named project folder, create an `index.html` file inside it, type the HTML boilerplate from memory, and open it in Live Server.

---

## Shot-by-Shot Outline

| # | Segment | Duration | On-Screen | Narration Script |
|---|---------|----------|-----------|-----------------|
| 1 | The one rule that saves everything | 30s | `GRAPHIC: file-structure-diagram.html` | "Before you write a single line of code, you need to know the rule that prevents 90% of beginner headaches. Every project gets its own folder. Inside that folder, the main file is always called index.html. That name is not optional — it is what browsers look for by default." |
| 2 | File naming rules | 40s | `GRAPHIC: file-naming-rules.html` — shows good vs. bad examples | "Three rules for every file and folder name you create this semester: lowercase only, hyphens instead of spaces, no special characters. 'My Project' becomes 'my-project.' 'About Me' becomes 'about-me.' This matches how professional developers name things and it prevents broken links." |
| 3 | Dr. Q demonstrates the folder structure | 45s | `drQ-Whiteboard.png` alongside `file-structure-diagram.html` | "Here is what your ADD103 folder should look like. One root folder called ADD103. Inside it, a folder for each project — named after the project. Inside each project folder, your index.html. Images go inside the project folder too, not loose in ADD103. If you follow this structure every week, you will never have a 'why is my image broken' moment." |
| 4 | Type the boilerplate live | 90s | Screen recording of VS Code — type the boilerplate from scratch | "Open VS Code. File → New File. Save it immediately as index.html inside your project folder. Now type this — do not copy-paste it. Type it. Every character. Typing it is how you remember it." *(Narrate each line as it appears: doctype, html tag, head, title, body)* |
| 5 | Open in Live Server | 30s | VS Code + browser side by side | "Right-click the file in the Explorer panel. Open with Live Server. Your browser opens. You should see a blank white page — that is correct. That blank page is yours. You built it. Change the title tag, save, watch it update. That is your feedback loop for the rest of the semester." |
| 6 | Dr. Q sends them off | 25s | `drQ-Joy.png` | "That is it. Folder, file, boilerplate, Live Server. Do not skip any of those steps — they are the foundation every future lesson assumes is already done. Head down to the project steps below and build your first page for real." |

---

## Sample Code

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My First Page</title>
</head>
<body>
    <h1>Hello, World</h1>
</body>
</html>
```

---

## Assets Needed

| Asset | File | Notes |
|-------|------|-------|
| File structure diagram | `video_notes/assets/file-structure-diagram.html` | **TO BE CREATED** — see below |
| File naming rules graphic | `video_notes/assets/file-naming-rules.html` | **TO BE CREATED** — see below |
| Dr. Q at whiteboard | `ducktor/drQ-Whiteboard.png` | ✅ Exists — use for segment 3 |
| Dr. Q celebrating | `ducktor/drQ-Joy.png` | ✅ Exists — use for segment 6 |

---

## HTML Graphics to Create

### 1. `video_notes/assets/file-structure-diagram.html`
A dark-background graphic showing the folder tree:
```
ADD103/
├── manifesto/
│   └── index.html
├── about-me/
│   ├── index.html
│   └── images/
└── portfolio/
    ├── index.html
    └── images/
```
Style: dark terminal look (`#121212` background, white monospace font), MCC purple accent (`#582C83`), large enough to read as a screenshot in Gemini.

### 2. `video_notes/assets/file-naming-rules.html`
A two-column graphic — ❌ Bad / ✅ Good examples:

| ❌ Bad | ✅ Good |
|--------|---------|
| `My Project` | `my-project` |
| `About Me.html` | `about-me.html` |
| `INDEX.HTML` | `index.html` |
| `photo 1.jpg` | `photo-1.jpg` |

Style: match the `file-structure-diagram.html` look — dark background, red/green accent for bad/good columns.

---

## Gemini Prompt

Copy and paste this block directly into your Gemini Video prompt:

---

**GEMINI PROMPT — Video 1A-V3:**

You are presenting a short instructional video for a college web development course. Your tone is clear, direct, and practical — like a senior developer explaining something to a new hire on their first day. No fluff. No filler. This audience is mostly first-generation college students and career changers.

Follow this structure exactly:

1. **The one rule (30 seconds):** Every project gets its own folder. The main file inside is always `index.html`. That name is not optional — browsers look for it by default.

2. **File naming rules (40 seconds):** Show the image `file-naming-rules.html` on screen. Three rules: lowercase only, hyphens instead of spaces, no special characters. Explain each with the bad/good examples shown in the graphic.

3. **Folder structure (45 seconds):** Show `drQ-Whiteboard.png` and `file-structure-diagram.html` on screen together. Walk through the ADD103 folder structure. One root folder. One folder per project. `index.html` inside each. Images stay inside their project folder.

4. **Boilerplate typing demo (90 seconds):** Show a screen recording of VS Code. Narrate each line of the HTML boilerplate as it is typed — doctype, html, head, title, body. Emphasize: type it, don't copy it. Typing builds memory.

5. **Live Server proof (30 seconds):** Show VS Code and a browser side by side. Right-click → Open with Live Server. Edit the title tag. Save. Show it update live. Name this the "feedback loop."

6. **Dr. Q sends them off (25 seconds):** Show `drQ-Joy.png` on screen. Send students to the project steps. Reinforce: folder, file, boilerplate, Live Server — in that order, every time.

**Visual assets to upload to Gemini alongside this prompt:**
- `file-structure-diagram.html` — screenshot of folder tree graphic
- `file-naming-rules.html` — screenshot of bad/good naming examples
- `drQ-Whiteboard.png` — Dr. Q at the whiteboard (show during segment 3)
- `drQ-Joy.png` — Dr. Q celebrating (show during segment 6)

**Do not include:**
- Semester names, dates, or instructor names
- Any mention of grades or deadlines
- Anything that would make this video expire at the end of a term

---

## Gemini Settings to Verify Before Recording

| Setting | What to look for |
|---------|-----------------|
| **Presenter / Avatar** | Custom avatar selected, not the default |
| **Voice** | Warm and clear — confirm it matches Video 1 |
| **Aspect ratio** | 16:9 for Canvas/Panopto embed |
| **Captions** | Auto-captions ON (ADA required) |
| **Intro/Outro** | Disable default Gemini branded intro for a clean cut |

---

## Production Notes

- **Evergreen rule:** No semester name, no instructor name, no due dates — this video must work any term
- **Create the two HTML graphics first** (see "HTML Graphics to Create" above) before recording
- **Screen recording for segment 4:** Gemini may not do live VS Code recording — you may need to record that segment yourself and splice it in, or provide a screenshot sequence
- **Canvas placement:** VIDEO 3 embed in Week 1A lesson page, below Videos 1 and 2
- **Panopto:** Upload final render to Panopto, then embed in Canvas using the Panopto LTI
