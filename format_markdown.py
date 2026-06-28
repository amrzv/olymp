from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


ANSWER_SUMMARY = "Відповідь"
SOLUTION_SUMMARY = "Розв’язання"


MATH_REPLACEMENTS = (
    (r"\Longrightarrow", r"\implies"),
    (r"\Rightarrow", r"\implies"),
    (r"\Longleftrightarrow", r"\iff"),
    (r"\Leftrightarrow", r"\iff"),
    ("\u21d2", r"\implies"),
    ("\u27f9", r"\implies"),
    ("\u21d4", r"\iff"),
    ("\u27fa", r"\iff"),
    ("\u2192", r"\to"),
    ("\u2264", r"\le"),
    ("\u2265", r"\ge"),
    ("\u2260", r"\neq"),
    ("\u00b1", r"\pm"),
    ("\u2212", "-"),
    ("\u2013", "-"),
    ("\u00d7", r"\times"),
    ("\u22c5", r"\cdot"),
    ("\u2026", r"\ldots"),
    ("\u2208", r"\in"),
    ("\u2209", r"\notin"),
    ("\u2200", r"\forall"),
    ("\u2203", r"\exists"),
    ("\u221e", r"\infty"),
)


@dataclass
class Issue:
    path: Path
    line: int
    message: str


@dataclass
class FormatResult:
    text: str
    issues: list[Issue]


def line_at(text: str, offset: int) -> int:
    return text.count("\n", 0, max(0, offset)) + 1


def is_escaped(text: str, index: int) -> bool:
    slash_count = 0
    i = index - 1
    while i >= 0 and text[i] == "\\":
        slash_count += 1
        i -= 1
    return slash_count % 2 == 1


def normalize_plain(text: str) -> str:
    text = text.replace("\u2116 ", "\u2116")
    text = re.sub("озв'яз", "озв’яз", text)
    # text = re.sub(r"\b\u0440\u043e\u0437\u0432'\u044f\u0437", "\u0440\u043e\u0437\u0432\u2019\u044f\u0437", text)
    # text = text.replace(
    #     "<summary>\u0420\u043e\u0437\u0432'\u044f\u0437\u0430\u043d\u043d\u044f</summary>",
    #     f"<summary>{SOLUTION_SUMMARY}</summary>",
    # )
    return text


def strip_delimiter_inner_spaces(content: str) -> str:
    left_right_delim = r"(?:\\[{}]|\\langle|\\rangle|[()\[\]{}|.])"

    for _ in range(3):
        content = re.sub(rf"(\\left{left_right_delim})[ \t]+", r"\1", content)
        content = re.sub(rf"[ \t]+(\\right{left_right_delim})", r"\1", content)
        content = re.sub(r"(?<!\\)([({\[])[ \t]+", r"\1", content)
        content = re.sub(r"[ \t]+([)}\]])", r"\1", content)
        content = re.sub(r"(\\\{)[ \t]+", r"\1", content)
        content = re.sub(r"[ \t]+(\\\})", r"\1", content)
        content = re.sub(r"(\\langle)[ \t]+", r"\1", content)
        content = re.sub(r"[ \t]+(\\rangle)", r"\1", content)
        content = re.sub(r"(?<!\\)\|[ \t]*([^|\n]*?\S)[ \t]*(?<!\\)\|", r"|\1|", content)

    return content


def normalize_math(content: str, *, display: bool) -> str:
    if not display:
        content = content.strip()

    for before, after in MATH_REPLACEMENTS:
        content = content.replace(before, after)

    content = content.replace(r"\not =", r"\neq")
    content = re.sub(r"\\Delta\s+([A-Z][A-Z0-9_{}]*)", r"\\triangle \1", content)
    content = re.sub(r"\\geq(?![A-Za-z])", r"\\ge", content)
    content = re.sub(r"\\leq(?![A-Za-z])", r"\\le", content)
    content = re.sub(r"(?<!\\)\.\.\.", r"\\ldots", content)
    content = re.sub(r"(?<=[A-Z])\s*\|\|\s*(?=[A-Z])", r" \\parallel ", content)
    content = re.sub(
        r"\\mod\s+(?:\{([^{}]*)\}|\(([^()]*)\)|([^\s\\(),]+(?:\{[^}]*\})?[^,\s\\)]*))",
        lambda match: r"\pmod{" + (match.group(1) or match.group(2) or match.group(3)).strip() + "}",
        content,
    )
    content = strip_delimiter_inner_spaces(content)
    return content


def matching_outer_pair(content: str) -> bool:
    pairs = {"(": ")", "[": "]", "{": "}"}
    if len(content) < 2 or content[0] not in pairs:
        return False

    expected = pairs[content[0]]
    depth = 0
    for index, char in enumerate(content):
        if is_escaped(content, index):
            continue
        if char == content[0]:
            depth += 1
        elif char == expected:
            depth -= 1
            if depth == 0 and index != len(content) - 1:
                return False
    return depth == 0


def split_top_level_commas(content: str) -> list[str] | None:
    if "," not in content:
        return None
    if "\n" in content or any(token in content for token in (r"\begin", r"\end", r"\pmod")):
        return None
    if re.search(
        r"(=|<|>|\\(?:in|notin|subset|supset|leq?|geq?|ne|neq|equiv|mid)\b)",
        content,
    ):
        return None
    if matching_outer_pair(content.strip()):
        return None

    stack: list[str] = []
    pairs = {"(": ")", "[": "]", "{": "}"}
    closers = {")", "]", "}"}
    parts: list[str] = []
    start = 0

    for index, char in enumerate(content):
        escaped = is_escaped(content, index)
        if escaped and char not in "{}[]":
            continue
        if char in pairs:
            stack.append(pairs[char])
            continue
        if char in closers:
            if stack and stack[-1] == char:
                stack.pop()
            continue
        if char != "," or stack:
            continue

        prev_char = content[index - 1] if index > 0 else ""
        next_char = content[index + 1] if index + 1 < len(content) else ""
        if prev_char.isdigit() and next_char.isdigit():
            return None

        parts.append(content[start:index].strip())
        start = index + 1

    if not parts:
        return None
    parts.append(content[start:].strip())
    if len(parts) < 2 or any(not part for part in parts):
        return None
    if any(part in (r"\ldots", r"\dots", r"\cdots", r"\ldots{}") for part in parts):
        return None
    expression_parts = [part for part in parts if part not in (r"\ldots", r"\dots", r"\cdots", r"\ldots{}")]
    compound_parts = [part for part in expression_parts if re.search(r"(\\cdot|\\times|\\frac|\\sqrt|[+\-*/^])", part)]
    if len(compound_parts) < 2:
        return None
    return parts


def format_inline_math(content: str, *, split_commas: bool) -> str:
    content = normalize_math(content, display=False)

    trailing = ""
    while content and content[-1] in ",.;:" and not content.endswith(r"\ldots"):
        trailing = content[-1] + trailing
        content = content[:-1].rstrip()

    parts = split_top_level_commas(content) if split_commas else None
    if parts:
        return ", ".join(f"${part}$" for part in parts) + trailing
    return f"${content}${trailing}"


def process_non_fenced(text: str, path: Path, issues: list[Issue], *, split_commas: bool) -> str:
    out: list[str] = []
    plain: list[str] = []
    i = 0

    def flush_plain() -> None:
        if plain:
            out.append(normalize_plain("".join(plain)))
            plain.clear()

    while i < len(text):
        if text.startswith("$$", i) and not is_escaped(text, i):
            end = text.find("$$", i + 2)
            if end == -1:
                issues.append(Issue(path, line_at(text, i), "unclosed display math block"))
                plain.append(text[i:])
                break
            flush_plain()
            body = normalize_math(text[i + 2 : end], display=True)
            out.append("$$" + body + "$$")
            i = end + 2
            continue

        if text[i] == "$" and not is_escaped(text, i):
            line_end = text.find("\n", i + 1)
            search_limit = len(text) if line_end == -1 else line_end
            end = i + 1
            while True:
                end = text.find("$", end, search_limit)
                if end == -1:
                    issues.append(Issue(path, line_at(text, i), "unclosed inline math span"))
                    plain.append(text[i])
                    i += 1
                    break
                if not is_escaped(text, end) and not text.startswith("$$", end):
                    break
                end += 1
            if end == -1:
                continue
            flush_plain()
            body = text[i + 1 : end]
            out.append(format_inline_math(body, split_commas=split_commas))
            i = end + 1
            continue

        plain.append(text[i])
        i += 1

    flush_plain()
    return "".join(out)


def process_math_fence(segment: str) -> str:
    lines = segment.splitlines(keepends=True)
    if len(lines) < 2:
        return segment
    opener = lines[0]
    closer = lines[-1]
    body = "".join(lines[1:-1])
    return opener + normalize_math(body, display=True) + closer


def contains_latex(text: str) -> bool:
    return bool(
        re.search(
            r"(?<!\\)\$|```math\b|\\begin\{|\\\(|\\\[",
            text,
            flags=re.IGNORECASE,
        )
    )


def contains_markdown_list(text: str) -> bool:
    return bool(re.search(r"(?m)^[ \t]*(?:\d+\.|[-+*])\s+\S", text))


def split_fenced_segments(text: str, path: Path, issues: list[Issue]) -> list[tuple[str, str]]:
    lines = text.splitlines(keepends=True)
    segments: list[tuple[str, str]] = []
    plain: list[str] = []
    fence: list[str] | None = None
    fence_marker = ""
    fence_kind = "fence"

    def flush_plain() -> None:
        if plain:
            segments.append(("plain", "".join(plain)))
            plain.clear()

    for line_number, line in enumerate(lines, start=1):
        stripped = line.lstrip(" \t")
        indent = len(line) - len(stripped)
        opener = re.match(r"(`{3,}|~{3,})(.*)$", stripped.rstrip("\n\r"))

        if fence is None and indent <= 3 and opener:
            flush_plain()
            fence_marker = opener.group(1)
            info = opener.group(2).strip().lower()
            fence_kind = "math_fence" if info.startswith("math") else "fence"
            fence = [line]
            continue

        if fence is not None:
            fence.append(line)
            closer = stripped.rstrip("\n\r")
            if indent <= 3 and closer.startswith(fence_marker) and set(closer[: len(fence_marker)]) == {fence_marker[0]}:
                segments.append((fence_kind, "".join(fence)))
                fence = None
                fence_marker = ""
            continue

        plain.append(line)

    if fence is not None:
        issues.append(Issue(path, len(lines), "unclosed fenced code block"))
        segments.append((fence_kind, "".join(fence)))
    flush_plain()
    return segments


def details_immediate_body(text: str, start: int) -> str:
    stop = re.search(r"<details><summary>|</details>", text[start:])
    end = len(text) if stop is None else start + stop.start()
    return text[start:end]


def normalize_summary_spacing(text: str) -> str:
    summary_re = re.compile(r"(<details><summary>[^<]+</summary>)[ \t]*(?:\r?\n){1,2}")
    out: list[str] = []
    pos = 0

    for match in summary_re.finditer(text):
        out.append(text[pos : match.start()])
        body = details_immediate_body(text, match.end())
        separator = "\n\n" if contains_latex(body) or contains_markdown_list(body) else "\n"
        out.append(match.group(1) + separator)
        pos = match.end()

    out.append(text[pos:])
    return "".join(out)


def normalize_markdown_layout(text: str) -> str:
    text = re.sub(r"</details>\s*\+\s*</details>", "</details></details>", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"\n{2,}(<details><summary>)", r"\n\1", text)
    text = normalize_summary_spacing(text)
    text = re.sub(r"(?m)^>\s*</details>\s*$", "</details>", text)
    return text.rstrip() + "\n"


def strip_regular_code_fences(path: Path, text: str) -> str:
    ignored_issues: list[Issue] = []
    return "".join(segment if kind != "fence" else "\n" * segment.count("\n") for kind, segment in split_fenced_segments(text, path, ignored_issues))


def validate_balanced_tag(path: Path, text: str, tag: str, issues: list[Issue]) -> None:
    stack: list[int] = []
    for match in re.finditer(rf"</?{tag}\b[^>]*>", text, flags=re.IGNORECASE):
        token = match.group(0)
        line = line_at(text, match.start())
        if token.startswith("</"):
            if stack:
                stack.pop()
            else:
                issues.append(Issue(path, line, f"unmatched </{tag}>"))
        else:
            stack.append(line)

    for line in stack:
        issues.append(Issue(path, line, f"unclosed <{tag}>"))


def validate(path: Path, text: str, issues: list[Issue]) -> None:
    validation_text = strip_regular_code_fences(path, text)

    validate_balanced_tag(path, validation_text, "details", issues)
    validate_balanced_tag(path, validation_text, "summary", issues)
    if "\u00d0" in validation_text or "\u00d1" in validation_text:
        issues.append(Issue(path, 1, "possible mojibake characters found"))

    for match in re.finditer(r"(?s)(\$.*?\$|```math\n.*?```|\$\$.*?\$\$)", validation_text):
        math = match.group(0)
        left_count = math.count(r"\left")
        right_count = math.count(r"\right") - math.count(r"\rightarrow")
        if left_count != right_count:
            issues.append(
                Issue(
                    path,
                    line_at(validation_text, match.start()),
                    f"unbalanced \\left/\\right in math span ({left_count}/{right_count})",
                )
            )


def format_text(path: Path, text: str, *, split_commas: bool) -> FormatResult:
    issues: list[Issue] = []
    pieces: list[str] = []
    for kind, segment in split_fenced_segments(text, path, issues):
        if kind == "plain":
            pieces.append(process_non_fenced(segment, path, issues, split_commas=split_commas))
        elif kind == "math_fence":
            pieces.append(process_math_fence(segment))
        else:
            pieces.append(segment)

    formatted = normalize_markdown_layout("".join(pieces))
    validate(path, formatted, issues)
    return FormatResult(text=formatted, issues=issues)


def discover_files(paths: Iterable[Path]) -> list[Path]:
    files: list[Path] = []
    ignored_dirs = {".git", ".venv", "__pycache__"}
    ignored_files = {"CLAUDE.md", "eval.md"}
    for path in paths:
        if path.is_file():
            if path.suffix.lower() == ".md":
                files.append(path)
            continue
        if path.is_dir():
            for child in path.rglob("*.md"):
                if ignored_dirs.intersection(child.parts):
                    continue
                if child.name in ignored_files:
                    continue
                files.append(child)
    return sorted(set(files))


def print_diff(path: Path, before: str, after: str) -> None:
    diff = difflib.unified_diff(
        before.splitlines(keepends=True),
        after.splitlines(keepends=True),
        fromfile=str(path),
        tofile=str(path),
    )
    sys.stdout.writelines(diff)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and reformat olympiad Markdown files.")
    parser.add_argument("paths", nargs="*", type=Path, default=[Path(".")])
    parser.add_argument("--write", action="store_true", help="Write changes in place.")
    parser.add_argument("--diff", action="store_true", help="Print unified diffs for changed files.")
    parser.add_argument("--check", action="store_true", help="Exit non-zero if changes or issues are found.")
    parser.add_argument(
        "--no-split-commas",
        action="store_true",
        help="Do not split top-level comma-separated inline math into separate spans.",
    )
    args = parser.parse_args()

    files = discover_files(args.paths)
    changed: list[Path] = []
    all_issues: list[Issue] = []

    for path in files:
        before = path.read_text(encoding="utf-8")
        result = format_text(path, before, split_commas=not args.no_split_commas)
        all_issues.extend(result.issues)
        if result.text == before:
            continue
        changed.append(path)
        if args.diff:
            print_diff(path, before, result.text)
        if args.write:
            path.write_text(result.text, encoding="utf-8")

    action = "Updated" if args.write else "Would update"
    print(f"{action} {len(changed)} of {len(files)} Markdown files.")

    if all_issues:
        print(f"Found {len(all_issues)} validation issue(s):")
        for issue in all_issues:
            print(f"{issue.path}:{issue.line}: {issue.message}")

    if args.check and (changed or all_issues):
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
