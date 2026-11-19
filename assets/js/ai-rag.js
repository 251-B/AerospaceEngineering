/*!
 * Aerospace Engineering Study Portal: client-side RAG retriever over vault/ shards.
 *
 * Loaded on every page by assets/js/theme.js (after assets/data/ai-models.js). Skipped in PDF
 * print mode (?print=...). Shards live under assets/data/ai-index/<subject>.json (built by
 * python tools/build_ai_index.py) and are fetched lazily ONLY when Sideris answers a question.
 *
 * Ranking: lightweight BM25 (k1=1.5, b=0.75) over normalised Spanish/English words + LaTeX
 * command tokens (\nabla, \omega, R_1, EBITDA...), boosted by title/heading match, current unit
 * and formula sheets, and most of all by the note the current page is built from. Chat filler is a
 * stop word, Spanish course words are expanded to the English of the notes, and weak hits are
 * dropped. The inverted index comes prebuilt in the shard (see buildIndex).
 *
 * API: window.AESiderisRAG = { currentSubject, currentUnit, loadSubject, search, formatContext,
 *      setData, clearCache }
 */
(function () {
  'use strict';

  if (window.AESiderisRAG) return;
  if (new URLSearchParams(location.search).has('print')) return;

  var SCRIPT = document.currentScript;
  var INDEX_BASE = SCRIPT && SCRIPT.src
    ? SCRIPT.src.replace(/js\/ai-rag\.js(\?.*)?$/, 'data/ai-index/')
    : 'assets/data/ai-index/';

  var ROOT = INDEX_BASE.replace(/assets\/data\/ai-index\/$/, '');
  var STOP = Object.create(null);
  (
    'the and for that this with from are was were have has had not but what all can will one two ' +
    'its into than then also only more most some such very how why when where which who whom whose ' +
    'los las del una uno unos unas por para con sin sobre entre desde hasta como cual cuales que ' +
    'este esta estos estas ese esa esos esas pero porque donde cuando quien quienes muy mas menos ' +
    'todo toda todos todas cada otro otra otros otras ser estar son esta estan hay tiene tienen ' +
    // chat filler: "explain this section", "explicame este paso" carry no topic
    'explain explica explicame section seccion page pagina step paso part parte here aqui esto eso ' +
    'of to in on by an as at be or it is if de el la en lo le se su al es si un mi me te tu ya ' +
    'do please favor help ayuda ayudame understand entender entiendo don dont know does mean significa'
  ).split(' ').forEach(function (w) { if (w) STOP[w] = 1; });

  /* Spanish course words -> English tokens of the notes (the vault is in English). Applied to the
     query only, so the dictionary can grow without rebuilding any index; plurals are found by
     dropping a final "s" or "es". Ambiguous words list every reading ("momento"). */
  var SYN = Object.create(null);
  (
    // mechanics
    'velocidad:velocity,speed aceleracion:acceleration fuerza:force par:torque,moment momento:moment,momentum ' +
    'inercia:inertia masa:mass peso:weight energia:energy cinetica:kinetic potencial:potential trabajo:work ' +
    'potencia:power rozamiento:friction friccion:friction gravedad:gravity centro:centre,center eje:axis ' +
    'giro:rotation,spin rotacion:rotation traslacion:translation angulo:angle posicion:position base:basis ' +
    'movimiento:motion trayectoria:trajectory,path curvatura:curvature radio:radius tangente:tangent ' +
    'triedro:triad,frame intrinseca:intrinsic intrinseco:intrinsic relativo:relative relativa:relative ' +
    'absoluto:absolute absoluta:absolute arrastre:transport,drag centrifuga:centrifugal centripeta:centripetal ' +
    'solido:solid,body rigido:rigid cuerpo:body ligadura:constraint vinculo:constraint rodadura:rolling ' +
    'deslizamiento:slip,sliding contacto:contact reaccion:reaction diagrama:diagram libre:free choque:impact,collision ' +
    'impulso:impulse orbita:orbit gravitatoria:gravitational excentricidad:eccentricity conica:conic elipse:ellipse ' +
    'hiperbola:hyperbola precesion:precession nutacion:nutation giroscopo:gyroscope,gyroscopic peonza:top ' +
    'oscilador:oscillator oscilacion:oscillation amortiguamiento:damping amortiguado:damped resonancia:resonance ' +
    'frecuencia:frequency periodo:period amplitud:amplitude pendulo:pendulum muelle:spring resorte:spring ' +
    'particula:particle sistema:system referencia:reference ' +
    // maths
    'matriz:matrix determinante:determinant autovalor:eigenvalue autovector:eigenvector derivada:derivative ' +
    'ecuacion:equation diferencial:differential solucion:solution lineal:linear homogenea:homogeneous ' +
    'homogeneo:homogeneous condicion:condition contorno:boundary frontera:boundary inicial:initial ' +
    'estabilidad:stability equilibrio:equilibrium retrato:portrait fase:phase plano:plane coeficiente:coefficient ' +
    'constante:constant separacion:separation cambio:change funcion:function serie:series transformada:transform ' +
    'orden:order grado:degree exacta:exact integrante:integrating wronskiano:wronskian existencia:existence ' +
    'unicidad:uniqueness punto:point silla:saddle nodo:node foco:focus,spiral espiral:spiral traza:trace ' +
    'cuerda:string vibrante:vibrating modelo:model poblacion:population logistica:logistic crecimiento:growth ' +
    'mezcla:mixing,mixture tanque:tank circuito:circuit calor:heat onda:wave autonoma:autonomous ' +
    // fluids
    'temperatura:temperature presion:pressure densidad:density viscosidad:viscosity fluido:fluid flujo:flow,flux ' +
    'caudal:flow,rate tension:stress,tension esfuerzo:stress deformacion:strain,deformation cortante:shear ' +
    'superficie:surface volumen:volume continuidad:continuity conservacion:conservation hidrostatica:hydrostatics,hydrostatic ' +
    'flotacion:buoyancy,floating empuje:thrust,buoyancy compuerta:gate manometro:manometer metacentro:metacentre,metacenter ' +
    'adimensional:dimensionless semejanza:similarity numero:number capa:layer limite:boundary,limit tuberia:pipe ' +
    'conducto:duct,pipe chorro:jet estela:wake resistencia:drag,resistance sustentacion:lift alabe:blade bomba:pump ' +
    'turbina:turbine tobera:nozzle difusor:diffuser remanso:stagnation pelicula:film lubricacion:lubrication ' +
    'cuna:wedge placa:plate cilindro:cylinder esfera:sphere viscoso:viscous estacionario:steady incompresible:incompressible ' +
    // materials
    'enlace:bond ionico:ionic covalente:covalent metalico:metallic cristal:crystal cristalina:crystalline red:lattice ' +
    'celda:cell indice:index,indices difraccion:diffraction defecto:defect dislocacion:dislocation vacante:vacancy ' +
    'difusion:diffusion dureza:hardness ductilidad:ductility fragil:brittle tenacidad:toughness fluencia:yield,creep ' +
    'elastico:elastic plastico:plastic modulo:modulus traccion:tensile,tension compresion:compression fatiga:fatigue ' +
    'fractura:fracture grieta:crack aleacion:alloy eutectico:eutectic eutectoide:eutectoid peritectico:peritectic ' +
    'acero:steel hierro:iron carbono:carbon austenita:austenite ferrita:ferrite perlita:pearlite cementita:cementite ' +
    'martensita:martensite templado:quenching,quenched temple:quenching revenido:tempering recocido:annealing ' +
    'solubilidad:solubility palanca:lever regla:rule polimero:polymer ceramica:ceramic compuesto:composite ' +
    'banda:band prohibida:gap conductividad:conductivity electrica:electrical termica:thermal dilatacion:expansion ' +
    'oxidacion:oxidation grano:grain solidificacion:solidification enfriamiento:cooling ' +
    // business
    'empresa:company,firm beneficio:profit ingreso:revenue,income gasto:expense coste:cost costo:cost fijo:fixed ' +
    'amortizacion:depreciation,amortization activo:asset,assets pasivo:liability,liabilities patrimonio:equity neto:net ' +
    'cuenta:account resultado:income,result tesoreria:cash caja:cash cobro:collection,collections pago:payment,payments ' +
    'venta:sales,sale compra:purchase,purchases inventario:inventory existencia:inventory deuda:debt interes:interest ' +
    'impuesto:tax inversion:investment rentabilidad:return,profitability apalancamiento:leverage umbral:threshold,break ' +
    'produccion:production productividad:productivity eficiencia:efficiency mercado:market precio:price demanda:demand ' +
    'oferta:supply direccion:management gestion:management organizacion:organization estrategia:strategy ' +
    'recurso:resources humano:human proveedor:supplier cliente:customer,client'
  ).split(' ').forEach(function (pair) {
    var i = pair.indexOf(':');
    if (i > 0) SYN[pair.slice(0, i)] = pair.slice(i + 1).split(',');
  });

  function synonyms(tok) {
    return SYN[tok] ||
      (tok.length > 4 && /es$/.test(tok) && SYN[tok.slice(0, -2)]) ||
      (tok.length > 3 && /s$/.test(tok) && SYN[tok.slice(0, -1)]) || null;
  }

  function expandQuery(tokens) {
    var out = tokens.slice();
    tokens.forEach(function (t) { var en = synonyms(t); if (en) out.push.apply(out, en); });
    return out;
  }

  var MIN_SCORE = 3;                 // calibrated on the Mechanics shard: "torque" 4.6, "weather forecast" 1.7
  var shards = Object.create(null);   // slug -> { chunks, pages, ix, hx, dl, avgdl, N }
  var pending = Object.create(null);  // slug -> Promise

  function currentSubject() {
    var m = location.pathname.match(/\/subjects\/([^/]+)\//);
    return m ? m[1] : '';
  }

  function currentUnit() {
    var f = location.pathname.split('/').pop() || '';
    var m = f.match(/(?:topic|unit)-0*(\d+)/i);
    return m ? parseInt(m[1], 10) : 0;
  }

  function normalise(str) {
    var s = String(str || '').toLowerCase();
    if (s.normalize) s = s.normalize('NFD').replace(/[\u0300-\u036f]/g, '');
    return s;
  }

  /* Extract both natural words and LaTeX macro / symbol tokens (\nabla, \tau, r_1, ebitda). */
  function tokenize(text) {
    var raw = normalise(text);
    var out = [];
    var m, re = /\\[a-z]+|[a-z0-9]+(?:_[a-z0-9]+)?/g;
    while ((m = re.exec(raw)) !== null) {
      var tok = m[0];
      if (tok.charAt(0) === '\\') {
        tok = tok.slice(1);
        if (tok.length >= 2 && tok !== 'text' && tok !== 'left' && tok !== 'right' && tok !== 'frac' && tok !== 'cdot') {
          out.push(tok);
        }
        continue;
      }
      if (tok.length < 2 || /^\d+$/.test(tok) || STOP[tok]) continue;
      out.push(tok);
    }
    return out;
  }

  /* build_ai_index.py ships each shard with an inverted index already built ("ix": term -> [chunk,
     tf, chunk, tf, ...] over the text, "hx": term -> [chunk, ...] over title and heading, "dl":
     token count per chunk), made with a Python copy of tokenize() above. Tokenizing 3-4 MB here
     took about half a second on a phone on every page; now loading a shard is a JSON.parse.
     A shard without "ix" (tests, older builds) is indexed here with the same tokenize(). */
  function buildIndex(chunks) {
    var ix = Object.create(null), hx = Object.create(null), dl = [];
    chunks.forEach(function (c, d) {
      var body = tokenize(c.x), tf = Object.create(null), t;
      for (var i = 0; i < body.length; i++) tf[body[i]] = (tf[body[i]] || 0) + 1;
      for (t in tf) (ix[t] || (ix[t] = [])).push(d, tf[t]);
      var head = tokenize((c.t || '') + ' ' + (c.h || '')), seen = Object.create(null);
      for (var j = 0; j < head.length; j++) {
        if (seen[head[j]]) continue;
        seen[head[j]] = 1;
        (hx[head[j]] || (hx[head[j]] = [])).push(d);
      }
      dl.push(body.length);
    });
    return { ix: ix, hx: hx, dl: dl };
  }

  function own(map, key) {
    return Object.prototype.hasOwnProperty.call(map, key) ? map[key] : null;
  }

  function prepareShard(raw) {
    var chunks = Array.isArray(raw && raw.chunks) ? raw.chunks : [];
    var idx = raw && raw.ix && raw.hx && Array.isArray(raw.dl) ? raw : buildIndex(chunks);
    var total = 0;
    var dl = idx.dl.map(function (n) { n = Math.max(1, n); total += n; return n; });
    return {
      subject: (raw && raw.subject) || '',
      label: (raw && raw.label) || '',
      pages: Array.isArray(raw && raw.pages) ? raw.pages : [],
      chunks: chunks,
      ix: idx.ix,
      hx: idx.hx,
      dl: dl,
      avgdl: dl.length ? total / dl.length : 1,
      N: chunks.length
    };
  }

  function setData(slug, raw) {
    if (!slug) return null;
    shards[slug] = prepareShard(raw);
    return shards[slug];
  }

  function loadSubject(slug) {
    if (!slug) return Promise.resolve(null);
    if (shards[slug]) return Promise.resolve(shards[slug]);
    if (pending[slug]) return pending[slug];
    var url = INDEX_BASE + encodeURIComponent(slug) + '.json';
    pending[slug] = fetch(url).then(function (res) {
      if (!res.ok) throw new Error('Could not load course notes index (' + res.status + ')');
      return res.json();
    }).then(function (data) {
      delete pending[slug];
      return setData(slug, data);
    }).catch(function (err) {
      delete pending[slug];
      throw err;
    });
    return pending[slug];
  }

  function inferSubjectFromQuery(q) {
    var s = normalise(q);
    if (/navier|stokes|bernoulli|reynolds|hydrostat|manometer|viscos|continuum|fluido|fluid/.test(s)) return 'fluid-mechanics';
    if (/miller|crystal|bragg|diffus|fick|disloc|martensit|austenit|semiconductor|band gap|material/.test(s)) return 'aerospace-materials-1';
    if (/coriolis|kinemat|euler|rigid body|change of basis|angular velocity|frenet|mecanic|mechanic/.test(s)) return 'engineering-mechanics';
    if (/wronsk|eigen|ode|edo|picard|integrating factor|laplace|bernoulli equation|phase portrait|math/.test(s)) return 'advanced-maths';
    if (/ebitda|ebit|balance sheet|income statement|cash flow|depreciation|amortization|business|empresa/.test(s)) return 'business-management';
    return '';
  }

  // Chunks of the note this very page is built from rank first ("g" in the shard, see build_ai_index.py).
  function currentPage() {
    var m = location.pathname.match(/\/(subjects\/[^?#]+)$/);
    return m ? m[1] : '';
  }

  function scoreShard(shard, qTokens, unit, anchor) {
    var here = currentPage();
    if (!shard || !shard.N || !qTokens.length) return [];
    var k1 = 1.5, b = 0.75, N = shard.N, avgdl = shard.avgdl;
    var score = new Float64Array(N), touched = [], seenQ = Object.create(null);
    for (var q = 0; q < qTokens.length; q++) {
      var term = qTokens[q];
      if (seenQ[term]) continue;
      seenQ[term] = 1;
      var post = own(shard.ix, term) || [], heads = own(shard.hx, term) || [];
      if (!post.length && !heads.length) continue;
      // df = chunks with the term in their text or in their title/heading
      var inDoc = Object.create(null), df = 0, i;
      for (i = 0; i < post.length; i += 2) { inDoc[post[i]] = 1; df++; }
      for (i = 0; i < heads.length; i++) if (!inDoc[heads[i]]) df++;
      var idf = Math.log(1 + (N - df + 0.5) / (df + 0.5));
      for (i = 0; i < post.length; i += 2) {
        var d = post[i], tf = post[i + 1];
        if (!score[d]) touched.push(d);
        score[d] += idf * ((tf * (k1 + 1)) / (tf + k1 * (1 - b + b * (shard.dl[d] / avgdl))));
      }
      for (i = 0; i < heads.length; i++) {
        if (!score[heads[i]]) touched.push(heads[i]);
        score[heads[i]] += idf * 2.2;
      }
    }
    var scored = [];
    for (var t = 0; t < touched.length; t++) {
      var di = touched[t], s = score[di];
      if (s <= 0) continue;
      var c = shard.chunks[di];
      var page = c.g ? shard.pages[c.g - 1] || '' : '';
      if (page && here && page.split('#')[0] === here) s *= anchor && page === here + '#' + anchor ? 2.4 : 1.8;
      if (unit && c.u === unit) s *= 1.35;
      if (c.k === 'f') s *= 1.15;
      if (c.k === 't') s *= 1.08;
      scored.push({
        score: s,
        subject: shard.subject,
        label: shard.label,
        unit: c.u,
        kind: c.k,
        title: c.t,
        heading: c.h,
        url: page ? ROOT + page : '',
        text: c.x
      });
    }
    scored.sort(function (x, y) { return y.score - x.score; });
    return scored;
  }

  function search(query, opts) {
    opts = opts || {};
    var slug = opts.subject || currentSubject() || inferSubjectFromQuery(query);
    var unit = opts.unit != null ? opts.unit : currentUnit();
    var limit = opts.limit || 4;
    var qTokens = expandQuery(tokenize(query));
    if (!slug || !qTokens.length) return Promise.resolve([]);
    // Weak matches are noise the model would treat as ground truth: drop the lot when even the
    // best is below MIN_SCORE (an off-topic question), and anything under half of the best.
    var cutoff = opts.cutoff != null ? opts.cutoff : 0.45;
    return loadSubject(slug).then(function (shard) {
      var hits = scoreShard(shard, qTokens, unit, opts.anchor || '');
      if (!cutoff) return hits.slice(0, limit);
      if (!hits.length || hits[0].score < MIN_SCORE) return [];
      var floor = hits[0].score * cutoff;
      return hits.filter(function (h) { return h.score >= floor; }).slice(0, limit);
    }).catch(function () {
      return [];
    });
  }

  function formatContext(hits, maxChars) {
    maxChars = maxChars || 3600;
    if (!hits || !hits.length) return '';
    var parts = ['[UC3M COURSE NOTES RETRIEVED FROM VAULT — GROUND YOUR NOTATION AND EQUATIONS HERE]'];
    var used = parts[0].length;
    for (var i = 0; i < hits.length; i++) {
      var h = hits[i];
      var head = '\n\n[' + (i + 1) + '] ' + h.title + (h.heading && h.heading !== h.title ? ' — ' + h.heading : '') +
        (h.unit ? ' (Unit ' + h.unit + ')' : '') + '\n';
      var avail = maxChars - used - head.length;
      if (avail < 120) break;
      var body = h.text.length > avail ? h.text.slice(0, avail - 1) + '…' : h.text;
      parts.push(head + body);
      used += head.length + body.length;
    }
    return parts.join('');
  }

  function clearCache() {
    shards = Object.create(null);
    pending = Object.create(null);
  }

  window.AESiderisRAG = {
    currentSubject: currentSubject,
    currentUnit: currentUnit,
    loadSubject: loadSubject,
    search: search,
    formatContext: formatContext,
    setData: setData,
    tokenize: tokenize,
    clearCache: clearCache
  };
})();
