# Levering: wat de webserver moet doen

De site is statisch: HTML, CSS, JS en assets, geen bouwstap en geen backend. Wat
de laadtijd bepaalt zit daarom voor een groot deel niet in de bestanden maar in
de headers die de server eromheen zet. Deze twee dingen zijn het belangrijkst.

## 1. Comprimeer de tekstbestanden

Zonder compressie is `styleguide.css` 96 kB en `index.html` 61 kB. Met brotli is
dat 22 en 10 kB. Gemeten met Lighthouse op mobiel scheelde dat alleen al bijna
een seconde.

Comprimeren: `text/html`, `text/css`, `text/javascript`, `application/json`,
`image/svg+xml`, `application/xml`, `text/plain`.

Niet comprimeren: webp, mp4 en woff2. Die zitten al in een gecomprimeerd formaat;
er nog een ronde overheen kost tijd en levert niets op.

## 2. Zet de cachetijden goed

| soort | header | waarom |
|---|---|---|
| afbeeldingen, video, fonts | `public, max-age=31536000, immutable` | de maat staat in de naam (`logistiek-1200.webp`); een andere versie krijgt een andere naam |
| CSS en JS | `public, max-age=31536000, immutable` **met een versie in de naam of de query** | anders zie je een wijziging niet |
| HTML | `no-cache` | moet elke keer opnieuw gecontroleerd worden, anders blijft een oude pagina hangen |

Let op bij CSS en JS: er staat nu geen versie in de bestandsnaam. Zolang dat zo
is moeten die op `no-cache`, precies zoals de ontwikkelserver het doet. Wil je ze
wel lang cachen, hang er dan een `?v=` achter en verhoog dat bij elke wijziging;
`page-transitions.js` wisselt de paginastylesheet op `data-page-css`, dus die
query moet daar meebewegen.

## Voorbeelden

**Netlify of Cloudflare Pages** (`_headers` in de hoofdmap, compressie doen ze
zelf):

```
/assets/*
  Cache-Control: public, max-age=31536000, immutable
/*.html
  Cache-Control: no-cache
```

**nginx**:

```nginx
brotli on;
brotli_types text/html text/css text/javascript application/json image/svg+xml;
gzip on;
gzip_types text/html text/css text/javascript application/json image/svg+xml;

location /assets/ { add_header Cache-Control "public, max-age=31536000, immutable"; }
location ~* \.html$ { add_header Cache-Control "no-cache"; }
```

**Apache** (`.htaccess`): `mod_deflate` of `mod_brotli` voor de tekstsoorten
hierboven, en `mod_expires` met dezelfde tijden.

## 3. Ondersteun Range-aanvragen voor de video

Een browser haalt een video niet in één keer op. Hij vraagt om stukken
(`Range: bytes=0-1`, daarna verder) en verwacht daar **206 Partial Content** op
met precies dat stuk, plus `Accept-Ranges: bytes` in het antwoord.

Safari en iOS spelen niets af als de server dat negeert en gewoon 200 met het
hele bestand terugstuurt. Chrome is er soepeler in, dus je ziet het makkelijk
over het hoofd. Vrijwel elke echte webserver en elk statisch platform doet dit
uit zichzelf; de ontwikkelserver doet het nu ook.

## Wat de ontwikkelserver doet

`_generator/server.js` doet dit al: brotli of gzip naar wat de browser accepteert,
Range-aanvragen met 206, zwakke etags zodat `no-cache` iets heeft om tegen te
valideren, een dag cache op afbeeldingen, video en fonts, en `no-cache` op de
rest. Handig om lokaal te meten met Lighthouse, maar het is geen productieserver.

Let op het verschil met de tabel hierboven: daar staat een jaar met `immutable`,
hier een dag zonder. Tijdens het bouwen wordt een bestand weleens vervangen
zonder dat de naam verandert, en met `immutable` zit je daar een jaar aan vast.

## Nog te doen bij het live zetten

- **CDN.** De site heeft er nu geen. Vanaf Nederland scheelt dat weinig, maar de
  vier scripts van GSAP en Barba komen wel van jsDelivr; daar staat een
  `preconnect` voor in de kop van elke pagina.
- **HTTP/2 of HTTP/3.** De pagina's doen 20 tot 28 verzoeken. Over HTTP/1.1 is
  dat merkbaar, over HTTP/2 niet.
