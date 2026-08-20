import os
import re
import subprocess
import unicodedata

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
md_path = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_35REAIS.md")

with open(md_path, "r", encoding="utf-8") as f:
    raw_md = f.read()

def normalize_slug(text):
    text = text.lower().strip()
    # Normalize unicode
    text = unicodedata.normalize('NFKD', text)
    text = ''.join([c for c in text if not unicodedata.combining(c)])
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_-]+', '-', text)
    return text.strip('-')

lines = raw_md.split('\n')
clean_md = []
for line in lines:
    if line.strip().startswith("feito:") or line.strip().startswith("Description:"):
        continue
    clean_md.append(line)

content_md = "\n".join(clean_md)

def md_to_smart_html(md_text):
    out = []
    blocks = md_text.split('\n\n')
    
    for block in blocks:
        block = block.strip()
        if not block:
            continue

        # Code block
        if block.startswith('```'):
            code_content = re.sub(r'^```.*?\n', '', block)
            code_content = re.sub(r'\n```$', '', code_content)
            code_content = code_content.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
            out.append(f'<div class="code-box"><pre><code>{code_content}</code></pre></div>')
            continue

        # Aside / Callout block
        if block.startswith('<aside>') or block.startswith('blockquote'):
            clean_aside = re.sub(r'</?aside>', '', block)
            clean_aside = re.sub(r'^\> ', '', clean_aside, flags=re.M)
            out.append(f'<div class="callout-box">{inline_format(clean_aside)}</div>')
            continue

        # Blockquote
        if block.startswith('>'):
            clean_bq = re.sub(r'^\> ', '', block, flags=re.M)
            out.append(f'<blockquote>{inline_format(clean_bq)}</blockquote>')
            continue

        # Heading 1 (Module)
        if block.startswith('# '):
            title = block[2:].strip()
            slug1 = normalize_slug(title)
            slug2 = normalize_slug(re.sub(r'^[#⚡🚀📋🛡️]+\s*', '', title))
            out.append(f'<div class="module-header" id="{slug1}"><h1 id="{slug2}">{inline_format(title)}</h1></div>')
            continue

        # Heading 2 (Chapter)
        if block.startswith('## '):
            title = block[3:].strip()
            slug1 = normalize_slug(title)
            slug2 = normalize_slug(re.sub(r'^[0-9\.\s\-\:\#]+', '', title))
            out.append(f'<h2 class="chapter-title" id="{slug1}"><span id="{slug2}"></span><span class="h2-icon">📌</span> {inline_format(title)}</h2>')
            continue

        # Heading 3 (Sub-section)
        if block.startswith('### '):
            title = block[4:].strip()
            slug1 = normalize_slug(title)
            out.append(f'<h3 class="section-title" id="{slug1}">{inline_format(title)}</h3>')
            continue

        # Horizontal rule
        if block == '---':
            out.append('<hr class="divider"/>')
            continue

        # Bullet list
        if block.startswith('- ') or block.startswith('* '):
            items = block.split('\n')
            list_html = '<ul class="custom-list">\n'
            for item in items:
                item_text = re.sub(r'^[\-\*]\s+', '', item.strip())
                if item_text:
                    list_html += f'  <li>{inline_format(item_text)}</li>\n'
            list_html += '</ul>'
            out.append(list_html)
            continue

        # Numbered list
        if re.match(r'^\d+\.\s', block):
            items = block.split('\n')
            list_html = '<ol class="custom-num-list">\n'
            for item in items:
                item_text = re.sub(r'^\d+\.\s+', '', item.strip())
                if item_text:
                    list_html += f'  <li>{inline_format(item_text)}</li>\n'
            list_html += '</ol>'
            out.append(list_html)
            continue

        # Image tag
        if block.startswith('!['):
            m = re.match(r'!\[(.*?)\]\((.*?)\)', block)
            if m:
                alt, src = m.group(1), m.group(2)
                out.append(f'<div class="img-container"><img src="{src}" alt="{alt}" class="ebook-img"/><p class="img-caption">{alt}</p></div>')
                continue

        # Paragraph
        paragraphs = block.split('\n')
        p_html = '<p>' + '<br/>'.join([inline_format(p) for p in paragraphs]) + '</p>'
        out.append(p_html)

    return '\n\n'.join(out)

def inline_format(text):
    text = text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
    # Strong
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Em
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Inline code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    # Links with custom button styling if CTA or external link
    def link_repl(match):
        label = match.group(1)
        url = match.group(2)
        if url.startswith("#"):
            target_id = normalize_slug(url[1:])
            return f'<a href="#{target_id}" class="toc-link">{label}</a>'
        if any(k in url for k in ["pay.", "gumroad", "wa.link", "loom.com", "kiwify"]):
            return f'<a href="{url}" target="_blank" class="cta-link-btn">🚀 {label}</a>'
        return f'<a href="{url}" target="_blank" class="inline-link">{label}</a>'

    text = re.sub(r'\[(.*?)\]\((.*?)\)', link_repl, text)
    return text

parsed_body = md_to_smart_html(content_md)

# Cover Page HTML
cover_html = """
<div class="cover-page">
    <div class="badge-pill">⚡ EBOOK MASTER &amp; GUIA INTERATIVO COMPLETO</div>
    <h1 class="cover-title">GUIA DEFINITIVO DO CRIADOR DIGITAL</h1>
    <p class="cover-subtitle">O Manual de Ação Prático para Criar, Crescer e Monetizar no Instagram do Zero</p>

    <div class="cover-features">
        <div class="feature-item">
            <span class="icon">📖</span>
            <div>
                <strong>72 Páginas de Puro Conteúdo</strong>
                <span>5 Módulos e 31 Capítulos Práticos</span>
            </div>
        </div>
        <div class="feature-item">
            <span class="icon">🎯</span>
            <div>
                <strong>Estratégia R$ 1.000,00</strong>
                <span>Monetização e Vendas Perpétuas</span>
            </div>
        </div>
        <div class="feature-item">
            <span class="icon">🎁</span>
            <div>
                <strong>Kit Bônus Exclusivo</strong>
                <span>Templates Notion, Presets &amp; Scripts</span>
            </div>
        </div>
    </div>

    <div class="cover-footer">
        <div class="price-tag">OFERTA ESPECIAL DE ENTRADA: <span>R$ 35,00</span></div>
        <div class="author-tag">Edição de Alta Conversão 2026 • zeronightslp</div>
    </div>
</div>
<div class="page-break"></div>
"""

css_styles = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@500;700;800&display=swap');

@page {
    size: A4;
    margin: 20mm 15mm 20mm 15mm;
    @bottom-right {
        content: counter(page);
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 9pt;
        color: #64748b;
    }
    @bottom-left {
        content: "Guia Definitivo do Criador Digital • Pack R$ 35";
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 9pt;
        color: #64748b;
    }
}

:root {
    --bg-dark: #090d16;
    --card-bg: #131b2e;
    --card-border: rgba(56, 189, 248, 0.15);
    --primary: #38bdf8;
    --primary-gradient: linear-gradient(135deg, #38bdf8 0%, #818cf8 100%);
    --accent: #f43f5e;
    --emerald: #10b981;
    --text-light: #f8fafc;
    --text-muted: #94a3b8;
    --border: #1e293b;
}

* {
    box-sizing: border-box;
    -webkit-print-color-adjust: exact;
    print-color-adjust: exact;
}

body {
    font-family: 'Plus Jakarta Sans', -apple-system, sans-serif;
    background-color: var(--bg-dark);
    color: var(--text-light);
    line-height: 1.75;
    font-size: 11pt;
    margin: 0;
    padding: 0;
}

.page-break {
    page-break-after: always;
    break-after: page;
}

/* COVER PAGE */
.cover-page {
    min-height: 88vh;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    text-align: center;
    background: radial-gradient(circle at top right, rgba(56, 189, 248, 0.15), transparent 50%),
                radial-gradient(circle at bottom left, rgba(129, 140, 248, 0.15), transparent 50%),
                #090d16;
    border: 1px solid rgba(255, 255, 255, 0.12);
    border-radius: 24px;
    padding: 60px 40px;
    margin-bottom: 40px;
    position: relative;
}

.badge-pill {
    display: inline-block;
    background: rgba(56, 189, 248, 0.12);
    border: 1px solid rgba(56, 189, 248, 0.35);
    color: var(--primary);
    padding: 8px 22px;
    border-radius: 50px;
    font-weight: 700;
    font-size: 10pt;
    letter-spacing: 1px;
}

.cover-title {
    font-family: 'Outfit', sans-serif;
    font-size: 32pt;
    font-weight: 800;
    line-height: 1.15;
    background: linear-gradient(135deg, #ffffff 0%, #38bdf8 50%, #818cf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin: 20px 0;
}

.cover-subtitle {
    font-size: 13.5pt;
    color: var(--text-muted);
    max-width: 650px;
    margin: 0 auto;
}

.cover-features {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
    width: 100%;
    margin: 40px 0;
}

.feature-item {
    background: rgba(30, 41, 59, 0.55);
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 18px 16px;
    text-align: left;
    display: flex;
    gap: 12px;
    align-items: center;
}

.feature-item .icon {
    font-size: 20pt;
}

.feature-item strong {
    display: block;
    font-size: 10.5pt;
    color: #fff;
}

.feature-item span {
    font-size: 9pt;
    color: var(--text-muted);
}

.cover-footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    border-top: 1px solid var(--border);
    padding-top: 20px;
}

.price-tag {
    font-size: 11pt;
    font-weight: 600;
    color: var(--text-muted);
}

.price-tag span {
    color: var(--emerald);
    font-weight: 800;
    font-size: 14pt;
}

.author-tag {
    font-size: 10pt;
    color: #64748b;
}

/* HEADINGS */
.module-header {
    margin-top: 50px;
    padding-top: 30px;
    page-break-before: always;
}

.module-header h1 {
    font-family: 'Outfit', sans-serif;
    font-size: 22pt;
    font-weight: 800;
    color: #ffffff;
    background: linear-gradient(135deg, #0284c7, #6366f1);
    padding: 16px 24px;
    border-radius: 14px;
    margin: 0 0 30px 0;
}

.chapter-title {
    font-family: 'Outfit', sans-serif;
    font-size: 15.5pt;
    font-weight: 700;
    color: #38bdf8;
    margin-top: 36px;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 10px;
    page-break-inside: avoid;
}

.section-title {
    font-size: 12.5pt;
    font-weight: 700;
    color: #f43f5e;
    margin-top: 26px;
    margin-bottom: 12px;
    page-break-inside: avoid;
}

p {
    color: #cbd5e1;
    font-size: 11pt;
    margin-bottom: 16px;
}

strong {
    color: #ffffff;
    font-weight: 700;
}

ul.custom-list, ol.custom-num-list {
    padding-left: 24px;
    margin-bottom: 24px;
}

ul.custom-list li, ol.custom-num-list li {
    color: #cbd5e1;
    margin-bottom: 10px;
}

ul.custom-list li::marker {
    color: var(--primary);
}

ol.custom-num-list li::marker {
    color: #818cf8;
    font-weight: 700;
}

blockquote {
    background: rgba(30, 41, 59, 0.6);
    border-left: 4px solid var(--primary);
    padding: 16px 20px;
    border-radius: 0 12px 12px 0;
    margin: 24px 0;
    color: #e2e8f0;
    font-style: italic;
    page-break-inside: avoid;
}

.callout-box {
    background: linear-gradient(135deg, rgba(30, 41, 59, 0.85), rgba(15, 23, 42, 0.95));
    border: 1px solid rgba(56, 189, 248, 0.25);
    border-radius: 14px;
    padding: 20px 24px;
    margin: 24px 0;
    color: #f1f5f9;
    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
    page-break-inside: avoid;
}

.code-box {
    background: #020617;
    border: 1px solid #1e293b;
    border-radius: 12px;
    padding: 16px 20px;
    margin: 20px 0;
    overflow-x: auto;
    font-family: 'Fira Code', monospace;
    font-size: 10pt;
    color: #38bdf8;
    page-break-inside: avoid;
}

.code-box code {
    white-space: pre-wrap;
    word-break: break-word;
}

a.inline-link, a.toc-link {
    color: #38bdf8;
    text-decoration: underline;
    text-underline-offset: 3px;
    font-weight: 600;
}

a.cta-link-btn {
    display: inline-block;
    background: linear-gradient(135deg, #10b981, #059669);
    color: #ffffff !important;
    text-decoration: none !important;
    font-weight: 700;
    font-size: 10.5pt;
    padding: 10px 20px;
    border-radius: 10px;
    margin: 10px 0;
    box-shadow: 0 4px 14px rgba(16, 185, 129, 0.3);
    page-break-inside: avoid;
}

.img-container {
    text-align: center;
    margin: 28px 0;
    page-break-inside: avoid;
}

.ebook-img {
    max-width: 100%;
    height: auto;
    border-radius: 14px;
    border: 1px solid var(--border);
}

.img-caption {
    font-size: 9.5pt;
    color: var(--text-muted);
    margin-top: 8px;
}

hr.divider {
    border: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.15), transparent);
    margin: 40px 0;
}
"""

full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia Definitivo do Criador Digital - Ebook Master &amp; PDF Inteligente</title>
    <style>
    {css_styles}
    </style>
</head>
<body>
    <div class="ebook-wrapper">
        {cover_html}
        {parsed_body}
    </div>
</body>
</html>"""

html_out_path = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_35REAIS.html")
with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

pdf_out_path = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf")
cmd = [
    "google-chrome",
    "--headless",
    "--no-sandbox",
    "--disable-gpu",
    "--no-pdf-header-footer",
    f"--print-to-pdf={pdf_out_path}",
    html_out_path
]

res = subprocess.run(cmd, capture_output=True, text=True)
if os.path.exists(pdf_out_path):
    size_mb = os.path.getsize(pdf_out_path) / (1024 * 1024)
    print(f"SUCCESS: Smart PDF updated at {pdf_out_path} ({size_mb:.2f} MB)")
