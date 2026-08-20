import os
import json
import subprocess

dir_path = "/home/zeronight/Downloads/a5f8ef87-6cf1-4184-947b-a330eb96429a_ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3/ExportBlock-7fcd78ed-6da1-4722-8116-335129f8f7d3-Part-1"
json_path = os.path.join(dir_path, "ebook_chapters.json")

with open(json_path, "r", encoding="utf-8") as f:
    chapters = json.load(f)

json_str = json.dumps(chapters, ensure_ascii=False)

html_template = """<!DOCTYPE html>
<html lang="pt-BR" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guia Definitivo do Criador Digital - Leitor Interativo &amp; E-Book Completo</title>

    <!-- Tailwind CSS -->
    <script src="https://cdn.tailwindcss.com"></script>
    
    <!-- Google Fonts & Lucide Icons -->
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Outfit:wght@600;700;800&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>

    <script>
        tailwind.config = {
            darkMode: 'class',
            theme: {
                extend: {
                    fontFamily: {
                        sans: ['Plus Jakarta Sans', 'sans-serif'],
                        heading: ['Outfit', 'sans-serif'],
                    },
                    colors: {
                        brand: {
                            50: '#f0f9ff',
                            400: '#38bdf8',
                            500: '#0ea5e9',
                            600: '#0284c7',
                            900: '#0c4a6e',
                            950: '#082f49',
                        }
                    }
                }
            }
        }
    </script>
    <style>
        body { font-family: 'Plus Jakarta Sans', sans-serif; }
        .font-heading { font-family: 'Outfit', sans-serif; }

        .glass-panel {
            background: rgba(15, 23, 42, 0.85);
            backdrop-filter: blur(20px);
            border: 1px solid rgba(255, 255, 255, 0.08);
        }
        
        .custom-scrollbar::-webkit-scrollbar {
            width: 6px;
        }
        .custom-scrollbar::-webkit-scrollbar-track {
            background: #090d16;
        }
        .custom-scrollbar::-webkit-scrollbar-thumb {
            background: #1e293b;
            border-radius: 6px;
        }

        /* Sepia Theme Mode */
        .theme-sepia {
            background-color: #fbf0d9 !important;
            color: #3b2f2f !important;
        }
        .theme-sepia .glass-panel {
            background: rgba(244, 230, 206, 0.9) !important;
            border-color: rgba(180, 140, 90, 0.2) !important;
            color: #2b1f1f !important;
        }
        .theme-sepia p, .theme-sepia li {
            color: #4a3b3b !important;
        }
        .theme-sepia h1, .theme-sepia h2, .theme-sepia h3, .theme-sepia strong {
            color: #1a0f0f !important;
        }

        /* Highlight Search Terms */
        mark.search-highlight {
            background-color: #f59e0b;
            color: #000;
            padding: 2px 4px;
            border-radius: 4px;
            font-weight: 700;
        }

        /* Smooth Page Transition */
        .page-flip-anim {
            animation: fadeIn 0.25s cubic-bezier(0.16, 1, 0.3, 1);
        }

        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(6px); }
            to { opacity: 1; transform: translateY(0); }
        }
    </style>
</head>
<body id="app-body" class="bg-slate-950 text-slate-100 min-h-screen flex flex-col antialiased selection:bg-cyan-500 selection:text-white custom-scrollbar">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-50 glass-panel border-b border-slate-800 px-4 md:px-8 py-3.5 flex items-center justify-between">
        <div class="flex items-center gap-3">
            <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-cyan-500 to-indigo-600 flex items-center justify-center font-black text-white shadow-lg shadow-cyan-500/20 text-lg">
                📖
            </div>
            <div>
                <h1 class="font-heading font-extrabold text-slate-100 text-base leading-tight flex items-center gap-2">
                    Guia do Criador Digital <span class="bg-cyan-500/10 text-cyan-400 text-xs px-2.5 py-0.5 rounded-full border border-cyan-500/20 font-semibold">Leitor Interativo</span>
                </h1>
                <p class="text-xs text-slate-400">Manual Master Completo • Busca Instantânea &amp; Troca de Páginas</p>
            </div>
        </div>

        <!-- Center Tabs -->
        <nav class="hidden lg:flex items-center gap-1 bg-slate-900/90 p-1 rounded-xl border border-slate-800 text-xs font-semibold">
            <button onclick="switchTab('reader')" id="tab-reader" class="tab-btn px-4 py-2 rounded-lg text-slate-100 bg-slate-800 shadow-sm flex items-center gap-2 transition-all">
                <i data-lucide="book-open" class="w-4 h-4 text-cyan-400"></i> Leitor de E-Book
            </button>
            <button onclick="switchTab('pdf')" id="tab-pdf" class="tab-btn px-4 py-2 rounded-lg text-slate-400 hover:text-slate-200 flex items-center gap-2 transition-all">
                <i data-lucide="file-text" class="w-4 h-4 text-indigo-400"></i> Visualizador PDF
            </button>

            <button onclick="switchTab('dashboard')" id="tab-dashboard" class="tab-btn px-4 py-2 rounded-lg text-slate-400 hover:text-slate-200 flex items-center gap-2 transition-all">
                <i data-lucide="layout-dashboard" class="w-4 h-4 text-emerald-400"></i> Dashboard R$35
            </button>
            <button onclick="switchTab('generator')" id="tab-generator" class="tab-btn px-4 py-2 rounded-lg text-slate-400 hover:text-slate-200 flex items-center gap-2 transition-all">
                <i data-lucide="sparkles" class="w-4 h-4 text-rose-400"></i> Gerador de Ganchos
            </button>
        </nav>

        <!-- Right Quick Actions -->
        <div class="flex items-center gap-2">
            <a href="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf" download class="flex items-center gap-1.5 bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-400 hover:to-blue-500 text-slate-950 font-extrabold text-xs px-3.5 py-2.5 rounded-xl transition-all shadow-md">
                <i data-lucide="download" class="w-4 h-4"></i> <span class="hidden sm:inline">Baixar PDF</span>
            </a>
            <a href="./LANDING_PAGE_OFERTA_35.html" target="_blank" class="hidden sm:flex items-center gap-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-semibold px-3 py-2.5 rounded-xl border border-slate-700 transition-all">
                <i data-lucide="external-link" class="w-3.5 h-3.5"></i> Landing Page
            </a>
        </div>
    </header>

    <!-- Main Content Area -->
    <main class="flex-1 max-w-7xl w-full mx-auto p-4 sm:p-6 space-y-6">

        <!-- TAB 1: E-BOOK INTERACTIVE READER (DEFAULT ACTIVE VIEW) -->
        <section id="sec-reader" class="tab-content space-y-5">

            <!-- Search Bar & Controls Banner -->
            <div class="glass-panel p-4 sm:p-5 rounded-2xl flex flex-col md:flex-row items-center justify-between gap-4">
                
                <!-- Live Search Box -->
                <div class="relative w-full md:w-1/2">
                    <i data-lucide="search" class="w-5 h-5 text-slate-400 absolute left-3.5 top-1/2 -translate-y-1/2"></i>
                    <input type="text" id="chapter-search-input" onkeyup="handleSearch(this.value)" placeholder="🔍 Pesquisar em todos os capítulos e tópicos do livro..." 
                           class="w-full bg-slate-900 border border-slate-700/80 rounded-xl pl-11 pr-10 py-3 text-sm text-slate-100 placeholder-slate-400 focus:outline-none focus:border-cyan-500 focus:ring-2 focus:ring-cyan-500/20 transition-all">
                    <button onclick="clearSearch()" id="clear-search-btn" class="hidden absolute right-3 top-1/2 -translate-y-1/2 text-slate-400 hover:text-white">
                        <i data-lucide="x" class="w-4 h-4"></i>
                    </button>
                </div>

                <!-- Reading Mode Toggles & Font Controls -->
                <div class="flex items-center justify-between w-full md:w-auto gap-3">
                    <div class="flex items-center bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs">
                        <button onclick="setTheme('dark')" class="px-3 py-1.5 rounded-lg text-slate-200 hover:bg-slate-800 transition-all" title="Modo Escuro">🌙 Escuro</button>
                        <button onclick="setTheme('sepia')" class="px-3 py-1.5 rounded-lg text-amber-300 hover:bg-slate-800 transition-all" title="Modo Sépia Leitura">📜 Sépia</button>
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

                <!-- Table of Contents Sidebar (4 cols on desktop) -->
                <aside id="toc-sidebar" class="lg:col-span-4 glass-panel rounded-2xl p-4 flex flex-col max-h-[750px]">
                    <div class="flex items-center justify-between pb-3 border-b border-slate-800 mb-3">
                        <h3 class="font-heading font-extrabold text-sm text-slate-100 flex items-center gap-2">
                            <i data-lucide="book" class="w-4 h-4 text-cyan-400"></i> Sumário do Livro
                        </h3>
                        <span id="chapter-count-badge" class="text-xs bg-slate-800 text-cyan-400 px-2.5 py-0.5 rounded-full font-mono border border-slate-700">36 Capítulos</span>
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

                    <!-- Filterable List of Chapters -->
                    <div id="toc-list" class="flex-1 overflow-y-auto space-y-1.5 custom-scrollbar pr-1">
                        <!-- Populated by JavaScript -->
                    </div>
                </aside>

                <!-- Chapter Reader Body (8 cols on desktop) -->
                <article class="lg:col-span-8 glass-panel rounded-2xl p-6 sm:p-8 flex flex-col justify-between min-h-[650px]">
                    
                    <!-- Chapter Top Controls (Module Badge & Page Switcher) -->
                    <div>
                        <div class="flex flex-wrap items-center justify-between gap-3 pb-4 border-b border-slate-800/80 mb-6">
                            <div class="flex items-center gap-2">
                                <span id="reader-module-badge" class="text-xs bg-indigo-500/10 text-indigo-400 border border-indigo-500/20 px-3 py-1 rounded-full font-bold">
                                    Módulo 1
                                </span>
                                <span id="reader-page-indicator" class="text-xs text-slate-400 font-mono">
                                    Capítulo 1 de 36
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

                        <!-- Rendered Chapter Content -->
                        <div id="reader-content-box" class="page-flip-anim space-y-4 max-h-[500px] overflow-y-auto pr-3 custom-scrollbar text-base">
                            <!-- Populated dynamically -->
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
            <div class="glass-panel p-6 rounded-2xl flex items-center justify-between gap-4">
                <div>
                    <h2 class="font-heading text-xl font-bold text-white flex items-center gap-2">
                        <i data-lucide="file-text" class="w-5 h-5 text-indigo-400"></i> Visualizador do PDF Master (72 Páginas)
                    </h2>
                    <p class="text-xs text-slate-400">Versão formatada para leitura, impressão e download em alta definição.</p>
                </div>
                <a href="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf" download class="bg-emerald-500 hover:bg-emerald-400 text-slate-950 font-bold text-xs px-5 py-2.5 rounded-xl shadow transition-all flex items-center gap-2">
                    <i data-lucide="download" class="w-4 h-4"></i> Baixar Arquivo PDF (2.0 MB)
                </a>
            </div>

            <div class="glass-panel rounded-2xl overflow-hidden h-[750px] border border-slate-800">
                <iframe src="./GUIA_MEGAPACK_CRIADOR_DIGITAL_COMPLETO.pdf" class="w-full h-full border-0"></iframe>
            </div>
        </section>

        <!-- TAB 3: DASHBOARD METRICS -->
        <section id="sec-dashboard" class="tab-content hidden space-y-6">
            <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
                <div class="glass-panel p-5 rounded-2xl">
                    <div class="flex items-center justify-between text-slate-400 mb-2">
                        <span class="text-xs font-semibold uppercase">Faturamento R$35</span>
                        <div class="p-2 rounded-xl bg-emerald-500/10 text-emerald-400"><i data-lucide="dollar-sign" class="w-5 h-5"></i></div>
                    </div>
                    <div class="text-3xl font-extrabold text-white">R$ 4.235,00</div>
                    <div class="mt-2 text-xs text-emerald-400 font-semibold">+24.8% este mês</div>
                </div>

                <div class="glass-panel p-5 rounded-2xl">
                    <div class="flex items-center justify-between text-slate-400 mb-2">
                        <span class="text-xs font-semibold uppercase">Vendas Aprovadas</span>
                        <div class="p-2 rounded-xl bg-cyan-500/10 text-cyan-400"><i data-lucide="shopping-cart" class="w-5 h-5"></i></div>
                    </div>
                    <div class="text-3xl font-extrabold text-white">121 E-books</div>
                    <div class="mt-2 text-xs text-cyan-400 font-semibold">Conversão: 5.2%</div>
                </div>

                <div class="glass-panel p-5 rounded-2xl">
                    <div class="flex items-center justify-between text-slate-400 mb-2">
                        <span class="text-xs font-semibold uppercase">Visitas no Funil</span>
                        <div class="p-2 rounded-xl bg-indigo-500/10 text-indigo-400"><i data-lucide="users" class="w-5 h-5"></i></div>
                    </div>
                    <div class="text-3xl font-extrabold text-white">2.327 Clientes</div>
                    <div class="mt-2 text-xs text-indigo-400 font-semibold">Orgânico + Instagram</div>
                </div>

                <div class="glass-panel p-5 rounded-2xl">
                    <div class="flex items-center justify-between text-slate-400 mb-2">
                        <span class="text-xs font-semibold uppercase">ROI Estimado</span>
                        <div class="p-2 rounded-xl bg-rose-500/10 text-rose-400"><i data-lucide="pie-chart" class="w-5 h-5"></i></div>
                    </div>
                    <div class="text-3xl font-extrabold text-white">680% ROI</div>
                    <div class="mt-2 text-xs text-rose-400 font-semibold">Zero custo de estoque</div>
                </div>
            </div>
        </section>

        <!-- TAB 4: REELS HOOK GENERATOR -->
        <section id="sec-generator" class="tab-content hidden space-y-6">
            <div class="glass-panel p-6 sm:p-8 rounded-2xl max-w-3xl mx-auto space-y-6">
                <div>
                    <h3 class="font-heading text-xl font-bold text-white flex items-center gap-2">
                        <i data-lucide="sparkles" class="w-5 h-5 text-rose-400"></i> Gerador de Ganchos Virais para o Instagram
                    </h3>
                    <p class="text-xs text-slate-400">Crie scripts de 7 segundos focados em promover seu e-book de R$ 35 com alta retenção.</p>
                </div>

                <div class="flex gap-3">
                    <select id="niche-select" class="bg-slate-900 border border-slate-800 text-slate-200 text-xs rounded-xl p-3 flex-1 font-semibold focus:outline-none focus:border-cyan-500">
                        <option>Curiosidade (Alta Retenção)</option>
                        <option>Controvérsia Negativa</option>
                        <option>FOMO (Medo de Perder)</option>
                        <option>CTA de Venda Direta R$35</option>
                    </select>

                    <button onclick="generateHook()" class="bg-gradient-to-r from-rose-500 to-pink-600 hover:from-rose-400 hover:to-pink-500 text-white font-bold text-xs px-6 py-3 rounded-xl transition-all shadow-lg flex items-center gap-2">
                        <i data-lucide="zap" class="w-4 h-4"></i> Gerar Gancho
                    </button>
                </div>

                <div id="hook-output" class="bg-slate-900/90 border border-slate-800 p-5 rounded-xl font-mono text-xs text-emerald-400 whitespace-pre-wrap leading-relaxed">
Clique em "Gerar Gancho" para obter um script otimizado para o seu perfil!
                </div>
            </div>
        </section>

    </main>

    <!-- JavaScript Data & Reader Logic -->
    <script>
        const EBOOK_CHAPTERS = __EBOOK_CHAPTERS_DATA__;

        let currentChapterIdx = 0;
        let fontScale = 1.0;
        let searchQuery = "";

        // Initialize Application
        document.addEventListener('DOMContentLoaded', () => {
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
            renderTOC();
            loadChapterByIdx(0);

            // Keyboard navigation
            document.addEventListener('keydown', (e) => {
                if (e.target.tagName === 'INPUT') return;
                if (e.key === 'ArrowRight') nextChapter();
                if (e.key === 'ArrowLeft') prevChapter();
            });
        });

        function renderTOC(filteredList = EBOOK_CHAPTERS) {
            const container = document.getElementById('toc-list');
            document.getElementById('chapter-count-badge').innerText = filteredList.length + ' Capítulos';

            if (filteredList.length === 0) {
                container.innerHTML = '<div class="p-4 text-center text-xs text-slate-500">Nenhum capítulo encontrado para "' + searchQuery + '"</div>';
                return;
            }

            container.innerHTML = filteredList.map((ch) => {
                const originalIdx = EBOOK_CHAPTERS.findIndex(c => c.id === ch.id);
                const isActive = originalIdx === currentChapterIdx;

                const activeClass = isActive 
                    ? 'bg-cyan-500/15 text-cyan-300 border border-cyan-500/30 shadow-sm' 
                    : 'text-slate-400 hover:bg-slate-900 hover:text-slate-200 border border-transparent';

                return '<button onclick="loadChapterByIdx(' + originalIdx + ')" class="w-full text-left p-2.5 rounded-xl text-xs font-semibold transition-all flex items-center justify-between gap-2 ' + activeClass + '">' +
                        '<div class="truncate">' +
                            '<span class="text-[10px] text-slate-500 block font-mono font-normal truncate">' + ch.module + '</span>' +
                            '<span class="truncate font-bold">' + highlightMatch(ch.title, searchQuery) + '</span>' +
                        '</div>' +
                        '<i data-lucide="chevron-right" class="w-3.5 h-3.5 shrink-0 opacity-50"></i>' +
                    '</button>';
            }).join('');

            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        }

        function loadChapterByIdx(idx) {
            if (idx < 0 || idx >= EBOOK_CHAPTERS.length) return;
            currentChapterIdx = idx;
            const ch = EBOOK_CHAPTERS[idx];

            document.getElementById('reader-module-badge').innerText = ch.module;
            document.getElementById('reader-page-indicator').innerText = 'Capítulo ' + (idx + 1) + ' de ' + EBOOK_CHAPTERS.length;

            const box = document.getElementById('reader-content-box');
            box.classList.remove('page-flip-anim');
            void box.offsetWidth;
            box.classList.add('page-flip-anim');

            box.style.fontSize = (fontScale * 1.0) + 'rem';
            box.innerHTML = '<h2 class="font-heading font-extrabold text-xl sm:text-2xl text-white pb-3 border-b border-slate-800">' + ch.title + '</h2>' +
                '<div class="prose prose-invert max-w-none text-slate-300 text-sm sm:text-base leading-relaxed space-y-4">' +
                    ch.html +
                '</div>';

            box.scrollTop = 0;

            const percent = Math.round(((idx + 1) / EBOOK_CHAPTERS.length) * 100);
            document.getElementById('progress-percent').innerText = percent + '%';
            document.getElementById('progress-bar-fill').style.width = percent + '%';

            renderTOC(filterChapters(searchQuery));
            if (typeof lucide !== 'undefined') {
                lucide.createIcons();
            }
        }

        function nextChapter() {
            if (currentChapterIdx < EBOOK_CHAPTERS.length - 1) {
                loadChapterByIdx(currentChapterIdx + 1);
            }
        }

        function prevChapter() {
            if (currentChapterIdx > 0) {
                loadChapterByIdx(currentChapterIdx - 1);
            }
        }

        function handleSearch(query) {
            searchQuery = query.trim();
            const clearBtn = document.getElementById('clear-search-btn');
            if (searchQuery.length > 0) {
                clearBtn.classList.remove('hidden');
            } else {
                clearBtn.classList.add('hidden');
            }

            const filtered = filterChapters(searchQuery);
            renderTOC(filtered);

            if (filtered.length > 0 && searchQuery.length > 1) {
                const firstMatchIdx = EBOOK_CHAPTERS.findIndex(c => c.id === filtered[0].id);
                loadChapterByIdx(firstMatchIdx);
            }
        }

        function clearSearch() {
            document.getElementById('chapter-search-input').value = '';
            handleSearch('');
        }

        function filterChapters(query) {
            if (!query) return EBOOK_CHAPTERS;
            const q = query.toLowerCase();
            return EBOOK_CHAPTERS.filter(ch => 
                ch.title.toLowerCase().includes(q) || 
                ch.module.toLowerCase().includes(q) || 
                ch.content.toLowerCase().includes(q)
            );
        }

        function highlightMatch(text, query) {
            if (!query) return text;
            const escaped = query.replace(/[.*+?^${}()|[\]\\]/g, '\\$&');
            const reg = new RegExp('(' + escaped + ')', 'gi');
            return text.replace(reg, '<mark class="search-highlight">$1</mark>');
        }

        function adjustFontSize(delta) {
            if (delta > 0 && fontScale < 1.4) fontScale += 0.1;
            if (delta < 0 && fontScale > 0.8) fontScale -= 0.1;
            document.getElementById('font-size-label').innerText = Math.round(fontScale * 100) + '%';
            loadChapterByIdx(currentChapterIdx);
        }

        function setTheme(mode) {
            const body = document.getElementById('app-body');
            if (mode === 'sepia') {
                body.classList.add('theme-sepia');
            } else {
                body.classList.remove('theme-sepia');
            }
        }

        function switchTab(tabId) {
            document.querySelectorAll('.tab-content').forEach(el => el.classList.add('hidden'));
            document.querySelectorAll('.tab-btn').forEach(el => {
                el.classList.remove('bg-slate-800', 'text-slate-100');
                el.classList.add('text-slate-400');
            });

            document.getElementById('sec-' + tabId).classList.remove('hidden');
            const activeBtn = document.getElementById('tab-' + tabId);
            if (activeBtn) {
                activeBtn.classList.add('bg-slate-800', 'text-slate-100');
                activeBtn.classList.remove('text-slate-400');
            }
        }

        function toggleSidebar() {
            const sidebar = document.getElementById('toc-sidebar');
            sidebar.classList.toggle('hidden');
        }

        const hooks = [
            "🚨 'Pare de tentar vender produtos físicos se você não quer se estressar com frete. Este e-book de R$ 35,00 me gerou R$ 4.200 em 7 dias.' (Leia a legenda)",
            "⚠️ 'Este erro simples ao postar Reels está destruindo o seu alcance no Instagram...' (Comente 'GUIA' para receber o PDF completo por R$ 35)",
            "💡 'A estrutura exata de 3 linhas na bio do Instagram que converte visitantes em clientes fiéis. Salve esse vídeo!'",
            "🔥 'Se você tem 1 hora por dia livre e acesso à internet, esta é a forma mais barata de construir seu produto digital.'"
        ];

        function generateHook() {
            const randomHook = hooks[Math.floor(Math.random() * hooks.length)];
            document.getElementById('hook-output').innerText = randomHook;
        }
    </script>
</body>
</html>
"""

# Replace placeholder with json string cleanly
final_html = html_template.replace("__EBOOK_CHAPTERS_DATA__", json_str)

index_out_path = os.path.join(dir_path, "index.html")
with open(index_out_path, "w", encoding="utf-8") as f:
    f.write(final_html)

print("Updated index.html safely!")
