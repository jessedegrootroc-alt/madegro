# -*- coding: utf-8 -*-
"""Eén template, drie servicepagina's. Alleen de inhoud verschilt."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from iconen import icoon as _icoon
from schil import _plat
import json

UIT = pathlib.Path("/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE/madegro")

# Namen in de iconenset (assets/iconen/), per voordeel; zie iconen.py.
ICONEN = {
    "vinkje": "check",
    "schild": "shield-check",
    "lijst": "list-check",
    "trap": "stairs",
    "klok": "clock",
    "mensen": "users",
    "grafiek": "chart-bar-trend-up",
    "document": "file-check",
}


def icoon(naam):
    return _icoon(ICONEN[naam], klasse="voordeel__icoon", maat=24)


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


def sponsors(items):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">{sub}</span>
            <h3 class="panel__title">{naam}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (naam, sub, tekst, link) in enumerate(items))


def projecten(dienst):
    """De cases die bij deze dienst horen, uit dezelfde lijst als het overzicht."""
    van_ons = [c for c in CASES if c["dienst"] == dienst]
    return "\n".join(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="case.html?slug=case-{c["slug"]}" aria-label="{c["klant"]}: {_plat(c["titel"])}">
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
    # Welke kant van de foto overblijft als het vak smaller is dan de foto.
    # Op een bureaublad is het vak bijna vierkant en de foto's zijn liggend, dus
    # er valt altijd een deel af; "links" houdt de linkerhelft, anders het midden.
    hero_klasse = " paginahero--beeld-links" if cfg.get("hero_positie") == "links" else ""
    inhoud = f'''  <!-- ================= 01 INTRODUCTIE ================= -->
  <section class="paginahero paginahero--hoog{hero_klasse}" id="s01-introductie">
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

  <!-- ================= 06 SPONSORS ================= -->
  <section class="content-block" id="s06-sponsors">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Sponsoring</span>
            <h2 class="section-heading">Onze sponsors</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              MADEGRO wordt gesteund door een aantal sponsors. Dit zijn ze.
            </p>
          </div>
        </div>
      </div>
      <!-- TODO-CONTENT: welke sponsors worden getoond, met welk logo en welke link? -->
      <div class="panel-row panel-row--3">
{sponsors(cfg["sponsors"])}
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
