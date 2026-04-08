#!/usr/bin/env python3
"""
Detect outdated translations compared to English version.

This script compares modification times between English and translated
documentation files to identify which translations need updating.

Usage:
    python scripts/sync_translations.py
    python scripts/sync_translations.py --lang es
    python scripts/sync_translations.py --lang vi --verbose
"""

import argparse
from datetime import datetime
from pathlib import Path

SUPPORTED_LANGS = ["vi", "zh", "es"]
LANG_NAMES = {"vi": "Vietnamese", "zh": "Chinese", "es": "Spanish"}


def check_translation_status(
    root_path: Path | None = None,
    lang: str = "vi",
    verbose: bool = False,
) -> tuple[list[dict], list[dict]]:
    """
    Compare modification times between English and translated files.

    Args:
        root_path: Root directory of the repository (default: script parent parent)
        lang: Language code to check (e.g. 'vi', 'zh', 'es')
        verbose: Print detailed information

    Returns:
        Tuple of (outdated files, not translated files) with metadata
    """
    if root_path is None:
        root_path = Path(__file__).parent.parent

    # Exclude all translation directories and internal dirs from English files
    exclude_dirs = set(SUPPORTED_LANGS) | {".claude"}

    en_files = [
        f
        for f in root_path.rglob("*.md")
        if not any(f"/{d}/" in str(f) or str(f).startswith(str(root_path / d)) for d in exclude_dirs)
    ]

    # Get translated markdown files
    lang_dir = root_path / lang
    lang_files = list(lang_dir.rglob("*.md")) if lang_dir.exists() else []

    # Build modification time mapping
    en_mtime = {f: f.stat().st_mtime for f in en_files}
    lang_mtime = {f: f.stat().st_mtime for f in lang_files}

    outdated = []
    not_translated = []

    for en_file, en_time in sorted(en_mtime.items()):
        try:
            rel_path = en_file.relative_to(root_path)
        except ValueError:
            if verbose:
                print(f"⚠️  Skipping non-relative file: {en_file}")
            continue

        lang_file = root_path / lang / rel_path

        if lang_file in lang_mtime:
            lang_time = lang_mtime[lang_file]
            if en_time > lang_time:
                outdated.append(
                    {
                        "file": rel_path,
                        "en_mtime": datetime.fromtimestamp(en_time),
                        "lang_mtime": datetime.fromtimestamp(lang_time),
                        "days_diff": (en_time - lang_time) / 86400,
                    }
                )
        else:
            not_translated.append(
                {
                    "file": rel_path,
                    "status": "NOT_TRANSLATED",
                }
            )

    outdated.sort(key=lambda x: x["days_diff"], reverse=True)

    return outdated, not_translated


def format_outdated_table(outdated: list[dict], lang: str) -> str:
    """Format outdated files as a Markdown table."""
    if not outdated:
        return "✅ **No outdated translations found!** All files are up to date.\n"

    lang_upper = lang.upper()
    table = "### 🕰️ Outdated Translations (Need Update)\n\n"
    table += f"| File | Last EN Update | Last {lang_upper} Update | Days Behind |\n"
    table += "|------|----------------|----------------|-------------|\n"

    for item in outdated:
        file_path = str(item["file"])
        en_date = item["en_mtime"].strftime("%Y-%m-%d")
        lang_date = item["lang_mtime"].strftime("%Y-%m-%d")
        days = int(item["days_diff"])

        if len(file_path) > 50:
            file_path = "..." + file_path[-47:]

        table += f"| `{file_path}` | {en_date} | {lang_date} | 🔴 **{days} days** |\n"

    return table


def format_not_translated_table(not_translated: list[dict]) -> str:
    """Format not translated files as a Markdown table."""
    if not not_translated:
        return "\n✅ **All files have been translated!**\n"

    table = "\n### 📝 Not Translated Yet\n\n"
    table += "| File | Status |\n"
    table += "|------|--------|\n"

    for item in not_translated:
        file_path = str(item["file"])

        if len(file_path) > 60:
            file_path = "..." + file_path[-57:]

        table += f"| `{file_path}` | ⏳ **Not translated** |\n"

    return table


def format_summary(outdated: list[dict], not_translated: list[dict]) -> str:
    """Format summary statistics."""
    total_outdated = len(outdated)
    total_not_translated = len(not_translated)
    total_files = total_outdated + total_not_translated

    summary = "## 📊 Summary\n\n"
    summary += f"- **Total files needing attention:** {total_files}\n"
    summary += f"- **Outdated translations:** {total_outdated}\n"
    summary += f"- **Not translated yet:** {total_not_translated}\n"

    if total_outdated > 0:
        most_outdated = max(outdated, key=lambda x: x["days_diff"])
        summary += f"- **Most outdated file:** {most_outdated['file']} ({int(most_outdated['days_diff'])} days behind)\n"

    summary += "\n---\n\n"

    return summary


def main():
    parser = argparse.ArgumentParser(
        description="Check translation status against English version"
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Print detailed information"
    )
    parser.add_argument(
        "--root",
        "-r",
        type=Path,
        default=None,
        help="Root directory of repository (default: auto-detect)",
    )
    parser.add_argument(
        "--lang",
        "-l",
        type=str,
        default="vi",
        choices=SUPPORTED_LANGS,
        help="Language to check (default: vi)",
    )
    parser.add_argument(
        "--update-queue",
        action="store_true",
        help="Update TRANSLATION_QUEUE.md with current status (experimental)",
    )

    args = parser.parse_args()

    root_path = args.root or Path(__file__).parent.parent
    lang = args.lang
    lang_name = LANG_NAMES[lang]

    if args.verbose:
        print(f"🔍 Checking {lang_name} translations in: {root_path}")
        print()

    outdated, not_translated = check_translation_status(root_path, lang, args.verbose)

    print("=" * 60)
    print(f"🌏 {lang_name} Translation Status Report")
    print("=" * 60)
    print()

    total_outdated = len(outdated)
    total_not_translated = len(not_translated)

    if total_outdated == 0 and total_not_translated == 0:
        print("✅ **Congratulations!** All files are up to date.")
        print()
        return

    print(
        f"📊 Found {total_outdated} outdated + {total_not_translated} not translated files"
    )
    print()

    lang_upper = lang.upper()

    if args.verbose and outdated:
        print("🕰️  OUTDATED FILES (need update):")
        print("-" * 60)
        for i, item in enumerate(outdated, 1):
            print(f"{i}. {item['file']}")
            print(f"   EN: {item['en_mtime'].strftime('%Y-%m-%d %H:%M')}")
            print(f"   {lang_upper}: {item['lang_mtime'].strftime('%Y-%m-%d %H:%M')}")
            print(f"   Behind by: {int(item['days_diff'])} days")
            print()

    if args.verbose and not_translated:
        print("📝 NOT TRANSLATED FILES:")
        print("-" * 60)
        for i, item in enumerate(not_translated[:20], 1):
            print(f"{i}. {item['file']}")

        if len(not_translated) > 20:
            print(f"... and {len(not_translated) - 20} more files")
        print()

    print("=" * 60)
    print("📄 Markdown Report (copy to TRANSLATION_QUEUE.md)")
    print("=" * 60)
    print()

    report = format_summary(outdated, not_translated)
    report += format_outdated_table(outdated, lang)
    report += format_not_translated_table(not_translated)

    print(report)

    if args.update_queue and args.verbose:
        print("⚠️  --update-queue is experimental and not yet implemented")
        print("   Please manually update TRANSLATION_QUEUE.md")


if __name__ == "__main__":
    main()
