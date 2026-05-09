"""
find_featured.py
────────────────
Scans every public repo owned by GITHUB_USER.
If a repo's README contains the text SEARCH_TEXT ("Featured-repo"),
that repo is included in the Featured Projects section.

The script replaces __FEATURED_PROJECTS__ inside README.source.md
with a JSON array that the readme-aura build can use directly.

Run by the GitHub Actions workflow before `readme-aura` builds.
"""

import urllib.request
import urllib.error
import json
import base64
import os
import sys

# ── Config ────────────────────────────────────────────────────────
GITHUB_USER  = "YashChaudhari999"
SOURCE_FILE  = "README.source.md"
PLACEHOLDER  = "__FEATURED_PROJECTS__"
SEARCH_TEXT  = "Featured-repo"      # exact text to look for in repo READMEs
MAX_FEATURED = 6                    # max cards to show (layout supports up to 6)
MAX_DESC_LEN = 120                  # truncate long descriptions

# ── GitHub language → badge color ────────────────────────────────
LANG_COLORS = {
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "Python":     "#3572A5",
    "Java":       "#b07219",
    "PHP":        "#4F5D95",
    "HTML":       "#e34c26",
    "CSS":        "#563d7c",
    "C":          "#555555",
    "C++":        "#f34b7d",
    "C#":         "#178600",
    "Go":         "#00ADD8",
    "Rust":       "#dea584",
    "Ruby":       "#701516",
    "Swift":      "#F05138",
    "Kotlin":     "#A97BFF",
    "Shell":      "#89e051",
    "Vue":        "#41b883",
    "Dart":       "#00B4AB",
    "Jupyter Notebook": "#DA5B0B",
}
DEFAULT_COLOR = "#6e50dc"

# ── Helpers ───────────────────────────────────────────────────────
def api_get(url: str, token: str) -> dict | list:
    req = urllib.request.Request(
        url,
        headers={
            "Authorization": f"token {token}",
            "Accept":        "application/vnd.github.v3+json",
            "User-Agent":    "readme-aura-featured-scanner",
        },
    )
    with urllib.request.urlopen(req, timeout=15) as r:
        return json.loads(r.read())


def readme_contains(repo_name: str, token: str) -> bool:
    """Return True if the repo's default-branch README contains SEARCH_TEXT."""
    url = f"https://api.github.com/repos/{GITHUB_USER}/{repo_name}/readme"
    try:
        data    = api_get(url, token)
        content = base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        return SEARCH_TEXT in content
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False   # no README — skip silently
        print(f"  ⚠  {repo_name}: HTTP {e.code}", flush=True)
        return False
    except Exception as exc:
        print(f"  ⚠  {repo_name}: {exc}", flush=True)
        return False


def truncate(text: str, length: int) -> str:
    return text if len(text) <= length else text[:length].rstrip() + "…"


# ── Main ──────────────────────────────────────────────────────────
def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("❌  GITHUB_TOKEN env var is not set.", file=sys.stderr)
        sys.exit(1)

    print(f"🔍  Scanning repos of {GITHUB_USER} for '{SEARCH_TEXT}' …", flush=True)

    # Fetch all public repos (paginated)
    all_repos: list[dict] = []
    page = 1
    while True:
        url   = f"https://api.github.com/users/{GITHUB_USER}/repos?per_page=100&page={page}&type=public"
        batch = api_get(url, token)
        if not batch:
            break
        all_repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    print(f"   Found {len(all_repos)} public repos. Checking READMEs …", flush=True)

    featured: list[dict] = []
    for repo in all_repos:
        name = repo["name"]
        print(f"   checking {name} …", end=" ", flush=True)
        if readme_contains(name, token):
            lang      = repo.get("language") or "Code"
            desc_raw  = repo.get("description") or "No description provided."
            featured.append({
                "name":      name,
                "desc":      truncate(desc_raw, MAX_DESC_LEN),
                "lang":      lang,
                "langColor": LANG_COLORS.get(lang, DEFAULT_COLOR),
                "link":      repo.get("html_url", f"https://github.com/{GITHUB_USER}/{name}"),
            })
            print("✅  FEATURED", flush=True)
            if len(featured) >= MAX_FEATURED:
                break
        else:
            print("–", flush=True)

    print(f"\n🎯  {len(featured)} featured repo(s): {[r['name'] for r in featured]}", flush=True)

    if not featured:
        print("⚠   No featured repos found — injecting empty array.", flush=True)

    # Read source file
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        source = f.read()

    if PLACEHOLDER not in source:
        print(f"❌  '{PLACEHOLDER}' not found in {SOURCE_FILE}.", file=sys.stderr)
        sys.exit(1)

    # Inject JSON (compact, single-line — safe inside JS string context)
    injection = json.dumps(featured, ensure_ascii=False)
    source = source.replace(PLACEHOLDER, injection)

    with open(SOURCE_FILE, "w", encoding="utf-8") as f:
        f.write(source)

    print(f"✅  Injected {len(featured)} project(s) into {SOURCE_FILE}.", flush=True)


if __name__ == "__main__":
    main()
