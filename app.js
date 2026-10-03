/* Die Bröltalbahn. Erz, Dampf und Sommerfrische 1862–1914 — ein Quellenapparat. Vanilla JS, Hash-Routen. */
"use strict";

const view = document.getElementById("view");
const D = { mods: null, plates: null, timeline: null, compare: null, texts: {} };
const SIDES = { gesellschaft: "Die Gesellschaft", gruben: "Gruben und Werke", staat: "Staat und Kreis", tal: "Gemeinden und Fahrgäste", nachwelt: "Reiseführer und Nachwelt" };
const LANGS = { de: "Original", en: "Lesefassung" };

const esc = s => String(s ?? "").replace(/[&<>"]/g, c => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]));
const side = s => `<span class="side ${s}">${esc(SIDES[s] || s)}</span>`;
const plateOf = id => (D.plates.plates || []).find(p => p.id === id);
const getJSON = url => fetch(url).then(r => { if (!r.ok) throw new Error(url); return r.json(); });

let langPref = "both";
try { langPref = localStorage.getItem("broeltal_lang") || "both"; } catch (e) { /* storage blocked */ }

async function boot() {
  [D.mods, D.plates, D.timeline, D.compare] = await Promise.all(
    ["data/modules.json", "data/plates.json", "data/timeline.json", "data/compare.json"].map(getJSON));
  document.getElementById("navCompare").hidden = !(D.compare.pairs || []).length;
  document.getElementById("navPlates").hidden = !(D.plates.plates || []).length;
  window.addEventListener("hashchange", route);
  route();
}

async function text(id) {
  if (!D.texts[id]) D.texts[id] = await getJSON(`data/${id}.json`);
  return D.texts[id];
}

function route() {
  const parts = (location.hash.replace(/^#\/?/, "") || "").split("/").filter(Boolean);
  const [page, ...args] = parts;
  document.querySelectorAll(".top nav a").forEach(a => {
    const t = a.getAttribute("href").replace(/^#\/?/, "");
    a.classList.toggle("on", (t || "") === (page === "text" ? "texts" : page || ""));
  });
  view.innerHTML = "";
  window.scrollTo(0, 0);
  const pages = { "": overview, texts, text: reader, compare, timeline, plates, sources };
  (pages[page || ""] || overview)(args);
}

/* ------------------------------------------------------------ overview */
function overview() {
  view.innerHTML = `
  <div class="hero one">
    <div>
      <span class="tag">1862–1914 · Hennef · das Bröltal · Erz · Dampf · Basalt · Sommerfrische</span>
      <h1>Die Bröltalbahn</h1>
      <p class="lede">1862 fuhr von Hennef an der Sieg eine schmale Bahn ins Bröltal, zuerst mit Pferden, bald mit Dampf. Gebaut hatten sie Hüttenleute und Kaufleute für das Erz aus den Gruben um Ruppichteroth. Wenige Jahre später ging der Bergbau zu Ende, und die Bahn, die für das Erz gebaut war, musste sich einen neuen Zweck suchen: Fahrgäste, Basalt aus den Steinbrüchen, Papier, Milch, Ausflügler aus Bonn und Köln. Um 1900 reichte das Netz von Beuel bis Waldbröl und Asbach; der Baedeker nannte Hennef den „Knotenpunkt für die Bröltalbahn“ und das Tal eine Sommerfrische.</p>
      <p class="readable">Dieser Apparat folgt der Bahn durch die Quellen ihrer Zeit, gemeinfreie Zeitungen, Fachzeitschriften, Bilanzen und Reiseführer, von der Gründung bis zum Ersten Weltkrieg. Was danach kam, die Rhein-Sieg-Eisenbahn, der Niedergang und die Stilllegung bis 1967, steht als Ausblick nach der neueren Literatur.</p>
    </div>
  </div>

  <h2>Was der Apparat enthält</h2>
  ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : `<p class="fine">Die ersten Module sind in Arbeit; die Seite „Texte“ nennt sie mit ihren Quellen.</p>`}

  <h2>Die Fragen</h2>
  <div class="grid g2">
    <div class="panel"><h3>Wofür wurde die Bahn gebaut, und wofür fuhr sie?</h3>
      <p>Für das Erz, das die Hütten an Rhein und Sieg brauchten. Als die Gruben schlossen, blieb die Bahn: ein Fall, an dem sich zeigen lässt, wie die Industrialisierung ein Tal erreichte und wie wenig sie sich um ihre ersten Pläne kümmerte.</p></div>
    <div class="panel"><h3>Wer bezahlte?</h3>
      <p>Eine Kommanditgesellschaft, dann eine Aktiengesellschaft, der Staat mit einer Beihilfe, später Kölner und Berliner Banken. Die Bilanzen im Reichsanzeiger zeigen, ob sich das rechnete.</p></div>
    <div class="panel"><h3>Was brachte die Bahn dem Tal?</h3>
      <p>Anschluss an die Welt, Arbeit in den Steinbrüchen, Gäste in den Dörfern, und eine Abhängigkeit von einer Gesellschaft, die anderswo rechnete. Die Lokalzeitungen erzählen beides.</p></div>
    <div class="panel"><h3>Lässt sich das spielen?</h3>
      <p>Das Begleitspiel <a href="https://mit-volldampf-ins-broeltal.netlify.app/"><em>Mit Volldampf ins Bröltal</em></a> ist in Vorbereitung: Man führt die Direktion der Gesellschaft, zwischen Aktionären, Grubenbesitzern, Gemeinden und Behörden. Das Erz geht aus, was man auch tut; gewertet wird, was die Bahn dem Tal ließ. Jede Karte wird auf eine Stelle verweisen, die hier abgedruckt ist.</p></div>
  </div>`;
}

function card(m) {
  return `<a class="card" href="#/text/${m.id}">
    <div>${side(m.side)} <span class="fine">${esc(m.zk)}</span></div>
    <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p></a>`;
}

/* ------------------------------------------------------------ texts */
function texts() {
  view.innerHTML = `
    <span class="tag">Texte</span><h1>Das Korpus</h1>
    <p class="lede">Jedes Modul ist vollständig lesbar, in der Schreibung der Drucke. Geplante Module nennen ihre Quellen; was geprüft und nicht aufgenommen wurde, steht unten mit Begründung.</p>
    ${D.mods.shipped.length ? `<h2>Abgedruckt</h2><div class="grid g2">${D.mods.shipped.map(card).join("")}</div>` : ""}
    ${(D.mods.planned || []).length ? `<h2>Geplant</h2><div class="grid g2">${D.mods.planned.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">geplant</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Quelle:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}
    ${(D.mods.missing || []).length ? `<h2 id="missing">Geprüft und nicht aufgenommen</h2><div class="grid g2">${D.mods.missing.map(m => `
      <div class="card planned"><div>${side(m.side)} <span class="fine">nicht aufgenommen</span></div>
      <h3>${esc(m.kurz)}</h3><p class="fine">${esc(m.warum)}</p><p class="fine"><b>Quelle:</b> ${esc(m.quelle)}</p></div>`).join("")}</div>` : ""}`;
}

async function reader([id, secId, unitN]) {
  const m = D.mods.shipped.find(x => x.id === id);
  if (!m) { location.hash = "#/texts"; return; }
  view.innerHTML = `<p class="fine">Wird geladen…</p>`;
  const t = await text(m.datei);
  const sec = t.sections.find(s => s.id === secId) || t.sections[0];
  const bilingual = sec.units.some(u => u.orig && u.en);
  const lang = bilingual ? langPref : "en";
  const langs = [...new Set(sec.units.filter(u => u.orig).map(u => u.lang || t.orig_sprache))];
  const origName = langs.length === 1 ? (LANGS[langs[0]] || "Original") : langs.length === 2 ? langs.map(l => LANGS[l] || l).join(" oder ") : "Original";
  view.innerHTML = `
    <p class="fine"><a href="#/texts">← Alle Texte</a></p>
    <span class="tag">${side(m.side)} ${esc(t.jahr)} · zitiert als ${esc(sec.zk)} [n]</span>
    <h1>${esc(t.titel)}</h1>
    <p class="fine">${esc(t.autor)}</p>
    <nav class="toc">${t.sections.map(s => `<a href="#/text/${id}/${s.id}" class="${s.id === sec.id ? "on" : ""}">${esc(s.titel)}</a>`).join("")}</nav>
    <div class="panel readable"><h3>${esc(sec.titel)}</h3><p>${esc(sec.blurb)}</p></div>
    ${bilingual ? `<div class="langbar" id="langbar">
      ${[["both", `${origName} + Übersetzung`], ["orig", origName], ["en", "Übersetzung"]].map(([k, l]) =>
        `<button data-l="${k}" class="${k === lang ? "on" : ""}">${l}</button>`).join("")}</div>` : ""}
    <div id="units"></div>
    <div class="panel readable hinweis"><span class="tag">Quelle und Editionsnotiz</span>
      <p><b>Quelle.</b> ${esc(t.quelle)}</p><p>${esc(t.hinweis)}</p></div>`;
  const box = view.querySelector("#units");
  for (const u of sec.units) {
    const showO = u.orig && (!bilingual || lang !== "en"), showE = u.en && (!u.orig || lang !== "orig");
    const cls = ["unit", String(u.n) === unitN ? "hl" : ""].join(" ");
    box.insertAdjacentHTML("beforeend", `
      <div class="${cls}" id="u${u.n}">
        <div class="num"><a href="#/text/${id}/${sec.id}/${u.n}" title="Zitieren als ${esc(sec.zk)} [${u.n}]">[${u.n}]</a>
          ${u.pg ? `<span class="pg" title="${esc(t.pg_label || "")} page.line">${esc(t.pg_label || "")} ${esc(u.pg)}</span>` : ""}</div>
        <div>${u.titel ? `<h4>${esc(u.titel)}${u.lang && langs.length > 1 ? ` <span class="fine">(${esc(LANGS[u.lang] || u.lang)})</span>` : ""}</h4>` : ""}
          <div class="cols ${showO && showE ? "" : "one"}">
            ${showO ? `<div class="origcol"><div class="orig" lang="${esc(u.lang || t.orig_sprache)}"${t.rtl ? ' dir="rtl"' : ""}>${esc(u.orig)}</div>${u.tr ? `<div class="translit">${esc(u.tr)}</div>` : ""}</div>` : ""}
            ${showE ? `<div class="text">${esc(u.en)}</div>` : ""}
          </div></div>
        ${u.note ? `<div class="note">${esc(u.note)}</div>` : ""}
      </div>`);
  }
  view.querySelectorAll("#langbar button").forEach(b => b.onclick = () => {
    langPref = b.dataset.l;
    try { localStorage.setItem("broeltal_lang", langPref); } catch (e) { /* storage blocked */ }
    route();
  });
  if (unitN) { const el = document.getElementById("u" + unitN); if (el) el.scrollIntoView({ block: "center" }); }
}

/* ------------------------------------------------------------ compare */
async function compare([pid]) {
  const CMP = D.compare;
  const pair = (CMP.pairs || []).find(p => p.id === pid);
  if (!pair) {
    view.innerHTML = `
      <span class="tag">Vergleich</span><h1>Stimmen nebeneinander</h1>
      <p class="lede">${esc(CMP.lede)}</p>
      <div class="grid g2">${(CMP.pairs || []).map(p => `<a class="card" href="#/compare/${p.id}">
        <div>${p.voices.map(v => side((D.mods.shipped.find(m => m.id === v.text) || {}).side)).join(" ")}</div>
        <h3>${esc(p.titel)}</h3><p class="fine">${esc(p.frage)}</p></a>`).join("")}</div>`;
    return;
  }
  view.innerHTML = `<p class="fine"><a href="#/compare">← Alle Vergleiche</a></p><p class="fine">Wird geladen…</p>`;
  const docs = await Promise.all(pair.voices.map(v => {
    const m = D.mods.shipped.find(x => x.id === v.text);
    return text(m.datei).then(t => ({ v, m, t }));
  }));
  const col = ({ v, m, t }) => {
    const sec = t.sections.find(s => s.id === v.sec);
    const units = v.n.map(n => sec.units.find(u => u.n === n)).filter(Boolean);
    return `<div class="voice">
      <div class="vhead">${side(m.side)} <b>${esc(t.autor)}</b><br><span class="fine">${esc(t.jahr)} · ${esc(sec.titel)}</span></div>
      ${units.map(u => `<div class="vunit">
        <div class="fine"><a href="#/text/${m.id}/${sec.id}/${u.n}">${esc(sec.zk)} [${u.n}]</a>${u.titel ? ` · ${esc(u.titel)}` : ""}</div>
        <div class="text">${esc(u.en || u.orig)}</div></div>`).join("")}
    </div>`;
  };
  view.innerHTML = `
    <p class="fine"><a href="#/compare">← Alle Vergleiche</a></p>
    <span class="tag">Vergleich</span><h1>${esc(pair.titel)}</h1>
    <p class="lede">${esc(pair.frage)}</p>
    <div class="panel readable"><p>${esc(pair.note)}</p></div>
    <div class="cmp n${docs.length}">${docs.map(col).join("")}</div>`;
}

/* ------------------------------------------------------------ timeline */
function timeline() {
  const T = D.timeline;
  view.innerHTML = `
    <span class="tag">Zeitleiste</span><h1>1853–1914, mit Ausblick bis 1967</h1>
    <p class="lede">${esc(T.lede)}</p>
    <div class="legend">${Object.keys(SIDES).map(side).join(" ")}</div>
    <div class="tl">${T.stations.map(s => {
      const p = s.plate && plateOf(s.plate);
      return `<div class="st" style="--c:var(--${s.side})">
        <div><div class="d">${esc(s.d)} · ${side(s.side)}</div><h3>${esc(s.titel)}</h3><p>${esc(s.text)}</p>
        ${s.cite ? `<p class="fine"><a href="${s.cite}">✦ ${esc(s.citeLabel)}</a></p>` : ""}</div>
        ${p ? `<img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}" title="${esc(p.titel)}">` : "<span></span>"}
      </div>`;
    }).join("")}</div>`;
}

/* ------------------------------------------------------------ plates */
function plates() {
  view.innerHTML = `
    <span class="tag">Tafeln</span><h1>Karten, Ansichten, Papiere</h1>
    <p class="lede">${esc(D.plates.lede || "")}</p>
    <div class="grid g4">${D.plates.plates.map(p => `
      <figure class="plate card"><a href="#" data-p="${p.id}"><img src="assets/plates/${p.id}_t.jpg" alt="${esc(p.titel)}"></a>
      <figcaption>${side(p.side)} <b>${esc(p.titel)}</b><br>${esc(p.caption)}<br><i>${esc(p.source)}</i></figcaption></figure>`).join("")}</div>
    <p class="fine">${esc(D.plates.credit)}</p>`;
  view.querySelectorAll("[data-p]").forEach(a => a.onclick = e => {
    e.preventDefault();
    const p = plateOf(a.dataset.p);
    const lb = document.createElement("div");
    lb.className = "lightbox";
    lb.innerHTML = `<figure><img src="assets/plates/${p.id}.jpg" alt="${esc(p.titel)}"><figcaption class="cap"><b>${esc(p.titel)}.</b> ${esc(p.caption)}</figcaption></figure>`;
    lb.onclick = () => lb.remove();
    document.body.append(lb);
  });
}

/* ------------------------------------------------------------ sources */
function sources() {
  view.innerHTML = `
    <span class="tag">Quellen, Methode, Grenzen</span><h1>Wie dieser Apparat gemacht ist</h1>
    <div class="readable">
    <p><b>Nur Gemeinfreies.</b> Jeder Text stammt aus einem Druck, dessen Schutzfrist abgelaufen ist; die Quelle steht auf seiner Seite. Moderne Editionen und Übersetzungen, die noch geschützt sind, werden nicht benutzt.</p>
    <p><b>Die Seite ist maßgeblich.</b> Die Quellen sind Zeitungen, Fachzeitschriften, amtliche Bekanntmachungen, Bilanzen und Reiseführer der Jahre 1855–1914, gelesen an den Seitenbildern der Digitalisate (zeitpunkt.nrw, Bayerische Staatsbibliothek, Internet Archive, Deutscher Reichsanzeiger). Die maschinelle Texterkennung ist nur Hilfsmittel; Fraktur wird am Bild geprüft. Schreibung und Zeichensetzung der Drucke bleiben erhalten („Brölthal“, „Actien“); jede Korrektur, die über das Offensichtliche hinausgeht, steht in den Anmerkungen.</p>
    <p><b>Keine Übersetzung, aber Erklärungen.</b> Die Texte sind deutsch und brauchen keine Übersetzung. Wo Maße, Münzen, Tarife oder Fachwörter des 19. Jahrhunderts erklärt werden müssen (Taler, Silbergroschen, Centner, Spurweite), sagt es die Anmerkung.</p>
    <p><b>Was nicht gemeinfrei ist.</b> Die neuere Literatur zur Bahn und das 20. Jahrhundert, die Rhein-Sieg-Eisenbahn ab 1921 bis zur Stilllegung 1967, werden nur referiert, mit Angabe der Quelle. Unveröffentlichte Akten aus Archiven werden nur mit Zustimmung des Archivs gezeigt.</p>
    <p><b>Daten.</b> Wo die Quellen sich in Daten widersprechen (etwa beim Gründungstag 1860 oder beim ersten Dampfbetrieb 1863), stehen beide Angaben mit ihrer Herkunft.</p>
    </div>
    <h2>Abgedruckte Quellen</h2>
    ${D.mods.shipped.length ? `<div class="grid g2">${D.mods.shipped.map(m => `<div class="panel"><b>${esc(m.kurz)}</b><p class="fine" id="src-${m.id}">…</p></div>`).join("")}</div>` : `<p class="fine">Noch keine; die geplanten Module nennen ihre Quellen auf der Seite „Texte“.</p>`}
    ${(D.plates.plates || []).length ? `<h2>Tafeln</h2><p class="fine readable">${esc(D.plates.credit)}</p>` : ""}`;
  D.mods.shipped.forEach(async m => {
    const t = await text(m.datei);
    const el = document.getElementById("src-" + m.id);
    if (el) el.textContent = t.quelle;
  });
}

boot().catch(e => { view.innerHTML = `<p>Der Apparat konnte nicht geladen werden: ${esc(e.message)}</p>`; });
