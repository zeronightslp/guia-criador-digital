import os
import re

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
md_master = os.path.join(dir_path, "PRODUTO_MASTER_GUIA_CRIADOR_DIGITAL.md")

with open(md_master, "r", encoding="utf-8") as f:
    raw_text = f.read()

# Enhance text for R$ 35 premium low-ticket product
header = """# ⚡ GUIA DEFINITIVO DO CRIADOR DIGITAL (PACK PREMIUM R$ 35)
> **O Manual de Ação Prático para Criar, Crescer e Monetizar no Instagram do Zero.**
> *Preço Sugerido de Venda: R$ 35,00 (Oferta de Entrada de Alta Conversão)*

---

### 🛡️ O QUE ESTÁ INCLUSO NESTE PACOTE:
- 📖 **Manual Master:** 5 Módulos e 31 Capítulos Práticos de Execução Imediata
- 🎯 **Checklist de Implementação:** Passo a passo para os primeiros R$ 1.000,00 online
- 🎁 **Kit Bônus Exclusivo:** Links de Presets, Templates Notion, Scripts de Ganchos e Banco de Vídeos Virais

---
"""

# Enhance readability, clean up duplicate title headers
cleaned_text = re.sub(r"# “O que é um Produto Digital.”", "", raw_text)
cleaned_text = re.sub(r"## “O que é um Produto Digital ”", "## 1. O que é um Produto Digital e Como Lucrar Hoje", cleaned_text)
cleaned_text = re.sub(r"## Quais as vantagens", "## 2. As 10 Vantagens Brutais dos Produtos Digitais", cleaned_text)
cleaned_text = re.sub(r"## Melhores nichos para Produtos Digitais", "## 3. Os 10 Nichos Mais Lucrativos", cleaned_text)

full_enhanced_md = header + "\n" + cleaned_text

output_md = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_35REAIS.md")
with open(output_md, "w", encoding="utf-8") as f:
    f.write(full_enhanced_md)

# Generate HTML Ebook with Avant-Garde Design for PDF/Web
html_ebook = os.path.join(dir_path, "GUIA_MEGAPACK_CRIADOR_DIGITAL_35REAIS.html")

body_html = full_enhanced_md.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
body_html = re.sub(r"^# (.*?)$", r"<h1>\1</h1>", body_html, flags=re.M)
body_html = re.sub(r"^## (.*?)$", r"<h2>\1</h2>", body_html, flags=re.M)
body_html = re.sub(r"^### (.*?)$", r"<h3>\1</h3>", body_html, flags=re.M)
body_html = re.sub(r"^\> (.*?)$", r"<blockquote>\1</blockquote>", body_html, flags=re.M)
body_html = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", body_html)
body_html = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2" target="_blank">\1</a>', body_html)
body_html = body_html.replace("\n\n", "</p><p>")

html_template = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia do Criador Digital - Pack R$35</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;600;700;800&display=swap');
        :root {{
            --bg: #0b0f17;
            --card-bg: rgba(30, 41, 59, 0.7);
            --primary: #38bdf8;
            --accent: #f43f5e;
            --text: #f8fafc;
            --subtext: #94a3b8;
            --border: rgba(255, 255, 255, 0.08);
        }}
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: var(--bg);
            color: var(--text);
            line-height: 1.8;
            max-width: 860px;
            margin: 0 auto;
            padding: 40px 24px;
        }}
        h1 {{
            font-size: 2.4rem;
            font-weight: 800;
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-top: 40px;
            padding-bottom: 16px;
            border-bottom: 1px solid var(--border);
        }}
        h2 {{
            font-size: 1.6rem;
            color: #818cf8;
            margin-top: 36px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        h3 {{
            font-size: 1.25rem;
            color: var(--accent);
            margin-top: 24px;
        }}
        blockquote {{
            background: var(--card-bg);
            backdrop-filter: blur(12px);
            border-left: 4px solid var(--primary);
            padding: 18px 24px;
            border-radius: 12px;
            margin: 24px 0;
            border-top: 1px solid var(--border);
            border-right: 1px solid var(--border);
            border-bottom: 1px solid var(--border);
        }}
        a {{
            color: var(--primary);
            text-decoration: none;
            font-weight: 600;
            transition: all 0.2s;
        }}
        a:hover {{
            color: #7dd3fc;
            text-decoration: underline;
        }}
        p {{
            color: var(--subtext);
            font-size: 1.05rem;
            margin-bottom: 1.4rem;
        }}
        strong {{
            color: #ffffff;
        }}
        hr {{
            border: 0;
            height: 1px;
            background: var(--border);
            margin: 40px 0;
        }}
        .price-badge {{
            display: inline-block;
            background: linear-gradient(135deg, #10b981, #059669);
            color: white;
            padding: 6px 16px;
            border-radius: 20px;
            font-weight: 700;
            font-size: 0.9rem;
            margin-bottom: 20px;
        }}
    </style>
</head>
<body>
    <div class="price-badge">💰 PRODUTO PRONTO PARA VENDA: R$ 35,00</div>
    <div>{body_html}</div>
</body>
</html>"""

with open(html_ebook, "w", encoding="utf-8") as f:
    f.write(html_template)

print("Generated MD & HTML for R$ 35 offer!")
