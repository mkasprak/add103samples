#!/usr/bin/env python3
"""
build_imscc.py — Packages this course into a Canvas-compatible IMS Common Cartridge (.imscc)

Usage:
    python3 build_imscc.py

Output:
    add103_course.imscc   (importable into Canvas via Settings > Import Course Content)

How Canvas handles webcontent HTML files:
  - They appear under Files in the course.
  - Each week becomes a Module; each HTML file becomes a Module Item linking to its file.
  - All internal links between pages are preserved because relative paths remain intact.
"""

import os
import re
import zipfile
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

BASE_DIR = Path(__file__).parent

# Folders to exclude from the package
EXCLUDE_DIRS = {"_COURSE_GENESIS", "_Jeanie_Specs", "documentation", "samples", ".git"}

# Human-readable folder titles
FOLDER_TITLES = {
    "week_01_setup":                  "Week 1: Setup & Orientation",
    "week_02_structure":              "Week 2: HTML Structure",
    "week_03_styling":                "Week 3: CSS Basics",
    "week_04_styling_advanced":       "Week 4: Advanced Styling",
    "week_05_layout_flexbox":         "Week 5: Layout — Flexbox",
    "week_06_layout_grid":            "Week 6: Layout — Grid",
    "week_07_layout_responsive":      "Week 7: Responsive Layout",
    "week_08_midterm_studio":         "Week 8: Midterm Studio (Open Lab)",
    "week_09_midterm_review":         "Week 9: Midterm Review & Critique",
    "week_10_advanced_media":         "Week 10: Advanced Media",
    "week_11_interactivity":          "Week 11: Interactivity & Animation",
    "week_12_deployment":             "Week 12: Deployment & Site Audit",
    "week_13_project_planning":       "Week 13: Final Project Planning",
    "week_14_project_build_structure":"Week 14: Final Project Build — Structure",
    "week_15_project_build_polish":   "Week 15: Final Project Build — Polish",
    "week_16_finals":                 "Week 16: Finals",
}


def slug_to_title(slug: str) -> str:
    """Convert a filename slug like 'week_1a_welcome' to 'Welcome'."""
    # Strip leading week prefix (e.g. week_1a_, week_10b_)
    name = re.sub(r"^week_\d+[a-z]?_", "", slug)
    # Replace underscores with spaces and title-case
    return name.replace("_", " ").title()


def build_manifest(week_folders):
    """Return a pretty-printed imsmanifest.xml string."""
    NS_CP  = "http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1"
    NS_LOM = "http://ltsc.ieee.org/xsd/imsccv1p1/LOM/manifest"
    NS_XSI = "http://www.w3.org/2001/XMLSchema-instance"
    SCHEMA_LOC = (
        "http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1 "
        "http://www.imsglobal.org/profile/cc/ccv1p1/ccv1p1_imscp_v1p2_v1p0.xsd"
    )

    manifest = Element("manifest", {
        "identifier": "add103_manifest",
        "xmlns": NS_CP,
        "xmlns:lom": NS_LOM,
        "xmlns:xsi": NS_XSI,
        "xsi:schemaLocation": SCHEMA_LOC,
    })

    # --- metadata ---
    meta = SubElement(manifest, "metadata")
    SubElement(meta, "schema").text = "IMS Common Cartridge"
    SubElement(meta, "schemaversion").text = "1.1.0"
    lom = SubElement(meta, "lom:lom")
    general = SubElement(lom, "lom:general")
    title_el = SubElement(general, "lom:title")
    SubElement(title_el, "lom:string").text = "ADD 103: Web Design Fundamentals"

    # --- organizations ---
    orgs = SubElement(manifest, "organizations")
    org = SubElement(orgs, "organization", {"identifier": "org_1", "structure": "rooted-hierarchy"})
    root_item = SubElement(org, "item", {"identifier": "root"})

    # --- resources ---
    resources = SubElement(manifest, "resources")

    resource_entries = []  # [(res_id, rel_path)]

    for folder_name, html_files in week_folders:
        module_id = f"mod_{folder_name}"
        module_title = FOLDER_TITLES.get(folder_name, folder_name.replace("_", " ").title())

        mod_item = SubElement(root_item, "item", {"identifier": module_id})
        SubElement(mod_item, "title").text = module_title

        for html_path in html_files:
            stem = html_path.stem
            res_id = f"res_{stem}"
            rel = html_path.relative_to(BASE_DIR).as_posix()

            item = SubElement(mod_item, "item", {
                "identifier": f"item_{stem}",
                "identifierref": res_id,
            })
            SubElement(item, "title").text = slug_to_title(stem)

            resource_entries.append((res_id, rel, html_path))

    # Write resource elements
    for res_id, rel, html_path in resource_entries:
        res = SubElement(resources, "resource", {
            "identifier": res_id,
            "type": "webcontent",
            "href": rel,
        })
        SubElement(res, "file", {"href": rel})

        # Include any sibling assets in the same folder (css, js, images, etc.)
        # that aren't already declared as their own resources
        parent = html_path.parent
        for asset in sorted(parent.iterdir()):
            if asset.is_file() and asset.suffix.lower() in {
                ".css", ".js", ".png", ".jpg", ".jpeg", ".gif", ".svg",
                ".webp", ".woff", ".woff2", ".ttf", ".ico",
            }:
                asset_rel = asset.relative_to(BASE_DIR).as_posix()
                SubElement(res, "file", {"href": asset_rel})

    # Pretty-print
    raw = tostring(manifest, encoding="unicode")
    dom = minidom.parseString(raw)
    return dom.toprettyxml(indent="  ", encoding="UTF-8").decode("UTF-8")


def collect_weeks():
    """Return ordered list of (folder_name, [sorted html Paths])."""
    week_dirs = sorted(
        d for d in BASE_DIR.iterdir()
        if d.is_dir() and d.name.startswith("week_") and d.name not in EXCLUDE_DIRS
    )
    result = []
    for d in week_dirs:
        html_files = sorted(d.glob("*.html"))
        if html_files:
            result.append((d.name, html_files))
    return result


def build_imscc(output_name="add103_course.imscc"):
    week_folders = collect_weeks()
    manifest_xml = build_manifest(week_folders)

    output_path = BASE_DIR / output_name
    with zipfile.ZipFile(output_path, "w", zipfile.ZIP_DEFLATED) as zf:
        # Write manifest at root of ZIP
        zf.writestr("imsmanifest.xml", manifest_xml)

        # Write all HTML files and their folder assets
        added = set()
        for folder_name, html_files in week_folders:
            folder_path = BASE_DIR / folder_name
            for f in sorted(folder_path.iterdir()):
                if f.is_file() and f.suffix.lower() not in {".ds_store"}:
                    rel = f.relative_to(BASE_DIR).as_posix()
                    if rel not in added:
                        zf.write(f, rel)
                        added.add(rel)

    size_kb = output_path.stat().st_size // 1024
    print(f"✓  Created {output_name}  ({size_kb} KB)")
    print(f"   {len(week_folders)} modules, "
          f"{sum(len(h) for _, h in week_folders)} HTML pages")
    print()
    print("To import into Canvas:")
    print("  Course Settings → Import Course Content → Common Cartridge 1.x Package")
    print(f"  Upload: {output_name}")


if __name__ == "__main__":
    build_imscc()
