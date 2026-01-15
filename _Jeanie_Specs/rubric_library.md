# 📊 The Grading Rubric Library

Use these standard rows to build consistent rubrics for Canvas Lessons. Use the **zebra striping** pattern (white / #f9f9f9) when stacking them.

## 🛠️ General Quality
| Row Type | HTML |
| :--- | :--- |
| **Documentation** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Documentation</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Full PEP 8 compliance; docstrings and snake_case throughout.</td><td style="padding: 10px; border: 1px solid #ddd;">Naming is inconsistent or comments are sparse.</td><td style="padding: 10px; border: 1px solid #ddd;">Code is unreadable or messily formatted.</td></tr>` |
| **Resilience** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Resilience</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Successfully uses try/except to prevent common crashes (e.g. ValueError).</td><td style="padding: 10px; border: 1px solid #ddd;">Try block used but logic is flawed or handling is generic.</td><td style="padding: 10px; border: 1px solid #ddd;">Program crashes on bad input.</td></tr>` |
| **Architecture** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Architecture</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Successfully uses the main pattern and global constants/Scope correctly.</td><td style="padding: 10px; border: 1px solid #ddd;">Used main but scope is leaking or constants are local.</td><td style="padding: 10px; border: 1px solid #ddd;">No clear architectural structure.</td></tr>` |

## 🧩 Concepts
| Row Type | HTML |
| :--- | :--- |
| **Functions** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Function Logic</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Definitions are perfect; functions return values and use multiple parameters correctly.</td><td style="padding: 10px; border: 1px solid #ddd;">Functions used but return logic is missing or parameters are mismatched.</td><td style="padding: 10px; border: 1px solid #ddd;">No functions used. Logic is a single wall of code.</td></tr>` |
| **Lists/Dicts** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Data Structures</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Appropriately uses Dictionaries or Lists to store data efficiently.</td><td style="padding: 10px; border: 1px solid #ddd;">Data structure used but inefficiently (e.g., parallel lists instead of dicts).</td><td style="padding: 10px; border: 1px solid #ddd;">Hard-coded variables used instead of structures.</td></tr>` |
| **File I/O** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Data Persistence</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Seamlessly reads from and writes to external .txt files.</td><td style="padding: 10px; border: 1px solid #ddd;">File I/O works but connection handling is inconsistent.</td><td style="padding: 10px; border: 1px solid #ddd;">Files not used or program crashes on file error.</td></tr>` |
| **OOP (Classes)** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>OOP Structure</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Class encapsulates data (Attributes) and behavior (Methods) logically.</td><td style="padding: 10px; border: 1px solid #ddd;">Class exists but methods are merely functions inside it (no self usage).</td><td style="padding: 10px; border: 1px solid #ddd;">No Class defined.</td></tr>` |
| **Inheritance** | `<tr><td style="padding: 10px; border: 1px solid #ddd;"><strong>Inheritance</strong></td><td style="padding: 10px; border: 1px solid #ddd;">Complex use of Inheritance, super(), and specialized child attributes.</td><td style="padding: 10px; border: 1px solid #ddd;">Classes used but inheritance logic is weak or broken.</td><td style="padding: 10px; border: 1px solid #ddd;">No Inheritance used.</td></tr>` |

## 🎨 Zebra Striping Tip
Add `style="background-color: #f9f9f9;"` to the `<td>` and `<th>` tags for every other row to create the zebra stripe effect.
