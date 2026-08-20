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

lines = clean_md.split("\n")

raw_chapters = []
current_module = "Módulo 1: Fundamentos dos Produtos Digitais"
current_title = "⚡ Guia Definitivo do Criador Digital"
current_body = []

for line in lines:
    line_s = line.strip()
    
    # Check for Módulo Header
    if line_s.startswith("# MÓDULO "):
        if current_body:
            content_str = "\n".join(current_body).strip()
            if len(content_str) > 20:
                raw_chapters.append({
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
            if len(content_str) > 20:
                raw_chapters.append({
                    "module": current_module,
                    "title": current_title,
                    "content": content_str
                })
            current_body = []
        current_title = re.sub(r"^##\s*", "", line_s).strip()
        continue

    # Skip duplicate # headers that repeat the chapter title
    if line_s.startswith("# ") and not line_s.startswith("# MÓDULO"):
        header_text = re.sub(r"^#\s*", "", line_s).strip()
        header_clean = re.sub(r"^[0-9\.\s\-\:\#]+", "", header_text).lower()
        title_clean = re.sub(r"^[0-9\.\s\-\:\#]+", "", current_title).lower()
        if header_clean and title_clean and (header_clean in title_clean or title_clean in header_clean):
            continue

    current_body.append(line)

if current_body:
    content_str = "\n".join(current_body).strip()
    if len(content_str) > 20:
        raw_chapters.append({
            "module": current_module,
            "title": current_title,
            "content": content_str
        })

# Convert chapter Markdown content to Rich Responsive HTML
def md_to_html(md_text):
    md_text = md_text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    md_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", md_text)
    md_text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", md_text)
    md_text = re.sub(r"`(.*?)`", r"<code class='bg-slate-900 border border-slate-700 text-cyan-400 px-1.5 py-0.5 rounded text-xs'>\1</code>", md_text)
    
    # CTA Buttons / Links
    def link_repl(match):
        label, url = match.group(1), match.group(2)
        if any(k in url for k in ["pay.", "gumroad", "wa.link", "loom.com", "kiwify"]):
            return f'<a href="{url}" target="_blank" class="inline-flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-extrabold text-xs rounded-xl shadow-lg transition-all my-2">🚀 {label}</a>'
        return f'<a href="{url}" target="_blank" class="text-cyan-400 hover:text-cyan-300 underline font-semibold">{label}</a>'
    
    md_text = re.sub(r"\[(.*?)\]\((.*?)\)", link_repl, md_text)
    
    # Asides / Callouts
    md_text = re.sub(r"\<aside\>(.*?)\</aside\>", r'<div class="my-4 p-4 rounded-xl bg-slate-900/90 border border-cyan-500/30 text-cyan-200 text-sm font-medium shadow-md">\1</div>', md_text, flags=re.S)
    
    # Images
    md_text = re.sub(r"!\[(.*?)\]\((.*?)\)", r'<div class="my-5 text-center"><img src="\2" alt="\1" class="max-w-full h-auto rounded-xl border border-slate-800 shadow-xl mx-auto"/><p class="text-xs text-slate-400 mt-2 font-mono">\1</p></div>', md_text)

    # Paragraphs and Lists
    paragraphs = md_text.split("\n\n")
    html_paragraphs = []
    for p in paragraphs:
        p = p.strip()
        if not p:
            continue
        if p.startswith("- ") or p.startswith("* "):
            items = [f'<li class="ml-4 list-disc text-slate-300 my-1">{li[2:]}</li>' for li in p.split("\n") if li.strip()]
            html_paragraphs.append(f'<ul class="my-3 space-y-1 bg-slate-900/40 p-3 rounded-xl border border-slate-800/80">{"".join(items)}</ul>')
        elif re.match(r'^\d+\.', p):
            items = [f'<li class="ml-4 list-decimal text-slate-300 my-1">{re.sub(r"^\d+\.\s*", "", li)}</li>' for li in p.split("\n") if li.strip()]
            html_paragraphs.append(f'<ol class="my-3 space-y-1 bg-slate-900/40 p-3 rounded-xl border border-slate-800/80">{"".join(items)}</ol>')
        elif p.startswith(">"):
            clean_q = p.replace(">", "").strip()
            html_paragraphs.append(f'<blockquote class="border-l-4 border-cyan-500 pl-4 py-3 my-4 italic text-slate-200 bg-slate-900/70 rounded-r-xl">{clean_q}</blockquote>')
        else:
            html_paragraphs.append(f'<p class="mb-3 text-slate-300 leading-relaxed text-sm sm:text-base">{p.replace("\n", "<br/>")}</p>')
            
    return "".join(html_paragraphs)

processed_chapters = []
for idx, ch in enumerate(raw_chapters):
    ch["id"] = idx + 1
    ch["html"] = md_to_html(ch["content"])
    processed_chapters.append(ch)

json_output_path = os.path.join(dir_path, "ebook_chapters.json")
with open(json_output_path, "w", encoding="utf-8") as f:
    json.dump(processed_chapters, f, ensure_ascii=False, indent=2)

print(f"Successfully generated {len(processed_chapters)} rich, non-empty chapters in ebook_chapters.json")
