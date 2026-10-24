"""Bundle notes/*.md into assets/notes.js so the site works on Vercel and when index.html is opened directly.

Run after editing any note:  python3 build.py
"""
import json
import pathlib
import re

ROOT = pathlib.Path(__file__).parent
NOTES = ROOT / "notes"

# Sidebar order and short labels. Any new .md file not listed here is appended at the end.
ORDER = [
    # (slug, sidebar label, tag, group)
    ("README", "About these notes", "", "start"),
    ("rapid-revision", "Rapid Revision", "★", "start"),
    ("exam-playbook", "Exam Playbook", "EX", "focus"),
    ("pyq-trishul", "Past Paper: Trishul", "PYQ", "focus"),
    ("pyq-kaveri", "Past Paper: Kaveri Motors", "PYQ", "focus"),
    ("chain-reaction-playbook", "Chain Reaction Playbook", "CR", "focus"),
    ("course-frameworks", "All 37 Course Frameworks", "FW", "focus"),
    ("numericals", "Numericals (50 worked)", "#", "focus"),
    ("case-library", "Case Library", "CS", "focus"),
    ("ch00-scm-fundamentals", "SCM Fundamentals", "00", "chapters"),
    ("ch01-ai-in-operations-and-scm", "AI in Ops & SCM", "01", "chapters"),
    ("ch02-ai-readiness-data-technology", "Readiness: Data & Tech", "02", "chapters"),
    ("ch03-ai-readiness-process-organisation", "Readiness: Process & Org", "03", "chapters"),
    ("ch04-agentic-ai-systems", "Agentic AI Systems", "04", "chapters"),
    ("ch05-ai-platforms", "AI Platforms", "05", "chapters"),
    ("ch06-machine-learning-for-operations", "ML for Operations", "06", "chapters"),
    ("ch07-demand-forecasting", "Demand Forecasting", "07", "chapters"),
    ("ch08-inventory-optimisation", "Inventory Optimisation", "08", "chapters"),
    ("ch09-predictive-maintenance-digital-twins", "Maintenance & Digital Twins", "09", "chapters"),
    ("ch10-logistics-routing-optimisation", "Logistics & Optimisation", "10", "chapters"),
    ("ch11-nlp-procurement-token-economics", "NLP Procurement & Tokens", "11", "chapters"),
    ("ch12-genai-design-multi-agent", "GenAI Design & Multi-Agent", "12", "chapters"),
    ("ch13-responsible-ai-ethics", "Responsible AI & Debrief", "13", "chapters"),
    ("practice-cases", "Mock Papers (3)", "MOCK", "practice"),
    ("exam-questions-qna", "Exam Q&A Bank", "Q&A", "practice"),
    ("mcq-bank", "MCQ Bank", "MCQ", "practice"),
    ("glossary", "Glossary A–Z", "A–Z", "practice"),
]


def first_heading(md: str, fallback: str) -> str:
    m = re.search(r"^#\s+(.+)$", md, re.M)
    return m.group(1).strip() if m else fallback


def main() -> None:
    files = {p.stem: p for p in NOTES.glob("*.md")}
    entries = []
    for slug, label, tag, group in ORDER:
        if slug in files:
            md = files.pop(slug).read_text(encoding="utf-8")
            entries.append({"slug": slug, "label": label, "tag": tag, "group": group, "title": first_heading(md, label), "md": md})
    for slug, path in sorted(files.items()):
        md = path.read_text(encoding="utf-8")
        title = first_heading(md, slug)
        entries.append({"slug": slug, "label": title, "tag": "", "group": "practice", "title": title, "md": md})

    out = ROOT / "assets" / "notes.js"
    out.write_text("window.NOTES = " + json.dumps(entries, ensure_ascii=False) + ";\n", encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} with {len(entries)} notes")


if __name__ == "__main__":
    main()
