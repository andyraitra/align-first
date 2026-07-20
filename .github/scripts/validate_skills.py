#!/usr/bin/env python3
"""Validate every skills/*/SKILL.md has correct frontmatter.

Checks, per skill:
  - file exists
  - frontmatter delimited by --- ... ---
  - `name`: present, lowercase letters/numbers/hyphens only
  - `description`: present, starts with "Use when"

No third-party deps — runs on a bare runner. Exit 1 on any failure.
"""
import glob
import os
import re
import sys

FRONTMATTER = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def parse_frontmatter(text):
    m = FRONTMATTER.match(text)
    if not m:
        return None
    fields = {}
    for line in m.group(1).splitlines():
        if ":" in line and not line.startswith((" ", "\t")):
            key, _, val = line.partition(":")
            fields[key.strip()] = val.strip()
    return fields


def main():
    skills = sorted(glob.glob("skills/*/SKILL.md"))
    if not skills:
        print("::error::no skills/*/SKILL.md found")
        return 1

    errors = []
    for path in skills:
        with open(path, encoding="utf-8") as f:
            text = f.read()

        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{path}: missing or malformed frontmatter (--- ... ---)")
            continue

        name = fm.get("name")
        if not name:
            errors.append(f"{path}: missing `name`")
        elif not NAME_RE.match(name):
            errors.append(f"{path}: `name` must be lowercase letters/numbers/hyphens (got '{name}')")
        else:
            folder = os.path.basename(os.path.dirname(path))
            if name != folder:
                errors.append(f"{path}: `name` '{name}' should match folder '{folder}'")

        desc = fm.get("description")
        if not desc:
            errors.append(f"{path}: missing `description`")
        elif not desc.startswith("Use when"):
            errors.append(f"{path}: `description` should start with 'Use when' (got '{desc[:40]}...')")

    if errors:
        for e in errors:
            print(f"::error::{e}")
        print(f"\n{len(errors)} problem(s) across {len(skills)} skill(s).")
        return 1

    print(f"OK — {len(skills)} skill(s) valid:")
    for path in skills:
        print(f"  - {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
