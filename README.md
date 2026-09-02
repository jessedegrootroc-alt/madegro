# MADEGRO: website

Statische site voor Madegro Advies B.V.: HTML, CSS en vanilla JavaScript, geen
build-stap en geen npm-afhankelijkheden. Van een CDN komen alleen GSAP (met de
plug-ins ScrollTrigger en ScrollSmoother) en Barba.js: samen doen die de
pagina-overgangen en het vloeiende scrollen.

## Lokaal draaien

Open `index.html` in de browser, of draai een server vanuit deze map:

    npx serve -l 5500 .

De site staat nu in een submap van het referentieproject, dus via die server draait
hij ook op `http://localhost:5500/madegro/`. Alle links zijn relatief, dus de map
kan zonder aanpassing als eigen site gepubliceerd worden.

## Publiceren

Statisch, werkt zonder configuratie op GitHub Pages, Netlify, Vercel of Cloudflare
Pages: wijs de host naar deze map. Zet daarna in `sitemap.xml`, `robots.txt` en de
`canonical`- en Open Graph-tags het juiste domein.

## Structuur

```
index.html              Home
veilig-gedrag.html      ┐
ehs-rie.html            ├ drie servicepagina's, één sectieskelet
safety-checks.html      ┘
cases.html              overzicht met filters
case-*.html             zes casepagina's, één sectieskelet
cursusaanbod.html       overzicht
cursus-*.html           vier cursuspagina's, één sectieskelet
over-ons.html  contact.html
privacybeleid.html  cookies.html

STYLEGUIDE.md           het ontwerpsysteem en waar deze site afwijkt
SECTIONS.md             het sectieskelet dat de pagina's delen
CONTENT-TODO.md         alles wat nog aangeleverd moet worden

styleguide.css          tokens en componenten, geldt overal
index.css  service.css  cursus.css  cases.css  contact.css  over-ons.css  tekstpagina.css
cookiebalk.css  transitions.css

site.js                 header, mobiel paneel, accordeons, op elke pagina
contactformulier.js     het contactformulier, één keer
index.js                alleen de tellers op de homepage
cases.js                de filters op het cases-overzicht
smooth-scroll.js        vloeiend scrollen met GSAP ScrollSmoother
page-transitions.js     Barba.js + GSAP
cookiebalk.js  analytics.js

assets/                 logo, fonts, favicons, deelafbeelding
sitemap.xml  robots.txt
```

## Werken aan deze site

- Lees eerst `SECTIONS.md`. Pagina's van hetzelfde type delen hun structuur; er zijn
  geen includes, dus een wijziging aan een servicesectie moet in alle drie.
- Nieuwe kleuren, maten of afstanden komen uit de tokens in `styleguide.css`.
- Het contactformulier verstuurt nog niets: zet het endpoint in `contactformulier.js`.
- Statistieken laden pas na toestemming en alleen als er een meet-ID staat in
  `analytics.js`. Dat veld is nu bewust leeg.
