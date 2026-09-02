# -*- coding: utf-8 -*-
"""Eén template, drie servicepagina's. Alleen de inhoud verschilt."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from schil import _plat
import json

UIT = pathlib.Path("/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE/madegro")

ICONEN = {
    "vinkje": '<path d="M9.6 16.2 5.4 12l-1.4 1.4 5.6 5.6L20.4 8.2 19 6.8 9.6 16.2Z"/>',
    "schild": '<path d="M12 2 4 5v6.5c0 4.6 3.2 8.4 8 10.5 4.8-2.1 8-5.9 8-10.5V5l-8-3Zm0 2.2 6 2.2v5.1c0 3.5-2.3 6.5-6 8.3-3.7-1.8-6-4.8-6-8.3V6.4l6-2.2Z"/>',
    "lijst": '<path d="M3 5h4v4H3V5Zm6 1h12v2H9V6ZM3 10h4v4H3v-4Zm6 1h12v2H9v-2ZM3 15h4v4H3v-4Zm6 1h12v2H9v-2Z"/>',
    "trap": '<path d="M3 21v-4h5v-4h5V9h5V5h3v18H3Zm2-2h14V7h-1v4h-5v4H8v4H5v0Z"/>',
    "klok": '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Zm0 2a8 8 0 1 1 0 16 8 8 0 0 1 0-16Zm-1 3v6l5 3 1-1.7-4-2.3V7h-2Z"/>',
    "mensen": '<path d="M9 11a4 4 0 1 0 0-8 4 4 0 0 0 0 8Zm0-6a2 2 0 1 1 0 4 2 2 0 0 1 0-4Zm7 6a3 3 0 1 0 0-6 3 3 0 0 0 0 6ZM2 21v-2c0-2.8 3.1-4 7-4s7 1.2 7 4v2H2Zm2-2h10c0-1.2-1.9-2-5-2s-5 .8-5 2Zm14 2v-2c0-1.2-.4-2.2-1.1-3 3 .3 5.1 1.5 5.1 3v2h-4Z"/>',
    "grafiek": '<path d="M3 21V3h2v16h16v2H3Zm4-4V9h3v8H7Zm5 0V5h3v12h-3Zm5 0v-6h3v6h-3Z"/>',
    "document": '<path d="M6 2h8l6 6v14H6V2Zm2 2v16h10V9h-5V4H8Zm7 .4V7h2.6L15 4.4ZM9 12h8v2H9v-2Zm0 4h8v2H9v-2Z"/>',
}


def icoon(naam):
    return f'<svg class="voordeel__icoon" width="24" height="24" viewBox="0 0 24 24" aria-hidden="true">{ICONEN[naam]}</svg>'


def herkenningskaarten(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">Situatie {i + 1:02d}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (titel, tekst) in enumerate(items))


def stappen(items):
    """Het stappenplan als oplopende trap. Bij Veilig gedrag zijn dit de vijf
       treden van de Veiligheidsladder, bij de andere diensten drie stappen."""
    return "\n".join(f'''        <li class="trede" style="--trede:{i}">
          <span class="trede__nummer">{i + 1:02d}</span>
          <div class="trede__inhoud">
            <h3 class="trede__titel">{titel}</h3>
            <p class="trede__tekst">{tekst}</p>
            {f'<p class="trede__gedrag"><span>Herkenbaar gedrag</span> {gedrag}</p>' if gedrag else ''}
          </div>
        </li>''' for i, (titel, tekst, gedrag) in enumerate(items))


def voordelen(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            {icoon(ico)}
            <h3 class="voordeel__titel">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (ico, titel, tekst) in enumerate(items))


def partners(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">{sub}</span>
            <h3 class="panel__title">{naam}</h3>
            <p class="panel__body">{tekst}</p>
            <p class="panel__actie">
              <a class="button button--link" href="{link}" target="_blank" rel="noopener">
                Naar de website
              </a>
            </p>
          </div>
        </div>''' for i, (naam, sub, tekst, link) in enumerate(items))


def projecten(dienst):
    """De cases die bij deze dienst horen, uit dezelfde lijst als het overzicht."""
    van_ons = [c for c in CASES if c["dienst"] == dienst]
    return "\n".join(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="case-{c["slug"]}.html" aria-label="{c["klant"]}: {_plat(c["titel"])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">
            <span class="cases-grid__meta-item">{c["branche"]}</span>
            <span class="cases-grid__meta-item">{c["plaats"]}</span>
          </div>
          <h3 class="cases-grid__title">{c["klant"]}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{c["kort"]}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(c["beeld"], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>''' for i, c in enumerate(van_ons))


def servicepagina(cfg):
    inhoud = f'''  <!-- ================= 01 INTRODUCTIE ================= -->
  <section class="paginahero" id="s01-introductie">
    <div class="paginahero__kop">
      <span class="subtitle">{cfg["eyebrow"]}</span>
      <h1 class="paginahero__titel">{cfg["h1"]}</h1>
    </div>
    <div class="paginahero__beeld">
      {foto(cfg["hero_foto"], laden="eager", maten="(max-width: 767px) 100vw, 50vw")}
    </div>
  </section>

  <!-- ================= 02 STATEMENT ================= -->
  <section class="content-text-side-cta" id="s02-statement">
    <div class="container">
      <div class="content-text-side-cta--container">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body">
{cfg["intro"]}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop("Contact opnemen", "contact.html")}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 03 WANNEER GESCHIKT ================= -->
  <section class="content-block" id="s03-wanneer-geschikt">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Herkenbaar?</span>
            <h2 class="section-heading">Wanneer is dit iets voor jouw bedrijf?</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">{cfg["wanneer_intro"]}</p>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--3">
{herkenningskaarten(cfg["herkenning"])}
      </div>
    </div>
  </section>

  <!-- ================= 04 HOE WERKEN WIJ ================= -->
  <section class="band background--grey" id="s04-hoe-werken-wij">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Aanpak</span>
          <h2 class="section-heading">{cfg["aanpak_kop"]}</h2>
          <p class="article-body" style="margin-top:var(--space-500)">{cfg["aanpak_intro"]}</p>
        </div>
        <div class="col-lg-8 col-12">
          {cfg.get("stappen_comment", "")}
          <ol class="trap" role="list">
{stappen(cfg["stappen"])}
          </ol>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 05 VOORDELEN ================= -->
  <section class="content-block" id="s05-voordelen">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Wat het oplevert</span>
            <h2 class="section-heading">{cfg["voordelen_kop"]}</h2>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--4">
{voordelen(cfg["voordelen"])}
      </div>
    </div>
  </section>

  <!-- ================= 06 PARTNERS ================= -->
  <section class="content-block" id="s06-samenwerking">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Samenwerking</span>
            <h2 class="section-heading">Met wie we samenwerken</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              Sommige vragen zijn zo specialistisch dat je er een partner bij wilt. We werken vast samen met een aantal bureaus, zodat je niet zelf op zoek hoeft.
            </p>
          </div>
        </div>
      </div>
      <!-- TODO-CONTENT: welke partners worden getoond, met welk logo en welke link? -->
      <div class="panel-row panel-row--3">
{partners(cfg["partners"])}
      </div>
    </div>
  </section>

  <!-- ================= 07 PROJECTEN ================= -->
  <section class="cases-grid" id="s07-projecten">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">Uit de praktijk</h2>
        {knop("Alle cases", "cases.html", "secundair")}
      </div>
      <!-- TODO-CONTENT: echte projecten aanleveren; onderstaande zijn fictief -->
      <div class="cases-grid__list">
{projecten(cfg["service_naam_kort"])}
      </div>
    </div>
  </section>

{faq_blok("08", cfg["faq"])}

{slotblok("09", cfg["contact_kop"])}
'''

    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"],
        titel=cfg["titel"],
        omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"],
        pagina_css="service.css",
        css_naam="service",
        inhoud=inhoud,
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "Service",
            "serviceType": cfg["service_type"],
            "name": cfg["service_naam"],
            "description": cfg["omschrijving"],
            "areaServed": "NL",
            "provider": {"@type": "Organization", "name": "Madegro Advies B.V."},
        }, ensure_ascii=False, indent=2) + "\n</script>\n<script type=\"application/ld+json\">\n" + faq_ld(cfg["faq"]),
    ), encoding="utf-8")
    print(cfg["bestand"], "geschreven")
