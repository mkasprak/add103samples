# 🎓 MCC E-Portfolio Emoji System — ADD-103 Reference

**Source:** MCC Institutional Standard (All Courses)
**Maintained by:** Jeanie & Meri

> These 5 emojis are **standardized across all MCC courses**. Faculty place them on assignments they believe demonstrate the corresponding general education goal. Students use them to identify and collect work for their e-portfolio.
> 
> In Canvas, students can **search for these emojis** to quickly find qualifying assignments when building their e-portfolio.

---

## 📋 The 5 Official Emojis

| Emoji | Goal | Full Definition |
|-------|------|-----------------|
| 💡 | **Critical Thinking** | The thorough and ongoing exploration and analysis of issues, ideas, artifacts, information, and events to accept or formulate an argument or conclusion. |
| 📢 | **Effective Communication** | The ability to send and receive a clear message or idea appropriate to a context and audience to increase knowledge, foster understanding, or promote change in attitudes, values, beliefs, or behaviors. |
| 📚 | **Information Literacy** | The ability to recognize when information is needed, locate information, evaluate information, and use information effectively and ethically. |
| 📊 | **Quantitative Reasoning** | The application of mathematical processes to reach solutions or conclusions and to understand the interrelated nature of numerical information. It is the ability to acquire, analyze, use, and represent numerical information symbolically, visually, or verbally. |
| 🌎 | **Social Responsibility** | The ability to seek out diverse perspectives related to communal issues and/or cultivate leadership and collaborative practices in the service of the broader community. |

---

## 📣 Student-Facing Blurb
*Copy this HTML block into any Canvas page that contains an e-portfolio emoji, placed directly above the rubric.*

```html
<!-- EPORTFOLIO INDICATOR — place above rubric when applicable -->
<div style="background-color: #fff8e1; border: 2px solid #FFC629; border-radius: 8px; padding: 15px 20px; margin: 20px 0;">
  <strong style="color: #582C83; font-size: 1.05rem;">🎓 E-Portfolio Eligible Assignment</strong>
  <p style="margin: 8px 0 4px 0; font-size: 0.95rem;">This assignment has been identified by your instructor as a strong example of one or more MCC General Education goals:</p>
  <ul style="margin: 8px 0; font-size: 0.95rem;">
    <!-- Include only the applicable lines below -->
    <li>💡 <strong>Critical Thinking</strong></li>
    <li>📢 <strong>Effective Communication</strong></li>
    <li>📚 <strong>Information Literacy</strong></li>
    <li>📊 <strong>Quantitative Reasoning</strong></li>
    <li>🌎 <strong>Social Responsibility</strong></li>
  </ul>
  <p style="margin: 8px 0 0 0; font-size: 0.9rem; color: #555;">Consider saving your completed work for your e-portfolio. If you have questions about why this assignment qualifies, ask your instructor.</p>
</div>
```

---

## 🗓️ ADD-103 Assignment Eligibility Map

> **Rule:** No assignments in Weeks 1–4 are eligible (too foundational/toolchain-focused).
> **Process:** Review each assignment starting Week 5. If it qualifies, add the HTML block above the rubric and note it here.

| Week | Assignment | Emoji(s) | Notes |
|------|-----------|----------|-------|
| 1–4 | All | ❌ None | Foundational setup weeks — not eligible |
| 5A | Typography System | — | *To be reviewed* |
| 5B | Color Palette + Contrast | — | *To be reviewed* |
| 6A | Box Model DevTools | — | *To be reviewed* |
| 6B | Positioning Demo | — | *To be reviewed* |
| 7A | FTP + Live Deploy | — | *To be reviewed* |
| 8A | WAVE Accessibility Audit | — | *To be reviewed* |
| 8B | Midterm Project | — | *To be reviewed* |
| 9–11 | Layout assignments | — | *To be reviewed* |
| 12–13 | Bootstrap + AI Audit | — | *To be reviewed* |
| 14–16 | Final Portfolio | — | *To be reviewed* |

---

## 💭 Likely Candidates (Preliminary)

| Assignment | Likely Emoji(s) | Rationale |
|-----------|----------------|-----------|
| WAVE Accessibility Audit (8A) | 🌎 Social Responsibility | Accessibility = designing for the broader community |
| AI Output Audit & Refactor (13B) | 💡 Critical Thinking | Analyzing, evaluating, and arguing against AI-generated code |
| Final Portfolio (14–16) | 📢 Effective Communication | The portfolio *is* a communication artifact |
| Writing for the Web (3A) | 📢 Effective Communication | Audience awareness, clarity, scannable writing |
| SEO & Metadata (3A) | 📚 Information Literacy | Understanding how information is found and structured |
| AI Tools Overview (13A) | 📚 Information Literacy | Evaluating AI-generated information critically |

---

## ⚙️ Implementation Instructions for Jeanie

1. **Do not add the e-portfolio block to any Week 1–4 pages.**
2. **Starting Week 5**, when building or reviewing an assignment, check if it meets one of the 5 goals.
3. If it qualifies, insert the HTML block (from the section above) **directly above the rubric table**.
4. Delete the `<li>` lines for emojis that do NOT apply — only list the ones that do.
5. Update the eligibility map table in this file.
6. The emoji(s) should also appear **in the assignment title** in Canvas (e.g., `Week 8A: WAVE Audit 🌎`).
