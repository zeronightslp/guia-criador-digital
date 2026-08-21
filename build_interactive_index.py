import os
import json

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
json_path = os.path.join(dir_path, "ebook_chapters.json")

with open(json_path, "r", encoding="utf-8") as f:
    all_books = json.load(f)

json_str = json.dumps(all_books, ensure_ascii=False)

# Pre-render initial TOC and Chapter 0 for instant SSR/no-JS display
master_chapters = all_books.get("master_guide", [])
initial_toc_items = []
for idx, ch in enumerate(master_chapters):
    is_active = idx == 0
    active_cls = "bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 shadow-sm" if is_active else "text-slate-400 hover:bg-slate-900 hover:text-slate-200 border border-transparent"
    initial_toc_items.append(f"""
        <button onclick="loadChapterByIdx({idx})" 
                class="w-full text-left p-2.5 rounded-xl text-xs font-semibold transition-all flex items-center justify-between gap-2 {active_cls}">
            <div class="truncate">
                <span class="text-[10px] text-slate-500 block font-mono font-normal truncate">{ch.get('module', '')}</span>
                <span class="truncate font-bold">{ch.get('title', '')}</span>
            </div>
            <i data-lucide="chevron-right" class="w-3.5 h-3.5 shrink-0 opacity-50"></i>
        </button>
    """)

initial_toc_html = "".join(initial_toc_items)
initial_chapter = master_chapters[0] if master_chapters else {"title": "Carregando...", "html": "<p>Carregando conteúdo...</p>", "module": "Módulo 1"}

initial_content_html = f"""
    <h2 class="font-heading font-extrabold text-xl sm:text-2xl text-white pb-3 border-b border-slate-800">{initial_chapter.get('title', '')}</h2>
    <div class="prose prose-invert max-w-none text-slate-300 text-sm sm:text-base leading-relaxed space-y-4">
        {initial_chapter.get('html', '')}
    </div>
"""

index_html_content = f"""<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia Definitivo do Criador Digital - Leitor Interativo &amp; E-Books Completo</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts & Lucide Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>

    <script>
        tailwind.config = {{
            darkMode: 'class',
            theme: {{
                extend: {{
                    fontFamily: {{
                        sans: ['Plus Jakarta Sans', 'sans-serif'],
                        heading: ['Outfit', 'sans-serif'],
                    }},
                    colors: {{
                        brand: {{
                            50: '#f0f9ff',
                            400: '#38bdf8',
                            500: '#0ea5e9',
                            600: '#0284c7',
                            900: '#0c4a6e',
                            950: '#082f49',
                        }}
                    }}
                }}
            }}
        }}
    </script>
    <style>
        body {{ font-family: 'Plus Jakarta Sans', sans-serif; }}
        .font-heading {{ font-family: 'Outfit', sans-serif; }}

        .glass-panel {{
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }}
        
        .custom-scrollbar::-webkit-scrollbar {{
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #090d16;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #1e293b;
            border-radius: 6px;
        }}

        /* Sepia Theme Mode Overrides */
        .theme-sepia {{
            background-color: #f5eccb !important;
            color: #2c221e !important;
        }}
        .theme-sepia .glass-panel {{
            background: rgba(247, 240, 219, 0.95) !important;
            border-color: rgba(180, 140, 90, 0.3) !important;
            color: #2c221e !important;
        }}
        .theme-sepia p, .theme-sepia li, .theme-sepia span {{
            color: #3d302a !important;
        }}
        .theme-sepia h1, .theme-sepia h2, .theme-sepia h3, .theme-sepia h4, .theme-sepia strong {{
            color: #1c130e !important;
        }}
        .theme-sepia .text-white, .theme-sepia .text-slate-100, .theme-sepia .text-slate-200, .theme-sepia .text-slate-300, .theme-sepia .text-slate-400 {{
            color: #2c221e !important;
        }}
        .theme-sepia .bg-slate-900, .theme-sepia .bg-slate-950 {{
            background-color: #ede3c0 !important;
            border-color: #d8cba0 !important;
        }}
        .theme-sepia .border-slate-800, .theme-sepia .border-slate-700 {{
            border-color: #d4c59a !important;
        }}

        /* Highlight Search Terms */
        mark.search-highlight {{
            background-color: #f59e0b;
            color: #000;
            padding: 2px 4px;
            border-radius: 4px;
            font-weight: 700;
        }}

        /* Smooth Page Transition */
        .page-flip-anim {{
            animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>
</head>
<body id="app-body" class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-cyan-500 selection:text-white custom-scrollbar">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-50 glass-panel border-b border-slate-800 px-4 md:px-8 py-3.5 flex flex-wrap items-center justify-between gap-4">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center font-black text-white shadow-lg shadow-cyan-500/20 text-lg">
                📖
            </div>
            <div>
                <h1 class="font-heading font-extrabold text-slate-100 text-base leading-tight flex items-center gap-2">
                    Guia do Criador Digital <span class="bg-cyan-500/10 text-cyan-400 text-xs px-2.5 py-0.5 rounded-full border border-cyan-500/20 font-semibold">Leitor Interativo &amp; PDF</span>
                </h1>
                <p class="text-xs text-slate-400">Ecossistema Completo de E-Books • Busca &amp; Leitura em HD</p>
            </div>
        </div>

        <!-- Center Tabs (Visible on all screens) -->
        <nav class="flex flex-wrap items-center gap-1 bg-slate-900/90 p-1 rounded-xl border border-slate-800 text-xs font-semibold">
            <button onclick="switchTab('reader')" id="tab-reader" class="tab-btn px-3 sm:px-4 py-2 rounded-lg text-slate-100 bg-slate-800 shadow-sm flex items-center gap-2 transition-all">
                <i data-lucide="book-open" class="w-4 h-4 text-cyan-400"></i> Leitor de E-Book
            </button>
            <button onclick="switchTab('pdf')" id="tab-pdf" class="tab-btn px-3 sm:px-4 py-2 rounded-lg text-slate-400 hover:text-slate-200 flex items-center gap-2 transition-all">
                <i data-lucide="file-text" class="w-4 h-4 text-indigo-400"></i> Visualizador PDF
            </button>
            <button onclick="switchTab('generator')" id="tab-generator" class="tab-btn px-3 sm:px-4 py-2 rounded-lg text-slate-400 hover:text-slate-200 flex items-center gap-2 transition-all">
                <i data-lucide="sparkles" class="w-4 h-4 text-rose-400"></i> Gerador de Ganchos
            </button>
        </nav>

        <!-- Right Quick Actions -->
        <div class="flex items-center gap-2">
            <a href="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf" download class="flex items-center gap-1.5 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-extrabold text-xs px-3.5 py-2.5 rounded-xl transition-all shadow-md">
                <i data-lucide="download" class="w-4 h-4"></i> <span class="hidden sm:inline">Baixar PDF Master</span>
            </a>
            <a href="./ESTRUTURA_AQUECIMENTO_ORGANICO.pdf" download class="flex items-center gap-1.5 bg-gradient-to-r from-amber-500 to-orange-600 hover:from-amber-400 hover:to-orange-500 text-slate-950 font-extrabold text-xs px-3.5 py-2.5 rounded-xl transition-all shadow-md" title="Baixar E-Book Bônus: Estrutura Aquecimento Orgânico">
                <i data-lucide="flame" class="w-4 h-4"></i> <span class="hidden sm:inline">PDF Aquecimento</span>
            </a>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 space-y-6">

        <!-- TAB 1: E-BOOK INTERACTIVE READER -->
        <section id="sec-reader" class="tab-content space-y-5">

            <!-- E-Book Book Switcher Banner -->
            <div class="glass-panel p-3.5 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-3 border border-cyan-500/20 bg-cyan-950/20">
                <div class="flex items-center gap-2 text-xs font-bold text-slate-200">
                    <i data-lucide="library" class="w-4 h-4 text-cyan-400"></i>
                    <span>Selecione o E-Book para Leitura Interativa:</span>
                </div>
                <div class="flex items-center gap-2 w-full sm:w-auto">
                    <button onclick="selectBook('master_guide')" id="btn-book-master" class="flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-gradient-to-r from-cyan-500 to-blue-600 text-slate-950 shadow-md">
                        <i data-lucide="book" class="w-3.5 h-3.5"></i> 1. Manual Master Completo
                    </button>
                    <button onclick="selectBook('aquecimento')" id="btn-book-aquecimento" class="flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800">
                        <i data-lucide="flame" class="w-3.5 h-3.5 text-amber-400"></i> 2. E-Book Bônus Aquecimento
                    </button>
                </div>
            </div>

            <!-- Search Bar & Controls Banner -->
            <div class="glass-panel p-4 sm:p-5 rounded-2xl flex flex-col md:flex-row items-center justify-between gap-4">
                
                <!-- Live Search Box -->
                <div class="relative w-full md:w-1/2">
                    <i data-lucide="search" class="w-5 h-5 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2"></i>
                    <input type="text" id="chapter-search-input" onkeyup="handleSearch(this.value)" placeholder="🔍 Pesquisar em todos os tópicos deste livro..." 
                           class="w-full bg-slate-900 border border-slate-700/80 rounded-xl pl-11 pr-10 py-3 text-sm text-slate-100 placeholder-slate-400 focus:outline-none focus:border-cyan-500 focus:ring-2 focus:ring-cyan-500/20 transition-all">
                    <button onclick="clearSearch()" id="clear-search-btn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white">
                        <i data-lucide="x" class="w-4 h-4"></i>
                    </button>
                </div>

                <!-- Reading Mode Toggles & Font Controls -->
                <div class="flex items-center justify-between w-full md:w-auto gap-3">
                    <div class="flex items-center bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs">
                        <button onclick="setTheme('dark')" id="btn-theme-dark" class="px-3 py-1.5 rounded-lg text-slate-100 bg-slate-800 font-bold transition-all" title="Modo Escuro">🌙 Escuro</button>
                        <button onclick="setTheme('sepia')" id="btn-theme-sepia" class="px-3 py-1.5 rounded-lg text-slate-400 hover:text-amber-300 transition-all" title="Modo Sépia Leitura">📜 Sépia</button>
                    </div>

                    <div class="flex items-center bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs">
                        <button onclick="adjustFontSize(-1)" class="px-2.5 py-1.5 font-extrabold text-slate-300 hover:text-white" title="Diminuir Fonte">A-</button>
                        <span id="font-size-label" class="px-2 text-slate-400 text-xs">100%</span>
                        <button onclick="adjustFontSize(1)" class="px-2.5 py-1.5 font-extrabold text-slate-300 hover:text-white" title="Aumentar Fonte">A+</button>
                    </div>

                    <button onclick="toggleSidebar()" class="lg:hidden p-2.5 bg-slate-800 text-cyan-400 rounded-xl border border-slate-700">
                        <i data-lucide="list" class="w-5 h-5"></i>
                    </button>
                </div>
            </div>

            <!-- Reader Main Workspace (Sidebar + Flipbook Reader) -->
            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">

                <!-- Table of Contents Sidebar -->
                <aside id="toc-sidebar" class="lg:col-span-4 glass-panel rounded-2xl p-4 flex flex-col max-h-[750px]">
                    <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-3">
                        <h3 class="font-heading font-extrabold text-sm text-slate-100 flex items-center gap-2">
                            <i data-lucide="book" class="w-4 h-4 text-cyan-400"></i> Sumário do Livro
                        </h3>
                        <span id="chapter-count-badge" class="text-xs bg-slate-800 text-cyan-400 px-2.5 py-0.5 rounded-full font-mono border border-slate-700">{len(master_chapters)} Seções</span>
                    </div>

                    <!-- Reading Progress Bar -->
                    <div class="mb-3 space-y-1">
                        <div class="flex justify-between text-[11px] text-slate-400">
                            <span>Progresso da Leitura</span>
                            <span id="progress-percent" class="text-cyan-400 font-bold">1%</span>
                        </div>
                        <div class="w-full bg-slate-900 rounded-full h-1.5 overflow-hidden border border-slate-800">
                            <div id="progress-bar-fill" class="bg-gradient-to-r from-cyan-500 to-indigo-500 h-full w-[1%] transition-all duration-300"></div>
                        </div>
                    </div>

                    <!-- Filterable List of Chapters (Pre-rendered for instant visibility) -->
                    <div id="toc-list" class="flex-1 overflow-y-auto space-y-1.5 custom-scrollbar pr-1">
                        {initial_toc_html}
                    </div>
                </aside>

                <!-- Chapter Reader Body -->
                <article class="lg:col-span-8 glass-panel rounded-2xl p-6 sm:p-8 flex flex-col justify-between min-h-[650px]">
                    
                    <!-- Chapter Top Controls -->
                    <div>
                        <div class="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800/80 mb-6">
                            <div class="flex items-center gap-2">
                                <span id="reader-module-badge" class="text-xs bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 px-3 py-1 rounded-full font-bold">
                                    {initial_chapter.get('module', 'Módulo 1')}
                                </span>
                                <span id="reader-page-indicator" class="text-xs text-slate-400 font-mono">
                                    Capítulo 1 de {len(master_chapters)}
                                </span>
                            </div>

                            <!-- Flip Controls Header -->
                            <div class="flex items-center gap-2">
                                <button onclick="prevChapter()" class="px-3 py-1.5 bg-slate-900 hover:bg-slate-800 text-slate-300 hover:text-white rounded-lg text-xs font-bold flex items-center gap-1 border border-slate-800 transition-all">
                                    <i data-lucide="chevron-left" class="w-4 h-4"></i> Anterior
                                </button>
                                <button onclick="nextChapter()" class="px-3 py-1.5 bg-cyan-500 hover:bg-cyan-400 text-slate-950 font-extrabold rounded-lg text-xs flex items-center gap-1 shadow-md shadow-cyan-500/20 transition-all">
                                    Próximo <i data-lucide="chevron-right" class="w-4 h-4"></i>
                                </button>
                            </div>
                        </div>

                        <!-- Rendered Chapter Content (Pre-rendered Chapter 0 for instant load) -->
                        <div id="reader-content-box" class="page-flip-anim space-y-4 max-h-[500px] overflow-y-auto pr-3 custom-scrollbar text-base">
                            {initial_content_html}
                        </div>
                    </div>

                    <!-- Chapter Bottom Page Switcher Footer -->
                    <div class="pt-6 border-t border-slate-800/80 mt-8 flex flex-col sm:flex-row items-center justify-between gap-4">
                        <button onclick="prevChapter()" class="w-full sm:w-auto px-5 py-2.5 bg-slate-900 hover:bg-slate-800 text-slate-200 font-bold rounded-xl text-xs flex items-center justify-center gap-2 border border-slate-800 transition-all">
                            <i data-lucide="arrow-left" class="w-4 h-4"></i> Capítulo Anterior
                        </button>

                        <div class="text-xs text-slate-400 text-center font-mono">
                            Use as setas <kbd class="px-1.5 py-0.5 bg-slate-900 border border-slate-700 rounded text-[10px]">◀</kbd> <kbd class="px-1.5 py-0.5 bg-slate-900 border border-slate-700 rounded text-[10px]">▶</kbd> do teclado para navegar
                        </div>

                        <button onclick="nextChapter()" class="w-full sm:w-auto px-6 py-2.5 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-extrabold rounded-xl text-xs flex items-center justify-center gap-2 shadow-lg shadow-cyan-500/20 transition-all">
                            Próximo Capítulo <i data-lucide="arrow-right" class="w-4 h-4"></i>
                        </button>
                    </div>

                </article>
            </div>
        </section>

        <!-- TAB 2: FULL PDF EMBED VIEWER -->
        <section id="sec-pdf" class="tab-content hidden space-y-5">

            <!-- PDF Book Switcher Banner -->
            <div class="glass-panel p-3.5 rounded-2xl flex flex-col sm:flex-row items-center justify-between gap-3 border border-indigo-500/20 bg-indigo-950/20">
                <div class="flex items-center gap-2 text-xs font-bold text-slate-200">
                    <i data-lucide="file-check" class="w-4 h-4 text-indigo-400"></i>
                    <span>Selecione o Documento PDF para Visualização Completa:</span>
                </div>
                <div class="flex items-center gap-2 w-full sm:w-auto">
                    <button onclick="selectPdf('master')" id="btn-pdf-master" class="flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-indigo-600 text-white shadow-md">
                        <i data-lucide="file-text" class="w-3.5 h-3.5"></i> 1. Manual Master (81 Págs)
                    </button>
                    <button onclick="selectPdf('aquecimento')" id="btn-pdf-aquecimento" class="flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800">
                        <i data-lucide="flame" class="w-3.5 h-3.5 text-amber-400"></i> 2. E-Book Bônus Aquecimento
                    </button>
                </div>
            </div>

            <div class="glass-panel p-6 rounded-2xl flex flex-col sm:flex-row sm:items-center justify-between gap-4">
                <div>
                    <h2 id="pdf-viewer-title" class="font-heading text-xl font-bold text-white flex items-center gap-2">
                        <i data-lucide="file-text" class="w-5 h-5 text-indigo-400"></i> Visualizador do PDF Master Completo
                    </h2>
                    <p id="pdf-viewer-desc" class="text-xs text-slate-400">Versão completa formatada para leitura, impressão e navegação HD em todos os dispositivos.</p>
                </div>
                <div class="flex items-center gap-2 flex-wrap sm:flex-nowrap">
                    <a id="pdf-external-btn" href="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf" target="_blank" class="bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs px-4 py-2.5 rounded-xl shadow transition-all flex items-center gap-2">
                        <i data-lucide="external-link" class="w-4 h-4"></i> Abrir em Nova Aba
                    </a>
                    <a id="pdf-download-btn" href="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf" download class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs px-4 py-2.5 rounded-xl shadow transition-all flex items-center gap-2">
                        <i data-lucide="download" class="w-4 h-4"></i> Baixar PDF Master (2.5 MB)
                    </a>
                </div>
            </div>

            <div class="glass-panel rounded-2xl overflow-hidden h-[800px] border border-slate-800 relative bg-slate-950 flex flex-col">
                <object id="pdf-object-container" data="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf#toolbar=1&navpanes=1&scrollbar=1" type="application/pdf" class="w-full h-full min-h-[750px]">
                    <embed id="pdf-embed-container" src="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf#toolbar=1&navpanes=1" type="application/pdf" class="w-full h-full min-h-[750px]" />
                    <div class="p-8 text-center text-slate-300 space-y-4 my-auto">
                        <div class="inline-flex p-4 rounded-2xl bg-indigo-500/10 text-indigo-400 mb-2">
                            <i data-lucide="file-text" class="w-10 h-10"></i>
                        </div>
                        <h3 class="text-lg font-bold text-white">Visualização de PDF Integrada</h3>
                        <p class="text-xs text-slate-400 max-w-md mx-auto">Para visualizar as páginas diretamente ou salvar em seu dispositivo, clique no botão abaixo:</p>
                        <div class="flex items-center justify-center gap-3 pt-2">
                            <a id="pdf-fallback-btn" href="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf" target="_blank" class="bg-cyan-500 hover:bg-cyan-400 text-slate-950 px-6 py-3 rounded-xl font-bold text-xs transition-all shadow-lg flex items-center gap-2">
                                <i data-lucide="book-open" class="w-4 h-4"></i> Abrir PDF em Nova Aba
                            </a>
                        </div>
                    </div>
                </object>
            </div>
        </section>

        <!-- TAB 3: REELS HOOK GENERATOR -->
        <section id="sec-generator" class="tab-content hidden space-y-6">
            <div class="glass-panel p-6 sm:p-8 rounded-2xl max-w-3xl mx-auto space-y-6">
                <div>
                    <h3 class="font-heading text-xl font-bold text-white flex items-center gap-2">
                        <i data-lucide="sparkles" class="w-5 h-5 text-rose-400"></i> Gerador de Ganchos Virais para o Instagram
                    </h3>
                    <p class="text-xs text-slate-400">Crie scripts de 7 segundos focados em promover seu e-book de R$ 35 com alta retenção.</p>
                </div>

                <div class="flex flex-col sm:flex-row gap-3">
                    <select id="niche-select" class="bg-slate-900 border border-slate-800 text-slate-200 text-xs rounded-xl p-3 flex-1 font-semibold focus:outline-none focus:border-cyan-500">
                        <option value="curiosidade">Curiosidade (Alta Retenção)</option>
                        <option value="controversia">Controvérsia &amp; Quebra de Padrão</option>
                        <option value="fomo">FOMO (Medo de Ficar de Fora)</option>
                        <option value="venda">CTA de Venda Direta R$35</option>
                    </select>

                    <button onclick="generateHook()" class="bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-400 hover:to-pink-500 text-white font-bold text-xs px-6 py-3 rounded-xl transition-all shadow-lg flex items-center justify-center gap-2">
                        <i data-lucide="zap" class="w-4 h-4"></i> Gerar Gancho
                    </button>
                </div>

                <div class="relative">
                    <div id="hook-output" class="bg-slate-900/90 border border-slate-800 p-5 rounded-xl font-mono text-xs text-emerald-400 whitespace-pre-wrap leading-relaxed min-h-[100px] flex items-center">
🚨 'Pare de tentar vender produtos físicos se você não quer se estressar com frete. Este e-book de R$ 35,00 me gerou R$ 4.200 em 7 dias.' (Leia a legenda)
                    </div>
                    <button onclick="copyHookToClipboard()" id="btn-copy-hook" class="absolute right-3 bottom-3 bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white px-3 py-1.5 rounded-lg text-xs font-semibold flex items-center gap-1.5 transition-all border border-slate-700">
                        <i data-lucide="copy" class="w-3.5 h-3.5"></i> Copiar Script
                    </button>
                </div>
            </div>
        </section>

    </main>

    <!-- JavaScript Data & Reader Logic -->
    <script>
        const ALL_BOOKS = {json_str};

        let currentBookKey = 'master_guide';
        let currentChapterIdx = 0;
        let fontScale = 1.0;
        let searchQuery = "";

        function getActiveChapters() {{
            return ALL_BOOKS[currentBookKey] || [];
        }}

        // Safe Lucide Icon Creation Helper
        function safeCreateIcons() {{
            if (typeof lucide !== 'undefined' && lucide && lucide.createIcons) {{
                try {{ lucide.createIcons(); }} catch (e) {{ console.warn(e); }}
            }}
        }}

        function initApp() {{
            safeCreateIcons();
            renderTOC();
            loadChapterByIdx(0);

            // Restore Saved Theme
            try {{
                const savedTheme = localStorage.getItem('reader_theme');
                if (savedTheme) {{
                    setTheme(savedTheme);
                }}
            }} catch (e) {{}}

            // Keyboard navigation
            document.addEventListener('keydown', (e) => {{
                if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;
                if (e.key === 'ArrowRight') nextChapter();
                if (e.key === 'ArrowLeft') prevChapter();
            }});
        }}

        // Guaranteed Initialization on all load states
        if (document.readyState === 'complete' || document.readyState === 'interactive') {{
            setTimeout(initApp, 1);
        }} else {{
            document.addEventListener('DOMContentLoaded', initApp);
            window.addEventListener('load', initApp);
        }}

        // Book Switcher Logic
        function selectBook(bookKey) {{
            if (!ALL_BOOKS[bookKey]) return;
            currentBookKey = bookKey;
            currentChapterIdx = 0;
            searchQuery = "";

            const searchInput = document.getElementById('chapter-search-input');
            if (searchInput) searchInput.value = "";
            const clearBtn = document.getElementById('clear-search-btn');
            if (clearBtn) clearBtn.classList.add('hidden');

            const btnMaster = document.getElementById('btn-book-master');
            const btnAquecimento = document.getElementById('btn-book-aquecimento');

            if (bookKey === 'master_guide') {{
                if (btnMaster) btnMaster.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-gradient-to-r from-cyan-500 to-blue-600 text-slate-950 shadow-md";
                if (btnAquecimento) btnAquecimento.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800";
            }} else {{
                if (btnAquecimento) btnAquecimento.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-gradient-to-r from-amber-500 to-orange-600 text-slate-950 shadow-md";
                if (btnMaster) btnMaster.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800";
            }}

            renderTOC();
            loadChapterByIdx(0);
        }}

        // PDF Switcher Logic
        function selectPdf(pdfKey) {{
            const btnMaster = document.getElementById('btn-pdf-master');
            const btnAquecimento = document.getElementById('btn-pdf-aquecimento');
            const objContainer = document.getElementById('pdf-object-container');
            const embedContainer = document.getElementById('pdf-embed-container');
            const titleEl = document.getElementById('pdf-viewer-title');
            const descEl = document.getElementById('pdf-viewer-desc');
            const externalBtn = document.getElementById('pdf-external-btn');
            const downloadBtn = document.getElementById('pdf-download-btn');
            const fallbackBtn = document.getElementById('pdf-fallback-btn');

            let pdfUrl = './GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf';
            let pdfTitle = 'Visualizador do PDF Master Completo (81 Páginas)';
            let pdfDesc = 'Versão completa formatada para leitura, impressão e navegação HD em todos os dispositivos.';
            let downloadLabel = 'Baixar PDF Master (2.5 MB)';

            if (pdfKey === 'aquecimento') {{
                pdfUrl = './ESTRUTURA_AQUECIMENTO_ORGANICO.pdf';
                pdfTitle = 'Visualizador do E-Book Bônus: Estrutura Aquecimento Orgânico';
                pdfDesc = 'Manual prático de 52 perguntas e respostas para aquecer perfis e evitar shadowban.';
                downloadLabel = 'Baixar PDF Aquecimento (175 KB)';

                if (btnAquecimento) btnAquecimento.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-amber-500 text-slate-950 shadow-md";
                if (btnMaster) btnMaster.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800";
            }} else {{
                if (btnMaster) btnMaster.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-indigo-600 text-white shadow-md";
                if (btnAquecimento) btnAquecimento.className = "flex-1 sm:flex-none px-4 py-2 rounded-xl text-xs font-extrabold transition-all flex items-center justify-center gap-1.5 bg-slate-900 text-slate-400 hover:text-slate-200 border border-slate-800";
            }}

            if (objContainer) objContainer.data = pdfUrl + '#toolbar=1&navpanes=1&scrollbar=1';
            if (embedContainer) embedContainer.src = pdfUrl + '#toolbar=1&navpanes=1';
            if (titleEl) titleEl.innerHTML = `<i data-lucide="file-text" class="w-5 h-5 text-indigo-400"></i> ${{pdfTitle}}`;
            if (descEl) descEl.innerText = pdfDesc;
            if (externalBtn) externalBtn.href = pdfUrl;
            if (downloadBtn) {{
                downloadBtn.href = pdfUrl;
                downloadBtn.innerHTML = `<i data-lucide="download" class="w-4 h-4"></i> ${{downloadLabel}}`;
            }}
            if (fallbackBtn) fallbackBtn.href = pdfUrl;

            safeCreateIcons();
        }}

        function renderTOC(filteredList = getActiveChapters()) {{
            const container = document.getElementById('toc-list');
            const badge = document.getElementById('chapter-count-badge');
            const activeList = getActiveChapters();

            if (badge) badge.innerText = `${{filteredList.length}} Seções`;
            if (!container) return;

            if (filteredList.length === 0) {{
                container.innerHTML = `<div class="p-4 text-center text-xs text-slate-500">Nenhum capítulo encontrado para "${{searchQuery}}"</div>`;
                return;
            }}

            container.innerHTML = filteredList.map((ch, idx) => {{
                const originalIdx = activeList.findIndex(c => c.id === ch.id);
                const isActive = originalIdx === currentChapterIdx;

                return `
                    <button onclick="loadChapterByIdx(${{originalIdx}})" 
                            class="w-full text-left p-2.5 rounded-xl text-xs font-semibold transition-all flex items-center justify-between gap-2 ${{
                                isActive 
                                ? 'bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 shadow-sm' 
                                : 'text-slate-400 hover:bg-slate-900 hover:text-slate-200 border border-transparent'
                            }}">
                        <div class="truncate">
                            <span class="text-[10px] text-slate-500 block font-mono font-normal truncate">${{ch.module}}</span>
                            <span class="truncate font-bold">${{highlightMatch(ch.title, searchQuery)}}</span>
                        </div>
                        <i data-lucide="chevron-right" class="w-3.5 h-3.5 shrink-0 opacity-50"></i>
                    </button>
                `;
            }}).join('');

            safeCreateIcons();
        }}

        function loadChapterByIdx(idx) {{
            const activeList = getActiveChapters();
            if (idx < 0 || idx >= activeList.length) return;
            currentChapterIdx = idx;
            const ch = activeList[idx];

            const moduleBadge = document.getElementById('reader-module-badge');
            if (moduleBadge) moduleBadge.innerText = ch.module;

            const pageIndicator = document.getElementById('reader-page-indicator');
            if (pageIndicator) pageIndicator.innerText = `Capítulo ${{idx + 1}} de ${{activeList.length}}`;

            const box = document.getElementById('reader-content-box');
            if (box) {{
                box.classList.remove('page-flip-anim');
                void box.offsetWidth; // Trigger reflow for animation
                box.classList.add('page-flip-anim');

                box.style.fontSize = `${{fontScale * 1.0}}rem`;
                box.innerHTML = `
                    <h2 class="font-heading font-extrabold text-xl sm:text-2xl text-white pb-3 border-b border-slate-800">${{ch.title}}</h2>
                    <div class="prose prose-invert max-w-none text-slate-300 text-sm sm:text-base leading-relaxed space-y-4">
                        ${{ch.html}}
                    </div>
                `;

                box.scrollTop = 0;
            }}

            // Update Progress Bar
            const percent = Math.round(((idx + 1) / activeList.length) * 100);
            const progressPercent = document.getElementById('progress-percent');
            if (progressPercent) progressPercent.innerText = `${{percent}}%`;
            const progressBarFill = document.getElementById('progress-bar-fill');
            if (progressBarFill) progressBarFill.style.width = `${{percent}}%`;

            // Re-render TOC to highlight active item
            renderTOC(filterChapters(searchQuery));
            safeCreateIcons();
        }}

        function nextChapter() {{
            const activeList = getActiveChapters();
            if (currentChapterIdx < activeList.length - 1) {{
                loadChapterByIdx(currentChapterIdx + 1);
            }}
        }}

        function prevChapter() {{
            if (currentChapterIdx > 0) {{
                loadChapterByIdx(currentChapterIdx - 1);
            }}
        }}

        // Live Search Handling
        function handleSearch(query) {{
            searchQuery = query.trim();
            const clearBtn = document.getElementById('clear-search-btn');
            if (clearBtn) {{
                if (searchQuery.length > 0) {{
                    clearBtn.classList.remove('hidden');
                }} else {{
                    clearBtn.classList.add('hidden');
                }}
            }}

            const filtered = filterChapters(searchQuery);
            renderTOC(filtered);

            if (filtered.length > 0 && searchQuery.length > 1) {{
                const activeList = getActiveChapters();
                const firstMatchIdx = activeList.findIndex(c => c.id === filtered[0].id);
                if (firstMatchIdx !== -1) loadChapterByIdx(firstMatchIdx);
            }}
        }}

        function clearSearch() {{
            const searchInput = document.getElementById('chapter-search-input');
            if (searchInput) searchInput.value = '';
            handleSearch('');
        }}

        function filterChapters(query) {{
            const activeList = getActiveChapters();
            if (!query) return activeList;
            const q = query.toLowerCase();
            return activeList.filter(ch => 
                ch.title.toLowerCase().includes(q) || 
                ch.module.toLowerCase().includes(q) || 
                ch.content.toLowerCase().includes(q)
            );
        }}

        function highlightMatch(text, query) {{
            if (!query) return text;
            const reg = new RegExp(`(${{query.replace(/[.*+?^${{}}()|[\\]\\]/g, '\\\\$&')}})`, 'gi');
            return text.replace(reg, '<mark class="search-highlight">$1</mark>');
        }}

        function adjustFontSize(delta) {{
            if (delta > 0 && fontScale < 1.4) fontScale += 0.1;
            if (delta < 0 && fontScale > 0.8) fontScale -= 0.1;
            const label = document.getElementById('font-size-label');
            if (label) label.innerText = `${{Math.round(fontScale * 100)}}%`;
            loadChapterByIdx(currentChapterIdx);
        }}

        function setTheme(mode) {{
            const body = document.getElementById('app-body');
            const btnDark = document.getElementById('btn-theme-dark');
            const btnSepia = document.getElementById('btn-theme-sepia');

            if (!body) return;

            if (mode === 'sepia') {{
                body.classList.add('theme-sepia');
                if (btnSepia) {{
                    btnSepia.className = "px-3 py-1.5 rounded-lg text-amber-900 bg-amber-200 font-bold transition-all";
                }}
                if (btnDark) {{
                    btnDark.className = "px-3 py-1.5 rounded-lg text-slate-400 hover:text-white transition-all";
                }}
            }} else {{
                body.classList.remove('theme-sepia');
                if (btnDark) {{
                    btnDark.className = "px-3 py-1.5 rounded-lg text-slate-100 bg-slate-800 font-bold transition-all";
                }}
                if (btnSepia) {{
                    btnSepia.className = "px-3 py-1.5 rounded-lg text-slate-400 hover:text-amber-300 transition-all";
                }}
            }}
            try {{ localStorage.setItem('reader_theme', mode); }} catch (e) {{}}
        }}

        function switchTab(tabId) {{
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(el => {{
                el.classList.remove('bg-slate-800', 'text-slate-100');
                el.classList.add('text-slate-400');
            }});

            const targetSec = document.getElementById('sec-' + tabId);
            if (targetSec) targetSec.classList.remove('hidden');

            const activeBtn = document.getElementById('tab-' + tabId);
            if (activeBtn) {{
                activeBtn.classList.add('bg-slate-800', 'text-slate-100');
                activeBtn.classList.remove('text-slate-400');
            }}
            safeCreateIcons();
        }}

        function toggleSidebar() {{
            const sidebar = document.getElementById('toc-sidebar');
            if (sidebar) sidebar.classList.toggle('hidden');
        }}

        const hooks = {{
            curiosidade: [
                "🚨 'Pare de tentar vender produtos físicos se você não quer se estressar com frete. Este e-book de R$ 35,00 me gerou R$ 4.200 em 7 dias.' (Leia a legenda)",
                "💡 'A estrutura exata de 3 linhas na bio do Instagram que converte visitantes em clientes fiéis. Salve esse vídeo!'",
                "👀 'O segredo que os grandes criadores não te contam sobre como transformar 100 seguidores em R$ 1.000 no PIX.'"
            ],
            controversia: [
                "⚠️ 'Este erro simples ao postar Reels está destruindo o seu alcance no Instagram...' (Comente 'GUIA' para receber o PDF completo por R$ 35)",
                "🛑 'Cursos de R$ 2.000 são uma enganação. Tudo o que você precisa para faturar com produtos digitais cabe neste PDF de R$ 35.'",
                "❌ 'Se você ainda posta fotos normais no feed sem um produto digital na bio, você está jogando dinheiro no lixo.'"
            ],
            fomo: [
                "🔥 'Se você tem 1 hora por dia livre e acesso à internet, esta é a forma mais barata de construir seu produto digital.'",
                "⌛ 'O mercado de infoprodutos de R$ 35 está explodindo e quem começar esta semana vai dominar o nicho.'",
                "⚡ 'Baixe o Guia do Criador Digital antes que o valor do pacote completo volte para R$ 97!'"
            ],
            venda: [
                "💰 'Montei um Mega Pack com 31 modelos de produtos digitais + Guia completo por apenas R$ 35,00. Clique no link da bio!'",
                "📲 'Comente MEGAPACK para receber o link com desconto exclusivo do e-book + bônus de aquecimento orgânico por R$ 35.'",
                "🚀 'Transforme seu perfil do Instagram em uma máquina de vendas automática por apenas R$ 35,00 à vista no PIX.'"
            ]
        }};

        function generateHook() {{
            const select = document.getElementById('niche-select');
            const cat = select ? select.value : 'curiosidade';
            const catHooks = hooks[cat] || hooks.curiosidade;
            const randomHook = catHooks[Math.floor(Math.random() * catHooks.length)];
            const output = document.getElementById('hook-output');
            if (output) output.innerText = randomHook;
        }}

        function copyHookToClipboard() {{
            const output = document.getElementById('hook-output');
            const btn = document.getElementById('btn-copy-hook');
            if (!output) return;
            const text = output.innerText;
            navigator.clipboard.writeText(text).then(() => {{
                if (btn) {{
                    btn.innerHTML = `<i data-lucide="check" class="w-3.5 h-3.5 text-emerald-400"></i> Copiado!`;
                    setTimeout(() => {{
                        btn.innerHTML = `<i data-lucide="copy" class="w-3.5 h-3.5"></i> Copiar Script`;
                        safeCreateIcons();
                    }}, 2000);
                }}
            }}).catch(err => {{
                console.error('Erro ao copiar text: ', err);
            }});
        }}
    </script>
</body>
</html>
"""

index_out_path = os.path.join(dir_path, "index.html")
with open(index_out_path, "w", encoding="utf-8") as f:
    f.write(index_html_content)

print("SUCCESS: Updated build_interactive_index.py with SSR pre-rendered content and failproof initApp!")
