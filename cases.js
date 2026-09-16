/* ============================================================================
   cases.js: het cases-overzicht uit de database, met filters
   ----------------------------------------------------------------------------
   De kaarten komen uit Supabase (tabel posts, alleen published = true), zodat
   wat in het beheer wordt gepubliceerd hier meteen staat. De HTML bevat als
   vertrekpunt de kaarten die de generator kent; die blijven staan als de
   database niet antwoordt, dus de pagina is nooit leeg.

   Twee groepen filterpillen: dienst en branche. Binnen een groep geldt er één
   tegelijk, en de eerste pil ('alle') zet de groep weer open. De branchepillen
   worden opnieuw opgebouwd uit de geladen cases, want die lijst is niet vast.

   Alles in één functie, zodat het bestand opnieuw uitgevoerd kan worden na een
   pagina-overgang.
   ========================================================================== */

(() => {
  /* Tijdens een overgang staan twee pagina's in de DOM; zoek binnen de eigen. */
  const container = document.currentScript?.closest('[data-barba="container"]') || document;

  const raster = container.querySelector('#caseRaster');
  if (!raster) return;

  const SUPABASE_URL = 'https://ltkqjffncezrtidthbox.supabase.co/rest/v1/';
  const SUPABASE_KEY = 'sb_publishable__LAsCC26uaKcwBJdaQvPNw_hNs2t_mP';
  const TABEL = 'posts';

  const telling = container.querySelector('.cases-overzicht__telling');
  const leeg = container.querySelector('.cases-overzicht__leeg');
  const brancheGroep = container.querySelector('.filter-groep[data-groep="branche"]');
  const keuze = { dienst: 'alles', branche: 'alles' };

  const esc = (s) => String(s ?? '').replace(/[&<>"']/g, (m) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[m]));
  /* 'EHS RIE' -> 'ehs-rie', hetzelfde als sleutelvorm() in de generator. */
  const sleutel = (w) => String(w || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '')
    .replace(/[^a-z0-9]+/g, '-').replace(/^-+|-+$/g, '');

  const PIJL = '<svg class="arrow--animation is-1" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg>'
             + '<svg class="arrow--animation is-2" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg>';
  const ICOONKNOP = `<span class="button--icon  button--secundair" aria-hidden="true" inert><span class="button--circle"><span class="circle-container">${PIJL}</span></span></span>`;
  const VINKJE = '<span class="filter-pil__vink" aria-hidden="true"><svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor"><path d="M10 15.2 19.2 6l1.4 1.4L10 18 3.6 11.6 5 10.2 10 15.2Z"/></svg></span>';

  /* Kaartsamenvatting: de eigen tekst, anders de eerste twee zinnen van de
     inleiding. Dezelfde regel als in het beheer. */
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

  const kaart = (rij) => {
    const c = rij.content || {};
    const beeld = c.kaart?.afbeelding
      ? `<img src="${esc(c.kaart.afbeelding)}" alt="" loading="lazy" decoding="async">`
      : '';
    return `        <article class="case-kaart" data-dienst="${sleutel(c.dienst)}" data-branche="${sleutel(c.branche)}">
          <a class="case-kaart__link hover--icon" href="case.html?slug=${encodeURIComponent(rij.slug)}">
            <figure class="case-kaart__beeld">${beeld}</figure>
            <div class="case-kaart__inhoud">
              <div class="case-kaart__meta">
                <span class="case-kaart__label">${esc(c.dienst || '')}</span>
                <span class="case-kaart__label">${esc(c.locatie || '')}</span>
              </div>
              <h2 class="case-kaart__titel">${esc(c.klantnaam || c.titel || rij.slug)}</h2>
              <p class="case-kaart__tekst">${esc(samenvatting(c))}</p>
              <div class="case-kaart__voet">
                <span class="case-kaart__lees">Lees de case</span>
                ${ICOONKNOP}
              </div>
            </div>
          </a>
        </article>`;
  };

  const pil = (naam, waarde, tekst, actief) =>
    `<button type="button" class="filter-pil${actief ? ' is-actief' : ''}" data-filter="${naam}" data-waarde="${esc(waarde)}" aria-pressed="${actief}">${VINKJE}<span>${esc(tekst)}</span></button>`;

  /* ----------------------------------------------------------------------
     Filteren over wat er nu in het raster staat
     -------------------------------------------------------------------- */
  const werkBij = () => {
    const kaarten = [...raster.querySelectorAll('.case-kaart')];
    let zichtbaar = 0;
    kaarten.forEach((k) => {
      const past = (keuze.dienst === 'alles' || k.dataset.dienst === keuze.dienst)
                && (keuze.branche === 'alles' || k.dataset.branche === keuze.branche);
      k.hidden = !past;
      if (past) zichtbaar++;
    });

    /* De achtergrond van een kaart wisselt om en om. Omdat er kaarten
       wegvallen, moet die wisseling opnieuw geteld worden over wat er
       overblijft; anders staan er twee grijze naast elkaar. */
    let n = 0;
    kaarten.forEach((k) => {
      if (k.hidden) return;
      k.classList.toggle('is-even', n % 2 === 1);
      n++;
    });

    if (telling) {
      telling.textContent = zichtbaar === kaarten.length
        ? `${kaarten.length} cases`
        : `${zichtbaar} van ${kaarten.length} cases`;
    }
    if (leeg) leeg.hidden = zichtbaar > 0;
  };

  const bindPillen = () => {
    const pillen = [...container.querySelectorAll('.filter-pil')];
    pillen.forEach((p) => {
      if (p.dataset.gebonden) return;
      p.dataset.gebonden = '1';
      p.addEventListener('click', () => {
        const groep = p.dataset.filter;
        keuze[groep] = p.dataset.waarde;
        [...container.querySelectorAll(`.filter-pil[data-filter="${groep}"]`)].forEach((q) => {
          const aan = q === p;
          q.classList.toggle('is-actief', aan);
          q.setAttribute('aria-pressed', String(aan));
        });
        werkBij();
      });
    });
  };

  /* ----------------------------------------------------------------------
     Laden uit de database
     -------------------------------------------------------------------- */
  const datumVan = (r) => r.content?.publicatiedatum || (r.created_at || '').slice(0, 10) || '';

  const laad = async () => {
    let rijen;
    try {
      const antwoord = await fetch(`${SUPABASE_URL}${TABEL}?select=slug,created_at,content&published=is.true`, {
        headers: { apikey: SUPABASE_KEY, Authorization: `Bearer ${SUPABASE_KEY}`, Accept: 'application/json' },
      });
      if (!antwoord.ok) throw new Error(`HTTP ${antwoord.status}`);
      rijen = await antwoord.json();
    } catch (e) {
      /* Geen database: de kaarten uit de HTML blijven staan. */
      console.warn('Cases niet uit de database geladen, de vaste kaarten blijven staan.', e);
      return;
    }
    if (!Array.isArray(rijen) || !container.isConnected) return;

    rijen.sort((a, b) => datumVan(b).localeCompare(datumVan(a)));
    raster.innerHTML = rijen.map(kaart).join('\n');

    /* Branchepillen opnieuw, uit wat er werkelijk aan cases is. */
    if (brancheGroep) {
      const branches = [];
      rijen.forEach((r) => { const b = (r.content?.branche || '').trim(); if (b && !branches.includes(b)) branches.push(b); });
      if (!branches.some((b) => sleutel(b) === keuze.branche)) keuze.branche = 'alles';
      brancheGroep.innerHTML = pil('branche', 'alles', 'Alle branches', keuze.branche === 'alles')
        + branches.map((b) => pil('branche', sleutel(b), b, sleutel(b) === keuze.branche)).join('');
    }

    bindPillen();
    werkBij();
    window.ScrollTrigger?.refresh();
  };

  bindPillen();
  werkBij();
  laad();
})();
