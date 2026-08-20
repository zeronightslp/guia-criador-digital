import os

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
lp_file = os.path.join(dir_path, "LANDING_PAGE_OFERTA_35.html")

landing_html = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>O Guia do Criador Digital - Oferta Especial R$ 35,00</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
    </style>
</head>
<body class="bg-slate-950 text-slate-100 antialiased selection:bg-cyan-500 selection:text-white">
    <!-- Top Announcement Bar -->
    <div class="bg-gradient-to-r from-emerald-500 to-teal-600 text-white text-center py-2 text-xs md:text-sm font-bold tracking-wide uppercase shadow-md">
        🔥 OFERTA DE LANÇAMENTO EXCLUSIVA — DE <span class="line-through opacity-75">R$ 97,00</span> POR APENAS R$ 35,00
    </div>

    <!-- Hero Section -->
    <section class="max-w-5xl mx-auto px-6 pt-16 pb-20 text-center relative overflow-hidden">
        <div class="inline-flex items-center gap-2 px-4 py-2 rounded-full bg-slate-900 border border-slate-800 text-cyan-400 text-sm font-semibold mb-6">
            <span class="w-2 h-2 rounded-full bg-cyan-400 animate-ping"></span>
            O Guia Definitivo do Criador de Conteúdo
        </div>
        
        <h1 class="text-4xl md:text-6xl font-extrabold tracking-tight leading-tight text-white mb-6">
            Transforme seu Instagram em uma <span class="bg-gradient-to-r from-cyan-400 via-sky-400 to-indigo-400 bg-clip-text text-transparent">Máquina de Vendas Diárias</span>
        </h1>
        
        <p class="text-lg md:text-xl text-slate-400 max-w-3xl mx-auto mb-10 leading-relaxed">
            O passo a passo prático, compacto e ultra-robusto com 31 capítulos + bônus exclusivos para você criar seu produto digital e alcançar seus primeiros 10 mil seguidores engajados.
        </p>

        <!-- Product Hero Card -->
        <div class="max-w-lg mx-auto bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-3xl p-8 shadow-2xl relative mb-12">
            <div class="absolute -top-4 right-6 bg-gradient-to-r from-emerald-500 to-teal-500 text-slate-950 font-black text-xs px-3 py-1 rounded-full uppercase tracking-wider shadow-lg">
                Economize 64%
            </div>
            
            <div class="text-left mb-6 space-y-3">
                <div class="flex items-center gap-3 text-slate-200 font-semibold text-sm">
                    <span class="text-emerald-400 text-lg">✓</span> 5 Módulos Master Práticos (31 Capítulos)
                </div>
                <div class="flex items-center gap-3 text-slate-200 font-semibold text-sm">
                    <span class="text-emerald-400 text-lg">✓</span> Pack com +900 Ganchos Virais para Reels
                </div>
                <div class="flex items-center gap-3 text-slate-200 font-semibold text-sm">
                    <span class="text-emerald-400 text-lg">✓</span> Templates Prontos no Notion + Presets Lightroom
                </div>
                <div class="flex items-center gap-3 text-slate-200 font-semibold text-sm">
                    <span class="text-emerald-400 text-lg">✓</span> Guia de Aquecimento Anti-Bloqueio do Instagram
                </div>
            </div>

            <div class="border-t border-slate-800 pt-6 text-center">
                <div class="text-slate-500 text-sm line-through font-medium">De R$ 97,00</div>
                <div class="text-4xl font-extrabold text-white my-1">
                    <span class="text-sm font-semibold text-slate-400">12x de</span> R$ 3,50 <span class="text-sm font-semibold text-slate-400">ou</span>
                </div>
                <div class="text-3xl font-black text-emerald-400 mb-6">R$ 35,00 à vista</div>

                <a href="SEU_LINK_DE_CHECKOUT_AQUI" class="block w-full bg-gradient-to-r from-emerald-500 to-teal-500 hover:from-emerald-400 hover:to-teal-400 text-slate-950 font-extrabold text-lg py-4 rounded-2xl shadow-xl shadow-emerald-500/20 transition-all hover:scale-[1.02] active:scale-[0.98]">
                    QUERO ACESSO IMEDIATO — R$ 35
                </a>
                <p class="text-xs text-slate-500 mt-3 flex items-center justify-center gap-2">
                    🔒 Pagamento 100% Seguro • Liberado Instantaneamente
                </p>
            </div>
        </div>
    </section>

    <!-- Content Modules Section -->
    <section class="max-w-4xl mx-auto px-6 pb-24">
        <h2 class="text-2xl md:text-3xl font-bold text-center text-white mb-12">
            O que você vai dominar no <span class="text-cyan-400">Guia do Criador Digital</span>
        </h2>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div class="bg-slate-900/50 border border-slate-800 p-6 rounded-2xl">
                <div class="text-cyan-400 font-bold text-sm mb-2">MÓDULO 01</div>
                <h3 class="text-xl font-bold text-white mb-2">Fundamentos dos Produtos Digitais</h3>
                <p class="text-slate-400 text-sm">Como escolher os nichos mais lucrativos e estruturar seu primeiro produto de margem alta sem estoque.</p>
            </div>

            <div class="bg-slate-900/50 border border-slate-800 p-6 rounded-2xl">
                <div class="text-cyan-400 font-bold text-sm mb-2">MÓDULO 02</div>
                <h3 class="text-xl font-bold text-white mb-2">Modelos de Monetização</h3>
                <p class="text-slate-400 text-sm">As 6 formas comprovadas de gerar caixa diário com seu perfil no Instagram usando funis automáticos.</p>
            </div>

            <div class="bg-slate-900/50 border border-slate-800 p-6 rounded-2xl">
                <div class="text-cyan-400 font-bold text-sm mb-2">MÓDULO 03</div>
                <h3 class="text-xl font-bold text-white mb-2">Crescimento & Conteúdo Viral</h3>
                <p class="text-slate-400 text-sm">Como dominar os ganchos (Hooks), tempo de retenção, SEO do Instagram e engenharia reversa de Reels.</p>
            </div>

            <div class="bg-slate-900/50 border border-slate-800 p-6 rounded-2xl">
                <div class="text-cyan-400 font-bold text-sm mb-2">MÓDULO 04 & 05</div>
                <h3 class="text-xl font-bold text-white mb-2">Kit de Recursos & Bônus</h3>
                <p class="text-slate-400 text-sm">Templates no Notion, presets Lightroom, gerador de ideias infinitas e softwares gratuitos essenciais.</p>
            </div>
        </div>
    </section>

    <!-- Guarantee Footer Bar -->
    <footer class="border-t border-slate-800 py-12 text-center text-slate-500 text-sm">
        <p>© 2026 O Guia do Criador Digital. Todos os direitos reservados.</p>
    </footer>
</body>
</html>
"""

with open(lp_file, "w", encoding="utf-8") as f:
    f.write(landing_html)

print("Generated LANDING_PAGE_OFERTA_35.html successfully!")
