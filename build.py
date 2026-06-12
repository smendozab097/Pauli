import os
import re

with open("minimalista.html", "r", encoding="utf-8") as f:
    original_html = f.read()

# We will construct a minimal_optimized.html that looks EXACTLY like minimalista.html 
# but uses tailwind classes inline where possible.
# Actually, the user wants minimal_optimized.html to look like minimalista.html but using tailwind.
# The previous minimal_optimized.html was written by rewrite_tailwind.py and it was incomplete or inaccurate.
# To ensure EXACT visual parity and full tailwind conversion, let's write a python script that replaces the main CSS classes with their Tailwind equivalents.

# I will provide the fully converted HTML string.
html_content = r"""<!DOCTYPE html>
<html lang="es" class="scroll-smooth">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Salesforce Squad</title>
    <!-- Google Fonts - Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            fontFamily: { sans: ['Inter', 'sans-serif'] },
            colors: {
              experian: {
                'dark-blue': '#1D4F91',
                'light-blue': '#426DA9',
                'purple': '#77127B',
                'raspberry': '#C1188B',
                'magenta': '#E80070',
                'white': '#FFFFFF',
              },
              warm: {
                'casual': '#FAF7F2',
                'border': '#EFEAE2',
                'dark': '#2F2A26',
                'medium': '#6E6760',
              }
            },
            animation: {
              'highlight-pulse': 'highlightPulse 2.5s ease-out forwards',
            },
            keyframes: {
              highlightPulse: {
                '0%': { boxShadow: '0 0 0 0 rgba(119, 18, 123, 0.6)', borderColor: '#77127B', transform: 'scale(1.02)' },
                '50%': { boxShadow: '0 0 0 15px rgba(119, 18, 123, 0)', borderColor: '#77127B', transform: 'scale(1.02)' },
                '100%': { boxShadow: '0 0 0 0 rgba(119, 18, 123, 0)', transform: 'scale(1)' }
              }
            }
          }
        }
      }
    </script>
    <style type="text/tailwindcss">
      @layer utilities {
        .highlight-focus {
          @apply relative z-10;
          animation: highlight-pulse 2.5s ease-out forwards;
        }
        body.is-pulsing .card:not(.highlight-focus) {
          pointer-events: none;
        }
        summary::-webkit-details-marker {
          display: none;
        }
        .team-member[open] .details-arrow {
          transform: rotate(180deg);
          color: var(--accent-color);
        }
        .team-member[open] {
          border-color: var(--accent-color);
          background-color: #FFFFFF;
        }
        .hero-panel::before {
          content: '';
          @apply absolute top-0 left-0 right-0 h-[5px];
          background: linear-gradient(90deg, #1D4F91 0%, #77127B 50%, #E80070 100%);
        }
        /* Group hover variants with arbitrary values for dynamic accent colors are tricky, so we keep CSS vars for accent-color where needed */
        .card:hover {
            border-color: var(--accent-color);
            box-shadow: 0 15px 30px -10px rgba(139, 126, 116, 0.12), 0 0 0 1px var(--accent-color);
            transform: translateY(-5px);
        }
        .card:hover .card-icon {
            background-color: var(--accent-color);
            color: #FFFFFF;
            transform: scale(1.05);
        }
        .card:hover .check-bullet {
            transform: scale(1.1);
            background-color: var(--accent-color);
            color: #FFFFFF;
        }
        .card:hover .card-button {
            background-color: var(--accent-color);
            color: #FFFFFF;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        }
        .team-contact-card {
            --avatar-color: #1D4F91;
        }
        .team-contact-card:hover {
            border-color: #1D4F91;
            box-shadow: 0 10px 20px -5px rgba(139, 126, 116, 0.12);
            transform: translateY(-5px);
        }
      }
    </style>
</head>
<body class="font-sans text-warm-dark leading-relaxed antialiased">
<div class="bg-[linear-gradient(135deg,#f7f8fb_0%,#fdf6fa_50%,#f7f8fb_100%)] px-6 py-12 [&_*]:box-border">
    <svg style="display:none;">
        <symbol id="icon-alert" viewBox="0 0 24 24">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <line x1="12" y1="9" x2="12" y2="13" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
            <line x1="12" y1="17" x2="12.01" y2="17" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
        </symbol>
        <symbol id="icon-check" viewBox="0 0 24 24">
            <polyline points="20 6 9 17 4 12" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
        </symbol>
        <symbol id="icon-arrow" viewBox="0 0 24 24">
            <line x1="5" y1="12" x2="19" y2="12" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
            <polyline points="12 5 19 12 12 19" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
        </symbol>
        <symbol id="icon-file" viewBox="0 0 24 24">
            <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <polyline points="14 2 14 8 20 8" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
            <line x1="16" y1="13" x2="8" y2="13" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
            <line x1="16" y1="17" x2="8" y2="17" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
            <polyline points="10 9 9 9 8 9" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
        </symbol>
        <symbol id="icon-wrench" viewBox="0 0 24 24">
            <path d="M14.7 6.3a1 1 0 0 0 0 1.4l1.6 1.6a1 1 0 0 0 1.4 0l3.77-3.77a6 6 0 0 1-7.94 7.94l-6.91 6.91a2.12 2.12 0 0 1-3-3l6.91-6.91a6 6 0 0 1 7.94-7.94l-3.76 3.76z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
        </symbol>
        <symbol id="icon-key" viewBox="0 0 24 24">
            <rect x="3" y="11" width="18" height="11" rx="2" ry="2" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></rect>
            <path d="M7 11V7a5 5 0 0 1 10 0v4" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
        </symbol>
        <symbol id="icon-users" viewBox="0 0 24 24">
            <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <circle cx="9" cy="7" r="4" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></circle>
            <path d="M23 21v-2a4 4 0 0 0-3-3.87" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M16 3.13a4 4 0 0 1 0 7.75" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
        </symbol>
        <symbol id="icon-email" viewBox="0 0 24 24">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <polyline points="22,6 12,13 2,6" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
        </symbol>
        <symbol id="icon-chat" viewBox="0 0 24 24">
            <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
        </symbol>
        <symbol id="icon-help" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></circle>
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <line x1="12" y1="17" x2="12.01" y2="17" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
        </symbol>
    </svg>

    <div class="max-w-[1280px] mx-auto flex flex-col gap-8">
        
        <!-- Navbar -->
        <header class="flex flex-col md:flex-row justify-between items-center p-[0.6rem] pl-5 bg-white/90 backdrop-blur-[12px] border border-warm-border rounded-full mb-8 shadow-[0_4px_20px_-5px_rgba(29,79,145,0.08)] sticky top-6 z-[1000]">
            <div class="flex items-center gap-3">
                <div class="w-8 h-8 flex items-center justify-center bg-[linear-gradient(135deg,#77127B_0%,#E80070_100%)] rounded-full text-white font-bold text-base shadow-[0_2px_6px_rgba(119,18,123,0.2)]">S</div>
                <span class="font-bold text-[0.85rem] text-experian-dark-blue tracking-widest">SPLATAM · SALESFORCE SQUAD</span>
            </div>
            <nav class="flex items-center gap-1 mt-4 md:mt-0 flex-wrap justify-center">
                <a href="#servicios" class="text-[0.8rem] font-semibold text-warm-medium no-underline px-4 py-2 rounded-full transition-all duration-300 border border-transparent hover:text-experian-dark-blue hover:bg-warm-casual hover:border-warm-border">Servicios</a>
                <a href="#equipo" class="text-[0.8rem] font-semibold text-warm-medium no-underline px-4 py-2 rounded-full transition-all duration-300 border border-transparent hover:text-experian-dark-blue hover:bg-warm-casual hover:border-warm-border">Equipo</a>
                <a href="#indicadores" class="text-[0.8rem] font-semibold text-warm-medium no-underline px-4 py-2 rounded-full transition-all duration-300 border border-transparent hover:text-experian-dark-blue hover:bg-warm-casual hover:border-warm-border">Indicadores</a>
                <a href="#crear-solicitud" class="text-[0.8rem] font-semibold text-white no-underline px-5 py-2 rounded-full bg-[linear-gradient(135deg,#1D4F91_0%,#77127B_100%)] transition-all duration-300 ml-1 hover:shadow-[0_4px_10px_rgba(119,18,123,0.3)] hover:-translate-y-[1px]">Crear Solicitud</a>
            </nav>
        </header>

        <!-- Hero Section -->
        <section class="grid grid-cols-1 lg:grid-cols-[1.1fr_0.9fr] gap-16 items-center bg-white rounded-[24px] p-[4rem] border border-warm-border mb-4 shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] max-lg:p-12 max-lg:gap-12 max-md:p-6 max-md:gap-8">
            <div class="flex flex-col gap-5">
                <span class="self-start bg-[color-mix(in_srgb,#E80070_8%,#FFFFFF)] text-experian-magenta text-[0.75rem] font-bold px-4 py-[0.45rem] rounded-full uppercase tracking-wider flex items-center gap-2 border border-[color-mix(in_srgb,#E80070_15%,transparent)]">
                    <svg class="w-[1.1rem] h-[1.1rem]"><use href="#icon-help"></use></svg>
                    Habilitación Regional
                </span>
                <h1 class="text-[3.65rem] font-extrabold text-warm-dark leading-[1.1] tracking-[-0.03em] max-md:text-[2.25rem]">
                    Bienvenidos al<br><span class="text-experian-magenta">Squad Regional</span><br>de Salesforce
                </h1>
                <p class="text-[0.95rem] text-warm-medium leading-[1.6] mt-2">
                    Nuestro equipo está dedicado a recibir las necesidades regionales para mejorar los procesos gestionados a través de Salesforce, con el fin de generar eficiencias a nivel organizacional, con soluciones prácticas y de alto impacto, generando valor, no solo desarrollando soluciones en Salesforce e integrándolas con otros sistemas, sino también evaluando la utilidad y beneficio para la compañía.
                </p>
            </div>
            
            <div class="hero-panel bg-[linear-gradient(180deg,#F4F7FB_0%,#FFFFFF_100%)] rounded-[20px] p-[2.25rem] flex flex-col gap-6 border border-[color-mix(in_srgb,#1D4F91_12%,transparent)] shadow-[0_12px_30px_-10px_rgba(29,79,145,0.12)] relative overflow-hidden max-md:p-6">
                
                <div class="flex items-center gap-5 pb-4 border-b border-dashed border-warm-border relative z-10">
                    <div class="w-[44px] h-[44px] bg-[linear-gradient(135deg,#1D4F91_0%,#77127B_100%)] rounded-xl flex items-center justify-center shrink-0 text-white shadow-[0_4px_10px_rgba(119,18,123,0.2)]">
                        <svg class="w-[1.35rem] h-[1.35rem]"><use href="#icon-check"></use></svg>
                    </div>
                    <div>
                        <h3 class="text-[1.15rem] font-bold text-warm-dark mb-[0.2rem] tracking-[-0.01em]">¿Qué necesitas hacer hoy?</h3>
                        <p class="text-[0.85rem] text-warm-medium leading-[1.4]">Elige una opción para gestionar tu solicitud</p>
                    </div>
                </div>
                
                <div class="flex flex-col gap-3 relative z-10">
                    <a href="#card-title-1" class="hero-step bg-white border border-warm-border rounded-xl px-[1.15rem] py-[0.85rem] flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] no-underline text-inherit cursor-pointer hover:translate-x-1 hover:border-experian-purple hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] hover:bg-[#FAFAFB] group">
                        <div class="hero-step-icon w-[36px] h-[36px] flex items-center justify-center bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] rounded-lg shrink-0 text-experian-purple transition-all duration-300 text-[1.25rem] group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-[5deg] group-hover:shadow-[0_4px_10px_color-mix(in_srgb,#77127B_30%,transparent)]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-file"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-[0.1rem]">Nueva necesidad o mejora</h4>
                            <p class="text-[0.75rem] text-warm-medium leading-[1.3]">Crear HU</p>
                        </div>
                    </a>
                    <a href="#card-title-2" class="hero-step bg-white border border-warm-border rounded-xl px-[1.15rem] py-[0.85rem] flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] no-underline text-inherit cursor-pointer hover:translate-x-1 hover:border-experian-purple hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] hover:bg-[#FAFAFB] group">
                        <div class="hero-step-icon w-[36px] h-[36px] flex items-center justify-center bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] rounded-lg shrink-0 text-experian-purple transition-all duration-300 text-[1.25rem] group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-[5deg] group-hover:shadow-[0_4px_10px_color-mix(in_srgb,#77127B_30%,transparent)]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-wrench"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-[0.1rem]">Soporte o configuración</h4>
                            <p class="text-[0.75rem] text-warm-medium leading-[1.3]">Requerimiento</p>
                        </div>
                    </a>
                    <a href="#card-title-2" class="hero-step bg-white border border-warm-border rounded-xl px-[1.15rem] py-[0.85rem] flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] no-underline text-inherit cursor-pointer hover:translate-x-1 hover:border-experian-purple hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] hover:bg-[#FAFAFB] group">
                        <div class="hero-step-icon w-[36px] h-[36px] flex items-center justify-center bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] rounded-lg shrink-0 text-experian-purple transition-all duration-300 text-[1.25rem] group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-[5deg] group-hover:shadow-[0_4px_10px_color-mix(in_srgb,#77127B_30%,transparent)]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-alert"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-[0.1rem]">Algo no funciona</h4>
                            <p class="text-[0.75rem] text-warm-medium leading-[1.3]">Crear incidente</p>
                        </div>
                    </a>
                    <a href="#card-title-3" class="hero-step bg-white border border-warm-border rounded-xl px-[1.15rem] py-[0.85rem] flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] no-underline text-inherit cursor-pointer hover:translate-x-1 hover:border-experian-purple hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] hover:bg-[#FAFAFB] group">
                        <div class="hero-step-icon w-[36px] h-[36px] flex items-center justify-center bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] rounded-lg shrink-0 text-experian-purple transition-all duration-300 text-[1.25rem] group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-[5deg] group-hover:shadow-[0_4px_10px_color-mix(in_srgb,#77127B_30%,transparent)]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-key"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-[0.1rem]">Necesito acceso</h4>
                            <p class="text-[0.75rem] text-warm-medium leading-[1.3]">Solicitud acceso</p>
                        </div>
                    </a>                    
                    <a href="#card-title-4" class="hero-step bg-white border border-warm-border rounded-xl px-[1.15rem] py-[0.85rem] flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] no-underline text-inherit cursor-pointer hover:translate-x-1 hover:border-experian-purple hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] hover:bg-[#FAFAFB] group">
                        <div class="hero-step-icon w-[36px] h-[36px] flex items-center justify-center bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] rounded-lg shrink-0 text-experian-purple transition-all duration-300 text-[1.25rem] group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-[5deg] group-hover:shadow-[0_4px_10px_color-mix(in_srgb,#77127B_30%,transparent)]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-help"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-[0.1rem]">No estoy seguro</h4>
                            <p class="text-[0.75rem] text-warm-medium leading-[1.3]">Contactar equipo</p>
                        </div>
                    </a>
                </div>
            </div>
        </section>

        <div class="flex flex-col gap-1 -mb-4">
            <h2 class="text-[1.85rem] font-extrabold text-experian-dark-blue tracking-[-0.02em]">Gestión de Solicitudes Salesforce LATAM</h2>
            <p class="text-[1rem] text-warm-medium font-medium">Canal Oficial de Operaciones & Configuración Experian</p>
        </div>

        <main class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 scroll-mt-[110px]" id="servicios">

            <!-- Card 1 -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 scroll-mt-[110px]" style="--accent-color: #426DA9;" aria-labelledby="card-title-1">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="card-icon w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[color-mix(in_srgb,#426DA9_8%,#FFFFFF)] text-[1.15rem] text-[#426DA9]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-file"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-warm-dark tracking-[-0.01em] leading-[1.3] scroll-mt-[110px]" id="card-title-1">Historia de Usuario</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 min-h-[66px] leading-[1.5]">Crea y documenta requerimientos funcionales desde la perspectiva del usuario de negocio. Utiliza esta opción para nuevos requerimientos funcionales o ajuste en Salesforce.</p>
                    <ul class="flex flex-col gap-3 mb-8 list-none">
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#426DA9_8%,#FFFFFF)] text-[#426DA9] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Define claramente el usuario</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#426DA9_8%,#FFFFFF)] text-[#426DA9] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Especifica el valor esperado</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#426DA9_8%,#FFFFFF)] text-[#426DA9] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Evita duplicidades</span>
                        </li>
                    </ul>
                </div>
                <a href="#crear-historia" class="card-button inline-flex items-center justify-center w-full px-4 py-3 font-sans text-[0.875rem] font-semibold rounded-xl cursor-pointer transition-all duration-300 no-underline border-[1.5px] border-[#426DA9] bg-white text-[#426DA9] gap-[0.4rem]">
                    <span>Crear Historia en Jira</span>
                    <svg class="w-[1em] h-[1em]"><use href="#icon-arrow"></use></svg>
                </a>
            </section>

            <!-- Card 2 -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 scroll-mt-[110px]" style="--accent-color: #77127B;" aria-labelledby="card-title-2">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="card-icon w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] text-[1.15rem] text-[#77127B]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-wrench"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-warm-dark tracking-[-0.01em] leading-[1.3] scroll-mt-[110px]" id="card-title-2">Requerimiento Técnico</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 min-h-[66px] leading-[1.5]">Utiliza esta opción cuando necesites registrar un requerimiento general que no implique un desarrollo inmediato.</p>
                    <ul class="flex flex-col gap-3 mb-8 list-none">
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] text-[#77127B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Solicitudes funcionales operativas</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] text-[#77127B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Actualización de información</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] text-[#77127B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Creación o modificación de reportes</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] text-[#77127B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Modificacion de aprobadores</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#77127B_8%,#FFFFFF)] text-[#77127B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Soporte en procesos</span>
                        </li>
                    </ul>
                </div>
                <a href="#crear-requerimiento" class="card-button inline-flex items-center justify-center w-full px-4 py-3 font-sans text-[0.875rem] font-semibold rounded-xl cursor-pointer transition-all duration-300 no-underline border-[1.5px] border-[#77127B] bg-white text-[#77127B] gap-[0.4rem]">
                    <span>Crear Requerimiento en Service Now</span>
                    <svg class="w-[1em] h-[1em]"><use href="#icon-arrow"></use></svg>
                </a>
            </section>

            <!-- Card 3 -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 scroll-mt-[110px]" style="--accent-color: #C1188B;" aria-labelledby="card-title-3">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="card-icon w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[color-mix(in_srgb,#C1188B_8%,#FFFFFF)] text-[1.15rem] text-[#C1188B]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-key"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-warm-dark tracking-[-0.01em] leading-[1.3] scroll-mt-[110px]" id="card-title-3">Solicitud de Acceso</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 min-h-[66px] leading-[1.5]">Administración de usuarios. Utiliza esta opción si necesitas acceso a Salesforce o permisos adicionales dentro de la plataforma.</p>
                    <ul class="flex flex-col gap-3 mb-8 list-none">
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#C1188B_8%,#FFFFFF)] text-[#C1188B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Nuevos Usuarios</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#C1188B_8%,#FFFFFF)] text-[#C1188B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Modificación o ajuste de roles y permisos</span>
                        </li>
                        <li class="flex items-start gap-[0.65rem] text-[0.85rem] leading-[1.4]">
                            <span class="check-bullet inline-flex items-center justify-center w-[18px] h-[18px] bg-[color-mix(in_srgb,#C1188B_8%,#FFFFFF)] text-[#C1188B] rounded-full shrink-0 mt-[1px] transition-all duration-300 text-[0.75rem]">
                                <svg class="w-[1em] h-[1em]"><use href="#icon-check"></use></svg>
                            </span>
                            <span>Control de accesos</span>
                        </li>
                    </ul>
                </div>
                <a href="#solicitar-acceso" class="card-button inline-flex items-center justify-center w-full px-4 py-3 font-sans text-[0.875rem] font-semibold rounded-xl cursor-pointer transition-all duration-300 no-underline border-[1.5px] border-[#C1188B] bg-white text-[#C1188B] gap-[0.4rem]">
                    <span>Solicitar Acceso</span>
                    <svg class="w-[1em] h-[1em]"><use href="#icon-arrow"></use></svg>
                </a>
            </section>

            <!-- Card 4 -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 scroll-mt-[110px]" style="--accent-color: #E80070;" aria-labelledby="card-title-4">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="card-icon w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[color-mix(in_srgb,#E80070_8%,#FFFFFF)] text-[1.15rem] text-[#E80070]">
                            <svg class="w-[1em] h-[1em]"><use href="#icon-users"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-warm-dark tracking-[-0.01em] leading-[1.3] scroll-mt-[110px]" id="card-title-4">Equipo Salesforce</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 min-h-[66px] leading-[1.5]">Célula de desarrollo y soporte encargada del mantenimiento de la plataforma.</p>
                    <div class="flex flex-col gap-2 mb-6">
                        <!-- Miembro 1 -->
                        <details class="team-member border border-warm-border rounded-[10px] bg-warm-casual overflow-hidden transition-all duration-300 shrink-0" name="team-accordion">
                            <summary class="flex items-center gap-[0.6rem] p-[0.6rem] cursor-pointer list-none outline-none select-none">
                                <div class="w-[28px] h-[28px] rounded-full bg-[color-mix(in_srgb,#E80070_15%,#FFFFFF)] text-[#E80070] font-bold text-[0.75rem] flex items-center justify-center uppercase">AS</div>
                                <div class="flex flex-col leading-[1.2]"><span class="text-[0.8rem] font-semibold">Ana Silva</span><span class="text-[0.7rem] text-warm-medium">SF Admin</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250"><svg class="w-[1em] h-[1em]" style="font-size:0.65rem; stroke-width:3"><use href="#icon-arrow"></use></svg></span>
                            </summary>
                            <div class="px-[0.6rem] pb-[0.6rem] pt-[0.4rem] pl-[2.5rem] text-[0.75rem] text-warm-medium leading-[1.4] border-t border-dashed border-warm-border">
                                <p>Contactar para: Administración general, gestión de accesos, roles, perfiles y soporte del día a día en LATAM.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=ana.silva@experian.com" class="inline-flex items-center gap-[0.4rem] mt-[0.6rem] font-semibold text-[#E80070] no-underline px-[0.6rem] py-[0.3rem] rounded-[6px] bg-[color-mix(in_srgb,#E80070_8%,transparent)] transition-all duration-300 hover:bg-[#E80070] hover:text-white"><svg class="w-[1em] h-[1em]"><use href="#icon-chat"></use></svg> Contactar</a>
                            </div>
                        </details>
                        <!-- Miembro 2 -->
                        <details class="team-member border border-warm-border rounded-[10px] bg-warm-casual overflow-hidden transition-all duration-300 shrink-0" name="team-accordion">
                            <summary class="flex items-center gap-[0.6rem] p-[0.6rem] cursor-pointer list-none outline-none select-none">
                                <div class="w-[28px] h-[28px] rounded-full bg-[color-mix(in_srgb,#E80070_15%,#FFFFFF)] text-[#E80070] font-bold text-[0.75rem] flex items-center justify-center uppercase">CP</div>
                                <div class="flex flex-col leading-[1.2]"><span class="text-[0.8rem] font-semibold">Carlos Pérez</span><span class="text-[0.7rem] text-warm-medium">Lead Developer</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250"><svg class="w-[1em] h-[1em]" style="font-size:0.65rem; stroke-width:3"><use href="#icon-arrow"></use></svg></span>
                            </summary>
                            <div class="px-[0.6rem] pb-[0.6rem] pt-[0.4rem] pl-[2.5rem] text-[0.75rem] text-warm-medium leading-[1.4] border-t border-dashed border-warm-border">
                                <p>Contactar para: Desarrollo Apex, LWC, integraciones y flujos complejos de automatización.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=carlos.perez@experian.com" class="inline-flex items-center gap-[0.4rem] mt-[0.6rem] font-semibold text-[#E80070] no-underline px-[0.6rem] py-[0.3rem] rounded-[6px] bg-[color-mix(in_srgb,#E80070_8%,transparent)] transition-all duration-300 hover:bg-[#E80070] hover:text-white"><svg class="w-[1em] h-[1em]"><use href="#icon-chat"></use></svg> Contactar</a>
                            </div>
                        </details>
                        <!-- Miembro 3 -->
                        <details class="team-member border border-warm-border rounded-[10px] bg-warm-casual overflow-hidden transition-all duration-300 shrink-0" name="team-accordion">
                            <summary class="flex items-center gap-[0.6rem] p-[0.6rem] cursor-pointer list-none outline-none select-none">
                                <div class="w-[28px] h-[28px] rounded-full bg-[color-mix(in_srgb,#E80070_15%,#FFFFFF)] text-[#E80070] font-bold text-[0.75rem] flex items-center justify-center uppercase">MR</div>
                                <div class="flex flex-col leading-[1.2]"><span class="text-[0.8rem] font-semibold">María Rodríguez</span><span class="text-[0.7rem] text-warm-medium">Product Owner</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250"><svg class="w-[1em] h-[1em]" style="font-size:0.65rem; stroke-width:3"><use href="#icon-arrow"></use></svg></span>
                            </summary>
                            <div class="px-[0.6rem] pb-[0.6rem] pt-[0.4rem] pl-[2.5rem] text-[0.75rem] text-warm-medium leading-[1.4] border-t border-dashed border-warm-border">
                                <p>Contactar para: Definición de roadmap, priorización del backlog de solicitudes y alineación estratégica.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=maria.rodriguez@experian.com" class="inline-flex items-center gap-[0.4rem] mt-[0.6rem] font-semibold text-[#E80070] no-underline px-[0.6rem] py-[0.3rem] rounded-[6px] bg-[color-mix(in_srgb,#E80070_8%,transparent)] transition-all duration-300 hover:bg-[#E80070] hover:text-white"><svg class="w-[1em] h-[1em]"><use href="#icon-chat"></use></svg> Contactar</a>
                            </div>
                        </details>
                        <!-- Miembro 4 -->
                        <details class="team-member border border-warm-border rounded-[10px] bg-warm-casual overflow-hidden transition-all duration-300 shrink-0" name="team-accordion">
                            <summary class="flex items-center gap-[0.6rem] p-[0.6rem] cursor-pointer list-none outline-none select-none">
                                <div class="w-[28px] h-[28px] rounded-full bg-[color-mix(in_srgb,#E80070_15%,#FFFFFF)] text-[#E80070] font-bold text-[0.75rem] flex items-center justify-center uppercase">JG</div>
                                <div class="flex flex-col leading-[1.2]"><span class="text-[0.8rem] font-semibold">Juan Gómez</span><span class="text-[0.7rem] text-warm-medium">QA Engineer</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250"><svg class="w-[1em] h-[1em]" style="font-size:0.65rem; stroke-width:3"><use href="#icon-arrow"></use></svg></span>
                            </summary>
                            <div class="px-[0.6rem] pb-[0.6rem] pt-[0.4rem] pl-[2.5rem] text-[0.75rem] text-warm-medium leading-[1.4] border-t border-dashed border-warm-border">
                                <p>Contactar para: Pruebas automatizadas, reporte de bugs, aseguramiento de calidad de desarrollos.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=juan.gomez@experian.com" class="inline-flex items-center gap-[0.4rem] mt-[0.6rem] font-semibold text-[#E80070] no-underline px-[0.6rem] py-[0.3rem] rounded-[6px] bg-[color-mix(in_srgb,#E80070_8%,transparent)] transition-all duration-300 hover:bg-[#E80070] hover:text-white"><svg class="w-[1em] h-[1em]"><use href="#icon-chat"></use></svg> Contactar</a>
                            </div>
                        </details>
                        <!-- Miembro 5 -->
                        <details class="team-member border border-warm-border rounded-[10px] bg-warm-casual overflow-hidden transition-all duration-300 shrink-0" name="team-accordion">
                            <summary class="flex items-center gap-[0.6rem] p-[0.6rem] cursor-pointer list-none outline-none select-none">
                                <div class="w-[28px] h-[28px] rounded-full bg-[color-mix(in_srgb,#E80070_15%,#FFFFFF)] text-[#E80070] font-bold text-[0.75rem] flex items-center justify-center uppercase">DT</div>
                                <div class="flex flex-col leading-[1.2]"><span class="text-[0.8rem] font-semibold">Diana Torres</span><span class="text-[0.7rem] text-warm-medium">Business Analyst</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250"><svg class="w-[1em] h-[1em]" style="font-size:0.65rem; stroke-width:3"><use href="#icon-arrow"></use></svg></span>
                            </summary>
                            <div class="px-[0.6rem] pb-[0.6rem] pt-[0.4rem] pl-[2.5rem] text-[0.75rem] text-warm-medium leading-[1.4] border-t border-dashed border-warm-border">
                                <p>Contactar para: Toma de requerimientos, análisis de procesos de negocio, dudas sobre reglas funcionales.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=diana.torres@experian.com" class="inline-flex items-center gap-[0.4rem] mt-[0.6rem] font-semibold text-[#E80070] no-underline px-[0.6rem] py-[0.3rem] rounded-[6px] bg-[color-mix(in_srgb,#E80070_8%,transparent)] transition-all duration-300 hover:bg-[#E80070] hover:text-white"><svg class="w-[1em] h-[1em]"><use href="#icon-chat"></use></svg> Contactar</a>
                            </div>
                        </details>
                        <!-- Miembro 6 -->
                        <details class="team-member border border-warm-border rounded-[10px] bg-warm-casual overflow-hidden transition-all duration-300 shrink-0" name="team-accordion">
                            <summary class="flex items-center gap-[0.6rem] p-[0.6rem] cursor-pointer list-none outline-none select-none">
                                <div class="w-[28px] h-[28px] rounded-full bg-[color-mix(in_srgb,#E80070_15%,#FFFFFF)] text-[#E80070] font-bold text-[0.75rem] flex items-center justify-center uppercase">AM</div>
                                <div class="flex flex-col leading-[1.2]"><span class="text-[0.8rem] font-semibold">Andrés Mendoza</span><span class="text-[0.7rem] text-warm-medium">Integrations Eng.</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250"><svg class="w-[1em] h-[1em]" style="font-size:0.65rem; stroke-width:3"><use href="#icon-arrow"></use></svg></span>
                            </summary>
                            <div class="px-[0.6rem] pb-[0.6rem] pt-[0.4rem] pl-[2.5rem] text-[0.75rem] text-warm-medium leading-[1.4] border-t border-dashed border-warm-border">
                                <p>Contactar para: Fallos en integraciones con otros sistemas, APIs, validación de datos externos.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=andres.mendoza@experian.com" class="inline-flex items-center gap-[0.4rem] mt-[0.6rem] font-semibold text-[#E80070] no-underline px-[0.6rem] py-[0.3rem] rounded-[6px] bg-[color-mix(in_srgb,#E80070_8%,transparent)] transition-all duration-300 hover:bg-[#E80070] hover:text-white"><svg class="w-[1em] h-[1em]"><use href="#icon-chat"></use></svg> Contactar</a>
                            </div>
                        </details>
                        <!-- Miembro 7 -->
                        <details class="team-member border border-warm-border rounded-[10px] bg-warm-casual overflow-hidden transition-all duration-300 shrink-0" name="team-accordion">
                            <summary class="flex items-center gap-[0.6rem] p-[0.6rem] cursor-pointer list-none outline-none select-none">
                                <div class="w-[28px] h-[28px] rounded-full bg-[color-mix(in_srgb,#E80070_15%,#FFFFFF)] text-[#E80070] font-bold text-[0.75rem] flex items-center justify-center uppercase">LR</div>
                                <div class="flex flex-col leading-[1.2]"><span class="text-[0.8rem] font-semibold">Laura Restrepo</span><span class="text-[0.7rem] text-warm-medium">UX/UI Designer</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250"><svg class="w-[1em] h-[1em]" style="font-size:0.65rem; stroke-width:3"><use href="#icon-arrow"></use></svg></span>
                            </summary>
                            <div class="px-[0.6rem] pb-[0.6rem] pt-[0.4rem] pl-[2.5rem] text-[0.75rem] text-warm-medium leading-[1.4] border-t border-dashed border-warm-border">
                                <p>Contactar para: Mejoras en usabilidad, rediseño de pantallas, optimización de flujos de usuario.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=laura.restrepo@experian.com" class="inline-flex items-center gap-[0.4rem] mt-[0.6rem] font-semibold text-[#E80070] no-underline px-[0.6rem] py-[0.3rem] rounded-[6px] bg-[color-mix(in_srgb,#E80070_8%,transparent)] transition-all duration-300 hover:bg-[#E80070] hover:text-white"><svg class="w-[1em] h-[1em]"><use href="#icon-chat"></use></svg> Contactar</a>
                            </div>
                        </details>
                    </div>
                </div>
                <a href="#nuestro-equipo" class="card-button inline-flex items-center justify-center w-full px-4 py-3 font-sans text-[0.875rem] font-semibold rounded-xl cursor-pointer transition-all duration-300 no-underline border-[1.5px] border-[#E80070] bg-white text-[#E80070] gap-[0.4rem]">
                    <span>Contactar Equipo</span>
                    <svg class="w-[1em] h-[1em]"><use href="#icon-arrow"></use></svg>
                </a>
            </section>
        </main>

        <section class="flex flex-col gap-8 mt-4 scroll-mt-[110px]" id="equipo">
            <div class="flex flex-col gap-1 border-b border-warm-border pb-4">
                <h2 class="text-[1.35rem] font-bold text-experian-dark-blue leading-[1.3] tracking-[-0.01em]">Conoce a nuestro equipo</h2>
                <p class="text-[0.9rem] text-warm-medium">El equipo de expertos dedicado a la administración, desarrollo y evolución de la plataforma Salesforce LATAM.</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
                <!-- AS -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] p-6 flex flex-col justify-between items-center transition-all duration-300">
                    <div class="w-[64px] h-[64px] rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-[linear-gradient(135deg,#1D4F91_0%,color-mix(in_srgb,#1D4F91_60%,#FFFFFF)_100%)] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">AS</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Ana Silva</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Salesforce Administrator</p>
                    <div class="w-full flex flex-col gap-[0.4rem] border-t border-warm-border pt-4">
                        <a href="mailto:ana.silva@experian.com" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-email"></use></svg><span>ana.silva@experian.com</span>
                        </a>
                        <a href="#chat-asilva" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-chat"></use></svg><span>@asilva</span>
                        </a>
                    </div>
                </div>
                <!-- CP -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] p-6 flex flex-col justify-between items-center transition-all duration-300">
                    <div class="w-[64px] h-[64px] rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-[linear-gradient(135deg,#1D4F91_0%,color-mix(in_srgb,#1D4F91_60%,#FFFFFF)_100%)] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">CP</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Carlos Pérez</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Lead Developer</p>
                    <div class="w-full flex flex-col gap-[0.4rem] border-t border-warm-border pt-4">
                        <a href="mailto:carlos.perez@experian.com" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-email"></use></svg><span>carlos.perez@experian.com</span>
                        </a>
                        <a href="#chat-cperez" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-chat"></use></svg><span>@cperez</span>
                        </a>
                    </div>
                </div>
                <!-- MR -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] p-6 flex flex-col justify-between items-center transition-all duration-300">
                    <div class="w-[64px] h-[64px] rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-[linear-gradient(135deg,#1D4F91_0%,color-mix(in_srgb,#1D4F91_60%,#FFFFFF)_100%)] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">MR</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">María Rodríguez</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Product Owner</p>
                    <div class="w-full flex flex-col gap-[0.4rem] border-t border-warm-border pt-4">
                        <a href="mailto:maria.rodriguez@experian.com" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-email"></use></svg><span>maria.rodriguez@experian.com</span>
                        </a>
                        <a href="#chat-mrodriguez" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-chat"></use></svg><span>@mrodriguez</span>
                        </a>
                    </div>
                </div>
                <!-- JG -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] p-6 flex flex-col justify-between items-center transition-all duration-300">
                    <div class="w-[64px] h-[64px] rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-[linear-gradient(135deg,#1D4F91_0%,color-mix(in_srgb,#1D4F91_60%,#FFFFFF)_100%)] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">JG</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Juan Gómez</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">QA Automation Engineer</p>
                    <div class="w-full flex flex-col gap-[0.4rem] border-t border-warm-border pt-4">
                        <a href="mailto:juan.gomez@experian.com" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-email"></use></svg><span>juan.gomez@experian.com</span>
                        </a>
                        <a href="#chat-jgomez" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-chat"></use></svg><span>@jgomez</span>
                        </a>
                    </div>
                </div>
                <!-- DT -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] p-6 flex flex-col justify-between items-center transition-all duration-300">
                    <div class="w-[64px] h-[64px] rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-[linear-gradient(135deg,#1D4F91_0%,color-mix(in_srgb,#1D4F91_60%,#FFFFFF)_100%)] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">DT</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Diana Torres</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Business Analyst</p>
                    <div class="w-full flex flex-col gap-[0.4rem] border-t border-warm-border pt-4">
                        <a href="mailto:diana.torres@experian.com" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-email"></use></svg><span>diana.torres@experian.com</span>
                        </a>
                        <a href="#chat-dtorres" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-chat"></use></svg><span>@dtorres</span>
                        </a>
                    </div>
                </div>
                <!-- AM -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] p-6 flex flex-col justify-between items-center transition-all duration-300">
                    <div class="w-[64px] h-[64px] rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-[linear-gradient(135deg,#1D4F91_0%,color-mix(in_srgb,#1D4F91_60%,#FFFFFF)_100%)] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">AM</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Andrés Mendoza</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Integrations Engineer</p>
                    <div class="w-full flex flex-col gap-[0.4rem] border-t border-warm-border pt-4">
                        <a href="mailto:andres.mendoza@experian.com" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-email"></use></svg><span>andres.mendoza@experian.com</span>
                        </a>
                        <a href="#chat-amendoza" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-chat"></use></svg><span>@amendoza</span>
                        </a>
                    </div>
                </div>
                <!-- LR -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] p-6 flex flex-col justify-between items-center transition-all duration-300">
                    <div class="w-[64px] h-[64px] rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-[linear-gradient(135deg,#1D4F91_0%,color-mix(in_srgb,#1D4F91_60%,#FFFFFF)_100%)] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">LR</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Laura Restrepo</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">UX/UI Designer</p>
                    <div class="w-full flex flex-col gap-[0.4rem] border-t border-warm-border pt-4">
                        <a href="mailto:laura.restrepo@experian.com" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-email"></use></svg><span>laura.restrepo@experian.com</span>
                        </a>
                        <a href="#chat-lrestrepo" class="flex items-center justify-center gap-[0.4rem] text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-[0.75rem] h-[0.75rem] shrink-0"><use href="#icon-chat"></use></svg><span>@lrestrepo</span>
                        </a>
                    </div>
                </div>
            </div>
        </section>
    </div>
</div>

<script>
    document.addEventListener('DOMContentLoaded', () => {
        const steps = document.querySelectorAll('.hero-step');
        steps.forEach(step => {
            step.addEventListener('click', function(e) {
                const targetId = this.getAttribute('href');
                if (targetId && targetId.startsWith('#')) {
                    const targetElement = document.querySelector(targetId);
                    if (targetElement) {
                        const container = targetElement.closest('.card') || (targetElement.id === 'equipo' ? targetElement : null) || document.querySelector(targetId);
                        if (container) {
                            container.classList.remove('highlight-focus');
                            document.body.classList.remove('is-pulsing');
                            void container.offsetWidth; // trigger reflow to restart animation
                            container.classList.add('highlight-focus');
                            document.body.classList.add('is-pulsing');
                            
                            setTimeout(() => {
                                container.classList.remove('highlight-focus');
                                document.body.classList.remove('is-pulsing');
                            }, 2500);
                        }
                    }
                }
            });
        });
    });
</script>

</body>
</html>
"""

with open("minimal_optimized.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Successfully written minimal_optimized.html using tailwind")
