import os
import subprocess

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
md_path = os.path.join(dir_path, "4 Aquecendo sua conta 908780fb3d0a4ccb97aa5a1a24d6dcc1.md")

with open(md_path, "r", encoding="utf-8") as f:
    raw_md = f.read()

# Parse Q&A items
import re

qa_items = []
qa_matches = re.findall(r'(\d+)\.\s+\*\*(.*?)\*\*\n\s+-\s+(.*?)(?=\n\d+\.|\Z)', raw_md, re.DOTALL)

qa_html_cards = ""
for num, q, a in qa_matches:
    qa_html_cards += f"""
    <div class="qa-card">
        <div class="qa-num">DÚVIDA #{num}</div>
        <div class="qa-question">❓ {q.strip()}</div>
        <div class="qa-answer">💡 {a.strip()}</div>
    </div>
    """

full_html = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>E-Book: Estrutura Aquecimento Orgânico</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Outfit:wght@700;800;900&display=swap');
        
        @page {{
            size: A4;
            margin: 15mm;
        }}
        
        body {{
            font-family: 'Plus Jakarta Sans', sans-serif;
            background-color: #090d16;
            color: #e2e8f0;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            -webkit-print-color-adjust: exact;
        }}

        .cover {{
            text-align: center;
            padding: 40px 20px;
            background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #090d16 100%);
            border-radius: 20px;
            border: 2px solid #38bdf8;
            margin-bottom: 40px;
            page-break-after: always;
        }}

        .cover-badge {{
            display: inline-block;
            background: #0284c7;
            color: #ffffff;
            font-weight: 800;
            font-size: 14px;
            padding: 6px 18px;
            border-radius: 50px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 20px;
        }}

        .cover h1 {{
            font-family: 'Outfit', sans-serif;
            font-size: 38px;
            font-weight: 900;
            color: #ffffff;
            margin: 10px 0;
            line-height: 1.1;
        }}

        .cover p {{
            font-size: 16px;
            color: #94a3b8;
            max-width: 600px;
            margin: 15px auto;
        }}

        .cover-author {{
            margin-top: 30px;
            font-size: 14px;
            color: #38bdf8;
            font-weight: 700;
        }}

        .intro-box {{
            background: #1e293b;
            border-left: 4px solid #38bdf8;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 30px;
            font-size: 15px;
            color: #cbd5e1;
        }}

        .intro-box ul {{
            margin: 10px 0 0 20px;
            padding: 0;
        }}

        .section-title {{
            font-family: 'Outfit', sans-serif;
            font-size: 24px;
            font-weight: 800;
            color: #38bdf8;
            border-bottom: 2px solid #334155;
            padding-bottom: 8px;
            margin-top: 30px;
            margin-bottom: 20px;
        }}

        .qa-card {{
            background: #0f172a;
            border: 1px solid #1e293b;
            border-radius: 14px;
            padding: 16px 20px;
            margin-bottom: 16px;
            page-break-inside: avoid;
        }}

        .qa-num {{
            font-size: 11px;
            font-weight: 800;
            color: #38bdf8;
            letter-spacing: 1px;
            margin-bottom: 4px;
        }}

        .qa-question {{
            font-size: 15px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 6px;
        }}

        .qa-answer {{
            font-size: 14px;
            color: #cbd5e1;
            line-height: 1.5;
        }}

        .footer {{
            text-align: center;
            font-size: 12px;
            color: #64748b;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #1e293b;
        }}
    </style>
</head>
<body>

    <div class="cover">
        <span class="cover-badge">🔥 E-BOOK BÔNUS EXCLUSIVO</span>
        <h1>ESTRUTURA DE AQUECIMENTO ORGÂNICO</h1>
        <p>Manual Prático de 52 Perguntas e Respostas para Aquecer Perfis no Instagram, Evitar Shadowban e Maximizar o Alcance dos Reels.</p>
        <div class="cover-author">Desenvolvido por @joaolucas.slp</div>
    </div>

    <div class="intro-box">
        <strong style="color: #ffffff; font-size: 17px;">📌 Passos Iniciais para Aquecimento Estratégico:</strong>
        <ul>
            <li>Criar o perfil e cumprir todas as etapas obrigatórias do Instagram (sem impulsionar posts).</li>
            <li>Alterar a conta para tipo Profissional / Empresarial.</li>
            <li>Passar de 5 a 7 dias engajando com conteúdos do seu nicho antes das primeiras postagens.</li>
            <li>Pesquisar palavras-chave relevantes, curtir, comentar e salvar posts de referência.</li>
        </ul>
    </div>

    <div class="section-title">📑 52 Perguntas & Respostas do Aquecimento Orgânico</div>

    {qa_html_cards}

    <div class="footer">
        © 2026 Guia do Criador Digital • @joaolucas.slp • Todos os direitos reservados.
    </div>

</body>
</html>
"""

html_out_path = os.path.join(dir_path, "ESTRUTURA_AQUECIMENTO_ORGANICO.html")
pdf_out_path = os.path.join(dir_path, "ESTRUTURA_AQUECIMENTO_ORGANICO.pdf")

with open(html_out_path, "w", encoding="utf-8") as f:
    f.write(full_html)

print("Generated HTML for Aquecimento Organico!")

# Print to PDF using Headless Chrome
cmd = [
    "google-chrome",
    "--headless",
    "--disable-gpu",
    "--no-sandbox",
    f"--print-to-pdf={pdf_out_path}",
    html_out_path
]
res = subprocess.run(cmd, capture_output=True, text=True)

if res.returncode == 0:
    print(f"SUCCESS: E-book PDF created at {pdf_out_path}")
else:
    print("Chrome print error:", res.stderr)
