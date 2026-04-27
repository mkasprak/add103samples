#!/usr/bin/env python3
"""
Build a Canvas-compatible IMSCC where each lesson HTML file becomes a Canvas Assignment
with URL submission enabled (`online_url`).

Output:
    add103_canvas_assignments.imscc

Import in Canvas:
    Course Settings -> Import Course Content -> Common Cartridge 1.x Package
"""

from __future__ import annotations

import hashlib
import html
import re
import zipfile
from urllib.parse import urljoin
from pathlib import Path
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

BASE_DIR = Path(__file__).parent
OUTPUT_NAME = "add103_canvas_assignments.imscc"

FOLDER_TITLES = {
    "week_01_setup": "Week 1: Setup & Orientation",
    "week_02_structure": "Week 2: HTML Structure",
    "week_03_styling": "Week 3: CSS Basics",
    "week_04_styling_advanced": "Week 4: Advanced Styling",
    "week_05_layout_flexbox": "Week 5: Layout - Flexbox",
    "week_06_layout_grid": "Week 6: Layout - Grid",
    "week_07_layout_responsive": "Week 7: Responsive Layout",
    "week_08_midterm_studio": "Week 8: Midterm Studio",
    "week_09_midterm_review": "Week 9: Midterm Review",
    "week_10_advanced_media": "Week 10: Advanced Media",
    "week_11_interactivity": "Week 11: Interactivity",
    "week_12_deployment": "Week 12: Deployment",
    "week_13_project_planning": "Week 13: Project Planning",
    "week_14_project_build_structure": "Week 14: Project Build - Structure",
    "week_15_project_build_polish": "Week 15: Project Build - Polish",
    "week_16_finals": "Week 16: Finals",
}

ASSIGNMENT_NS = "http://www.imsglobal.org/xsd/imscc_extensions/assignment"
ASSIGNMENT_XSD = "http://www.imsglobal.org/profile/cc/cc_extensions/cc_extresource_assignmentv1p0_v1p0.xsd"
CANVAS_NS = "http://canvas.instructure.com/xsd/cccv1p0"
CANVAS_XSD = "https://canvas.instructure.com/xsd/cccv1p0.xsd"


def create_key(seed: str) -> str:
    # Canvas-style IDs are prefixed hashes like i<md5>
    return "i" + hashlib.md5(seed.encode("utf-8")).hexdigest()


def slug_to_title(slug: str) -> str:
    name = re.sub(r"^week_\d+[a-z]?_", "", slug)
    return name.replace("_", " ").title()


def extract_body_html(raw_html: str) -> str:
    match = re.search(r"<body[^>]*>(.*)</body>", raw_html, flags=re.IGNORECASE | re.DOTALL)
    if match:
        return match.group(1).strip()
    return raw_html.strip()


def rewrite_relative_urls(body_html: str, source_rel_path: str) -> str:
    """Rewrite relative src/href URLs to $IMS-CC-FILEBASE$/... for Canvas import safety."""
    base_dir = str(Path(source_rel_path).parent).replace("\\", "/")

    def repl(match):
        attr = match.group(1)
        quote = match.group(2)
        url = match.group(3).strip()

        # Leave absolute, data, anchor, and tokenized URLs untouched.
        lowered = url.lower()
        if (
            lowered.startswith(("http://", "https://", "mailto:", "tel:", "data:", "#"))
            or "$ims-cc-filebase$" in lowered
            or lowered.startswith("/")
        ):
            return match.group(0)

        joined = urljoin(f"{base_dir}/", url)
        joined = joined.replace("\\", "/")
        return f'{attr}={quote}$IMS-CC-FILEBASE$/{joined}{quote}'

    return re.sub(r'(href|src)\s*=\s*(["\'])([^"\']+)\2', repl, body_html, flags=re.IGNORECASE)


def collect_week_html():
    weeks = []
    for d in sorted(BASE_DIR.iterdir()):
        if not d.is_dir() or not d.name.startswith("week_"):
            continue
        html_files = sorted(d.glob("*.html"))
        if html_files:
            weeks.append((d.name, html_files))
    return weeks


def build_assignment_xml(assignment_id: str, title: str, body_html: str, points: float, position: int) -> str:
    esc_title = html.escape(title)

    xml = f'''<?xml version="1.0" encoding="UTF-8"?>
<assignment identifier="{assignment_id}"
  xmlns="{ASSIGNMENT_NS}"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="{ASSIGNMENT_NS} {ASSIGNMENT_XSD}">
  <title>{esc_title}</title>
  <text texttype="text/html"><![CDATA[{body_html}]]></text>
  <gradable points_possible="{points:.1f}">true</gradable>
  <submission_formats>
    <format type="url"/>
  </submission_formats>
  <extensions>
    <assignment identifier="{assignment_id}_canvas"
      xmlns="{CANVAS_NS}"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="{CANVAS_NS} {CANVAS_XSD}">
      <title>{esc_title}</title>
      <workflow_state>unpublished</workflow_state>
      <submission_types>online_url</submission_types>
      <grading_type>points</grading_type>
      <points_possible>{points:.1f}</points_possible>
      <position>{position}</position>
      <peer_reviews>false</peer_reviews>
      <automatic_peer_reviews>false</automatic_peer_reviews>
      <anonymous_peer_reviews>false</anonymous_peer_reviews>
    </assignment>
  </extensions>
</assignment>
'''
    return xml


def build_manifest(course_title: str, weeks_payload):
    manifest = Element(
        "manifest",
        {
            "identifier": create_key("common_cartridge_add103"),
            "xmlns": "http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1",
            "xmlns:lom": "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/resource",
            "xmlns:lomimscc": "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/manifest",
            "xmlns:cpx": "http://www.imsglobal.org/xsd/imsccv1p3/imscp_extensionv1p2",
            "xmlns:xsi": "http://www.w3.org/2001/XMLSchema-instance",
            "xsi:schemaLocation": (
                "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/resource "
                "http://www.imsglobal.org/profile/cc/ccv1p3/LOM/ccv1p3_lomresource_v1p0.xsd "
                "http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1 "
                "http://www.imsglobal.org/profile/cc/ccv1p3/ccv1p3_imscp_v1p2_v1p0.xsd "
                "http://ltsc.ieee.org/xsd/imsccv1p3/LOM/manifest "
                "http://www.imsglobal.org/profile/cc/ccv1p3/LOM/ccv1p3_lommanifest_v1p0.xsd "
                "http://www.imsglobal.org/xsd/imsccv1p3/imscp_extensionv1p2 "
                "http://www.imsglobal.org/profile/cc/ccv1p3/ccv1p3_cpextensionv1p2_v1p0.xsd"
            ),
        },
    )

    metadata = SubElement(manifest, "metadata")
    SubElement(metadata, "schema").text = "IMS Common Cartridge"
    SubElement(metadata, "schemaversion").text = "1.3.0"

    lom = SubElement(metadata, "lomimscc:lom")
    general = SubElement(lom, "lomimscc:general")
    title = SubElement(general, "lomimscc:title")
    SubElement(title, "lomimscc:string").text = course_title

    orgs = SubElement(manifest, "organizations")
    org = SubElement(orgs, "organization", {"identifier": "org_1", "structure": "rooted-hierarchy"})
    root_item = SubElement(org, "item", {"identifier": "root"})
    SubElement(root_item, "title").text = course_title

    resources = SubElement(manifest, "resources")

    for week_name, week_items in weeks_payload:
        week_id = f"mod_{week_name}"
        week_title = FOLDER_TITLES.get(week_name, week_name.replace("_", " ").title())
        week_item = SubElement(root_item, "item", {"identifier": week_id})
        SubElement(week_item, "title").text = week_title

        for row in week_items:
            assignment_id = row["assignment_id"]
            fallback_id = row["fallback_id"]
            assignment_xml_rel = row["assignment_xml_rel"]
            fallback_html_rel = row["fallback_html_rel"]
            source_html_rel = row["source_html_rel"]
            title_text = row["title"]
            source_res_id = row["source_res_id"]

            item = SubElement(
                week_item,
                "item",
                {"identifier": f"item_{assignment_id}", "identifierref": assignment_id},
            )
            SubElement(item, "title").text = title_text

            # Primary assignment resource
            res_assign = SubElement(
                resources,
                "resource",
                {"identifier": assignment_id, "type": "assignment_xmlv1p0", "href": assignment_xml_rel},
            )
            SubElement(res_assign, "file", {"href": assignment_xml_rel})

            # Fallback webcontent resource (matches Canvas export pattern)
            res_fallback = SubElement(
                resources,
                "resource",
                {"identifier": fallback_id, "type": "webcontent"},
            )
            variant = SubElement(
                res_fallback,
                "cpx:variant",
                {"identifier": f"{assignment_id}_variant", "identifierref": assignment_id},
            )
            SubElement(variant, "cpx:metadata")
            SubElement(res_fallback, "file", {"href": fallback_html_rel})

            # Original source lesson HTML as an importable file resource
            res_source = SubElement(
                resources,
                "resource",
                {"identifier": source_res_id, "type": "webcontent", "href": source_html_rel},
            )
            SubElement(res_source, "file", {"href": source_html_rel})

    xml_str = tostring(manifest, encoding="unicode")
    pretty = minidom.parseString(xml_str).toprettyxml(indent="  ", encoding="UTF-8")
    return pretty.decode("utf-8")


def main():
    weeks = collect_week_html()
    if not weeks:
        raise SystemExit("No week_*/.html files found.")

    weeks_payload = []
    position_counter = 1

    for week_name, html_files in weeks:
        week_items = []
        for html_path in html_files:
            rel = html_path.relative_to(BASE_DIR).as_posix()
            stem = html_path.stem
            title = slug_to_title(stem)
            assignment_id = create_key(f"assignment::{rel}")
            fallback_id = assignment_id + "_fallback"
            source_res_id = create_key(f"source::{rel}")

            assignment_dir = assignment_id
            assignment_xml_rel = f"{assignment_dir}/assignment.xml"
            fallback_html_rel = f"{assignment_dir}/{stem}.html"

            raw_html = html_path.read_text(encoding="utf-8", errors="replace")
            lesson_body = extract_body_html(raw_html)
            lesson_body = rewrite_relative_urls(lesson_body, rel)

            # Keep assignment instructions clear and include the full lesson body directly.
            assignment_body = (
                f"<h2>{html.escape(title)}</h2>"
                "<p><strong>Submission:</strong> Submit a URL to your published work.</p>"
                f"<p><strong>Source lesson file:</strong> <a href=\"$IMS-CC-FILEBASE$/{rel}\">Open original lesson file</a></p>"
                f"{lesson_body}"
            )

            assignment_xml = build_assignment_xml(
                assignment_id=assignment_id,
                title=title,
                body_html=assignment_body,
                points=10.0,
                position=position_counter,
            )
            position_counter += 1

            # Fallback HTML used by non-assignment-aware importers
            fallback_html = (
                "<!doctype html><html><head><meta charset=\"utf-8\">"
                f"<title>{html.escape(title)}</title></head><body>"
                f"{assignment_body}</body></html>"
            )

            week_items.append(
                {
                    "title": title,
                    "assignment_id": assignment_id,
                    "fallback_id": fallback_id,
                    "source_res_id": source_res_id,
                    "source_html_rel": rel,
                    "assignment_xml_rel": assignment_xml_rel,
                    "fallback_html_rel": fallback_html_rel,
                    "assignment_xml": assignment_xml,
                    "fallback_html": fallback_html,
                    "source_path": html_path,
                    "source_parent": html_path.parent,
                }
            )
        weeks_payload.append((week_name, week_items))

    manifest_xml = build_manifest("ADD 103: Canvas Assignments (URL Submission)", weeks_payload)

    out_path = BASE_DIR / OUTPUT_NAME
    with zipfile.ZipFile(out_path, "w", zipfile.ZIP_DEFLATED) as zf:
        added_paths = set()

        def add_file(path_obj, arcname):
            if arcname in added_paths:
                return
            zf.write(path_obj, arcname)
            added_paths.add(arcname)

        def add_text(arcname, content):
            if arcname in added_paths:
                return
            zf.writestr(arcname, content)
            added_paths.add(arcname)

        add_text("imsmanifest.xml", manifest_xml)

        for _, week_items in weeks_payload:
            for row in week_items:
                add_text(row["assignment_xml_rel"], row["assignment_xml"])
                add_text(row["fallback_html_rel"], row["fallback_html"])
                add_file(row["source_path"], row["source_html_rel"])

                # Include sibling assets so linked content renders after import.
                for asset in sorted(row["source_parent"].iterdir()):
                    if not asset.is_file() or asset == row["source_path"]:
                        continue
                    if asset.name.lower() == ".ds_store":
                        continue
                    # All lesson HTML files are added in the primary pass.
                    if asset.suffix.lower() == ".html":
                        continue
                    rel_asset = asset.relative_to(BASE_DIR).as_posix()
                    add_file(asset, rel_asset)

    total = sum(len(items) for _, items in weeks_payload)
    size_kb = out_path.stat().st_size // 1024
    print(f"Created {OUTPUT_NAME} ({size_kb} KB)")
    print(f"Assignments: {total}")
    print("Submission type: online_url")


if __name__ == "__main__":
    main()
