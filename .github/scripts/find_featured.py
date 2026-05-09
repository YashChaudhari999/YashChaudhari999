"""
find_featured.py
────────────────
Scans every public repo owned by GITHUB_USER.
If a repo's README contains the text SEARCH_TEXT ("Featured-repo"),
that repo is included in the Featured Projects section.

Replaces the content between /*FEATURED_START*/ and /*FEATURED_END*/
markers in README.source.md with live data.

If NO repos are found with the tag, the fallback (original hardcoded
repos already between the markers) is LEFT UNTOUCHED — the section
always renders something valid.

Add this text ANYWHERE in a repo's README to feature it:
    <!-- Featured-repo -->
"""

import urllib.request
import urllib.error
import json
import base64
import re
import os
import sys
import math

# ── Config ────────────────────────────────────────────────────────
GITHUB_USER  = "YashChaudhari999"
SOURCE_FILE  = "README.source.md"
SEARCH_TEXT  = "Featured-repo"       # text to scan for in repo READMEs
MAX_FEATURED = 6                     # max cards shown (layout fits up to 6)
MAX_DESC_LEN = 120                   # truncate long descriptions

# Repositories you contributed to that you want to check (owner/repo format)
EXTRA_REPOS = [
    "kunalkhaire302/carbon-footprint-ai",
]

# Regex that matches the marker block (single line, compact JSON inside)
MARKER_RE = re.compile(
    r"/\*FEATURED_START\*/.*?/\*FEATURED_END\*/",
    re.DOTALL,
)

# ── Language → badge colour (GitHub official colors) ─────────────
LANG_COLORS = {
    "JavaScript":      "#f1e05a",
    "TypeScript":      "#3178c6",
    "Python":          "#3572A5",
    "Java":            "#b07219",
    "PHP":             "#4F5D95",
    "HTML":            "#e34c26",
    "CSS":             "#563d7c",
    "C":               "#555555",
    "C++":             "#f34b7d",
    "C#":              "#178600",
    "Go":              "#00ADD8",
    "Rust":            "#dea584",
    "Ruby":            "#701516",
    "Swift":           "#F05138",
    "Kotlin":          "#A97BFF",
    "Shell":           "#89e051",
    "Vue":             "#41b883",
    "Dart":            "#00B4AB",
    "Jupyter Notebook":"#DA5B0B",
}
DEFAULT_COLOR = "#6e50dc"

# ── Helpers ───────────────────────────────────────────────────────
def api_get(url: str, token: str):
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


def readme_contains(full_repo_name: str, token: str) -> bool:
    """Return True if the repo's README contains SEARCH_TEXT. full_repo_name is 'owner/repo'"""
    url = f"https://api.github.com/repos/{full_repo_name}/readme"
    try:
        data    = api_get(url, token)
        content = base64.b64decode(data["content"]).decode("utf-8", errors="ignore")
        return SEARCH_TEXT in content
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return False   # no README — skip silently
        print(f"  ⚠  {full_repo_name}: HTTP {e.code}", flush=True)
        return False
    except Exception as exc:
        print(f"  ⚠  {full_repo_name}: {exc}", flush=True)
        return False


def get_repo_details(full_repo_name: str, token: str) -> dict | None:
    """Fetch details for a specific repository."""
    url = f"https://api.github.com/repos/{full_repo_name}"
    try:
        return api_get(url, token)
    except Exception as exc:
        print(f"  ⚠  Failed to fetch details for {full_repo_name}: {exc}", flush=True)
        return None

def truncate(text: str, length: int) -> str:
    return text if len(text) <= length else text[:length].rstrip() + "…"


# ── Main ──────────────────────────────────────────────────────────
def main():
    token = os.environ.get("GITHUB_TOKEN", "")
    if not token:
        print("❌  GITHUB_TOKEN env var is not set.", file=sys.stderr)
        sys.exit(1)

    # Read source file first — bail early if markers are missing
    with open(SOURCE_FILE, "r", encoding="utf-8") as f:
        source = f.read()

    if not MARKER_RE.search(source):
        print(f"❌  FEATURED_START/FEATURED_END markers not found in {SOURCE_FILE}.", file=sys.stderr)
        sys.exit(1)

    print(f"🔍  Scanning repos for '{SEARCH_TEXT}' …", flush=True)

    all_repos_to_check: list[dict] = []

    # 1. Add extra contributed repos first
    for extra_repo in EXTRA_REPOS:
        details = get_repo_details(extra_repo, token)
        if details:
            all_repos_to_check.append(details)

    # 2. Fetch all public repos owned by user (paginated)
    page = 1
    while True:
        url   = (
            f"https://api.github.com/users/{GITHUB_USER}/repos"
            f"?per_page=100&page={page}&type=public"
        )
        batch = api_get(url, token)
        if not batch:
            break
        all_repos_to_check.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    print(f"   Found {len(all_repos_to_check)} total repos to check. Checking READMEs …", flush=True)

    featured: list[dict] = []
    for repo in all_repos_to_check:
        full_name = repo["full_name"]  # e.g., 'kunalkhaire302/carbon-footprint-ai' or 'YashChaudhari999/repo'
        name = repo["name"]            # e.g., 'carbon-footprint-ai'
        
        print(f"   checking {full_name} …", end=" ", flush=True)
        if readme_contains(full_name, token):
            lang = repo.get("language") or "Code"
            desc = truncate(repo.get("description") or "No description provided.", MAX_DESC_LEN)
            featured.append({
                "name":      name,  # display the short name in the card
                "desc":      desc,
                "lang":      lang,
                "langColor": LANG_COLORS.get(lang, DEFAULT_COLOR),
                "link":      repo.get("html_url", f"https://github.com/{full_name}"),
            })
            print("✅  FEATURED", flush=True)
            if len(featured) >= MAX_FEATURED:
                break
        else:
            print("–", flush=True)

    print(f"\n🎯  {len(featured)} featured repo(s) found: {[r['name'] for r in featured]}", flush=True)

    if not featured:
        # ── No repos tagged → keep the existing fallback as-is ──
        print("ℹ️   No repos have 'Featured-repo' in their README yet.", flush=True)
        print("    Add  <!-- Featured-repo -->  to any repo's README to feature it.", flush=True)
        print("    Leaving current fallback projects unchanged.", flush=True)
        return   # exit without writing — fallback stays valid

    # ── Inject live data between markers ─────────────────────────
    injection = (
        "/*FEATURED_START*/"
        "var projects = " + json.dumps(featured, ensure_ascii=False) + ";"
        "/*FEATURED_END*/"
    )
    new_source = MARKER_RE.sub(injection, source)

    # ── Dynamically update SVG height based on number of rows ──
    # 1 row (1-2 items) = 200, 2 rows (3-4 items) = 300, etc.
    rows = math.ceil(len(featured) / 2)
    new_height = 100 + (rows * 100)
    
    # Regex targets specifically the aura block containing FEATURED_START
    height_pattern = r"(```aura\s+width=860\s+height=)\d+(?=\s*\n\(\s*function\s*\(\)\s*\{\s*\n\s*/\*FEATURED_START\*/)"
    new_source = re.sub(height_pattern, rf"\g<1>{new_height}", new_source, count=1)

    with open(SOURCE_FILE, "w", encoding="utf-8") as f:
        f.write(new_source)

    print(f"✅  Injected {len(featured)} project(s) into {SOURCE_FILE}.", flush=True)


if __name__ == "__main__":
    main()
