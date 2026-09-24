/**
 * ====================================================================
 * AerospaceEngineering (UC3M) — Universal Client-Side i18n System
 * File: assets/js/i18n.js
 * 
 * Provides instantaneous client-side bilingual translation (ES/EN)
 * for the study portal, persisting the choice in localStorage('ae_lang').
 * 
 * Features:
 * - Full dictionaries for site branding, hero, subjects, areas, shortcuts, footer
 * - Dual mode: key-based lookup (data-i18n) and inline bilingual attributes (data-i18n-es / data-i18n-en)
 * - Input attribute translation (placeholder, aria-label, title)
 * - Language button state management (.lang-btn[data-lang="..."])
 * - Keyboard shortcut support (Press 'L' to toggle language)
 * - Custom event 'ae:languageChange' dispatched on document
 * - Clean vanilla JavaScript with zero external dependencies
 * ====================================================================
 */

(function (root, factory) {
  'use strict';
  if (typeof define === 'function' && define.amd) {
    define([], factory);
  } else if (typeof module === 'object' && module.exports) {
    module.exports = factory();
  } else {
    root.AE_I18N = factory();
  }
})(typeof globalThis !== 'undefined' ? globalThis : window, function () {
  'use strict';

  var STORAGE_KEY = 'ae_lang';
  var DEFAULT_LANG = 'es';
  var SUPPORTED_LANGS = ['es', 'en'];

  /* ====================================================================
     TRANSLATION DICTIONARIES (ES / EN)
     Rigorous aeronautical and academic terminology
     ==================================================================== */
  var TRANSLATIONS = {
    es: {
      /* --- Site Branding & Header --- */
      'brand.title': 'Ingeniería Aeroespacial',
      'brand.subtitle': 'Portal de Estudio',
      'brand.course': '2º Curso',
      'brand.badge': '2º Curso',
      'site.title': 'Portal de Estudio — 2º Ingeniería Aeroespacial',
      'site.meta_desc': 'Portal centralizado de estudio para el 2º curso del Grado en Ingeniería Aeroespacial.',

      /* --- Navigation, Filter & Theme Toolbar --- */
      'nav.all': 'Todos',
      'nav.q1': '1.er Cuatrimestre',
      'nav.q2': '2.º Cuatrimestre',
      'nav.tabs_aria': 'Filtrar por cuatrimestre',
      'nav.main_portal': 'Portal Principal',
      'nav.topics': '← Temas',
      'nav.problems': '← Problemas',
      'nav.back_to_theory': '← Volver a Teoría',
      'nav.theory_index': '← Índice de Teoría',
      'search.placeholder': 'Buscar asignatura, tema o concepto…',
      'search.aria_label': 'Buscar asignaturas',
      'theme.theme': 'Tema',
      'theme.dark': 'Oscuro',
      'theme.light': 'Claro',
      'theme.toggle_aria': 'Cambiar tema claro/oscuro',
      'theme.toggle_title': 'Cambiar tema (T)',
      'lang.toggle_aria_es': 'Cambiar a Español',
      'lang.toggle_aria_en': 'Cambiar a Inglés',
      'lang.btn_label_es': 'ES',
      'lang.btn_label_en': 'EN',

      /* --- Hero Section --- */
      'hero.badge': '2º Curso · Grado en Ingeniería Aeroespacial · UC3M',
      'hero.title_p1': 'Tu centro de estudio',
      'hero.title_p2': 'para Ingeniería Aeroespacial',
      'hero.full_title': 'Tu centro de estudio para Ingeniería Aeroespacial',
      'hero.subtitle': 'Accede a teoría, problemas resueltos, formularios y herramientas interactivas para cada asignatura del curso.',
      'hero.stat_q1_count': '5',
      'hero.stat_q1_label': 'Asignaturas Q1',
      'hero.stat_areas_count': '5',
      'hero.stat_areas_label': 'Áreas por materia',
      'hero.stat_semesters_count': '2',
      'hero.stat_semesters_label': 'Cuatrimestres',

      /* --- Semester Sections Headers & Badges --- */
      'section.q1_title': 'Primer Cuatrimestre',
      'section.q1_count': '5 asignaturas',
      'section.q1_badge': '● Activo',
      'section.q2_title': 'Segundo Cuatrimestre',
      'section.q2_badge': '◯ Próximamente',

      /* --- Subject Cards --- */
      // 1. Fluid Mechanics
      'subject.fluid.title': 'Fluid Mechanics',
      'subject.fluid.subtitle': 'Mecánica de Fluidos',
      'subject.fluid.desc': 'Estática de fluidos, cinemática, ecuaciones de Navier-Stokes, análisis dimensional, flujo potencial, capa límite y compresibilidad.',
      'subject.fluid.keywords': 'fluidos mecánica flujo navier stokes bernoulli capa límite compresibilidad estática cinemática presión viscosidad reynolds',

      // 2. Aerospace Materials I
      'subject.materials.title': 'Aerospace Materials I',
      'subject.materials.subtitle': 'Materiales Aeroespaciales I',
      'subject.materials.desc': 'Estructura cristalina, diagramas de fase, tratamientos térmicos, aleaciones de aluminio, titanio y níquel, fatiga y mecánica de fractura.',
      'subject.materials.keywords': 'materiales cristalino diagrama fase aleación aluminio titanio níquel fatiga fractura tratamiento térmico corrosión compuestos propiedades mecánicas',

      // 3. Engineering Mechanics
      'subject.mechanics.title': 'Engineering Mechanics',
      'subject.mechanics.subtitle': 'Mecánica Aplicada a la Aeroespacial',
      'subject.mechanics.desc': 'Cinemática y dinámica del punto material, movimiento relativo, osciladores, dinámica 3D del sólido rígido, tensores de inercia, ecuaciones de Euler y mecánica de vuelo atmosférico.',
      'subject.mechanics.keywords': 'mecánica ingenieros aplicada aeroespacial punto material cinemática dinámica coordenadas cilíndricas esféricas frenet serret sólido rígido inercia euler kepler vuelo atmosférico',

      // 4. Advanced Mathematics
      'subject.maths.title': 'Advanced Maths',
      'subject.maths.subtitle': 'Matemáticas Avanzadas',
      'subject.maths.desc': 'EDOs de orden superior, EDPs clásicas (calor, onda, Laplace), series y transformadas de Fourier y Laplace, variable compleja.',
      'subject.maths.keywords': 'matemáticas EDO EDP ecuaciones diferenciales fourier laplace variable compleja series transformada calor onda residuos integral',

      // 5. Business Management
      'subject.business.title': 'Business Management',
      'subject.business.subtitle': 'Gestión de Empresas',
      'subject.business.desc': 'Organización industrial, gestión de proyectos aeroespaciales (Gantt/PERT), costes y viabilidad, contabilidad analítica y finanzas.',
      'subject.business.keywords': 'gestión empresas organización industrial proyecto gantt pert costes contabilidad finanzas viabilidad estrategia dirección',

      /* --- Area Labels --- */
      'area.theory': 'Teoría y Conceptos',
      'area.problems': 'Problemas y Exámenes',
      'area.formulas': 'Formularios y Prontuarios',
      'area.lab': 'Laboratorio / Simuladores',
      'area.tests': 'Tests y Quizzes',

      /* --- Badge Statuses & Counts --- */
      'badge.available': 'Disponible',
      'badge.soon': 'Próximamente',
      'badge.wip': 'En preparación',
      'count.2_topics': '2 temas',
      'count.3_topics': '3 temas',
      'count.1_topic': '1 tema',
      'count.10_problems': '10 problemas',
      'count.27_problems': '27 problemas',
      'count.35_problems_3_topics': '3 temas (35 prob.)',
      'count.6_problems_1_topic': '1 tema (6 prob.)',

      /* --- Q2 Banner & Cosmic Supernova Message --- */
      'upcoming.badge': 'En preparación',
      'upcoming.title': 'En preparación',
      'upcoming.desc': 'Las asignaturas del segundo cuatrimestre se incorporarán a medida que avance el curso y se habiliten los cuadernos de estudio correspondientes.',
      'upcoming.supernova': 'En preparación: lo bueno ya llegará ;) ✨ — Colapsando materia estelar para forjar las nuevas asignaturas',

      /* --- Empty State --- */
      'empty.title': 'Sin resultados',
      'empty.desc': 'No se encontraron asignaturas que coincidan con tu búsqueda.',

      /* --- Footer --- */
      'footer.brand': 'Portal de Estudio — 2º Ingeniería Aeroespacial',
      'footer.academic_year': 'Curso 2026 – 2027',
      'footer.built_with': 'Construido con precisión y determinación',
      'footer.institution': 'Grado en Ingeniería Aeroespacial · Universidad Carlos III de Madrid',

      /* --- Keyboard Shortcuts Hint --- */
      'shortcut.search': 'Buscar',
      'shortcut.theme': 'Cambiar tema',
      'shortcut.clear': 'Limpiar búsqueda',
      'shortcut.shortcuts': 'Mostrar atajos',
      'shortcut.lang': 'Cambiar idioma',

      /* --- Subpage / Academic Portal Common Terms --- */
      'common.back_to_portal': '← Volver al Portal de Estudio',
      'common.back_to_subject': '← Volver a la Asignatura',
      'common.theory_index': 'Índice de Teoría',
      'common.problems_index': 'Problemas Resueltos',
      'common.step_by_step': 'Paso a paso',
      'common.view_solution': 'Ver resolución completa',
      'common.hide_solution': 'Ocultar resolución',
      'common.topic': 'Tema',
      'common.problem': 'Problema',
      'common.difficulty': 'Dificultad',
      'common.formula': 'Fórmula',

      /* --- Aerospace Materials I --- */
      'materials.theory_subtitle': 'Teoría y Conceptos — Índice de Temas',
      'materials.problems_subtitle': 'Problemas y Exámenes Resueltos — Paso a Paso',
      'materials.topic_1_num': 'Tema 1 · Sesiones 1–2',
      'materials.topic_1_desc': 'Enlace iónico, covalente, metálico y secundario. Energía de red, orbitales híbridos, teoría de bandas, pozos de potencial interatómico y relación con propiedades macroscópicas.',
      'materials.topic_1_badge_theory': '6 módulos teóricos',
      'materials.topic_1_badge_problems': '4 problemas de examen',
      'materials.topic_1_badge_sim': 'Visualizador interactivo',
      'materials.tag_ionic': 'Iónico',
      'materials.tag_covalent': 'Covalente',
      'materials.tag_metallic': 'Metálico',
      'materials.tag_bands': 'Bandas de energía',
      'materials.topic_2_num': 'Tema 2 · Sesiones 3–4',
      'materials.topic_2_desc': 'Cristalografía: 7 sistemas cristalinos, 14 redes de Bravais, FCC/BCC/HCP, sitios intersticiales, índices de Miller. Defectos: vacantes, dislocaciones, fronteras de grano, polimorfismo.',
      'materials.topic_2_badge_theory': '13 módulos teóricos',
      'materials.topic_2_badge_problems': '26 problemas resueltos',
      'materials.topic_2_badge_sim': 'Simulador 3D de celdas',
      'materials.tag_vacancies': 'Vacantes',
      'materials.tag_dislocations': 'Dislocaciones',
      'materials.topic_3_num': 'Tema 3 · Sesión 5',
      'materials.topic_3_desc': 'Mecanismos atómicos de difusión, leyes de Fick (1.ª y 2.ª), función error, relación de Arrhenius, carburación superficial, difusión en semiconductores y sinterización.',
      'materials.topic_3_badge_theory': '6 módulos teóricos',
      'materials.topic_3_badge_sim': 'Calculadoras erf(z) y Arrhenius',
      'materials.tag_carburization': 'Carburación',
      'materials.prob_topic_3_num': 'Tema 3 · Difusión en Sólidos',
      'materials.prob_topic_3_desc': '6 problemas numéricos completos: carburación de acero (AISI 1018/1010), difusión de Al en Si monocristalino, energía de activación, transporte iónico en MgO y purificación de H₂ con membrana de Pd.',
      'materials.prob_topic_3_badge': '6 problemas resueltos',
      'materials.prob_topic_3_calc': 'Interpolador erf(z)',
      'materials.footer': 'Aerospace Materials I · 2º Ingeniería Aeroespacial · UC3M',
      'materials.sidebar_foundational': 'Teoría Fundamental',
      'materials.sidebar_mastery': 'Memorización y Práctica',
      'materials.sidebar_flashcards': 'Mazo de Flashcards',
      'materials.sidebar_speed_drill': 'Test Rápido V / F',
      'materials.sidebar_exam_probs': 'Problemas Oficiales de Examen',
      'materials.sidebar_structure_1': 'Sesión 3: Estructura I',
      'materials.sidebar_structure_2': 'Sesión 4: Estructura II',
      'materials.sidebar_diffusion_theory': 'Sesión 5: Teoría Completa',
      'materials.sidebar_practice_tools': 'Práctica y Herramientas',
      'materials.sidebar_prob_set': 'Problemas Oficiales Tema 3'
    },

    en: {
      /* --- Site Branding & Header --- */
      'brand.title': 'Aerospace Engineering',
      'brand.subtitle': 'Study Portal',
      'brand.course': '2nd Year',
      'brand.badge': '2nd Year',
      'site.title': 'Study Portal — 2nd Year Aerospace Engineering',
      'site.meta_desc': 'Centralized study portal for the 2nd Year of the Bachelor\'s Degree in Aerospace Engineering.',

      /* --- Navigation, Filter & Theme Toolbar --- */
      'nav.all': 'All',
      'nav.q1': '1st Semester',
      'nav.q2': '2nd Semester',
      'nav.tabs_aria': 'Filter by semester',
      'nav.main_portal': 'Main Portal',
      'nav.topics': '← Topics',
      'nav.problems': '← Problems',
      'nav.back_to_theory': '← Back to Theory',
      'nav.theory_index': '← Theory Index',
      'search.placeholder': 'Search subject, topic, or concept…',
      'search.aria_label': 'Search subjects',
      'theme.theme': 'Theme',
      'theme.dark': 'Dark',
      'theme.light': 'Light',
      'theme.toggle_aria': 'Toggle dark/light theme',
      'theme.toggle_title': 'Toggle theme (T)',
      'lang.toggle_aria_es': 'Switch to Spanish',
      'lang.toggle_aria_en': 'Switch to English',
      'lang.btn_label_es': 'ES',
      'lang.btn_label_en': 'EN',

      /* --- Hero Section --- */
      'hero.badge': '2nd Year · BSc in Aerospace Engineering · UC3M',
      'hero.title_p1': 'Your study hub',
      'hero.title_p2': 'for Aerospace Engineering',
      'hero.full_title': 'Your study hub for Aerospace Engineering',
      'hero.subtitle': 'Access theory notes, step-by-step solved problems, formula sheets, and interactive tools for each course.',
      'hero.stat_q1_count': '5',
      'hero.stat_q1_label': 'Q1 Subjects',
      'hero.stat_areas_count': '5',
      'hero.stat_areas_label': 'Areas per subject',
      'hero.stat_semesters_count': '2',
      'hero.stat_semesters_label': 'Semesters',

      /* --- Semester Sections Headers & Badges --- */
      'section.q1_title': 'First Semester',
      'section.q1_count': '5 subjects',
      'section.q1_badge': '● Active',
      'section.q2_title': 'Second Semester',
      'section.q2_badge': '◯ Coming Soon',

      /* --- Subject Cards --- */
      // 1. Fluid Mechanics
      'subject.fluid.title': 'Fluid Mechanics',
      'subject.fluid.subtitle': 'Fluid Mechanics',
      'subject.fluid.desc': 'Fluid statics, kinematics, Navier-Stokes equations, dimensional analysis, potential flow, boundary layer theory, and compressibility.',
      'subject.fluid.keywords': 'fluids mechanics flow navier stokes bernoulli boundary layer compressibility statics kinematics pressure viscosity reynolds',

      // 2. Aerospace Materials I
      'subject.materials.title': 'Aerospace Materials I',
      'subject.materials.subtitle': 'Aerospace Materials I',
      'subject.materials.desc': 'Crystal structures, phase diagrams, heat treatments, aluminum, titanium, and nickel alloys, fatigue, and fracture mechanics.',
      'subject.materials.keywords': 'materials crystal structure phase diagram alloys aluminum titanium nickel fatigue fracture heat treatment corrosion composites mechanical properties',

      // 3. Engineering Mechanics
      'subject.mechanics.title': 'Engineering Mechanics',
      'subject.mechanics.subtitle': 'Mechanics Applied to Aerospace Engineering',
      'subject.mechanics.desc': 'Point particle kinematics and dynamics, relative motion, oscillators, 3D rigid body dynamics, inertia tensors, Euler equations, and atmospheric flight mechanics.',
      'subject.mechanics.keywords': 'mechanics applied aerospace point particle kinematics dynamics cylindrical spherical coordinates frenet serret rigid body inertia euler kepler atmospheric flight',

      // 4. Advanced Mathematics
      'subject.maths.title': 'Advanced Maths',
      'subject.maths.subtitle': 'Advanced Mathematics',
      'subject.maths.desc': 'Higher-order ODEs, classic PDEs (heat, wave, Laplace), Fourier and Laplace series and transforms, complex variable theory.',
      'subject.maths.keywords': 'mathematics ODE PDE differential equations fourier laplace complex variable series transform heat wave residues integral',

      // 5. Business Management
      'subject.business.title': 'Business Management',
      'subject.business.subtitle': 'Business Management & Industrial Organization',
      'subject.business.desc': 'Industrial organization, aerospace project management (Gantt/PERT), cost accounting, investment appraisal, and corporate finance.',
      'subject.business.keywords': 'business management industrial organization project gantt pert costs accounting finance feasibility strategy operations',

      /* --- Area Labels --- */
      'area.theory': 'Theory & Concepts',
      'area.problems': 'Problems & Exams',
      'area.formulas': 'Formula Sheets',
      'area.lab': 'Laboratory & Simulators',
      'area.tests': 'Quizzes & Practice',

      /* --- Badge Statuses & Counts --- */
      'badge.available': 'Available',
      'badge.soon': 'Coming Soon',
      'badge.wip': 'In Preparation',
      'count.2_topics': '2 topics',
      'count.3_topics': '3 topics',
      'count.1_topic': '1 topic',
      'count.10_problems': '10 problems',
      'count.27_problems': '27 problems',
      'count.35_problems_3_topics': '3 topics (35 prob.)',
      'count.6_problems_1_topic': '1 topic (6 prob.)',

      /* --- Q2 Banner & Cosmic Supernova Message --- */
      'upcoming.badge': 'In Preparation',
      'upcoming.title': 'In preparation: the best is yet to come ;) ✨',
      'upcoming.desc': 'Collapsing cosmic dust into upcoming courses. Second-semester subjects will be unlocked as new course modules go live.',
      'upcoming.supernova': 'In preparation: the best is yet to come ;) ✨ — Collapsing cosmic dust into upcoming courses',

      /* --- Empty State --- */
      'empty.title': 'No results found',
      'empty.desc': 'No subjects matching your search criteria were found.',

      /* --- Footer --- */
      'footer.brand': 'Study Portal — 2nd Year Aerospace Engineering',
      'footer.academic_year': 'Academic Year 2026 – 2027',
      'footer.built_with': 'Built with precision and determination',
      'footer.institution': 'BSc in Aerospace Engineering · Universidad Carlos III de Madrid',

      /* --- Keyboard Shortcuts Hint --- */
      'shortcut.search': 'Search',
      'shortcut.theme': 'Toggle theme',
      'shortcut.clear': 'Clear search',
      'shortcut.shortcuts': 'Show shortcuts',
      'shortcut.lang': 'Switch language',

      /* --- Subpage / Academic Portal Common Terms --- */
      'common.back_to_portal': '← Back to Study Portal',
      'common.back_to_subject': '← Back to Subject',
      'common.theory_index': 'Theory Index',
      'common.problems_index': 'Solved Problems',
      'common.step_by_step': 'Step by step',
      'common.view_solution': 'View step-by-step solution',
      'common.hide_solution': 'Hide solution',
      'common.topic': 'Topic',
      'common.problem': 'Problem',
      'common.difficulty': 'Difficulty',
      'common.formula': 'Formula',

      /* --- Aerospace Materials I --- */
      'materials.theory_subtitle': 'Theory & Concepts — Topic Index',
      'materials.problems_subtitle': 'Solved Problems & Exams — Step-by-Step',
      'materials.topic_1_num': 'Topic 1 · Sessions 1–2',
      'materials.topic_1_desc': 'Ionic, covalent, metallic, and secondary bonding. Lattice energy, hybrid orbitals, band theory, interatomic potential wells, and macroscopic property relations.',
      'materials.topic_1_badge_theory': '6 theory modules',
      'materials.topic_1_badge_problems': '4 exam problems',
      'materials.topic_1_badge_sim': 'Interactive visualizer',
      'materials.tag_ionic': 'Ionic',
      'materials.tag_covalent': 'Covalent',
      'materials.tag_metallic': 'Metallic',
      'materials.tag_bands': 'Energy bands',
      'materials.topic_2_num': 'Topic 2 · Sessions 3–4',
      'materials.topic_2_desc': 'Crystallography: 7 crystal systems, 14 Bravais lattices, FCC/BCC/HCP, interstitial sites, Miller indices. Defects: vacancies, dislocations, grain boundaries, polymorphism.',
      'materials.topic_2_badge_theory': '13 theory modules',
      'materials.topic_2_badge_problems': '26 solved problems',
      'materials.topic_2_badge_sim': '3D unit cell simulator',
      'materials.tag_vacancies': 'Vacancies',
      'materials.tag_dislocations': 'Dislocations',
      'materials.topic_3_num': 'Topic 3 · Session 5',
      'materials.topic_3_desc': 'Atomic mechanisms of diffusion, Fick\'s laws (1st and 2nd), error function, Arrhenius equation, case hardening carburization, semiconductor diffusion, and sintering.',
      'materials.topic_3_badge_theory': '6 theory modules',
      'materials.topic_3_badge_sim': 'erf(z) & Arrhenius calculators',
      'materials.tag_carburization': 'Carburization',
      'materials.prob_topic_3_num': 'Topic 3 · Diffusion in Solids',
      'materials.prob_topic_3_desc': '6 complete numerical problems: steel carburization (AISI 1018/1010), Al diffusion in single-crystal Si, activation energy, ionic transport in MgO, and H₂ purification with Pd membrane.',
      'materials.prob_topic_3_badge': '6 solved problems',
      'materials.prob_topic_3_calc': 'erf(z) interpolator',
      'materials.footer': 'Aerospace Materials I · 2nd Year Aerospace Engineering · UC3M',
      'materials.sidebar_foundational': 'Foundational Theory',
      'materials.sidebar_mastery': 'Memorization & Mastery',
      'materials.sidebar_flashcards': 'Flashcard Deck',
      'materials.sidebar_speed_drill': 'True / False Speed Drill',
      'materials.sidebar_exam_probs': 'Official Exam Problems',
      'materials.sidebar_structure_1': 'Session 3: Structure I',
      'materials.sidebar_structure_2': 'Session 4: Structure II',
      'materials.sidebar_diffusion_theory': 'Session 5: Complete Theory',
      'materials.sidebar_practice_tools': 'Practice & Tools',
      'materials.sidebar_prob_set': 'Topic 3 Official Problem Set'
    }
  };

  /* ====================================================================
     CORE LOGIC & HELPERS
     ==================================================================== */

  var currentLang = DEFAULT_LANG;

  /**
   * Safely read language from localStorage
   */
  function getStoredLanguage() {
    try {
      var stored = localStorage.getItem(STORAGE_KEY);
      if (stored && SUPPORTED_LANGS.indexOf(stored) !== -1) {
        return stored;
      }
    } catch (e) {
      // In case localStorage is blocked/disabled
    }
    return null;
  }

  /**
   * Safely save language to localStorage
   */
  function setStoredLanguage(lang) {
    try {
      localStorage.setItem(STORAGE_KEY, lang);
    } catch (e) {
      // Ignore storage errors
    }
  }

  /**
   * Get translation string by key
   * Supports flat keys ('hero.title') or underscores ('hero_title')
   */
  function t(key, fallback) {
    if (!key) return '';
    var dict = TRANSLATIONS[currentLang] || TRANSLATIONS[DEFAULT_LANG];
    
    // Direct match
    if (dict[key] !== undefined) {
      return dict[key];
    }

    // Try converting dots to underscores or vice versa
    var altKey = key.indexOf('.') !== -1 ? key.replace(/\./g, '_') : key.replace(/_/g, '.');
    if (dict[altKey] !== undefined) {
      return dict[altKey];
    }

    // Fallback to English if current was Spanish, or vice versa
    var otherLang = currentLang === 'es' ? 'en' : 'es';
    var otherDict = TRANSLATIONS[otherLang];
    if (otherDict && otherDict[key] !== undefined) {
      return otherDict[key];
    }
    if (otherDict && otherDict[altKey] !== undefined) {
      return otherDict[altKey];
    }

    return fallback !== undefined ? fallback : key;
  }

  /**
   * Apply translations to DOM elements in the given container (or document)
   */
  function applyTranslations(rootElement) {
    var root = rootElement || document;

    // 1. Text elements with data-i18n
    var i18nElements = root.querySelectorAll('[data-i18n]');
    for (var i = 0; i < i18nElements.length; i++) {
      var el = i18nElements[i];
      var key = el.getAttribute('data-i18n');
      var val = t(key);
      if (val) {
        if (el.tagName === 'INPUT' || el.tagName === 'TEXTAREA') {
          el.setAttribute('placeholder', val);
        } else {
          el.textContent = val;
        }
      }
    }

    // 2. HTML elements with data-i18n-html
    var htmlElements = root.querySelectorAll('[data-i18n-html]');
    for (var h = 0; h < htmlElements.length; h++) {
      var hEl = htmlElements[h];
      var hKey = hEl.getAttribute('data-i18n-html');
      var hVal = t(hKey);
      if (hVal) {
        hEl.innerHTML = hVal;
      }
    }

    // 3. Elements with explicit inline language attributes: data-i18n-es and data-i18n-en
    var inlineElements = root.querySelectorAll('[data-i18n-es], [data-i18n-en]');
    for (var j = 0; j < inlineElements.length; j++) {
      var inEl = inlineElements[j];
      var textForLang = inEl.getAttribute('data-i18n-' + currentLang);
      if (textForLang !== null && textForLang !== undefined) {
        if (inEl.hasAttribute('data-i18n-is-html')) {
          inEl.innerHTML = textForLang;
        } else {
          inEl.textContent = textForLang;
        }
      }
    }

    // 4. Input placeholders
    var placeholderElements = root.querySelectorAll('[data-i18n-placeholder], [data-i18n-placeholder-es], [data-i18n-placeholder-en]');
    for (var p = 0; p < placeholderElements.length; p++) {
      var pEl = placeholderElements[p];
      var pKey = pEl.getAttribute('data-i18n-placeholder');
      if (pKey) {
        pEl.setAttribute('placeholder', t(pKey, pEl.getAttribute('placeholder')));
      } else {
        var pText = pEl.getAttribute('data-i18n-placeholder-' + currentLang);
        if (pText !== null) pEl.setAttribute('placeholder', pText);
      }
    }

    // 5. Aria-labels
    var ariaElements = root.querySelectorAll('[data-i18n-aria-label], [data-i18n-aria-es], [data-i18n-aria-en]');
    for (var a = 0; a < ariaElements.length; a++) {
      var aEl = ariaElements[a];
      var aKey = aEl.getAttribute('data-i18n-aria-label');
      if (aKey) {
        aEl.setAttribute('aria-label', t(aKey, aEl.getAttribute('aria-label')));
      } else {
        var aText = aEl.getAttribute('data-i18n-aria-' + currentLang);
        if (aText !== null) aEl.setAttribute('aria-label', aText);
      }
    }

    // 6. Titles
    var titleElements = root.querySelectorAll('[data-i18n-title], [data-i18n-title-es], [data-i18n-title-en]');
    for (var tl = 0; tl < titleElements.length; tl++) {
      var tlEl = titleElements[tl];
      var tlKey = tlEl.getAttribute('data-i18n-title');
      if (tlKey) {
        tlEl.setAttribute('title', t(tlKey, tlEl.getAttribute('title')));
      } else {
        var tlText = tlEl.getAttribute('data-i18n-title-' + currentLang);
        if (tlText !== null) tlEl.setAttribute('title', tlText);
      }
    }

    // 7. Update document lang and title if set
    document.documentElement.lang = currentLang;
    var docTitleEl = document.querySelector('title[data-i18n]');
    if (docTitleEl) {
      document.title = t(docTitleEl.getAttribute('data-i18n'), document.title);
    }

    // 8. Update language switcher buttons (.lang-btn or [data-lang])
    updateLangButtons();

    // 9. Sync theme label if present on page
    syncThemeLabel();
  }

  /**
   * Update active status on language selector buttons
   */
  function updateLangButtons() {
    var buttons = document.querySelectorAll('.lang-btn, [data-lang-switch]');
    for (var i = 0; i < buttons.length; i++) {
      var btn = buttons[i];
      var btnLang = btn.getAttribute('data-lang') || btn.getAttribute('data-lang-switch');
      var isActive = btnLang === currentLang;

      if (isActive) {
        btn.classList.add('active');
        btn.setAttribute('aria-pressed', 'true');
        btn.setAttribute('aria-selected', 'true');
      } else {
        btn.classList.remove('active');
        btn.setAttribute('aria-pressed', 'false');
        btn.setAttribute('aria-selected', 'false');
      }
    }
  }

  /**
   * Keep theme label in sync with current language
   */
  function syncThemeLabel() {
    var themeLabel = document.getElementById('themeLabel');
    if (themeLabel) {
      var currentTheme = document.documentElement.getAttribute('data-theme') || 'dark';
      themeLabel.textContent = currentTheme === 'dark' ? t('theme.dark', 'Oscuro') : t('theme.light', 'Claro');
    }
  }

  /**
   * Set active language, apply translations and persist
   */
  function setLanguage(lang) {
    if (SUPPORTED_LANGS.indexOf(lang) === -1) {
      console.warn('[AE_I18N] Unsupported language:', lang);
      return;
    }

    var prevLang = currentLang;
    currentLang = lang;
    setStoredLanguage(lang);

    applyTranslations();

    // Notify listeners via CustomEvent
    try {
      var event = new CustomEvent('ae:languageChange', {
        detail: {
          lang: currentLang,
          prevLang: prevLang
        }
      });
      document.dispatchEvent(event);
    } catch (e) {
      // Fallback for older browsers
      var evt = document.createEvent('CustomEvent');
      evt.initCustomEvent('ae:languageChange', true, true, {
        lang: currentLang,
        prevLang: prevLang
      });
      document.dispatchEvent(evt);
    }
  }

  /**
   * Toggle between 'es' and 'en'
   */
  function toggleLanguage() {
    setLanguage(currentLang === 'es' ? 'en' : 'es');
  }

  /**
   * Get current language code ('es' or 'en')
   */
  function getLanguage() {
    return currentLang;
  }

  /**
   * Bind event listeners for buttons and keyboard shortcut
   */
  function bindEvents() {
    // Click delegation for language buttons
    document.addEventListener('click', function (e) {
      var target = e.target.closest('.lang-btn, [data-lang-switch]');
      if (target) {
        e.preventDefault();
        var targetLang = target.getAttribute('data-lang') || target.getAttribute('data-lang-switch');
        if (targetLang) {
          setLanguage(targetLang);
        }
      }
    });

    // Keyboard shortcut: Press 'L' to switch language when not typing
    document.addEventListener('keydown', function (e) {
      var tag = (e.target && e.target.tagName) ? e.target.tagName : '';
      var isInput = tag === 'INPUT' || tag === 'TEXTAREA' || (e.target && e.target.isContentEditable);
      
      if ((e.key === 'l' || e.key === 'L') && !isInput && !e.ctrlKey && !e.metaKey && !e.altKey) {
        e.preventDefault();
        toggleLanguage();
      }
    });

    // Listen to theme changes to keep theme label translated
    var themeToggle = document.getElementById('themeToggle');
    if (themeToggle) {
      themeToggle.addEventListener('click', function () {
        setTimeout(syncThemeLabel, 20);
      });
    }
  }

  /**
   * Initialization
   */
  function init() {
    var stored = getStoredLanguage();
    if (stored) {
      currentLang = stored;
    } else {
      // Optional check: navigator language
      var navLang = (navigator.language || navigator.userLanguage || '').toLowerCase();
      if (navLang.indexOf('en') === 0) {
        currentLang = 'en';
      } else {
        currentLang = DEFAULT_LANG;
      }
    }

    applyTranslations();
    bindEvents();
  }

  // Auto-init when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

  /* Public API */
  return {
    setLanguage: setLanguage,
    getLanguage: getLanguage,
    toggleLanguage: toggleLanguage,
    t: t,
    applyTranslations: applyTranslations,
    translations: TRANSLATIONS
  };
});
