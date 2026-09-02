/* ============================================================================
   contactformulier.js: het contactformulier, één keer
   ----------------------------------------------------------------------------
   Het formulier komt op bijna elke pagina terug. In plaats van dezelfde honderd
   regels HTML dertien keer te herhalen, staat het hier één keer en rendert het
   zich in elke <div data-contactformulier data-onderwerp="…"> op de pagina.

   Voor bezoekers zonder JavaScript staat er in de HTML een <noscript> met het
   e-mailadres en telefoonnummer, zodat de pagina bruikbaar blijft.

   Alles zit in één functie, zodat het bestand ook opnieuw uitgevoerd kan worden
   na een pagina-overgang (zie page-transitions.js).
   ========================================================================== */

(() => {
  /* Tijdens een pagina-overgang staan de oude en de nieuwe pagina even samen in
     de DOM. document.getElementById zou dan het element van de oude pagina
     teruggeven, en dan hangt het gedrag aan een pagina die zo verdwijnt.
     Daarom zoeken we alles binnen de container waar dit script zelf in staat. */
  const container = document.currentScript?.closest('[data-barba="container"]') || document;

  const ONDERWERPEN = [
    ['veilig-gedrag', 'Veilig gedrag'],
    ['ehs-rie', 'EHS RIE'],
    ['safety-checks', 'Safety Checks'],
    ['cursus', 'Cursus'],
    ['overig', 'Overig'],
  ];

  /* TODO-CONTENT: waar moet de inzending naartoe? Zolang dit niet gekoppeld is,
     laat het formulier zien dat het verstuurd is, maar gaat er niets de deur
     uit. Zet hieronder het endpoint of de formulierdienst neer. */
  const ENDPOINT = '';

  async function submitContactForm(payload) {
    // TODO: koppel aan endpoint (eigen backend of formulierdienst)
    if (!ENDPOINT) {
      console.info('Contactformulier nog niet gekoppeld. Inzending:', payload);
      return { ok: true, gekoppeld: false };
    }
    const antwoord = await fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
      body: JSON.stringify(payload),
    });
    return { ok: antwoord.ok, gekoppeld: true };
  }
  window.submitContactForm = submitContactForm;

  const VELDEN = [
    { naam: 'naam',    label: 'Naam',        type: 'text',  autocomplete: 'name',              verplicht: true },
    { naam: 'bedrijf', label: 'Bedrijfsnaam', type: 'text', autocomplete: 'organization',      verplicht: false },
    { naam: 'email',   label: 'E-mailadres', type: 'email', autocomplete: 'email',             verplicht: true },
    { naam: 'telefoon', label: 'Telefoonnummer', type: 'tel', autocomplete: 'tel',             verplicht: false },
  ];

  const fout = {
    naam: 'Vul je naam in.',
    email: 'Vul een geldig e-mailadres in.',
    telefoon: 'Vul een geldig telefoonnummer in, of laat het veld leeg.',
    bericht: 'Schrijf kort waar het over gaat.',
    akkoord: 'Je moet akkoord gaan met het privacybeleid.',
  };

  const geldigEmail = (waarde) => /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(waarde.trim());
  const geldigTelefoon = (waarde) => waarde.trim() === '' || /^[+\d][\d\s().-]{7,}$/.test(waarde.trim());

  const bouw = (houder) => {
    const gekozen = houder.dataset.onderwerp || 'overig';
    const id = 'cf-' + Math.abs(gekozen.split('').reduce((a, c) => a + c.charCodeAt(0), 0)) + '-' + houder.dataset.index;

    const velden = VELDEN.map((v) => `
      <div class="veld">
        <label class="field__label" for="${id}-${v.naam}">${v.label}${v.verplicht ? ' *' : ''}</label>
        <input class="field" id="${id}-${v.naam}" name="${v.naam}" type="${v.type}"
               autocomplete="${v.autocomplete}"${v.verplicht ? ' required' : ''}
               aria-describedby="${id}-${v.naam}-fout">
        <p class="veld__fout" id="${id}-${v.naam}-fout" hidden></p>
      </div>`).join('');

    const opties = ONDERWERPEN.map(([waarde, label]) =>
      `<option value="${waarde}"${waarde === gekozen ? ' selected' : ''}>${label}</option>`).join('');

    houder.innerHTML = `
      <form class="contactformulier" novalidate>
        <div class="veld-rij">
          ${velden}
        </div>

        <div class="veld">
          <label class="field__label" for="${id}-onderwerp">Waar gaat het over?</label>
          <select class="field" id="${id}-onderwerp" name="onderwerp">${opties}</select>
        </div>

        <div class="veld">
          <label class="field__label" for="${id}-bericht">Bericht *</label>
          <textarea class="field" id="${id}-bericht" name="bericht" rows="6" required
                    aria-describedby="${id}-bericht-fout"></textarea>
          <p class="veld__fout" id="${id}-bericht-fout" hidden></p>
        </div>

        <div class="veld">
          <label class="akkoord">
            <input type="checkbox" id="${id}-akkoord" name="akkoord" required
                   aria-describedby="${id}-akkoord-fout">
            <span>Ik ga akkoord met het <a href="privacybeleid.html">privacybeleid</a> *</span>
          </label>
          <p class="veld__fout" id="${id}-akkoord-fout" hidden></p>
        </div>

        <!-- Onzichtbaar veld tegen spambots: mensen zien het niet, bots vullen het in. -->
        <input type="text" name="_bericht_extra" tabindex="-1" autocomplete="off"
               aria-hidden="true" class="honeypot">

        <div class="contactformulier__voet">
          <button type="submit" class="button button--primary"><span class="button__inhoud">Versturen<span class="button__spoor" aria-hidden="true"><svg class="arrow--animation is-1" width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg><svg class="arrow--animation is-2" width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg></span></span></button>
        </div>

        <p class="contactformulier__melding" role="status" aria-live="polite"></p>
      </form>`;

    const form = houder.querySelector('form');
    const melding = houder.querySelector('.contactformulier__melding');

    const toonFout = (veld, tekst) => {
      const doel = form.elements[veld];
      const regel = houder.querySelector(`#${id}-${veld}-fout`);
      if (!doel || !regel) return;
      if (tekst) {
        regel.textContent = tekst;
        regel.hidden = false;
        doel.setAttribute('aria-invalid', 'true');
      } else {
        regel.hidden = true;
        doel.removeAttribute('aria-invalid');
      }
    };

    const controleer = () => {
      const w = (naam) => (form.elements[naam]?.value || '').trim();
      const fouten = [];
      if (!w('naam')) fouten.push(['naam', fout.naam]);
      if (!geldigEmail(w('email'))) fouten.push(['email', fout.email]);
      if (!geldigTelefoon(w('telefoon'))) fouten.push(['telefoon', fout.telefoon]);
      if (w('bericht').length < 5) fouten.push(['bericht', fout.bericht]);
      if (!form.elements.akkoord.checked) fouten.push(['akkoord', fout.akkoord]);

      ['naam', 'email', 'telefoon', 'bericht', 'akkoord'].forEach((veld) => toonFout(veld, null));
      fouten.forEach(([veld, tekst]) => toonFout(veld, tekst));
      return fouten;
    };

    /* Pas controleren zodra iemand een veld verlaat: tijdens het typen
       foutmeldingen tonen leest als vitten. */
    form.addEventListener('blur', (e) => {
      if (e.target.name && e.target.getAttribute('aria-invalid')) controleer();
    }, true);

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const fouten = controleer();

      if (fouten.length) {
        melding.textContent = fouten.length === 1
          ? 'Er staat nog iets open in het formulier.'
          : `Er staan nog ${fouten.length} dingen open in het formulier.`;
        melding.className = 'contactformulier__melding is-fout';
        form.elements[fouten[0][0]].focus();
        return;
      }

      /* Honeypot ingevuld: doen alsof het gelukt is en niets versturen. */
      if (form.elements._bericht_extra.value) {
        melding.textContent = 'Bedankt, je bericht is verstuurd.';
        melding.className = 'contactformulier__melding is-goed';
        return;
      }

      const knop = form.querySelector('button[type="submit"]');
      knop.disabled = true;
      const oudeTekst = knop.textContent;
      knop.textContent = 'Versturen…';

      try {
        const payload = {
          naam: form.elements.naam.value.trim(),
          bedrijf: form.elements.bedrijf.value.trim(),
          email: form.elements.email.value.trim(),
          telefoon: form.elements.telefoon.value.trim(),
          onderwerp: form.elements.onderwerp.value,
          bericht: form.elements.bericht.value.trim(),
        };
        const { ok } = await submitContactForm(payload);
        if (!ok) throw new Error('verzenden mislukt');

        form.reset();
        melding.textContent = 'Bedankt, je bericht is binnen. We reageren binnen twee werkdagen.';
        melding.className = 'contactformulier__melding is-goed';
      } catch (err) {
        melding.textContent = 'Het versturen lukte niet. Mail ons op info@madegro.nl of bel 0184 00 00 00.';
        melding.className = 'contactformulier__melding is-fout';
      } finally {
        knop.disabled = false;
        knop.textContent = oudeTekst;
      }
    });
  };

  container.querySelectorAll('[data-contactformulier]').forEach((houder, i) => {
    houder.dataset.index = i;
    bouw(houder);
  });
})();
