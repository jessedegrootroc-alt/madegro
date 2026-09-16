/* ============================================================================
   case.js: één casepagina uit de database
   ----------------------------------------------------------------------------
   case.html?slug=case-… haalt de case met die slug uit Supabase (tabel posts,
   alleen published = true) en bouwt de secties in dezelfde volgorde en met
   dezelfde klassen als de vaste casepagina's van de generator: hero,
   kerncijfers, inleiding, over de klant, uitdaging, citaat, aanpak met
   sfeerfoto, resultaat, andere trajecten en het contactvlak. Secties zonder
   inhoud worden weggelaten.

   De hero staat al in de HTML (met data-header-theme voor het witte logo) en
   wordt hier alleen gevuld; de rest komt in #caseSecties.

   Alles in één functie, zodat het bestand opnieuw uitgevoerd kan worden na een
   pagina-overgang.
   ========================================================================== */

(() => {
  const container = document.currentScript?.closest('[data-barba="container"]') || document;
  const wortel = container.querySelector('#caseDetail');
  if (!wortel) return;

  const SUPABASE_URL = 'https://ltkqjffncezrtidthbox.supabase.co/rest/v1/';
  const SUPABASE_KEY = 'sb_publishable__LAsCC26uaKcwBJdaQvPNw_hNs2t_mP';
  const TABEL = 'posts';
  const HEADERS = { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}`, Accept: 'application/json' };

  const slug = new URLSearchParams(location.search).get('slug') || '';
  const secties = wortel.querySelector('#caseSecties');
  const veld = (naam) => wortel.querySelector(`[data-veld="${naam}"]`);

  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (m) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));
  const heeft = (s) => String(s || '').trim().length > 0;
  const alinea = (t) => String(t || '').split(/\n{2,}/).map((x) => x.trim()).filter(Boolean)
    .map((x) => `<p>${esc(x).replace(/\n/g, '<br>')}</p>`).join('\n          ');

  const pijl = (m) => `<svg class="arrow--animation is-1" width="${m}" height="${m}" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg>`
                   + `<svg class="arrow--animation is-2" width="${m}" height="${m}" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg>`;
  const knop = (tekst, href, soort = 'primary') =>
    `<a href="${esc(href)}" class="button button--${soort}"><span class="button__inhoud">${esc(tekst)}<span class="button__spoor" aria-hidden="true">${pijl(14)}</span></span></a>`;
  const ICOONKNOP_54 = `<span class="button--icon button--icon--54 button--secundair" aria-hidden="true" inert><span class="button--circle"><span class="circle-container">${pijl(16)}</span></span></span>`;

  const samenvatting = (c) => {
    const eigen = (c.kaart?.samenvatting || '').trim();
    if (eigen) return eigen;
    const bron = (c.inleiding || '').replace(/\s+/g, ' ').trim();
    if (!bron) return '';
    const zinnen = bron.match(/[^.!?]+[.!?]+|[^.!?]+$/g) || [bron];
    let uit = zinnen.slice(0, 2).map((z) => z.trim()).join(' ');
    if (uit.length > 160) uit = uit.slice(0, 157).replace(/\s+\S*$/, '') + '…';
    return uit;
  };

  /* Titel, beschrijving en canonical van het document horen bij deze case,
     anders delen alle cases dezelfde "Case | MADEGRO". */
  let laatsteKop = null;
  const zetKop = (titel, beschrijving) => {
    laatsteKop = [titel, beschrijving];
    document.title = titel;
    const zet = (kiezer, attr, waarde) => { const el = document.head.querySelector(kiezer); if (el) el.setAttribute(attr, waarde); };
    zet('meta[name="description"]', 'content', beschrijving);
    zet('meta[property="og:title"]', 'content', titel);
    zet('meta[name="twitter:title"]', 'content', titel);
    zet('meta[property="og:description"]', 'content', beschrijving);
    zet('meta[name="twitter:description"]', 'content', beschrijving);
    const url = `${location.origin}${location.pathname}?slug=${encodeURIComponent(slug)}`;
    zet('link[rel="canonical"]', 'href', url);
    zet('meta[property="og:url"]', 'content', url);
  };

  /* ----------------------------------------------------------------------
     Bouwstenen, gelijk aan de generator
     -------------------------------------------------------------------- */
  const blok = (nr, ident, kop, tekst, lijst) => {
    const punten = (lijst || []).map((p) => String(p).trim()).filter(Boolean);
    if (!heeft(tekst) && !punten.length) return '';
    const ul = punten.length ? `\n        <ul class="case-lijst">\n${punten.map((p) => `          <li>${esc(p)}</li>`).join('\n')}\n        </ul>` : '';
    return `  <section class="band background--white case-blok" id="s${nr}-${ident}">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="section-heading case-blok__kop">${esc(kop)}</h2>
        <div class="case-blok__body">
          ${alinea(tekst)}
        </div>${ul}
      </div>
    </div>
  </section>`;
  };

  const bleed = (pad, alt) => heeft(pad) ? `  <figure class="case-bleed">
    <img src="${esc(pad)}" alt="${esc(alt || '')}" loading="lazy" decoding="async">
  </figure>` : '';

  const verwantRij = (rij, i) => {
    const c = rij.content || {};
    return `      <a class="cases-grid__row ${i % 2 === 0 ? 'cases-grid__row--grey' : 'cases-grid__row--white'} hover--icon"
         href="case.html?slug=${encodeURIComponent(rij.slug)}" aria-label="${esc(c.klantnaam)}: ${esc(c.titel)}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">
            <span class="cases-grid__meta-item">${esc(c.dienst || '')}</span>
            <span class="cases-grid__meta-item">${esc(c.locatie || '')}</span>
          </div>
          <h3 class="cases-grid__title">${esc(c.klantnaam || rij.slug)}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">${esc(samenvatting(c))}</p>
            ${ICOONKNOP_54}
          </div>
        </div>
        <figure class="cases-grid__image">
          ${c.kaart?.afbeelding ? `<img src="${esc(c.kaart.afbeelding)}" alt="${esc(c.kaart.alt || '')}" loading="lazy" decoding="async">` : ''}
        </figure>
      </a>`;
  };

  /* ----------------------------------------------------------------------
     Weergave
     -------------------------------------------------------------------- */
  const toonHero = (label, titel, acties, beeld, alt) => {
    const img = veld('beeld');
    if (img) {
      if (heeft(beeld)) { img.src = beeld; img.alt = alt || ''; img.hidden = false; }
      else img.hidden = true;
    }
    veld('label').textContent = label;
    veld('titel').textContent = titel;
    veld('acties').innerHTML = acties;
  };

  const nietGevonden = () => {
    toonHero('Case', 'Deze case is er niet, of nog niet gepubliceerd.', knop('Alle cases', 'cases.html', 'secundair'), '', '');
    secties.innerHTML = `  <section class="band background--white"><div class="container">
      <p class="case-lead">Misschien is de link verouderd, of staat de case nog als concept in het beheer.</p>
    </div></section>`;
    zetKop('Case niet gevonden | MADEGRO', 'Deze case is er niet of is nog niet gepubliceerd.');
  };

  const toon = (rij, verwant) => {
    const c = rij.content || {};
    const klant = c.klantnaam || rij.slug;
    const label = heeft(c.hero?.label) ? c.hero.label : [c.dienst, c.branche].filter(Boolean).join(' · ').toUpperCase();
    const acties = [
      heeft(c.hero?.ctaPrimair) ? knop(c.hero.ctaPrimair, 'contact.html') : '',
      heeft(c.hero?.ctaSecundair) ? knop(c.hero.ctaSecundair, 'cases.html', 'secundair') : '',
    ].join('\n          ');
    toonHero(label, c.titel || klant, acties, c.hero?.afbeelding, c.hero?.alt);
    zetKop(`${klant} | Case | MADEGRO`, (samenvatting(c) || `Een traject uit de praktijk van MADEGRO bij ${klant}.`).slice(0, 155));

    const cijfers = (c.kerncijfers || []).filter((k) => heeft(k.getal) || heeft(k.label));
    const delen = [];

    if (cijfers.length) delen.push(`  <section class="band background--white" id="s02-kerncijfers">
    <div class="container">
      <div class="kerncijfers">
${cijfers.map((k) => `          <div class="kerncijfer">
            <span class="kerncijfer__label">${esc(k.label)}</span>
            <p class="kerncijfer__getal">${esc(k.getal)}<span class="kerncijfer__eenheid">${esc(k.eenheid || '')}</span></p>
          </div>`).join('\n')}
      </div>
    </div>
  </section>`);

    if (heeft(c.inleiding)) delen.push(`  <section class="band background--white" id="s03-inleiding">
    <div class="container">
      <p class="case-lead">${esc(c.inleiding)}</p>
    </div>
  </section>`);

    delen.push(blok('04', 'over', heeft(c.over?.kop) ? c.over.kop : `Over ${klant}`, c.over?.body));
    delen.push(blok('05', 'uitdaging', heeft(c.uitdaging?.kop) ? c.uitdaging.kop : 'De uitdaging', c.uitdaging?.body, c.uitdaging?.lijst));

    if (c.citaat?.tonen !== false && heeft(c.citaat?.tekst)) {
      const wie = [heeft(c.citaat.naam) ? `<strong>${esc(c.citaat.naam)}</strong>` : '', heeft(c.citaat.functie) ? `<span>${esc(c.citaat.functie)}</span>` : ''].join('');
      delen.push(`  <section class="band background--white" id="s06-citaat">
    <div class="container">
      <figure class="case-citaat">
        <blockquote><p>&ldquo;${esc(c.citaat.tekst)}&rdquo;</p></blockquote>
        ${wie ? `<figcaption class="case-citaat__wie">${wie}</figcaption>` : ''}
      </figure>
    </div>
  </section>`);
    }

    delen.push(blok('07', 'aanpak', heeft(c.aanpak?.kop) ? c.aanpak.kop : 'De aanpak', c.aanpak?.body, c.aanpak?.lijst));
    delen.push(bleed(c.aanpak?.afbeelding, c.aanpak?.alt));
    delen.push(blok('08', 'resultaat', heeft(c.resultaat?.kop) ? c.resultaat.kop : 'Het resultaat', c.resultaat?.body));

    if (verwant.length) delen.push(`  <section class="cases-grid" id="s09-verwant">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">Andere trajecten</h2>
        ${knop('Alle cases', 'cases.html', 'secundair')}
      </div>
      <div class="cases-grid__list">
${verwant.map(verwantRij).join('\n')}
      </div>
    </div>
  </section>`);

    const cta = c.cta || {};
    if (heeft(cta.kop) || heeft(cta.tekst)) delen.push(`  <section class="cta-slot" id="s10-contact">
    <div class="container">
      <div class="cta-slot__hoofd">
        ${heeft(cta.label) ? `<span class="subtitle cta-slot__label">${esc(cta.label)}</span>` : ''}
        ${heeft(cta.kop) ? `<h2 class="cta-slot__kop">${esc(cta.kop)}</h2>` : ''}
        ${heeft(cta.tekst) ? `<p class="cta-slot__tekst">${esc(cta.tekst)}</p>` : ''}
        <div class="cta-slot__actie">
          ${knop(heeft(cta.knoptekst) ? cta.knoptekst : 'Neem contact op', 'contact.html')}
        </div>
      </div>
    </div>
  </section>`);

    secties.innerHTML = delen.filter(Boolean).join('\n\n');
    window.ScrollTrigger?.refresh();
  };

  /* ----------------------------------------------------------------------
     Laden
     -------------------------------------------------------------------- */
  /* Voorbeeldmodus voor het beheer: case.html?voorbeeld=1 staat in een iframe
     in admin.html en krijgt de nog niet opgeslagen case via postMessage. Er
     wordt dan niets uit de database gehaald; de cookiebalk blijft verborgen. */
  const voorbeeld = new URLSearchParams(location.search).get('voorbeeld') === '1';
  if (voorbeeld) {
    document.documentElement.classList.add('is-voorbeeld');
    const stijl = document.createElement('style');
    stijl.textContent = '.is-voorbeeld .cookiebalk { display: none !important; }';
    document.head.appendChild(stijl);
    window.addEventListener('message', (e) => {
      if (e.origin !== location.origin || !e.data || e.data.type !== 'madegro:voorbeeld') return;
      if (!container.isConnected) return;
      toon({ slug: e.data.slug || 'voorbeeld', content: e.data.content || {} }, Array.isArray(e.data.verwant) ? e.data.verwant : []);
    });
    veld('titel').textContent = 'Voorbeeld wordt geladen…';
    window.parent?.postMessage({ type: 'madegro:voorbeeld-klaar' }, location.origin);
    return;
  }

  const laad = async () => {
    if (!slug) { nietGevonden(); return; }
    try {
      const a = await fetch(`${SUPABASE_URL}${TABEL}?select=slug,created_at,content&slug=eq.${encodeURIComponent(slug)}&published=is.true&limit=1`, { headers: HEADERS });
      if (!a.ok) throw new Error(`HTTP ${a.status}`);
      const rijen = await a.json();
      if (!container.isConnected) return;
      if (!Array.isArray(rijen) || !rijen.length) { nietGevonden(); return; }
      const rij = rijen[0];

      let verwant = [];
      const slugs = (rij.content?.gerelateerd || []).filter((s) => typeof s === 'string' && s && s !== slug).slice(0, 2);
      if (slugs.length) {
        try {
          const b = await fetch(`${SUPABASE_URL}${TABEL}?select=slug,content&published=is.true&slug=in.(${slugs.map(encodeURIComponent).join(',')})`, { headers: HEADERS });
          if (b.ok) {
            const gevonden = await b.json();
            verwant = slugs.map((s) => gevonden.find((g) => g.slug === s)).filter(Boolean);
          }
        } catch (e) { /* zonder verwante cases verder */ }
      }
      if (!container.isConnected) return;
      toon(rij, verwant);
    } catch (e) {
      console.warn('Case niet geladen', e);
      toonHero('Case', 'De case kon niet worden geladen.', knop('Alle cases', 'cases.html', 'secundair'), '', '');
      secties.innerHTML = `  <section class="band background--white"><div class="container">
      <p class="case-lead">De verbinding met de database lukte niet. Probeer het over een ogenblik opnieuw.</p>
    </div></section>`;
    }
  };

  /* Na een pagina-overgang zet page-transitions.js de vaste waarden uit de
     HTML terug in de kop, meestal nadat de case al geladen is. Dan nog een
     keer de onze. Eén keer per pagina, en alleen zolang deze container er is. */
  document.addEventListener('madegro:kopbijgewerkt', () => {
    if (container.isConnected && laatsteKop) zetKop(...laatsteKop);
  }, { once: true });

  laad();
})();
