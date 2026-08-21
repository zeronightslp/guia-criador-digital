import os
import re
import json

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"

# High quality Markdown to HTML converter
def md_to_html(md_text):
    if not md_text:
        return ""
    
    # 1. Protect and format Aside / Callouts
    asides = []
    def aside_store(m):
        asides.append(m.group(1))
        return f"___ASIDE_PLACEHOLDER_{len(asides)-1}___"
    md_text = re.sub(r"<aside>(.*?)</aside>", aside_store, md_text, flags=re.S)

    # 2. Convert Images FIRST (so ![alt](url) isn't mangled by link regex)
    def img_repl(m):
        alt, src = m.group(1), m.group(2)
        return f'<div class="my-5 text-center"><img src="{src}" alt="{alt}" class="max-w-full h-auto rounded-xl border border-slate-700/80 shadow-xl mx-auto"/><p class="text-xs text-slate-400 mt-2 font-mono">{alt}</p></div>'
    md_text = re.sub(r"!\[(.*?)\]\((.*?)\)", img_repl, md_text)

    # 3. Convert CTA Buttons and Standard Links
    def link_repl(m):
        label, url = m.group(1), m.group(2)
        if any(k in url for k in ["pay.", "gumroad", "wa.link", "loom.com", "kiwify", "whatsapp"]):
            return f'<a href="{url}" target="_blank" class="inline-flex items-center gap-1.5 px-4 py-2 bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-extrabold text-xs rounded-xl shadow-lg transition-all my-2">🚀 {label}</a>'
        return f'<a href="{url}" target="_blank" class="text-cyan-400 hover:text-cyan-300 underline font-semibold">{label}</a>'
    md_text = re.sub(r"\[(.*?)\]\((.*?)\)", link_repl, md_text)

    # 4. Bold, Italic, Inline Code
    md_text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", md_text)
    md_text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", md_text)
    md_text = re.sub(r"`(.*?)`", r"<code class='bg-slate-900 border border-slate-700 text-cyan-400 px-1.5 py-0.5 rounded text-xs'>\1</code>", md_text)

    # 5. Restore Asides
    for i, a_content in enumerate(asides):
        clean_aside = a_content.replace("<img", "<img class='w-6 h-6 inline-block mr-2'").strip()
        formatted_aside = f'<div class="my-4 p-4 rounded-xl bg-slate-900/90 border border-cyan-500/30 text-cyan-200 text-sm font-medium shadow-md flex items-start gap-3"><div>{clean_aside}</div></div>'
        md_text = md_text.replace(f"___ASIDE_PLACEHOLDER_{i}___", formatted_aside)

    # 6. Parse Headings & Paragraph Blocks
    lines = md_text.split("\n")
    html_out = []
    in_list = False
    list_type = None

    for line in lines:
        l_str = line.strip()
        if not l_str:
            if in_list:
                html_out.append(f"</{list_type}>")
                in_list = False
            continue
        
        # Horizontal rules
        if l_str in ["---", "***", "___"]:
            if in_list: html_out.append(f"</{list_type}>"); in_list = False
            html_out.append('<hr class="my-5 border-slate-800"/>')
            continue

        # Headings
        if l_str.startswith("# "):
            if in_list: html_out.append(f"</{list_type}>"); in_list = False
            html_out.append(f'<h1 class="font-heading text-xl sm:text-2xl font-bold text-white mt-6 mb-3 pb-2 border-b border-slate-800">{l_str[2:]}</h1>')
            continue
        if l_str.startswith("## "):
            if in_list: html_out.append(f"</{list_type}>"); in_list = False
            html_out.append(f'<h2 class="font-heading text-lg sm:text-xl font-bold text-cyan-300 mt-5 mb-2">{l_str[3:]}</h2>')
            continue
        if l_str.startswith("### "):
            if in_list: html_out.append(f"</{list_type}>"); in_list = False
            html_out.append(f'<h3 class="font-heading text-base sm:text-lg font-semibold text-amber-300 mt-4 mb-2">{l_str[4:]}</h3>')
            continue
        if l_str.startswith("#### "):
            if in_list: html_out.append(f"</{list_type}>"); in_list = False
            html_out.append(f'<h4 class="font-heading text-sm sm:text-base font-semibold text-slate-200 mt-3 mb-1">{l_str[5:]}</h4>')
            continue

        # Blockquotes
        if l_str.startswith(">"):
            if in_list: html_out.append(f"</{list_type}>"); in_list = False
            clean_q = l_str[1:].strip()
            html_out.append(f'<blockquote class="border-l-4 border-cyan-500 pl-4 py-2 my-3 italic text-slate-300 bg-slate-900/60 rounded-r-xl">{clean_q}</blockquote>')
            continue

        # Lists
        if l_str.startswith("- ") or l_str.startswith("* "):
            if not in_list or list_type != "ul":
                if in_list: html_out.append(f"</{list_type}>")
                html_out.append('<ul class="my-3 space-y-1.5 bg-slate-900/40 p-3.5 rounded-xl border border-slate-800/80">')
                in_list = True
                list_type = "ul"
            html_out.append(f'<li class="ml-4 list-disc text-slate-300 text-sm leading-relaxed">{l_str[2:]}</li>')
            continue

        m_num = re.match(r"^(\d+)\.\s+(.*)", l_str)
        if m_num:
            if not in_list or list_type != "ol":
                if in_list: html_out.append(f"</{list_type}>")
                html_out.append('<ol class="my-3 space-y-1.5 bg-slate-900/40 p-3.5 rounded-xl border border-slate-800/80">')
                in_list = True
                list_type = "ol"
            html_out.append(f'<li class="ml-4 list-decimal text-slate-300 text-sm leading-relaxed">{m_num.group(2)}</li>')
            continue

        if in_list:
            html_out.append(f"</{list_type}>")
            in_list = False

        if l_str.startswith("<div") or l_str.startswith("<hr"):
            html_out.append(l_str)
        else:
            html_out.append(f'<p class="mb-3 text-slate-300 leading-relaxed text-sm sm:text-base">{l_str}</p>')

    if in_list:
        html_out.append(f"</{list_type}>")

    return "".join(html_out)


# --- BOOK 1: GUIA DEFINITIVO DO CRIADOR DIGITAL ---
md1_path = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_35REAIS.md")
with open(md1_path, "r", encoding="utf-8") as f:
    raw_md1 = f.read()

clean_lines1 = []
for line in raw_md1.split("\n"):
    if line.strip().startswith("feito:") or line.strip().startswith("Description:"):
        continue
    clean_lines1.append(line)

lines1 = "\n".join(clean_lines1).split("\n")

raw_chapters1 = []
current_module = "Módulo 1: Fundamentos dos Produtos Digitais"
current_title = "⚡ Guia Definitivo do Criador Digital"
current_body = []

for line in lines1:
    line_s = line.strip()
    if line_s.startswith("# MÓDULO "):
        if current_body:
            c_str = "\n".join(current_body).strip()
            if len(c_str) > 20:
                raw_chapters1.append({"module": current_module, "title": current_title, "content": c_str})
            current_body = []
        current_module = line_s.replace("# ", "").strip()
        current_title = current_module
        continue

    if line_s.startswith("## "):
        if current_body:
            c_str = "\n".join(current_body).strip()
            if len(c_str) > 20:
                raw_chapters1.append({"module": current_module, "title": current_title, "content": c_str})
            current_body = []
        current_title = re.sub(r"^##\s*", "", line_s).strip()
        continue

    if line_s.startswith("# ") and not line_s.startswith("# MÓDULO"):
        header_text = re.sub(r"^#\s*", "", line_s).strip()
        header_clean = re.sub(r"^[0-9\.\s\-\:\#]+", "", header_text).lower()
        title_clean = re.sub(r"^[0-9\.\s\-\:\#]+", "", current_title).lower()
        if header_clean and title_clean and (header_clean in title_clean or title_clean in header_clean):
            continue

    current_body.append(line)

if current_body:
    c_str = "\n".join(current_body).strip()
    if len(c_str) > 20:
        raw_chapters1.append({"module": current_module, "title": current_title, "content": c_str})

book1_chapters = []
for idx, ch in enumerate(raw_chapters1):
    ch["id"] = idx + 1
    ch["html"] = md_to_html(ch["content"])
    book1_chapters.append(ch)


# --- BOOK 2: ESTRUTURA AQUECIMENTO ORGÂNICO ---
md2_path = os.path.join(dir_path, "4 Aquecendo sua conta 908780fb3d0a4ccb97aa5a1a24d6dcc1.md")
with open(md2_path, "r", encoding="utf-8") as f:
    raw_md2 = f.read()

# Split Book 2 into Logical Sections
qa_matches = re.findall(r'(\d+)\.\s+\*\*(.*?)\*\*\n\s+-\s+(.*?)(?=\n\d+\.|\Z)', raw_md2, re.DOTALL)

book2_chapters = []
intro_content = """# 🚀 Passos Fundamentais do Aquecimento Orgânico

> **Antes de postar qualquer conteúdo, aqueça a sua conta durante 5 a 7 dias para evitar bloqueios do algoritmo.**

- Criar seu perfil e cumprir todas as etapas obrigatórias do Instagram.
- Mudar sua conta para empresarial ou profissional.
- Engajar de 5 a 7 dias com conteúdos do seu nicho antes das primeiras postagens.
- Pesquisar palavras-chave relevantes, curtir, comentar e salvar referências.
- Manter consistência sem realizar ações em massa que simulem robôs (spam).
"""
book2_chapters.append({
    "id": 1,
    "module": "Guia de Aquecimento Orgânico",
    "title": "🚀 Passos Fundamentais & Introdução",
    "content": intro_content,
    "html": md_to_html(intro_content)
})

# Group Q&A items in chunks of 10
chunk_size = 10
for i in range(0, len(qa_matches), chunk_size):
    chunk = qa_matches[i:i+chunk_size]
    start_num = chunk[0][0]
    end_num = chunk[-1][0]
    
    qa_md = f"### 📑 Perguntas & Respostas #{start_num} até #{end_num}\n\n"
    for num, q, a in chunk:
        qa_md += f"#### Dúvida #{num}: {q.strip()}\n"
        qa_md += f"💡 **Resposta:** {a.strip()}\n\n---\n\n"
        
    ch_obj = {
        "id": len(book2_chapters) + 1,
        "module": f"Perguntas Frequentes #{start_num}-{end_num}",
        "title": f"❓ Dúvidas #{start_num} a #{end_num} do Aquecimento",
        "content": qa_md,
        "html": md_to_html(qa_md)
    }
    book2_chapters.append(ch_obj)

all_books_data = {
    "master_guide": book1_chapters,
    "aquecimento": book2_chapters
}

json_output_path = os.path.join(dir_path, "ebook_chapters.json")
with open(json_output_path, "w", encoding="utf-8") as f:
    json.dump(all_books_data, f, ensure_ascii=False, indent=2)

print(f"SUCCESS: Generated ebook_chapters.json with Master Guide ({len(book1_chapters)} ch) and Aquecimento ({len(book2_chapters)} ch)!")
