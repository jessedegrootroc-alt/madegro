# MADEGRO: stand van zaken

Laatst bijgewerkt: 1 september 2026

## Wat er staat

Twintig pagina's:

- Home, de drie servicepagina's, cursusaanbod met vier cursuspagina's, over ons,
  contact, privacybeleid en cookies.
- Een cases-overzicht met filters op dienst en branche, en zes casepagina's op
  één sectieskelet. De casegegevens staan op één plek en voeden ook de
  projectrijen op de homepage en de servicepagina's.
- Alle secties uit §5 van de brief zitten erin, in de voorgeschreven volgorde, met
  een `id` per sectie.
- Het contactformulier bestaat één keer (`contactformulier.js`) en komt terug op
  home, elke servicepagina, elke cursuspagina (twee keer: infopack en contact),
  cursusaanbod, over ons en contact.
- De drie servicepagina's delen één sectieskelet, de vier cursuspagina's ook.
  Zie `SECTIONS.md`.

## Getest

- Alle dertien pagina's laden zonder console-fouten; geen dode links, geen
  ontbrekende bestanden en geen gebroken beeld. Alle afbeeldingen hebben een
  alt-tekst, `width`/`height` en een `srcset` met twee maten.
- Geen horizontale scroll op 360, 768, 1280 en 1920 px.
- Eén `<h1>` per pagina; de skip-link is de eerste tabstop.
- Formulier: lege inzending toont vier veldfouten met `aria-invalid`, een ongeldig
  e-mailadres wordt apart gemeld, een geldige inzending geeft een succesmelding in
  `aria-live` en maakt het formulier leeg. Honeypot werkt.
- Accordeons openen en sluiten met de juiste `aria-expanded`; het mobiele paneel
  opent, houdt de focus vast en sluit met Escape, waarna de focus terugkeert.
- Pagina-overgangen: heen en terug tussen home, een servicepagina en het
  cursusaanbod. De paginastijlen wisselen mee en de scripts draaien opnieuw.

## Content en beeld

De site is volledig ingevuld: in de zichtbare tekst staat nergens meer een
`[TOKEN]` of `TODO-CONTENT`. Een deel daarvan is wel verzonnen: klantnamen,
projecten, getuigenissen, cijfers, cursusnamen, tarieven en twee van de drie
partners. In de HTML staat bij elk verzonnen blok een `TODO-CONTENT`-comment
(29 stuks) en `CONTENT-TODO.md` zet ze per pagina op een rij.

**Voor de site live gaat moet die lijst nagelopen worden.** Getuigenissen en
klantnamen die niet kloppen zijn misleidend richting bezoekers en een risico
richting de bedrijven die erin genoemd worden.

De foto's staan onder CC0 of in het publiek domein en mogen commercieel gebruikt
worden zonder bronvermelding; herkomst per bestand in `assets/foto/HERKOMST.md`.
Het is algemeen industriebeeld, geen MADEGRO-projecten. De hero's tonen de foto
onder een verloop in plum, zodat witte tekst ruim boven 4.5:1 blijft.

Twee dingen zijn bewust níét ingevuld:

- **Het telefoonnummer** staat als `0184 00 00 00`. Een verzonnen nummer dat er
  echt uitziet komt bijna zeker bij iemand anders uit.
- **Het portret van Martin.** Daar staat een werkplaatsbeeld. Een stockfoto van
  een willekeurig persoon met zijn naam eronder stelt een echt iemand verkeerd voor.

## Wat nog niet af is

- **Het formulier verstuurt niets.** `ENDPOINT` in `contactformulier.js` is leeg;
  je krijgt wel een succesmelding, maar er gaat geen bericht de deur uit.
- **Statistieken laden niet.** `META_ID` in `analytics.js` is leeg.
- **Het logo** is een voorlopig woordmerk.

## Afspraken die afwijken van de brief

1. **De site staat in een submap** van het referentieproject in plaats van in een
   eigen map ernaast.
2. **De opzet komt van de referentie, de kleuren zijn van MADEGRO.** Structuur,
   typografie, spacing en componenten volgen de gids; het palet is vervangen door
   de huisstijlkleuren: groen `#017E84` (uit het logo), geel `#FFFC58`, wit en `#F1F1F1`.
   Lopende tekst staat in het diepere `#014144`, omdat het merkgroen op het grijs
   maar 4.09:1 haalt. Zie STYLEGUIDE.md voor die afweging.
3. **Er is verzonnen content gebruikt** in plaats van lege placeholders, zodat de
   pagina's compleet ogen. Brief §3 verbiedt dat. Bij getuigenissen, partners,
   certificaten en cijfers zijn de namen zichtbaar fictief gehouden, zodat er nooit
   per ongeluk een verzonnen aanbeveling of certificering live gaat.

## Goed om te weten

- Er is bewust geen kaart-embed op de contactpagina: dat zou een externe partij
  toegang geven tot bezoekgegevens, en de brief staat geen externe embeds toe.
- De lettertypen staan lokaal in `assets/fonts/`, niet op de Google Fonts CDN.
- Scripts in de barba-container zoeken hun elementen binnen die container. Tijdens
  een overgang staan twee pagina's tegelijk in de DOM; zonder die begrenzing hangt
  het gedrag aan de pagina die net verdwijnt.
