# 📊 The Grading Rubric Library

Use these standard rows to build consistent rubrics for Canvas Lessons. Use the **zebra striping** pattern (white / #f9f9f9) when stacking them.

## 🛠️ General Quality
| Row Type | HTML |
| :--- | :--- |
| **Documentation** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Documentation</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Full PEP 8 compliance; docstrings and snake_case throughout.</td><td style="padding: 10px; border: 1px solid #ddd;">Naming is inconsistent or comments are sparse.</td><td style="padding: 10px; border: 1px solid #ddd;">Code is unreadable or messily formatted.</td></tr>` |
| **Resilience** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Resilience</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Successfully uses try/except to prevent common crashes (e.g. ValueError).</td><td style="padding: 10px; border: 1px solid #ddd;">Try block used but logic is flawed or handling is generic.</td><td style="padding: 10px; border: 1px solid #ddd;">Program crashes on bad input.</td></tr>` |
| **Architecture** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Architecture</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Successfully uses the main pattern and global constants/Scope correctly.</td><td style="padding: 10px; border: 1px solid #ddd;">Used main but scope is leaking or constants are local.</td><td style="padding: 10px; border: 1px solid #ddd;">No clear architectural structure.</td></tr>` |

## 🎨 Zebra Striping Tip
Add `style="background-color: #f9f9f9;"` to the `<td>` and `<th>` tags for every other row to create the zebra stripe effect.
