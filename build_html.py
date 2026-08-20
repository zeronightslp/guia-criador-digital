import os
import re

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
md_file = os.path.join(dir_path, "PRODUTO_MASTER_GUIA_CRIADOR_DIGITAL.md")
html_file = os.path.join(dir_path, "PRODUTO_MASTER_GUIA_CRIADOR_DIGITAL.html")

with open(md_file, "r", encoding="utf-8") as f:
    text = f.read()

body = text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
body = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", body, flags=re.M)
body = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", body, flags=re.M)
body = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", body, flags=re.M)
body = re.sub(r"^\> (.*?)$", r"<blockquote>\1</blockquote>", body, flags=re.M)
body = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", body)
body = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2" target="_blank">\1</a>', body)
body = body.replace("\n\n", "</p><p>")

html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>O Guia do Criador Digital - Produto Master</title>
    <style>
        @import url("https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600;700;800&display=swap");
        body {{
            font-family: "Inter", sans-serif;
            background: #0f172a;
            color: #f8fafc;
            line-height: 1.7;
            max-width: 900px;
            margin: 0 auto;
            padding: 40px 20px;
        }}
        h1 {{ font-size: 2.5rem; color: #38bdf8; border-bottom: 2px solid #334155; padding-bottom: 15px; margin-top: 40px; }}
        h2 {{ font-size: 1.8rem; color: #818cf8; margin-top: 35px; border-left: 4px solid #818cf8; padding-left: 12px; }}
        h3 {{ font-size: 1.3rem; color: #f43f5e; margin-top: 25px; }}
        blockquote {{ background: #1e293b; border-left: 4px solid #38bdf8; padding: 15px 20px; border-radius: 8px; font-style: italic; margin: 20px 0; }}
        a {{ color: #38bdf8; text-decoration: none; font-weight: 600; }}
        a:hover {{ text-decoration: underline; }}
        hr {{ border: 0; height: 1px; background: #334155; margin: 40px 0; }}
        p {{ margin-bottom: 1.2rem; font-size: 1.05rem; color: #cbd5e1; }}
        strong {{ color: #ffffff; }}
    </style>
</head>
<body>
    <div>{body}</div>
</body>
</html>"""

with open(html_file, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"HTML Generated: {html_file}")
