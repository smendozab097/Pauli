with open("minimal_optimized.html", "w", encoding="utf-8") as f:
    f.write("""<script src="https://cdn.tailwindcss.com"></script>
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
            'magenta': '#E80070',
            'warm-bg': '#FAF7F2'
          },
          warm: {
            dark: '#2F2A26',
            medium: '#6E6760',
            border: '#EFEAE2'
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
      color: #1D4F91;
    }
  }
</style>

<!-- Google Fonts -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<div class="experian-container font-sans bg-gradient-to-br from-[#f7f8fb] via-[#fdf6fa] to-[#f7f8fb] text-warm-dark leading-relaxed antialiased p-6 md:p-12 w-full box-border [&_*]:box-border">
    <svg style="display:none;">
        <symbol id="icon-alert" viewBox="0 0 24 24">
            <path d="M10.29 3.86L1.82 18a2 2 0 0 0 1.71 3h16.94a2 2 0 0 0 1.71-3L13.71 3.86a2 2 0 0 0-3.42 0z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <line x1="12" y1="9" x2="12" y2="13" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
            <line x1="12" y1="17" x2="12.01" y2="17" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
        </symbol>
        <symbol id="icon-check" viewBox="0 0 24 24">
            <polyline points="20 6 9 17 4 12" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
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
            <path d="M21 2l-2 2m-7.61 7.61a5.5 5.5 0 1 1-7.778 7.778 5.5 5.5 0 0 1 7.777-7.777zm0 0L15.5 7.5m0 0l3 3L22 7l-3-3m-3.5 3.5L19 4" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
        </symbol>
        <symbol id="icon-help" viewBox="0 0 24 24">
            <circle cx="12" cy="12" r="10" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></circle>
            <path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <line x1="12" y1="17" x2="12.01" y2="17" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></line>
        </symbol>
        <symbol id="icon-arrow" viewBox="0 0 24 24">
            <polyline points="6 9 12 15 18 9" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
        </symbol>
        <symbol id="icon-chat" viewBox="0 0 24 24">
            <path d="M21 11.5a8.38 8.38 0 0 1-.9 3.8 8.5 8.5 0 0 1-7.6 4.7 8.38 8.38 0 0 1-3.8-.9L3 21l1.9-5.7a8.38 8.38 0 0 1-.9-3.8 8.5 8.5 0 0 1 4.7-7.6 8.38 8.38 0 0 1 3.8-.9h.5a8.48 8.48 0 0 1 8 8v.5z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
        </symbol>
        <symbol id="icon-email" viewBox="0 0 24 24">
            <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <polyline points="22,6 12,13 2,6" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></polyline>
        </symbol>
        <symbol id="icon-rocket" viewBox="0 0 24 24">
            <path d="M4.5 16.5c-1.5 1.26-2 5-2 5s3.74-.5 5-2c.71-.84.7-2.13-.09-2.91a2.18 2.18 0 0 0-2.91-.09z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M12 15l-3-3a22 22 0 0 1 2-3.95A12.88 12.88 0 0 1 22 2c0 2.72-.78 7.5-6 11a22.35 22.35 0 0 1-4 2z" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M9 12H4s.55-3.03 2-4c1.62-1.08 5 0 5 0" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
            <path d="M12 15v5s3.03-.55 4-2c1.08-1.62 0-5 0-5" stroke="currentColor" fill="none" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"></path>
        </symbol>
    </svg>

    <div class="max-w-[1280px] mx-auto flex flex-col gap-8">
        
        <!-- Navbar -->
        <nav class="flex flex-col md:flex-row justify-between items-center p-2.5 md:pl-5 bg-white/90 backdrop-blur-md border border-warm-border rounded-3xl md:rounded-full mb-8 shadow-sm sticky top-6 z-50">
            <div class="flex items-center gap-3">
                <div class="w-8 h-8 flex items-center justify-center bg-gradient-to-br from-experian-purple to-experian-magenta rounded-full text-white font-bold text-base shadow-md">
                    SF
                </div>
                <div class="font-bold text-sm text-experian-dark-blue tracking-wider">
                    SALESFORCE SQUAD
                </div>
            </div>
            <div class="flex flex-wrap items-center justify-center gap-2 mt-4 md:mt-0">
                <a href="#card-title-1" class="text-xs font-semibold text-warm-medium no-underline px-4 py-2 rounded-full transition-all border border-transparent hover:text-experian-dark-blue hover:bg-experian-warm-bg hover:border-warm-border">Crear HU</a>
                <a href="#card-title-2" class="text-xs font-semibold text-warm-medium no-underline px-4 py-2 rounded-full transition-all border border-transparent hover:text-experian-dark-blue hover:bg-experian-warm-bg hover:border-warm-border">Crear Requerimiento</a>
                <a href="#card-title-2" class="text-xs font-semibold text-warm-medium no-underline px-4 py-2 rounded-full transition-all border border-transparent hover:text-experian-dark-blue hover:bg-experian-warm-bg hover:border-warm-border">Crear Incidente</a>
                <a href="#card-title-3" class="text-xs font-semibold text-warm-medium no-underline px-4 py-2 rounded-full transition-all border border-transparent hover:text-experian-dark-blue hover:bg-experian-warm-bg hover:border-warm-border">Solicitud Acceso</a>
                <a href="https://experian.service-now.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_category_view.do%3Fv%3D1%26sysparm_category%3De15706fc0a0a0aa7007fc21e1ab70c2f" target="_blank" class="text-xs font-semibold text-white no-underline px-5 py-2 rounded-full bg-gradient-to-br from-experian-dark-blue to-experian-purple transition-transform duration-300 ml-1 hover:-translate-y-0.5 hover:shadow-lg">Ir a ServiceNow</a>
            </div>
        </nav>

        <!-- Hero Section -->
        <section class="grid grid-cols-1 lg:grid-cols-[1.1fr_0.9fr] gap-8 md:gap-16 items-center bg-white rounded-3xl p-6 md:p-16 border border-warm-border mb-4 shadow-sm">
            <div class="flex flex-col gap-5">
                <span class="self-start bg-[#E80070]/10 text-experian-magenta text-xs font-bold px-4 py-2 rounded-full uppercase tracking-wider flex items-center gap-2 border border-[#E80070]/20">
                    <svg class="w-4 h-4"><use href="#icon-help"></use></svg>
                    Habilitación Regional
                </span>
                <h1 class="text-4xl md:text-5xl lg:text-[3.65rem] font-extrabold text-warm-dark leading-tight tracking-tight">
                    Bienvenidos al<br><span class="text-experian-magenta">Squad Regional</span><br>de Salesforce
                </h1>
                <p class="text-[0.95rem] text-warm-medium leading-relaxed mt-2">
                    Nuestro equipo está dedicado a recibir las necesidades regionales para mejorar los procesos gestionados a través de Salesforce, con el fin de generar eficiencias a nivel organizacional, con soluciones prácticas y de alto impacto, generando valor, no solo desarrollando soluciones en Salesforce e integrándolas con otros sistemas, sino también evaluando la utilidad y beneficio para la compañía.
                </p>
            </div>
            
            <div class="relative overflow-hidden bg-gradient-to-b from-[#F4F7FB] to-white rounded-[20px] p-6 md:p-9 flex flex-col gap-6 border border-[#1D4F91]/10 shadow-[0_12px_30px_-10px_rgba(29,79,145,0.12)]">
                <div class="absolute top-0 left-0 right-0 h-[5px] bg-gradient-to-r from-experian-dark-blue via-experian-purple to-experian-magenta"></div>
                
                <div class="flex items-center gap-5 pb-4 border-b border-dashed border-warm-border relative z-10">
                    <div class="w-11 h-11 bg-gradient-to-br from-experian-dark-blue to-experian-purple rounded-xl flex items-center justify-center shrink-0 text-white shadow-[0_4px_10px_rgba(119,18,123,0.2)]">
                        <svg class="w-[1.35rem] h-[1.35rem]"><use href="#icon-check"></use></svg>
                    </div>
                    <div>
                        <h3 class="text-[1.15rem] font-bold text-warm-dark mb-1 tracking-tight">¿Qué necesitas hacer hoy?</h3>
                        <p class="text-[0.85rem] text-warm-medium leading-snug">Selecciona una opción para comenzar</p>
                    </div>
                </div>
                
                <div class="flex flex-col gap-3 relative z-10">
                    <a href="#card-title-1" class="hero-step bg-white border border-warm-border rounded-xl px-4 py-3.5 flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] hover:translate-x-1 hover:border-experian-purple hover:bg-[#FAFAFB] hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] cursor-pointer group">
                        <div class="w-9 h-9 flex items-center justify-center bg-[#77127B]/10 rounded-lg shrink-0 text-experian-purple transition-all duration-300 group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-3 group-hover:shadow-[0_4px_10px_rgba(119,18,123,0.3)]">
                            <svg class="w-5 h-5"><use href="#icon-file"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-0.5">Nueva necesidad o mejora</h4>
                            <p class="text-[0.75rem] text-warm-medium">Crear HU</p>
                        </div>
                    </a>
                    <a href="#card-title-2" class="hero-step bg-white border border-warm-border rounded-xl px-4 py-3.5 flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] hover:translate-x-1 hover:border-experian-purple hover:bg-[#FAFAFB] hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] cursor-pointer group">
                        <div class="w-9 h-9 flex items-center justify-center bg-[#77127B]/10 rounded-lg shrink-0 text-experian-purple transition-all duration-300 group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-3 group-hover:shadow-[0_4px_10px_rgba(119,18,123,0.3)]">
                            <svg class="w-5 h-5"><use href="#icon-wrench"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-0.5">Soporte o configuración</h4>
                            <p class="text-[0.75rem] text-warm-medium">Requerimiento</p>
                        </div>
                    </a>
                    <a href="#card-title-2" class="hero-step bg-white border border-warm-border rounded-xl px-4 py-3.5 flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] hover:translate-x-1 hover:border-experian-purple hover:bg-[#FAFAFB] hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] cursor-pointer group">
                        <div class="w-9 h-9 flex items-center justify-center bg-[#77127B]/10 rounded-lg shrink-0 text-experian-purple transition-all duration-300 group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-3 group-hover:shadow-[0_4px_10px_rgba(119,18,123,0.3)]">
                            <svg class="w-5 h-5"><use href="#icon-alert"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-0.5">Algo no funciona</h4>
                            <p class="text-[0.75rem] text-warm-medium">Crear incidente</p>
                        </div>
                    </a>
                    <a href="#card-title-3" class="hero-step bg-white border border-warm-border rounded-xl px-4 py-3.5 flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] hover:translate-x-1 hover:border-experian-purple hover:bg-[#FAFAFB] hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] cursor-pointer group">
                        <div class="w-9 h-9 flex items-center justify-center bg-[#77127B]/10 rounded-lg shrink-0 text-experian-purple transition-all duration-300 group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-3 group-hover:shadow-[0_4px_10px_rgba(119,18,123,0.3)]">
                            <svg class="w-5 h-5"><use href="#icon-key"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-0.5">Necesito acceso</h4>
                            <p class="text-[0.75rem] text-warm-medium">Solicitud acceso</p>
                        </div>
                    </a>                    
                    <a href="#nuestro-equipo" class="hero-step bg-white border border-warm-border rounded-xl px-4 py-3.5 flex items-center gap-4 transition-all duration-300 shadow-[0_2px_6px_rgba(0,0,0,0.02)] hover:translate-x-1 hover:border-experian-purple hover:bg-[#FAFAFB] hover:shadow-[0_4px_12px_rgba(119,18,123,0.08)] cursor-pointer group">
                        <div class="w-9 h-9 flex items-center justify-center bg-[#77127B]/10 rounded-lg shrink-0 text-experian-purple transition-all duration-300 group-hover:bg-experian-purple group-hover:text-white group-hover:scale-110 group-hover:-rotate-3 group-hover:shadow-[0_4px_10px_rgba(119,18,123,0.3)]">
                            <svg class="w-5 h-5"><use href="#icon-help"></use></svg>
                        </div>
                        <div>
                            <h4 class="text-[0.9rem] font-semibold text-warm-dark mb-0.5">No estoy seguro</h4>
                            <p class="text-[0.75rem] text-warm-medium">Contactar equipo</p>
                        </div>
                    </a>
                </div>
            </div>
        </section>

        <!-- Main Options Grid -->
        <main class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

            <!-- Card 1 -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 hover:-translate-y-1 hover:border-experian-light-blue hover:shadow-[0_15px_30px_-10px_rgba(139,126,116,0.12),0_0_0_1px_#426DA9] group" aria-labelledby="card-title-1">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[#426DA9]/10 text-experian-light-blue group-hover:bg-experian-light-blue group-hover:text-white group-hover:scale-105">
                            <svg class="w-5 h-5"><use href="#icon-file"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-warm-dark tracking-tight scroll-mt-28" id="card-title-1">Historia de Usuario</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 min-h-[66px] leading-relaxed">Crea y documenta requerimientos funcionales desde la perspectiva del usuario de negocio. Utiliza esta opción para nuevos requerimientos funcionales o ajuste en Salesforce.</p>
                    <ul class="flex flex-col gap-3 mb-8">
                        <li class="flex items-start gap-2.5 text-[0.85rem] leading-tight">
                            <span class="w-[18px] h-[18px] flex items-center justify-center bg-[#426DA9]/10 text-experian-light-blue rounded-full shrink-0 mt-0.5 transition-all duration-300 group-hover:scale-110 group-hover:bg-experian-light-blue group-hover:text-white">
                                <svg class="w-3 h-3"><use href="#icon-check"></use></svg>
                            </span>
                            Se aprueban a través de Jira - CCO Board.
                        </li>
                        <li class="flex items-start gap-2.5 text-[0.85rem] leading-tight">
                            <span class="w-[18px] h-[18px] flex items-center justify-center bg-[#426DA9]/10 text-experian-light-blue rounded-full shrink-0 mt-0.5 transition-all duration-300 group-hover:scale-110 group-hover:bg-experian-light-blue group-hover:text-white">
                                <svg class="w-3 h-3"><use href="#icon-check"></use></svg>
                            </span>
                            Requiere detalle del dolor/necesidad y criterios de aceptación.
                        </li>
                    </ul>
                </div>
                <a href="https://jira.experian.local/secure/CreateIssueDetails!init.jspa?pid=43596&issuetype=12200" target="_blank" class="flex items-center justify-center w-full px-4 py-3 text-[0.875rem] font-semibold rounded-xl cursor-pointer transition-all duration-300 no-underline border-[1.5px] border-experian-light-blue bg-white text-experian-light-blue gap-1.5 group-hover:bg-experian-light-blue group-hover:text-white group-hover:shadow-[0_4px_12px_rgba(0,0,0,0.05)]">
                    <span>Crear Historia</span>
                    <svg class="w-4 h-4"><use href="#icon-arrow"></use></svg>
                </a>
            </section>

            <!-- Card 2 -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 hover:-translate-y-1 hover:border-experian-purple hover:shadow-[0_15px_30px_-10px_rgba(139,126,116,0.12),0_0_0_1px_#77127B] group" aria-labelledby="card-title-2">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[#77127B]/10 text-experian-purple group-hover:bg-experian-purple group-hover:text-white group-hover:scale-105">
                            <svg class="w-5 h-5"><use href="#icon-wrench"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-warm-dark tracking-tight scroll-mt-28" id="card-title-2">Requerimiento Técnico</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 min-h-[66px] leading-relaxed">Utiliza esta opción cuando necesites registrar un requerimiento general que no implique un desarrollo inmediato.</p>
                    <ul class="flex flex-col gap-3 mb-8">
                        <li class="flex items-start gap-2.5 text-[0.85rem] leading-tight">
                            <span class="w-[18px] h-[18px] flex items-center justify-center bg-[#77127B]/10 text-experian-purple rounded-full shrink-0 mt-0.5 transition-all duration-300 group-hover:scale-110 group-hover:bg-experian-purple group-hover:text-white">
                                <svg class="w-3 h-3"><use href="#icon-check"></use></svg>
                            </span>
                            Registro general de necesidades técnicas o de soporte.
                        </li>
                        <li class="flex items-start gap-2.5 text-[0.85rem] leading-tight">
                            <span class="w-[18px] h-[18px] flex items-center justify-center bg-[#77127B]/10 text-experian-purple rounded-full shrink-0 mt-0.5 transition-all duration-300 group-hover:scale-110 group-hover:bg-experian-purple group-hover:text-white">
                                <svg class="w-3 h-3"><use href="#icon-check"></use></svg>
                            </span>
                            Para incidentes/bug utiliza la opción Bug dentro del board correspondiente.
                        </li>
                    </ul>
                </div>
                <a href="https://jira.experian.local/secure/CreateIssueDetails!init.jspa?pid=43596&issuetype=12201" target="_blank" class="flex items-center justify-center w-full px-4 py-3 text-[0.875rem] font-semibold rounded-xl cursor-pointer transition-all duration-300 no-underline border-[1.5px] border-experian-purple bg-white text-experian-purple gap-1.5 group-hover:bg-experian-purple group-hover:text-white group-hover:shadow-[0_4px_12px_rgba(0,0,0,0.05)]">
                    <span>Crear Req / Incidente</span>
                    <svg class="w-4 h-4"><use href="#icon-arrow"></use></svg>
                </a>
            </section>

            <!-- Card 3 -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 hover:-translate-y-1 hover:border-experian-magenta hover:shadow-[0_15px_30px_-10px_rgba(139,126,116,0.12),0_0_0_1px_#E80070] group" aria-labelledby="card-title-3">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[#E80070]/10 text-experian-magenta group-hover:bg-experian-magenta group-hover:text-white group-hover:scale-105">
                            <svg class="w-5 h-5"><use href="#icon-key"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-warm-dark tracking-tight scroll-mt-28" id="card-title-3">Solicitud de Acceso</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 min-h-[66px] leading-relaxed">Administración de usuarios. Utiliza esta opción si necesitas acceso a Salesforce o permisos adicionales.</p>
                    <ul class="flex flex-col gap-3 mb-8">
                        <li class="flex items-start gap-2.5 text-[0.85rem] leading-tight">
                            <span class="w-[18px] h-[18px] flex items-center justify-center bg-[#E80070]/10 text-experian-magenta rounded-full shrink-0 mt-0.5 transition-all duration-300 group-hover:scale-110 group-hover:bg-experian-magenta group-hover:text-white">
                                <svg class="w-3 h-3"><use href="#icon-check"></use></svg>
                            </span>
                            Tramitado 100% por SNOW (Service Now).
                        </li>
                        <li class="flex items-start gap-2.5 text-[0.85rem] leading-tight">
                            <span class="w-[18px] h-[18px] flex items-center justify-center bg-[#E80070]/10 text-experian-magenta rounded-full shrink-0 mt-0.5 transition-all duration-300 group-hover:scale-110 group-hover:bg-experian-magenta group-hover:text-white">
                                <svg class="w-3 h-3"><use href="#icon-check"></use></svg>
                            </span>
                            Requiere aprobación del Line Manager.
                        </li>
                    </ul>
                </div>
                <a href="https://experian.service-now.com/nav_to.do?uri=%2Fcom.glideapp.servicecatalog_category_view.do%3Fv%3D1%26sysparm_category%3De15706fc0a0a0aa7007fc21e1ab70c2f" target="_blank" class="flex items-center justify-center w-full px-4 py-3 text-[0.875rem] font-semibold rounded-xl cursor-pointer transition-all duration-300 no-underline border-[1.5px] border-experian-magenta bg-white text-experian-magenta gap-1.5 group-hover:bg-experian-magenta group-hover:text-white group-hover:shadow-[0_4px_12px_rgba(0,0,0,0.05)]">
                    <span>Solicitar en SNOW</span>
                    <svg class="w-4 h-4"><use href="#icon-arrow"></use></svg>
                </a>
            </section>

            <!-- Card 4 (Team Info) -->
            <section class="card bg-white border border-warm-border rounded-[18px] shadow-[0_4px_15px_-3px_rgba(139,126,116,0.04)] transition-all duration-300 flex flex-col justify-between p-7 hover:-translate-y-1 hover:border-experian-dark-blue hover:shadow-[0_15px_30px_-10px_rgba(139,126,116,0.12),0_0_0_1px_#1D4F91] group team-section scroll-mt-28" id="nuestro-equipo">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-[38px] h-[38px] rounded-[10px] flex items-center justify-center shrink-0 transition-all duration-300 bg-[#1D4F91]/10 text-experian-dark-blue group-hover:bg-experian-dark-blue group-hover:text-white group-hover:scale-105">
                            <svg class="w-5 h-5"><use href="#icon-rocket"></use></svg>
                        </div>
                        <h2 class="text-[1.15rem] font-bold text-experian-dark-blue tracking-tight">Conoce al Equipo</h2>
                    </div>
                    <p class="text-[0.875rem] text-warm-medium mb-6 leading-relaxed">Célula de desarrollo y soporte encargada del mantenimiento de la plataforma.</p>
                    
                    <div class="flex flex-col gap-2 mb-6">
                        <!-- Miembro 1 -->
                        <details class="team-member border border-warm-border rounded-lg bg-experian-warm-bg overflow-hidden transition-all duration-300 shrink-0 group/detail open:border-experian-dark-blue open:bg-white" name="team-accordion">
                            <summary class="flex items-center gap-2.5 p-2.5 cursor-pointer list-none outline-none select-none">
                                <div class="w-7 h-7 rounded-full bg-[#1D4F91]/15 text-experian-dark-blue font-bold text-[0.75rem] flex items-center justify-center uppercase shrink-0">AS</div>
                                <div class="flex flex-col leading-tight"><span class="text-[0.8rem] font-semibold">Ana Silva</span><span class="text-[0.7rem] text-warm-medium">SF Admin</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250">
                                    <svg class="w-3 h-3 stroke-[3]"><use href="#icon-arrow"></use></svg>
                                </span>
                            </summary>
                            <div class="px-2.5 pb-2.5 pt-1.5 pl-10 text-[0.75rem] text-warm-medium leading-relaxed border-t border-dashed border-warm-border">
                                <p>Contactar para: Administración general, gestión de accesos, roles, perfiles y soporte del día a día en LATAM.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=ana.silva@experian.com" class="inline-flex items-center gap-1.5 mt-2 font-semibold text-experian-dark-blue no-underline px-2.5 py-1.5 rounded-md bg-[#1D4F91]/10 transition-all duration-300 hover:bg-experian-dark-blue hover:text-white">
                                    <svg class="w-3.5 h-3.5"><use href="#icon-chat"></use></svg> Contactar
                                </a>
                            </div>
                        </details>
                        <!-- Miembro 2 -->
                        <details class="team-member border border-warm-border rounded-lg bg-experian-warm-bg overflow-hidden transition-all duration-300 shrink-0 group/detail open:border-experian-dark-blue open:bg-white" name="team-accordion">
                            <summary class="flex items-center gap-2.5 p-2.5 cursor-pointer list-none outline-none select-none">
                                <div class="w-7 h-7 rounded-full bg-[#1D4F91]/15 text-experian-dark-blue font-bold text-[0.75rem] flex items-center justify-center uppercase shrink-0">CP</div>
                                <div class="flex flex-col leading-tight"><span class="text-[0.8rem] font-semibold">Carlos Pérez</span><span class="text-[0.7rem] text-warm-medium">Lead Dev</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250">
                                    <svg class="w-3 h-3 stroke-[3]"><use href="#icon-arrow"></use></svg>
                                </span>
                            </summary>
                            <div class="px-2.5 pb-2.5 pt-1.5 pl-10 text-[0.75rem] text-warm-medium leading-relaxed border-t border-dashed border-warm-border">
                                <p>Contactar para: Desarrollo Apex, LWC, integraciones y flujos complejos de automatización.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=carlos.perez@experian.com" class="inline-flex items-center gap-1.5 mt-2 font-semibold text-experian-dark-blue no-underline px-2.5 py-1.5 rounded-md bg-[#1D4F91]/10 transition-all duration-300 hover:bg-experian-dark-blue hover:text-white">
                                    <svg class="w-3.5 h-3.5"><use href="#icon-chat"></use></svg> Contactar
                                </a>
                            </div>
                        </details>
                        <!-- Miembro 3 -->
                        <details class="team-member border border-warm-border rounded-lg bg-experian-warm-bg overflow-hidden transition-all duration-300 shrink-0 group/detail open:border-experian-dark-blue open:bg-white" name="team-accordion">
                            <summary class="flex items-center gap-2.5 p-2.5 cursor-pointer list-none outline-none select-none">
                                <div class="w-7 h-7 rounded-full bg-[#1D4F91]/15 text-experian-dark-blue font-bold text-[0.75rem] flex items-center justify-center uppercase shrink-0">MR</div>
                                <div class="flex flex-col leading-tight"><span class="text-[0.8rem] font-semibold">María Rodríguez</span><span class="text-[0.7rem] text-warm-medium">Product Owner</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250">
                                    <svg class="w-3 h-3 stroke-[3]"><use href="#icon-arrow"></use></svg>
                                </span>
                            </summary>
                            <div class="px-2.5 pb-2.5 pt-1.5 pl-10 text-[0.75rem] text-warm-medium leading-relaxed border-t border-dashed border-warm-border">
                                <p>Contactar para: Definición de roadmap, priorización del backlog de solicitudes y alineación estratégica.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=maria.rodriguez@experian.com" class="inline-flex items-center gap-1.5 mt-2 font-semibold text-experian-dark-blue no-underline px-2.5 py-1.5 rounded-md bg-[#1D4F91]/10 transition-all duration-300 hover:bg-experian-dark-blue hover:text-white">
                                    <svg class="w-3.5 h-3.5"><use href="#icon-chat"></use></svg> Contactar
                                </a>
                            </div>
                        </details>
                        <!-- Miembro 4 -->
                        <details class="team-member border border-warm-border rounded-lg bg-experian-warm-bg overflow-hidden transition-all duration-300 shrink-0 group/detail open:border-experian-dark-blue open:bg-white" name="team-accordion">
                            <summary class="flex items-center gap-2.5 p-2.5 cursor-pointer list-none outline-none select-none">
                                <div class="w-7 h-7 rounded-full bg-[#1D4F91]/15 text-experian-dark-blue font-bold text-[0.75rem] flex items-center justify-center uppercase shrink-0">JG</div>
                                <div class="flex flex-col leading-tight"><span class="text-[0.8rem] font-semibold">Juan Gómez</span><span class="text-[0.7rem] text-warm-medium">QA Engineer</span></div>
                                <span class="details-arrow ml-auto text-warm-medium flex items-center transition-transform duration-250">
                                    <svg class="w-3 h-3 stroke-[3]"><use href="#icon-arrow"></use></svg>
                                </span>
                            </summary>
                            <div class="px-2.5 pb-2.5 pt-1.5 pl-10 text-[0.75rem] text-warm-medium leading-relaxed border-t border-dashed border-warm-border">
                                <p>Contactar para: Pruebas automatizadas, reporte de bugs, aseguramiento de calidad de desarrollos.</p>
                                <a href="msteams://teams.microsoft.com/l/chat/0/0?users=juan.gomez@experian.com" class="inline-flex items-center gap-1.5 mt-2 font-semibold text-experian-dark-blue no-underline px-2.5 py-1.5 rounded-md bg-[#1D4F91]/10 transition-all duration-300 hover:bg-experian-dark-blue hover:text-white">
                                    <svg class="w-3.5 h-3.5"><use href="#icon-chat"></use></svg> Contactar
                                </a>
                            </div>
                        </details>
                    </div>
                </div>
            </section>
        </main>

        <!-- Equipo Completo Grid -->
        <section class="flex flex-col gap-8 mt-4">
            <div class="flex flex-col gap-1 border-b border-warm-border pb-4">
                <h2 class="text-2xl font-bold text-experian-dark-blue">Conoce a nuestro equipo</h2>
                <p class="text-[0.9rem] text-warm-medium">El equipo de expertos dedicado a la administración, desarrollo y evolución de la plataforma Salesforce LATAM.</p>
            </div>
            <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
                <!-- AS -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-sm p-6 flex flex-col items-center justify-between transition-all duration-300 hover:-translate-y-1 hover:border-experian-dark-blue hover:shadow-[0_10px_20px_-5px_rgba(139,126,116,0.12)]">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-gradient-to-br from-experian-dark-blue to-[#8ea7c8] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">AS</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Ana Silva</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Salesforce Administrator</p>
                    <div class="w-full flex flex-col gap-1.5 border-t border-warm-border pt-4">
                        <a href="mailto:ana.silva@experian.com" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-email"></use></svg><span>ana.silva@experian.com</span>
                        </a>
                        <a href="#chat-asilva" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-chat"></use></svg><span>@asilva</span>
                        </a>
                    </div>
                </div>
                <!-- CP -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-sm p-6 flex flex-col items-center justify-between transition-all duration-300 hover:-translate-y-1 hover:border-experian-dark-blue hover:shadow-[0_10px_20px_-5px_rgba(139,126,116,0.12)]">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-gradient-to-br from-experian-dark-blue to-[#8ea7c8] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">CP</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Carlos Pérez</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Lead Developer</p>
                    <div class="w-full flex flex-col gap-1.5 border-t border-warm-border pt-4">
                        <a href="mailto:carlos.perez@experian.com" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-email"></use></svg><span>carlos.perez@experian.com</span>
                        </a>
                        <a href="#chat-cperez" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-chat"></use></svg><span>@cperez</span>
                        </a>
                    </div>
                </div>
                <!-- MR -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-sm p-6 flex flex-col items-center justify-between transition-all duration-300 hover:-translate-y-1 hover:border-experian-dark-blue hover:shadow-[0_10px_20px_-5px_rgba(139,126,116,0.12)]">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-gradient-to-br from-experian-dark-blue to-[#8ea7c8] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">MR</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">María Rodríguez</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">Product Owner</p>
                    <div class="w-full flex flex-col gap-1.5 border-t border-warm-border pt-4">
                        <a href="mailto:maria.rodriguez@experian.com" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-email"></use></svg><span>maria.rodriguez@experian.com</span>
                        </a>
                        <a href="#chat-mrodriguez" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-chat"></use></svg><span>@mrodriguez</span>
                        </a>
                    </div>
                </div>
                <!-- JG -->
                <div class="team-contact-card bg-white border border-warm-border rounded-[18px] shadow-sm p-6 flex flex-col items-center justify-between transition-all duration-300 hover:-translate-y-1 hover:border-experian-dark-blue hover:shadow-[0_10px_20px_-5px_rgba(139,126,116,0.12)]">
                    <div class="w-16 h-16 rounded-full flex items-center justify-center text-[1.3rem] font-bold mb-4 text-white bg-gradient-to-br from-experian-dark-blue to-[#8ea7c8] shadow-[0_4px_10px_rgba(0,0,0,0.05)]">JG</div>
                    <h3 class="text-[1rem] font-semibold mb-1 text-warm-dark">Juan Gómez</h3>
                    <p class="text-[0.8rem] font-medium text-warm-medium mb-4">QA Automation Eng.</p>
                    <div class="w-full flex flex-col gap-1.5 border-t border-warm-border pt-4">
                        <a href="mailto:juan.gomez@experian.com" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-email"></use></svg><span>juan.gomez@experian.com</span>
                        </a>
                        <a href="#chat-jgomez" class="flex items-center justify-center gap-1.5 text-[0.775rem] text-warm-medium no-underline transition-all duration-300 hover:text-experian-dark-blue">
                            <svg class="w-3 h-3 shrink-0"><use href="#icon-chat"></use></svg><span>@jgomez</span>
                        </a>
                    </div>
                </div>
            </div>
        </section>

        <script>
            (function () {
                const experianContainer = document.querySelector('.experian-container');
                if (!experianContainer) return;

                experianContainer.addEventListener('click', e => {
                    const step = e.target.closest('.hero-step');
                    if (!step) return;

                    const targetId = step.getAttribute('href');
                    if (targetId && targetId.startsWith('#')) {
                        const targetElement = document.querySelector(targetId);
                        if (targetElement) {
                            const cardContainer = targetElement.closest('.card') ||
                                (targetElement.classList.contains('team-section') ? targetElement : null) ||
                                document.querySelector(targetId);
                            if (cardContainer) {
                                cardContainer.classList.remove('highlight-focus');
                                document.body.classList.remove('is-pulsing');
                                void cardContainer.offsetWidth; // Reflow
                                cardContainer.classList.add('highlight-focus');
                                document.body.classList.add('is-pulsing');

                                setTimeout(() => {
                                    cardContainer.classList.remove('highlight-focus');
                                    document.body.classList.remove('is-pulsing');
                                }, 2500);
                            }
                        }
                    }
                });
            })();
        </script>
    </div>
</div>"""
