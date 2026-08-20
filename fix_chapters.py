import os
import re
import json

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
md_path = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_35REAIS.md")

with open(md_path, "r", encoding="utf-8") as f:
    raw_md = f.read()

# Filter Notion export metadata lines
clean_lines = []
for line in raw_md.split("\n"):
    if line.strip().startswith("feito:") or line.strip().startswith("Description:"):
        continue
    clean_lines.append(line)

clean_md = "\n".join(clean_lines)

# Split into Módulos and Capítulos properly
# We group content under ## headings or # MÓDULO headings.
lines = clean_md.split("\n")

chapters = []
current_module = "Módulo 1: Fundamentos dos Produtos Digitais"
current_title = "⚡ Guia Definitivo do Criador Digital"
current_body = []

for line in lines:
    line_s = line.strip()
    
    # Check for Módulo Header
    if line_s.startswith("# MÓDULO "):
        if current_body:
            content_str = "\n".join(current_body).strip()
            if content_str:
                chapters.append({
                    "module": current_module,
                    "title": current_title,
                    "content": content_str
                })
            current_body = []
        current_module = line_s.replace("# ", "").strip()
        current_title = current_module
        continue

    # Check for Chapter Header (## )
    if line_s.startswith("## "):
        if current_body:
            content_str = "\n".join(current_body).strip()
            if content_str:
                chapters.append({
                    "module": current_module,
                    "title": current_title,
                    "content": content_str
                })
            current_body = []
        current_title = re.sub(r"^##\s*", "", line_s).strip()
        continue

    # Skip duplicate # headers that repeat the chapter title
    if line_s.startswith("# ") and not line_s.startswith("# MÓDULO"):
        # Check if title matches
        header_text = re.sub(r"^#\s*", "", line_s).strip()
        header_clean = re.sub(r"^[0-9\.\s\-\:\#]+", "", header_text).lower()
        title_clean = re.sub(r"^[0-9\.\s\-\:\#]+", "", current_title).lower()
        if header_clean and title_clean and (header_clean in title_clean or title_clean in header_clean):
            continue

    current_body.append(line)

if current_body:
    content_str = "\n".join(current_body).strip()
    if content_str:
        chapters.append({
            "module": current_module,
            "title": current_title,
            "content": content_str
        })

print(f"Total non-empty chapters parsed: {len(chapters)}")
for i, ch in enumerate(chapters):
    print(f"Ch {i+1}: [{ch['module']}] {ch['title']!r} -> {len(ch['content'])} chars")
