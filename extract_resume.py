"""One-off helper: extract text from the active resume PDF into a plain-text file.

Used to keep the rulebook / config in sync with the candidate's real resume.
Usage: python extract_resume.py
"""

import sys

import fitz

PDF_PATH = "docs/Rahul_Pal_Resume_Latest.pdf"
OUT_PATH = "resume_extracted.txt"


def main() -> int:
    doc = fitz.open(PDF_PATH)
    chunks = []
    for index, page in enumerate(doc, start=1):
        chunks.append("=== PAGE %d ===\n%s" % (index, page.get_text()))
    with open(OUT_PATH, "w", encoding="utf-8") as handle:
        handle.write("\n".join(chunks))
    print("wrote %s (%d pages)" % (OUT_PATH, doc.page_count))
    return 0


if __name__ == "__main__":
    sys.exit(main())
