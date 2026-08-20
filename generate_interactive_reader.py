import os
import re
import json
import unicodedata

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
md_path = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_35REAIS.md")

with open(md_path, "r", encoding="utf-8") as f:
    raw_md = f.read()

# Remove notion export headers
clean_lines = []
for line in raw_md.split("\n"):
    if line.strip().startswith("feito:") or line.strip().startswith("Description:"):
        continue
    clean_lines.append(line)

clean_md = "\n".join(clean_lines)

# Split into chapters based on headings
def parse_chapters_and_modules(md):
    chapters = []
    current_module = "Módulo 1: Fundamentos dos Produtos Digitais"
    current_title = "Introdução ao Guia"
    current_lines = []
    chapter_id = 0

    lines = md.split('\n')
    for line in lines:
        if line.startswith("# MÓDULO "):
            if current_lines:
                chapter_id += 1
                chapters.append({
                    "id": chapter_id,
                    "module": current_module,
                    "title": current_title,
                    "content": "\n".join(current_lines).strip()
                })
                current_lines = []
            current_module = line.replace("# ", "").strip()
            current_title = current_module
        elif line.startswith("## ") or (line.startswith("# ") and not line.startswith("# MÓDULO")):
            if current_lines:
                chapter_id += 1
                chapters.append({
                    "id": chapter_id,
                    "module": current_module,
                    "title": current_title,
                    "content": "\n".join(current_lines).strip()
                })
                current_lines = []
            current_title = re.sub(r'^[#\s]+', '', line).strip()
        else:
            current_lines.append(line)

    if current_lines:
        chapter_id += 1
        chapters.append({
            "id": chapter_id,
            "module": current_module,
            "title": current_title,
            "content": "\n".join(current_lines).strip()
        })

    return chapters

chapters_data = parse_chapters_and_modules(clean_md)

# Convert chapter Markdown content to HTML
def md_to_html(md_text):
    md_text = md_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    md_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", md_text)
    md_text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", md_text)
    md_text = re.sub(r"`(.*?)`", r"<code>\1</code>", md_text)
    
    # Links
    def link_repl(match):
        label, url = match.group(1), match.group(2)
        if any(k in url for k in ["pay.", "gumroad", "wa.link", "loom.com", "kiwify"]):
            return f'<a href="{url}" target="_blank" class="inline-flex items-center gap-1.5 px-3 py-1.5 bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs rounded-lg shadow transition-all my-1">🚀 {label}</a>'
        return f'<a href="{url}" target="_blank" class="text-cyan-400 hover:underline font-semibold">{label}</a>'
    
    md_text = re.sub(r"\[(.*?)\]\((.*?)\)", link_repl, md_text)
    
    # Asides / Callouts
    md_text = re.sub(r"\<aside\>(.*?)\</aside\>", r'<div class="my-4 p-4 rounded-xl bg-slate-900 border border-cyan-500/30 text-cyan-200 text-sm font-medium">\1</div>', md_text, flags=re.S)
    
    # Images
    md_text = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<div class="my-4 text-center"><img src="\2" alt="\1" class="max-w-full h-auto rounded-xl border border-slate-800 shadow-lg mx-auto"/><p class="text-xs text-slate-400 mt-1">\1</p></div>', md_text)

    # Paragraphs and Lists
    paragraphs = md_text.split("\n\n")
    html_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith("- ") or p.startswith("* "):
            items = [f'<li class="ml-4 list-disc text-slate-300 my-1">{li[2:]}</li>' for li in p.split("\n") if li.strip()]
            html_paragraphs.append(f'<ul class="my-3 space-y-1">{"".join(items)}</ul>')
        elif re.match(r'^\d+\.', p):
            items = [f'<li class="ml-4 list-decimal text-slate-300 my-1">{re.sub(r"^\d+\.\s*", "", li)}</li>' for li in p.split("\n") if li.strip()]
            html_paragraphs.append(f'<ol class="my-3 space-y-1">{"".join(items)}</ol>')
        elif p.startswith(">"):
            clean_q = p.replace(">", "").strip()
            html_paragraphs.append(f'<blockquote class="border-l-4 border-cyan-500 pl-4 py-2 my-3 italic text-slate-300 bg-slate-900/50 rounded-r-lg">{clean_q}</blockquote>')
        else:
            html_paragraphs.append(f'<p class="mb-3 text-slate-300 leading-relaxed">{p.replace("\n", "<br/>")}</p>')
            
    return "".join(html_paragraphs)

for ch in chapters_data:
    ch["html"] = md_to_html(ch["content"])

# Write out JSON file
json_output_path = os.path.join(dir_path, "ebook_chapters.json")
with open(json_output_path, "w", encoding="utf-8") as f:
    json.dump(chapters_data, f, ensure_ascii=False, indent=2)

print(f"Extracted {len(chapters_data)} chapters to ebook_chapters.json")
