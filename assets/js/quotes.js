/**
 * ==============================================================================
 * AerospaceEngineering Portal — Motivational & Witty Quotes Engine
 * File: assets/js/quotes.js
 *
 * Curated catalog of legendary quotes from pioneers of aerodynamics,
 * astronautics, astrophysics, orbital mechanics, and space exploration.
 *
 * Features:
 * - 16 curated quotes with authentic English and Spanish translations.
 * - Author achievements and rich aerospace/pedagogical context pills.
 * - Dynamic container injection via `initAerospaceQuote(containerSelector, options)`.
 * - Full bi-directional synchronization with `AE_I18N` and theme system.
 * - Built-in responsive styles, clipboard copying, and daily/random rotation modes.
 * ==============================================================================
 */

(function (root, factory) {
  'use strict';
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    var exports = factory();
    root.AE_QUOTES = exports;
    root.initAerospaceQuote = exports.initAerospaceQuote;
  }
})(typeof window !== 'undefined' ? window : this, function () {
  'use strict';

  /* ============================================================================
   * 1. CATALOG OF AEROSPACE MOTIVATIONAL & WITTY QUOTES
   * ============================================================================ */
  var AEROSPACE_QUOTES = [
    {
      id: 'von-karman',
      author: 'Theodore von Kármán',
      field: {
        en: 'Aerodynamics',
        es: 'Aerodinámica'
      },
      badgeIcon: '🌪️',
      role: {
        en: 'Pioneer of Modern Aerodynamics & Co-founder of JPL / GALCIT',
        es: 'Padre de la aerodinámica moderna y cofundador del JPL / GALCIT'
      },
      quote: {
        en: 'Scientists discover the world that exists; engineers create the world that never was.',
        es: 'Los científicos descubren el mundo que ya existe; los ingenieros crean el mundo que nunca ha existido.'
      },
      context: {
        en: 'Formulated boundary layer theory, supersonic wave drag laws, and the iconic Kármán vortex street shedding frequency.',
        es: 'Formuló la teoría de la capa límite, leyes de resistencia supersónica y la célebre calle de vórtices de Kármán.'
      }
    },
    {
      id: 'tsiolkovsky',
      author: 'Konstantin Tsiolkovsky',
      field: {
        en: 'Astronautics',
        es: 'Astronáutica'
      },
      badgeIcon: '🚀',
      role: {
        en: 'Founding Father of Theoretical Astronautics & Rocket Dynamics',
        es: 'Padre fundador de la astronáutica teórica y la dinámica de cohetes'
      },
      quote: {
        en: 'The Earth is the cradle of humanity, but one cannot live in a cradle forever.',
        es: 'La Tierra es la cuna de la humanidad, pero no se puede vivir en la cuna para siempre.'
      },
      context: {
        en: 'Derived the ideal rocket equation (Δv = ve · ln(m₀/mf)) in 1903, decades before the first liquid-propellant flight.',
        es: 'Formuló en 1903 la ecuación fundamental del cohete ideal (Δv = ve · ln(m₀/mf)) décadas antes del primer vuelo a propulsión líquida.'
      }
    },
    {
      id: 'sagan',
      author: 'Carl Sagan',
      field: {
        en: 'Astrophysics',
        es: 'Astrofísica'
      },
      badgeIcon: '🪐',
      role: {
        en: 'Astrophysicist, Cosmologist & Architect of the Voyager Golden Record',
        es: 'Astrofísico, cosmólogo y diseñador del Disco de Oro de las Voyager'
      },
      quote: {
        en: 'Somewhere, something incredible is waiting to be known.',
        es: 'En algún lugar, algo increíble está esperando a ser conocido.'
      },
      context: {
        en: 'Championed interplanetary robotic exploration (Mariner, Viking, Voyager) and popularized humanity\'s humble cosmic perspective.',
        es: 'Impulsó la exploración robótica interplanetaria (Mariner, Viking, Voyager) y nos recordó que somos polvo de estrellas.'
      }
    },
    {
      id: 'feynman',
      author: 'Richard Feynman',
      field: {
        en: 'Theoretical Physics',
        es: 'Física Teórica'
      },
      badgeIcon: '⚛️',
      role: {
        en: 'Nobel Laureate in Physics & Rogers Commission Investigator',
        es: 'Premio Nobel de Física e investigador clave de la Comisión Rogers'
      },
      quote: {
        en: 'What I cannot create, I do not understand.',
        es: 'Lo que no puedo crear, no lo entiendo.'
      },
      context: {
        en: 'Found on his Caltech blackboard at his death; famously cracked the Space Shuttle Challenger O-ring failure with a glass of ice water.',
        es: 'Inscrito en su pizarra de Caltech al fallecer; demostró el fallo del transbordador Challenger sumergiendo una junta tórica en agua con hielo.'
      }
    },
    {
      id: 'johnson-katherine',
      author: 'Katherine Johnson',
      field: {
        en: 'NASA Orbital Mechanics',
        es: 'Mecánica Orbital NASA'
      },
      badgeIcon: '📐',
      role: {
        en: 'NASA Lead Mathematician for Project Mercury & Apollo Trajectories',
        es: 'Matemática pionera de la NASA para trayectorias de Project Mercury y Apolo'
      },
      quote: {
        en: 'Like what you do, and then you will do your best.',
        es: 'Disfruta lo que haces, y entonces darás lo mejor de ti.'
      },
      context: {
        en: 'Manually verified the orbital rendezvous and re-entry equations for John Glenn\'s Friendship 7 and Apollo 11.',
        es: 'Calculó y verificó manualmente las trayectorias orbitales de John Glenn (Friendship 7) y el acoplamiento lunar del Apolo 11.'
      }
    },
    {
      id: 'johnson-kelly',
      author: 'Kelly Johnson',
      field: {
        en: 'Aircraft Design',
        es: 'Diseño Aeronáutico'
      },
      badgeIcon: '🦅',
      role: {
        en: 'Legendary Founder & Director of Lockheed Skunk Works',
        es: 'Legendario fundador y director de Lockheed Skunk Works'
      },
      quote: {
        en: 'Be quick, be quiet, be on time.',
        es: 'Sé rápido, sé discreto, llega a tiempo.'
      },
      context: {
        en: 'Masterminded the Mach 3.3+ SR-71 Blackbird, U-2 reconnaissance aircraft, and P-38 Lightning under his 14 rules of rapid engineering.',
        es: 'Diseñó el mítico avión supersónico SR-71 Blackbird (Mach 3.3+), el U-2 y el P-38, creador de las 14 reglas de ingeniería ágil.'
      }
    },
    {
      id: 'von-braun',
      author: 'Wernher von Braun',
      field: {
        en: 'Rocket Propulsion',
        es: 'Propulsión Cohete'
      },
      badgeIcon: '🛰️',
      role: {
        en: 'Chief Architect of the Saturn V Moon Rocket & Director of NASA MSFC',
        es: 'Arquitecto principal del cohete lunar Saturno V y director de NASA MSFC'
      },
      quote: {
        en: 'Research is what I\'m doing when I don\'t know what I\'m doing.',
        es: 'Investigar es lo que hago cuando no sé lo que estoy haciendo.'
      },
      context: {
        en: 'Engineered the multi-stage Saturn V rocket producing 34.5 MN of liftoff thrust to safely deliver Apollo crews to the lunar surface.',
        es: 'Lideró la ingeniería del Saturno V, con 34.5 MN de empuje en despegue, el lanzador más potente que llevó al ser humano a la Luna.'
      }
    },
    {
      id: 'armstrong',
      author: 'Neil Armstrong',
      field: {
        en: 'Flight Test & Spaceflight',
        es: 'Ensayos en Vuelo y Espacio'
      },
      badgeIcon: '🌕',
      role: {
        en: 'Apollo 11 Commander, First Human on the Moon & X-15 Research Pilot',
        es: 'Comandante del Apolo 11, primer humano en la Luna y piloto de pruebas del X-15'
      },
      quote: {
        en: 'Mystery creates wonder and wonder is the basis of man\'s desire to understand.',
        es: 'El misterio engendra asombro, y el asombro es la base del deseo humano de comprender.'
      },
      context: {
        en: 'Manually piloted the Lunar Module Eagle over a boulder field to land safely on Mare Tranquillitatis with only 25 seconds of fuel remaining.',
        es: 'Asumió el control manual del módulo lunar Eagle sobre un campo de rocas en el Mar de la Tranquilidad con solo 25 segundos de combustible.'
      }
    },
    {
      id: 'noether',
      author: 'Emmy Noether',
      field: {
        en: 'Mathematical Physics',
        es: 'Física Matemática'
      },
      badgeIcon: '🌌',
      role: {
        en: 'Preeminent Mathematician & Discoverer of Noether\'s Symmetries Theorem',
        es: 'Ilustre matemática y descubridora del Teorema de Noether'
      },
      quote: {
        en: 'My methods are really methods of working and thinking; this is why they have crept in everywhere anonymously.',
        es: 'Mis métodos son realmente métodos de trabajar y pensar; por eso se han introducido en todas partes de forma anónima.'
      },
      context: {
        en: 'Proved that continuous symmetries of action generate fundamental conservation laws (energy, linear momentum, and angular momentum).',
        es: 'Demostró que toda simetría continua de la acción engendra una ley de conservación (tiempo → energía, rotación → momento angular).'
      }
    },
    {
      id: 'da-vinci',
      author: 'Leonardo da Vinci',
      field: {
        en: 'Aviation Visionary',
        es: 'Visionario del Vuelo'
      },
      badgeIcon: '🕊️',
      role: {
        en: 'Renaissance Polymath & Pioneer of Fluid Vortices and Avian Flight',
        es: 'Polímata del Renacimiento y pionero del estudio de vórtices y vuelo aviar'
      },
      quote: {
        en: 'Once you have tasted flight, you will forever walk the earth with your eyes turned skyward, for there you have been, and there you will always long to return.',
        es: 'Una vez que hayas probado el vuelo, caminarás por la tierra con la mirada vuelta hacia el cielo, pues allí has estado y allí siempre desearás volver.'
      },
      context: {
        en: 'Authored the Codex on the Flight of Birds in 1505, pioneering aerodynamic lift analysis, gliding wing mechanics, and aerial screws.',
        es: 'Redactó en 1505 el Códice sobre el Vuelo de las Aves, conceptualizando la sustentación, alas planeadoras y el tornillo aéreo.'
      }
    },
    {
      id: 'hamilton',
      author: 'Margaret Hamilton',
      field: {
        en: 'Apollo Flight Software',
        es: 'Software de Vuelo Apolo'
      },
      badgeIcon: '💻',
      role: {
        en: 'Director of the Apollo Flight Software Division at MIT Instrumentation Lab',
        es: 'Directora de Ingeniería de Software del MIT para el Programa Apolo'
      },
      quote: {
        en: 'There was no choice but to be pioneers; no time to be beginners.',
        es: 'No había otra opción que ser pioneros; no había tiempo para ser principiantes.'
      },
      context: {
        en: 'Architected the priority-based asynchronous flight operating system that safely handled 1201/1202 radar cpu overload during Apollo 11 touchdown.',
        es: 'Creó el sistema operativo de vuelo asíncrono por prioridades que superó la sobrecarga del radar durante el alunizaje del Apolo 11.'
      }
    },
    {
      id: 'korolev',
      author: 'Sergei Korolev',
      field: {
        en: 'Space Systems Engineering',
        es: 'Ingeniería de Sistemas Espaciales'
      },
      badgeIcon: '🛰️',
      role: {
        en: 'Legendary Soviet Chief Designer & Architect of Sputnik 1 and Vostok 1',
        es: 'Mítico Diseñador Jefe del Programa Espacial Soviético (Sputnik 1 y Vostok 1)'
      },
      quote: {
        en: 'The simpler a design is, the less likely it is to fail. Complexity is the enemy of reliability.',
        es: 'Cuanto más simple es un diseño, menos probable es que falle. La complejidad es el enemigo de la fiabilidad.'
      },
      context: {
        en: 'The brilliant leader who launched the Space Age with Sputnik (1957) and sent Yuri Gagarin as the first human into orbit (1961).',
        es: 'El genial Diseñador Jefe que inauguró la era espacial con el Sputnik 1 y puso al primer ser humano en órbita en 1961.'
      }
    },
    {
      id: 'goddard',
      author: 'Robert H. Goddard',
      field: {
        en: 'Liquid Rocketry',
        es: 'Cohetería Líquida'
      },
      badgeIcon: '🔥',
      role: {
        en: 'Father of Modern Liquid-Fueled Rocketry & Gyroscopic Thrust Control',
        es: 'Padre de la cohetería de propergol líquido y guiado giroscópico'
      },
      quote: {
        en: 'It is difficult to say what is impossible, for the dream of yesterday is the hope of today and the reality of tomorrow.',
        es: 'Es difícil decir qué es imposible, pues el sueño de ayer es la esperanza de hoy y la realidad de mañana.'
      },
      context: {
        en: 'Constructed and successfully launched the world\'s first liquid-propellant rocket (LOX and gasoline) on March 16, 1926.',
        es: 'Construyó y lanzó el primer cohete de propergol líquido del mundo (oxígeno líquido y gasolina) el 16 de marzo de 1926.'
      }
    },
    {
      id: 'kranz',
      author: 'Gene Kranz',
      field: {
        en: 'Flight Operations & Mission Control',
        es: 'Operaciones de Vuelo y Control'
      },
      badgeIcon: '🎙️',
      role: {
        en: 'Legendary NASA Chief Flight Director (Apollo 11, Apollo 13)',
        es: 'Legendario Director de Vuelo de la NASA (Apolo 11 y Apolo 13)'
      },
      quote: {
        en: 'Tough and competent. From this day forward, Flight Control will be known by two words: tough and competent.',
        es: 'Exigentes y competentes. A partir de hoy, Control de Vuelo se definirá con dos palabras: exigentes y competentes.'
      },
      context: {
        en: 'Delivered the iconic Kranz Dictum following Apollo 1 and masterminded the mission control team that saved the Apollo 13 crew.',
        es: 'Proclamó el célebre Dictum de Kranz tras el Apolo 1 y lideró el equipo de control de misión que salvó a la tripulación del Apolo 13.'
      }
    },
    {
      id: 'lamarr',
      author: 'Hedy Lamarr',
      field: {
        en: 'Aerospace Communications',
        es: 'Telecomunicaciones Aeroespaciales'
      },
      badgeIcon: '📡',
      role: {
        en: 'Inventor of Frequency-Hopping Spread Spectrum & Telecom Pioneer',
        es: 'Inventora de las comunicaciones por salto de frecuencia y telecomunicaciones'
      },
      quote: {
        en: 'Hope and curiosity about the future seemed better than guarantees from the past.',
        es: 'La esperanza y la curiosidad por el futuro parecían mejores que las garantías del pasado.'
      },
      context: {
        en: 'Patented spread-spectrum frequency hopping in 1942, establishing the theoretical foundations for modern aerospace telemetry, GPS, and Wi-Fi.',
        es: 'Patentó el salto de frecuencia en 1942, sentando las bases teóricas para la telemetría espacial, el GPS militar y el Wi-Fi moderno.'
      }
    },
    {
      id: 'rutan',
      author: 'Burt Rutan',
      field: {
        en: 'Experimental Flight & Composites',
        es: 'Vuelo Experimental y Composites'
      },
      badgeIcon: '🛸',
      role: {
        en: 'Visionary Aircraft Designer & Ansari X-Prize Winner with SpaceShipOne',
        es: 'Visionario diseñador aeronáutico y ganador del Ansari X-Prize con SpaceShipOne'
      },
      quote: {
        en: 'If you don\'t take risks, you can\'t create breakthroughs. Innovation doesn\'t occur at the center of the road.',
        es: 'Si no tomas riesgos, no puedes lograr avances disruptivos. La innovación no ocurre en el centro del camino.'
      },
      context: {
        en: 'Designed Voyager (first unrefueled nonstop round-the-world flight in 1986) and SpaceShipOne (first private crewed suborbital spacecraft in 2004).',
        es: 'Diseñó el avión Voyager (vuelta al mundo sin escalas en 1986) y SpaceShipOne (primer vuelo espacial tripulado privado en 2004).'
      }
    }
  ];

  /* ============================================================================
   * 2. STYLESHEET INJECTION (SCOPED, LIGHT/DARK COMPATIBLE)
   * ============================================================================ */
  var STYLE_ELEMENT_ID = 'ae-quotes-engine-styles';

  function ensureStylesInjected() {
    if (typeof document === 'undefined') return;
    if (document.getElementById(STYLE_ELEMENT_ID)) return;

    var css = [
      '/* ============================================================',
      '   AEROSPACE QUOTES ENGINE STYLES',
      '   ============================================================ */',
      '.ae-quote-card {',
      '  position: relative;',
      '  display: flex;',
      '  flex-direction: column;',
      '  gap: 14px;',
      '  padding: 24px 28px;',
      '  border-radius: var(--radius-lg, 18px);',
      '  background: var(--bg-card, rgba(15, 23, 42, 0.70));',
      '  backdrop-filter: blur(16px) saturate(1.4);',
      '  -webkit-backdrop-filter: blur(16px) saturate(1.4);',
      '  border: 1px solid var(--border-card, rgba(255, 255, 255, 0.10));',
      '  box-shadow: var(--shadow-card, 0 10px 30px rgba(0, 0, 0, 0.35));',
      '  transition: transform var(--transition-medium, 0.3s ease),',
      '              box-shadow var(--transition-medium, 0.3s ease),',
      '              border-color var(--transition-medium, 0.3s ease);',
      '  overflow: hidden;',
      '  box-sizing: border-box;',
      '  margin: 16px 0;',
      '}',
      '.ae-quote-card:hover {',
      '  border-color: rgba(6, 182, 212, 0.45);',
      '  box-shadow: 0 12px 36px rgba(6, 182, 212, 0.15), var(--shadow-card, 0 10px 30px rgba(0,0,0,0.35));',
      '}',
      '.ae-quote-card::before {',
      '  content: "";',
      '  position: absolute;',
      '  top: 0;',
      '  left: 0;',
      '  width: 4px;',
      '  height: 100%;',
      '  background: linear-gradient(180deg, var(--accent-fluid, #06b6d4) 0%, var(--accent-maths, #6366f1) 100%);',
      '  border-radius: 4px 0 0 4px;',
      '}',
      '.ae-quote-header {',
      '  display: flex;',
      '  align-items: center;',
      '  justify-content: space-between;',
      '  gap: 12px;',
      '  flex-wrap: wrap;',
      '}',
      '.ae-quote-badges {',
      '  display: flex;',
      '  align-items: center;',
      '  gap: 8px;',
      '  flex-wrap: wrap;',
      '}',
      '.ae-quote-badge {',
      '  display: inline-flex;',
      '  align-items: center;',
      '  gap: 6px;',
      '  padding: 4px 10px;',
      '  border-radius: 9999px;',
      '  font-size: 0.76rem;',
      '  font-weight: 600;',
      '  letter-spacing: 0.03em;',
      '  text-transform: uppercase;',
      '  background: rgba(6, 182, 212, 0.12);',
      '  color: var(--accent-fluid, #06b6d4);',
      '  border: 1px solid rgba(6, 182, 212, 0.25);',
      '}',
      '.ae-quote-badge-alt {',
      '  background: rgba(99, 102, 241, 0.12);',
      '  color: var(--accent-maths, #818cf8);',
      '  border: 1px solid rgba(99, 102, 241, 0.25);',
      '}',
      '.ae-quote-actions {',
      '  display: flex;',
      '  align-items: center;',
      '  gap: 6px;',
      '  margin-left: auto;',
      '}',
      '.ae-quote-btn {',
      '  position: relative;',
      '  display: inline-flex;',
      '  align-items: center;',
      '  justify-content: center;',
      '  width: 32px;',
      '  height: 32px;',
      '  border-radius: var(--radius-sm, 8px);',
      '  background: var(--bg-input, rgba(255, 255, 255, 0.06));',
      '  border: 1px solid var(--border-subtle, rgba(255, 255, 255, 0.10));',
      '  color: var(--text-secondary, #94a3b8);',
      '  cursor: pointer;',
      '  transition: all var(--transition-fast, 0.2s ease);',
      '  padding: 0;',
      '}',
      '.ae-quote-btn:hover {',
      '  background: var(--accent-fluid, #06b6d4);',
      '  color: #ffffff;',
      '  border-color: var(--accent-fluid, #06b6d4);',
      '  transform: scale(1.05);',
      '}',
      '.ae-quote-btn:active {',
      '  transform: scale(0.95);',
      '}',
      '.ae-quote-btn svg {',
      '  width: 15px;',
      '  height: 15px;',
      '  fill: none;',
      '  stroke: currentColor;',
      '  stroke-width: 2;',
      '  stroke-linecap: round;',
      '  stroke-linejoin: round;',
      '}',
      '.ae-quote-copied-tooltip {',
      '  position: absolute;',
      '  bottom: calc(100% + 6px);',
      '  right: 0;',
      '  background: #10b981;',
      '  color: #ffffff;',
      '  font-size: 0.72rem;',
      '  font-weight: 600;',
      '  padding: 3px 8px;',
      '  border-radius: 4px;',
      '  opacity: 0;',
      '  pointer-events: none;',
      '  transition: opacity 0.2s ease, transform 0.2s ease;',
      '  transform: translateY(4px);',
      '  white-space: nowrap;',
      '  z-index: 10;',
      '}',
      '.ae-quote-copied-tooltip.visible {',
      '  opacity: 1;',
      '  transform: translateY(0);',
      '}',
      '.ae-quote-body {',
      '  position: relative;',
      '  margin: 0;',
      '  padding: 0;',
      '  display: flex;',
      '  align-items: flex-start;',
      '  gap: 6px;',
      '}',
      '.ae-quote-mark {',
      '  font-family: Georgia, "Times New Roman", serif;',
      '  font-size: 2.2rem;',
      '  line-height: 1;',
      '  color: var(--accent-fluid, #06b6d4);',
      '  opacity: 0.6;',
      '  user-select: none;',
      '}',
      '.ae-quote-mark-open {',
      '  margin-top: -6px;',
      '}',
      '.ae-quote-text {',
      '  flex: 1;',
      '  margin: 0;',
      '  font-size: 1.08rem;',
      '  font-style: italic;',
      '  line-height: 1.65;',
      '  color: var(--text-primary, #f1f5f9);',
      '  font-weight: 400;',
      '  letter-spacing: -0.01em;',
      '  transition: opacity 0.25s ease;',
      '}',
      '.ae-quote-footer {',
      '  display: flex;',
      '  align-items: flex-end;',
      '  justify-content: space-between;',
      '  gap: 16px;',
      '  flex-wrap: wrap;',
      '  padding-top: 10px;',
      '  border-top: 1px dashed var(--border-subtle, rgba(255, 255, 255, 0.08));',
      '}',
      '.ae-quote-author-info {',
      '  display: flex;',
      '  flex-direction: column;',
      '  gap: 3px;',
      '  min-width: 220px;',
      '  flex: 1;',
      '}',
      '.ae-quote-author-name {',
      '  font-weight: 700;',
      '  font-size: 0.98rem;',
      '  color: var(--text-primary, #f1f5f9);',
      '  display: flex;',
      '  align-items: center;',
      '  gap: 6px;',
      '}',
      '.ae-quote-author-role {',
      '  font-size: 0.82rem;',
      '  color: var(--text-secondary, #94a3b8);',
      '  line-height: 1.4;',
      '}',
      '.ae-quote-context-pill {',
      '  display: flex;',
      '  align-items: center;',
      '  gap: 8px;',
      '  padding: 6px 12px;',
      '  border-radius: var(--radius-sm, 8px);',
      '  background: var(--bg-glass, rgba(255, 255, 255, 0.04));',
      '  border: 1px solid var(--border-subtle, rgba(255, 255, 255, 0.06));',
      '  font-size: 0.78rem;',
      '  color: var(--text-muted, #64748b);',
      '  max-width: 480px;',
      '  line-height: 1.4;',
      '}',
      '.ae-quote-context-icon {',
      '  flex-shrink: 0;',
      '  font-size: 1rem;',
      '}',
      '.ae-quote-fade {',
      '  animation: aeQuoteFadeIn 0.35s ease forwards;',
      '}',
      '@keyframes aeQuoteFadeIn {',
      '  from { opacity: 0; transform: translateY(6px); }',
      '  to { opacity: 1; transform: translateY(0); }',
      '}',
      '@media (max-width: 640px) {',
      '  .ae-quote-card { padding: 18px 20px; gap: 12px; }',
      '  .ae-quote-text { font-size: 0.98rem; }',
      '  .ae-quote-footer { flex-direction: column; align-items: flex-start; gap: 10px; }',
      '  .ae-quote-context-pill { max-width: 100%; }',
      '}'
    ].join('\n');

    var styleEl = document.createElement('style');
    styleEl.id = STYLE_ELEMENT_ID;
    styleEl.type = 'text/css';
    styleEl.appendChild(document.createTextNode(css));
    document.head.appendChild(styleEl);
  }

  /* ============================================================================
   * 3. I18N DETECTION & SYNCHRONIZATION HELPERS
   * ============================================================================ */
  var currentForcedLang = null;
  var listenersRegistered = false;
  var activeInstances = [];

  function normalizeLang(lang) {
    if (!lang || typeof lang !== 'string') return 'en';
    var lower = lang.toLowerCase().trim();
    return lower.indexOf('es') === 0 ? 'es' : 'en';
  }

  function detectCurrentLanguage() {
    if (currentForcedLang) {
      return normalizeLang(currentForcedLang);
    }

    // 1. Check window.AE_I18N if defined
    if (typeof window !== 'undefined' && window.AE_I18N) {
      var i18n = window.AE_I18N;
      if (typeof i18n.getLanguage === 'function') {
        var res = i18n.getLanguage();
        if (res) return normalizeLang(res);
      }
      if (i18n.currentLanguage) return normalizeLang(i18n.currentLanguage);
      if (i18n.lang) return normalizeLang(i18n.lang);
      if (typeof i18n.getLocale === 'function') {
        var loc = i18n.getLocale();
        if (loc) return normalizeLang(loc);
      }
    }

    // 2. Check HTML lang attribute
    if (typeof document !== 'undefined' && document.documentElement) {
      var htmlLang = document.documentElement.getAttribute('lang') || document.documentElement.lang;
      if (htmlLang) return normalizeLang(htmlLang);
    }

    // 3. Check localStorage
    if (typeof localStorage !== 'undefined') {
      try {
        var stored = localStorage.getItem('ae_lang') ||
                     localStorage.getItem('ae_language') ||
                     localStorage.getItem('aero-portal-lang') ||
                     localStorage.getItem('lang');
        if (stored) return normalizeLang(stored);
      } catch (e) {}
    }

    // 4. Check navigator
    if (typeof navigator !== 'undefined' && navigator.language) {
      return normalizeLang(navigator.language);
    }

    // Default to English (primary portal language)
    return 'en';
  }

  function notifyLanguageChanged(newLang) {
    var lang = normalizeLang(newLang || detectCurrentLanguage());
    for (var i = 0; i < activeInstances.length; i++) {
      try {
        activeInstances[i].updateLanguage(lang);
      } catch (err) {
        if (typeof console !== 'undefined') console.error('AE_QUOTES: update error', err);
      }
    }
  }

  function setupGlobalLanguageListeners() {
    if (listenersRegistered || typeof window === 'undefined') return;
    listenersRegistered = true;

    // A. Listen for standard CustomEvents on both document and window
    var eventNames = [
      'ae:languageChange',
      'ae_language_change',
      'languagechange',
      'ae:lang',
      'aero:language'
    ];
    eventNames.forEach(function (eventName) {
      var handler = function (evt) {
        var lang = (evt && evt.detail && (evt.detail.lang || evt.detail.language)) || detectCurrentLanguage();
        notifyLanguageChanged(lang);
      };
      window.addEventListener(eventName, handler);
      if (typeof document !== 'undefined') {
        document.addEventListener(eventName, handler);
      }
    });

    // B. Hook window.AE_I18N if subscription API is provided
    if (window.AE_I18N) {
      if (typeof window.AE_I18N.onLanguageChange === 'function') {
        window.AE_I18N.onLanguageChange(function (lang) {
          notifyLanguageChanged(lang);
        });
      } else if (typeof window.AE_I18N.subscribe === 'function') {
        window.AE_I18N.subscribe(function (lang) {
          notifyLanguageChanged(lang);
        });
      }
    }

    // C. Observe document.documentElement for attribute changes (lang or data-lang)
    if (typeof MutationObserver !== 'undefined' && document.documentElement) {
      var observer = new MutationObserver(function (mutations) {
        mutations.forEach(function (m) {
          if (m.type === 'attributes' && (m.attributeName === 'lang' || m.attributeName === 'data-lang')) {
            notifyLanguageChanged(detectCurrentLanguage());
          }
        });
      });
      observer.observe(document.documentElement, {
        attributes: true,
        attributeFilter: ['lang', 'data-lang']
      });
    }

    // D. Storage event listener (multi-tab sync)
    window.addEventListener('storage', function (e) {
      if (e.key === 'ae_lang' || e.key === 'aero-portal-lang' || e.key === 'ae_language') {
        notifyLanguageChanged(e.newValue);
      }
    });
  }

  /* ============================================================================
   * 4. QUOTE SELECTION & QUERY ENGINE
   * ============================================================================ */
  function getRandomQuote(excludeId) {
    if (AEROSPACE_QUOTES.length === 1) return AEROSPACE_QUOTES[0];
    var filtered = excludeId
      ? AEROSPACE_QUOTES.filter(function (q) { return q.id !== excludeId; })
      : AEROSPACE_QUOTES;
    var index = Math.floor(Math.random() * filtered.length);
    return filtered[index];
  }

  function getDailyQuote() {
    var now = new Date();
    var start = new Date(now.getFullYear(), 0, 0);
    var diff = (now - start) + ((start.getTimezoneOffset() - now.getTimezoneOffset()) * 60 * 1000);
    var oneDay = 1000 * 60 * 60 * 24;
    var dayOfYear = Math.floor(diff / oneDay);
    var index = (dayOfYear + now.getFullYear()) % AEROSPACE_QUOTES.length;
    return AEROSPACE_QUOTES[index];
  }

  function getQuoteById(id) {
    if (!id) return null;
    for (var i = 0; i < AEROSPACE_QUOTES.length; i++) {
      if (AEROSPACE_QUOTES[i].id === id) return AEROSPACE_QUOTES[i];
    }
    return null;
  }

  function getAllQuotes() {
    return AEROSPACE_QUOTES.slice(0);
  }

  /* ============================================================================
   * 5. DOM RENDERER & INTERACTIVE INJECTOR
   * ============================================================================ */
  function renderQuoteCard(quote, lang, options) {
    options = options || {};
    var showControls = options.showControls !== false;
    var isDaily = options.mode === 'daily';
    var l = normalizeLang(lang);

    var text = (quote.quote && quote.quote[l]) || quote.quote.en || '';
    var field = (quote.field && quote.field[l]) || quote.field.en || 'Aerospace';
    var role = (quote.role && quote.role[l]) || quote.role.en || '';
    var context = (quote.context && quote.context[l]) || quote.context.en || '';
    var badgeIcon = quote.badgeIcon || '🚀';

    var refreshTitle = l === 'es' ? 'Siguiente cita aeroespacial' : 'Next aerospace quote';
    var copyTitle = l === 'es' ? 'Copiar cita al portapapeles' : 'Copy quote to clipboard';
    var copiedLabel = l === 'es' ? '¡Copiado!' : 'Copied!';
    var tagText = isDaily
      ? (l === 'es' ? 'Cita del Día' : 'Daily Quote')
      : (l === 'es' ? 'Inspiración Aeroespacial' : 'Aerospace Insight');

    var card = document.createElement('div');
    card.className = 'ae-quote-card ae-quote-fade';
    card.setAttribute('role', 'region');
    card.setAttribute('aria-label', l === 'es' ? 'Cita motivacional aeroespacial' : 'Motivational aerospace quote');

    // Header
    var header = document.createElement('div');
    header.className = 'ae-quote-header';

    var badges = document.createElement('div');
    badges.className = 'ae-quote-badges';

    var fieldBadge = document.createElement('span');
    fieldBadge.className = 'ae-quote-badge';
    fieldBadge.innerHTML = '<span class="ae-quote-badge-icon" aria-hidden="true">' + badgeIcon + '</span> ' +
                           '<span class="ae-quote-badge-field">' + field + '</span>';
    badges.appendChild(fieldBadge);

    var tagBadge = document.createElement('span');
    tagBadge.className = 'ae-quote-badge ae-quote-badge-alt';
    tagBadge.innerHTML = '<span class="ae-quote-badge-icon" aria-hidden="true">✨</span> ' +
                         '<span class="ae-quote-badge-tag">' + tagText + '</span>';
    badges.appendChild(tagBadge);

    header.appendChild(badges);

    // Actions (Controls)
    if (showControls) {
      var actions = document.createElement('div');
      actions.className = 'ae-quote-actions';

      // Refresh Button
      var refreshBtn = document.createElement('button');
      refreshBtn.type = 'button';
      refreshBtn.className = 'ae-quote-btn ae-quote-btn-refresh';
      refreshBtn.title = refreshTitle;
      refreshBtn.setAttribute('aria-label', refreshTitle);
      refreshBtn.innerHTML = '<svg viewBox="0 0 24 24"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>';
      actions.appendChild(refreshBtn);

      // Copy Button
      var copyBtn = document.createElement('button');
      copyBtn.type = 'button';
      copyBtn.className = 'ae-quote-btn ae-quote-btn-copy';
      copyBtn.title = copyTitle;
      copyBtn.setAttribute('aria-label', copyTitle);
      copyBtn.innerHTML = '<svg viewBox="0 0 24 24"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>' +
                          '<span class="ae-quote-copied-tooltip">' + copiedLabel + '</span>';
      actions.appendChild(copyBtn);

      header.appendChild(actions);
    }

    card.appendChild(header);

    // Body (Quote)
    var quoteBody = document.createElement('blockquote');
    quoteBody.className = 'ae-quote-body';

    var markOpen = document.createElement('span');
    markOpen.className = 'ae-quote-mark ae-quote-mark-open';
    markOpen.setAttribute('aria-hidden', 'true');
    markOpen.textContent = '“';

    var textEl = document.createElement('p');
    textEl.className = 'ae-quote-text';
    textEl.textContent = text;

    var markClose = document.createElement('span');
    markClose.className = 'ae-quote-mark ae-quote-mark-close';
    markClose.setAttribute('aria-hidden', 'true');
    markClose.textContent = '”';

    quoteBody.appendChild(markOpen);
    quoteBody.appendChild(textEl);
    quoteBody.appendChild(markClose);
    card.appendChild(quoteBody);

    // Footer (Author & Context)
    var footer = document.createElement('div');
    footer.className = 'ae-quote-footer';

    var authorInfo = document.createElement('div');
    authorInfo.className = 'ae-quote-author-info';

    var authorName = document.createElement('div');
    authorName.className = 'ae-quote-author-name';
    authorName.textContent = quote.author;

    var authorRole = document.createElement('div');
    authorRole.className = 'ae-quote-author-role';
    authorRole.textContent = role;

    authorInfo.appendChild(authorName);
    authorInfo.appendChild(authorRole);
    footer.appendChild(authorInfo);

    if (context) {
      var contextPill = document.createElement('div');
      contextPill.className = 'ae-quote-context-pill';
      contextPill.innerHTML = '<span class="ae-quote-context-icon" aria-hidden="true">💡</span> ' +
                              '<span class="ae-quote-context-text">' + context + '</span>';
      footer.appendChild(contextPill);
    }

    card.appendChild(footer);

    return card;
  }

  /**
   * Main Dynamic Injector Function
   *
   * @param {string|HTMLElement} containerSelector - CSS selector or DOM Node to inject into.
   * @param {Object} [options] - Configuration options:
   *   - {string} [mode='random'] - 'random' | 'daily' | <quote-id>
   *   - {boolean} [showControls=true] - Show shuffle & copy buttons.
   *   - {number} [autoRotate=0] - Interval in seconds to cycle quotes (0 = off).
   *   - {string} [lang=null] - Force specific lang ('en'|'es'), or null to auto-detect.
   *   - {function} [onQuoteChange=null] - Callback invoked when quote changes.
   * @returns {Object|null} Controller instance with API methods.
   */
  function initAerospaceQuote(containerSelector, options) {
    if (typeof document === 'undefined') return null;

    ensureStylesInjected();
    setupGlobalLanguageListeners();

    options = options || {};
    var container = typeof containerSelector === 'string'
      ? document.querySelector(containerSelector)
      : containerSelector;

    if (!container) {
      if (typeof console !== 'undefined' && console.warn) {
        console.warn('AE_QUOTES: Target container not found for selector:', containerSelector);
      }
      return null;
    }

    // Determine initial quote
    var currentQuote = null;
    if (options.mode === 'daily') {
      currentQuote = getDailyQuote();
    } else if (typeof options.mode === 'string' && getQuoteById(options.mode)) {
      currentQuote = getQuoteById(options.mode);
    } else {
      currentQuote = getRandomQuote();
    }

    var autoRotateTimer = null;
    var copyTimer = null;

    var controller = {
      container: container,
      options: options,
      currentQuote: currentQuote,

      getCurrentQuote: function () {
        return this.currentQuote;
      },

      setQuote: function (quoteOrId) {
        var target = typeof quoteOrId === 'string' ? getQuoteById(quoteOrId) : quoteOrId;
        if (!target) return;
        this.currentQuote = target;
        this.render();
        if (typeof options.onQuoteChange === 'function') {
          options.onQuoteChange(this.currentQuote, detectCurrentLanguage());
        }
      },

      nextQuote: function () {
        var next = getRandomQuote(this.currentQuote ? this.currentQuote.id : null);
        this.setQuote(next);
      },

      updateLanguage: function (newLang) {
        this.render(newLang);
      },

      render: function (forceLang) {
        var lang = forceLang || options.lang || detectCurrentLanguage();
        var card = renderQuoteCard(this.currentQuote, lang, options);

        // Bind interactive buttons
        var refreshBtn = card.querySelector('.ae-quote-btn-refresh');
        if (refreshBtn) {
          var self = this;
          refreshBtn.addEventListener('click', function (e) {
            e.preventDefault();
            self.nextQuote();
          });
        }

        var copyBtn = card.querySelector('.ae-quote-btn-copy');
        if (copyBtn) {
          var selfInstance = this;
          copyBtn.addEventListener('click', function (e) {
            e.preventDefault();
            var l = normalizeLang(forceLang || options.lang || detectCurrentLanguage());
            var quoteText = selfInstance.currentQuote.quote[l] || selfInstance.currentQuote.quote.en;
            var clipboardText = '“' + quoteText + '” — ' + selfInstance.currentQuote.author +
                                ' (' + (selfInstance.currentQuote.field[l] || selfInstance.currentQuote.field.en) + ')';

            var doFeedback = function () {
              var tooltip = copyBtn.querySelector('.ae-quote-copied-tooltip');
              if (tooltip) {
                tooltip.classList.add('visible');
                clearTimeout(copyTimer);
                copyTimer = setTimeout(function () {
                  tooltip.classList.remove('visible');
                }, 2000);
              }
            };

            if (navigator.clipboard && navigator.clipboard.writeText) {
              navigator.clipboard.writeText(clipboardText).then(doFeedback).catch(function () {
                fallbackCopy(clipboardText);
                doFeedback();
              });
            } else {
              fallbackCopy(clipboardText);
              doFeedback();
            }
          });
        }

        // Mount to container
        container.innerHTML = '';
        container.appendChild(card);
      },

      destroy: function () {
        if (autoRotateTimer) clearInterval(autoRotateTimer);
        if (copyTimer) clearTimeout(copyTimer);
        container.innerHTML = '';
        var idx = activeInstances.indexOf(this);
        if (idx !== -1) activeInstances.splice(idx, 1);
      }
    };

    function fallbackCopy(text) {
      try {
        var textArea = document.createElement('textarea');
        textArea.value = text;
        textArea.style.position = 'fixed';
        textArea.style.left = '-9999px';
        document.body.appendChild(textArea);
        textArea.focus();
        textArea.select();
        document.execCommand('copy');
        document.body.removeChild(textArea);
      } catch (err) {}
    }

    // Initial render
    controller.render();

    // Setup auto-rotation if configured
    if (typeof options.autoRotate === 'number' && options.autoRotate > 0) {
      autoRotateTimer = setInterval(function () {
        controller.nextQuote();
      }, options.autoRotate * 1000);
    }

    // Register active instance
    activeInstances.push(controller);

    return controller;
  }

  /* ============================================================================
   * 6. PUBLIC MODULE EXPORT
   * ============================================================================ */
  return {
    version: '1.0.0',
    quotes: AEROSPACE_QUOTES,
    initAerospaceQuote: initAerospaceQuote,
    getRandomQuote: getRandomQuote,
    getDailyQuote: getDailyQuote,
    getQuoteById: getQuoteById,
    getAllQuotes: getAllQuotes,
    getLanguage: detectCurrentLanguage,
    setLanguage: function (lang) {
      currentForcedLang = lang;
      notifyLanguageChanged(lang);
    }
  };
});
