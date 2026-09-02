/* ============================================================================
   cases.js: de filters op het cases-overzicht
   ----------------------------------------------------------------------------
   Twee groepen pillen: dienst en branche. Binnen een groep geldt er één
   tegelijk, en de eerste pil ('alle') zet de groep weer open. De kaarten staan
   gewoon in de HTML en worden alleen verborgen, zodat de pagina zonder
   JavaScript alle cases laat zien.

   Alles in één functie, zodat het bestand opnieuw uitgevoerd kan worden na een
   pagina-overgang.
   ========================================================================== */

(() => {
  /* Tijdens een overgang staan twee pagina's in de DOM; zoek binnen de eigen. */
  const container = document.currentScript?.closest('[data-barba="container"]') || document;

  const raster = container.querySelector('#caseRaster');
  if (!raster) return;

  const pillen = [...container.querySelectorAll('.filter-pil')];
  const kaarten = [...raster.querySelectorAll('.case-kaart')];
  const telling = container.querySelector('.cases-overzicht__telling');
  const leeg = container.querySelector('.cases-overzicht__leeg');

  const keuze = { dienst: 'alles', branche: 'alles' };

  const werkBij = () => {
    let zichtbaar = 0;
    kaarten.forEach((kaart) => {
      const past = (keuze.dienst === 'alles' || kaart.dataset.dienst === keuze.dienst)
                && (keuze.branche === 'alles' || kaart.dataset.branche === keuze.branche);
      kaart.hidden = !past;
      if (past) zichtbaar++;
    });

    /* De achtergrond van een kaart wisselt om en om. Omdat er kaarten
       wegvallen, moet die wisseling opnieuw geteld worden over wat er
       overblijft; anders staan er twee grijze naast elkaar. */
    let n = 0;
    kaarten.forEach((kaart) => {
      if (kaart.hidden) return;
      kaart.classList.toggle('is-even', n % 2 === 1);
      n++;
    });

    if (telling) {
      telling.textContent = zichtbaar === kaarten.length
        ? `${kaarten.length} cases`
        : `${zichtbaar} van ${kaarten.length} cases`;
    }
    if (leeg) leeg.hidden = zichtbaar > 0;
  };

  pillen.forEach((pil) => {
    pil.addEventListener('click', () => {
      const groep = pil.dataset.filter;
      keuze[groep] = pil.dataset.waarde;
      pillen.filter((p) => p.dataset.filter === groep).forEach((p) => {
        const aan = p === pil;
        p.classList.toggle('is-actief', aan);
        p.setAttribute('aria-pressed', String(aan));
      });
      werkBij();
    });
  });

  werkBij();
})();
