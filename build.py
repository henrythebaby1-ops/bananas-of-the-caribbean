"""Builds index.html for GitHub Pages from the single-file game source.

The source page (src/game.html) is written for Claude artifacts, which add the
document skeleton themselves. This wraps it in a full HTML document and plugs in Supabase Realtime
for online co-op.
"""
import pathlib, re

HERE = pathlib.Path(__file__).parent
SRC = HERE / "src" / "game.html"
SUPABASE_URL = "https://ckxwnswjjnefubnsvkhl.supabase.co"
# Public anon key: safe to ship in a web page. The game only uses Realtime channels, no tables.
SUPABASE_ANON_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImNreHduc3dqam5lZnVibnN2a2hsIiwicm9sZSI6ImFub24iLCJpYXQiOjE3OTI1MzcwMDcsImV4cCI6MjEwODExMzAwN30._KSOzoS1-4dgjfvUeqkDpE1UJNUw1pEwq3R7ABlry6s"

src = SRC.read_text()
head_parts = []
for pattern in (r"<title>.*?</title>", r"<link[^>]*>", r"<style>.*?</style>"):
    for m in re.findall(pattern, src, re.S):
        head_parts.append(m)
        src = src.replace(m, "", 1)
src = re.sub(r'<meta name="claude:viewport-fit-sides"[^>]*>\n?', "", src)
main_script = re.search(r"<script>.*</script>", src, re.S).group(0)
body = src.replace(main_script, "").strip()

doc = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#0d2433">
<meta name="description" content="A top-down action RPG: peel and eat your way around the world, alone or with up to 3 friends online.">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}}body{{margin:0;font:14px system-ui,sans-serif}}img{{max-width:100%}}[hidden]{{display:none!important}}</style>
{chr(10).join(head_parts)}
</head>
<body>
{body}
<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.45.4/dist/umd/supabase.js"></script>
<script>window.SB_CONFIG={{url:"{SUPABASE_URL}",key:"{SUPABASE_ANON_KEY}"}};</script>
{main_script}
</body>
</html>
"""
(HERE / "index.html").write_text(doc)
print("wrote index.html", len(doc), "bytes")
