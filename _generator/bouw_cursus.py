# -*- coding: utf-8 -*-
"""Eén template, vier cursuspagina's."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from schil import _plat

UIT = pathlib.Path("/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE/madegro")


def kaartrij(items, klasse="panel-row--4"):
    return "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <span class="panel__meta">{meta}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (meta, titel, tekst) in enumerate(items))


def tijdlijn(items):
    return "\n".join(f'''        <li class="trede" style="--trede:{i}">
          <span class="trede__nummer">{i + 1:02d}</span>
          <div class="trede__inhoud">
            <h3 class="trede__titel">{titel}</h3>
            <p class="trede__tekst">{tekst}</p>
            <p class="trede__gedrag"><span>Tijdsbeslag</span> {duur}</p>
          </div>
        </li>''' for i, (titel, tekst, duur) in enumerate(items))


def deelnemers_regel(cfg):
    """Hoeveel mensen de cursus al gedaan hebben. Zonder cijfer een zichtbaar
       gat in plaats van een aanname."""
    aantal = cfg.get("deelnemers")
    if not aantal:
        return ('Al <span class="invulveld">aantal nog invullen</span> deelnemers '
                'gingen je voor.')
    return f'Al <strong>{aantal}</strong> deelnemers gingen je voor.'


def cursuspagina(cfg):
    """De volgorde volgt wat iemand die de cursus overweegt achter elkaar wil
       weten: wat is het, wat kost het en hoe lang duurt het, is het voor mij,
       wat lever ik ermee op, hoe ziet het eruit, wat neem ik mee, waarom hier,
       wat zeggen anderen, en dan pas het formulier.

       De opbouw wisselt bewust van vorm: tekstband, cijferrij, beeld naast
       tekst, lijst, beeld met uitloop, trap, kaarten. Twee blokken van dezelfde
       soort staan nergens achter elkaar."""

    resultaten = chr(10).join(
        f'              <li><svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true">'
        f'<path d="M9.6 16.2 5.4 12l-1.4 1.4 5.6 5.6L20.4 8.2 19 6.8 9.6 16.2Z"/></svg>{r}</li>'
        for r in cfg["resultaten"])

    inhoud = f'''  <!-- ================= 01 INTRODUCTIE ================= -->
  <section class="service-hero" id="s01-introductie" data-header-theme="light">
    <div class="service-hero--beeld" aria-hidden="true">
      {foto(cfg["hero_foto"], laden="eager", maten="100vw")}
      <span class="service-hero--sluier"></span>
    </div>
    <div class="container">
      <div class="service-hero--inner">
        <span class="subtitle" style="color:var(--color-white)">Cursus &middot; {cfg["duur"]} &middot; {cfg["doelgroep"].replace("Voor ", "")}</span>
        <h1 class="service-hero--titel">{cfg["titel_kort"]}</h1>
        <div class="article-body service-hero--intro">
{cfg["intro_kort"]}
        </div>
        <div class="hero--actions">
          {knop("Infopack aanvragen", "#s11-infopack")}
          {knop("Alle cursussen", "cursusaanbod.html", "secondary")}
        </div>
        <!-- TODO-CONTENT: het aantal deelnemers moet van Martin komen. Er stond
             eerder "450 cursisten opgeleid" op de homepage; dat cijfer was
             verzonnen en is weggehaald. Hier dus geen nieuw getal verzinnen:
             zolang het veld leeg is staat er een geel invulveld, dat kan niet
             per ongeluk live. -->
        <p class="hero--bewijs">{deelnemers_regel(cfg)}</p>
      </div>
    </div>
  </section>

  <!-- ================= 02 STATEMENT =================
       De tweede alinea van de inleiding, losgetrokken uit de kop. Zo begint de
       pagina niet met vier alinea's onder elkaar. -->
  <section class="content-text-side-cta" id="s02-statement">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body">
{cfg["statement"]}
            </div>
          </div>
          <div class="col-lg-4 col-12 statement__actie">
            {knop("Infopack aanvragen", "#s11-infopack")}
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 03 IN HET KORT =================
       Duur, doorlooptijd, groep en prijs meteen bij de hand: dat zijn de vier
       dingen waar iemand op afhaakt of doorleest. -->
  <section class="band background--white" id="s03-in-het-kort">
    <div class="container">
      <div class="kerncijfers">
        <div class="kerncijfer">
          <span class="kerncijfer__label">Tijdsbeslag</span>
          <p class="kerncijfer__getal">{cfg["duur"].split()[0]}<span class="kerncijfer__eenheid">{" ".join(cfg["duur"].split()[1:])}</span></p>
        </div>
        <div class="kerncijfer">
          <span class="kerncijfer__label">Doorlooptijd</span>
          <p class="kerncijfer__getal">{cfg["doorlooptijd_getal"]}<span class="kerncijfer__eenheid">{cfg["doorlooptijd_eenheid"]}</span></p>
        </div>
        <div class="kerncijfer">
          <span class="kerncijfer__label">Groepsgrootte</span>
          <p class="kerncijfer__getal">{GROEP}<span class="kerncijfer__eenheid">deelnemers max.</span></p>
        </div>
        <div class="kerncijfer">
          <!-- TODO-CONTENT: het tarief is een aanname, laat Martin het bevestigen -->
          <span class="kerncijfer__label">Tarief</span>
          <p class="kerncijfer__getal">{PRIJS}<span class="kerncijfer__eenheid">{PRIJS_EENHEID}</span></p>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 04 VOOR WIE ================= -->
  <section class="cta-blocks-advanced" id="s04-voor-wie">
    <div class="container">
      <div class="row g-0">
        <div class="col-12">
          <div class="cta-blocks-advanced__card cta-blocks-advanced__card--horizontal">
            <figure class="cta-blocks-advanced__banner">
              {foto(cfg["voor_wie_foto"], maten="(max-width: 991px) 100vw, 50vw")}
              <span class="cta-blocks-advanced__backdrop" aria-hidden="true"></span>
            </figure>
            <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-grey">
              <span class="subtitle">Voor wie</span>
              <div class="cta-blocks-advanced__wrapper">
                <div>
                  <h2 class="cta-blocks-advanced__title" style="margin-bottom:var(--space-500)">{cfg["doelgroep"]}</h2>
                  <div class="cta-blocks-advanced__content"><p>{cfg["voor_wie"]}</p></div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 05 WAT JE ERMEE KUNT =================
       Stond eerder als lijstje onder de opzet-tekst. Als eigen sectie met twee
       kolommen krijgt het het gewicht dat het verdient: dit is waarvoor iemand
       de cursus boekt. -->
  <section class="band background--grey" id="s05-resultaat">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Resultaat</span>
          <h2 class="section-heading">Na afloop kun je</h2>
        </div>
        <div class="col-lg-8 col-12">
          <ul class="check-lijst check-lijst--twee" role="list">
{resultaten}
          </ul>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 06 DE INHOUD ================= -->
  <section class="content-text-side-visual background--white" id="s06-inhoud">
    <div class="container">
      <div class="row gx-0">
        <article class="col-lg-4 col-12">
          <div class="content-text-side-visual--stack content-text-side-visual--article">
            <h2>Hoe ziet de cursus eruit?</h2>
            <div class="content-text-side-visual--body content-fit--quarter">
{cfg["opzet"]}
            </div>
          </div>
        </article>
      </div>
    </div>
    <div class="content-text-side-visual--visual content-fit--half">
      {foto(cfg["inhoud_foto"], maten="(max-width: 991px) 100vw, 48vw")}
    </div>
  </section>

  <!-- ================= 07 PROGRAMMA ================= -->
  <section class="band background--grey" id="s07-programma">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="margin-bottom:var(--space-500)">Programma</span>
          <h2 class="section-heading">Zo loopt de dag</h2>
          <p class="article-body" style="margin-top:var(--space-500)">De cursus beslaat {cfg["duur"]}, met een doorlooptijd van {cfg["doorlooptijd"]}.</p>
        </div>
        <div class="col-lg-8 col-12">
          <ol class="trap" role="list">
{tijdlijn(cfg["tijdlijn"])}
          </ol>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 08 WAT JE MEENEEMT =================
       Certificaat en vervolgstap bij elkaar: allebei gaan ze over wat er na de
       laatste dag overblijft. -->
  <section class="band background--groen certificaat" id="s08-certificaat">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle" style="color:var(--color-white); margin-bottom:var(--space-500)">Daarna</span>
          <h2 class="section-heading">Wat je meeneemt</h2>
        </div>
        <div class="col-lg-8 col-12">
          <!-- TODO-CONTENT: dit is een eigen deelnamecertificaat van MADEGRO, geen
               extern erkend diploma. Wil Martin een erkend schema, dan moeten naam,
               uitgevende instantie en geldigheidsduur hier worden aangepast. -->
          <div class="article-body content-fit--half">
            <p>Deelnemers ontvangen na afloop het <strong>MADEGRO-deelnamecertificaat</strong>, uitgegeven door Madegro Advies B.V. Het vermeldt de cursus, de datum en de behandelde onderwerpen, en is <strong>twee jaar</strong> geldig. Werkgevers gebruiken het onder meer als onderbouwing bij audits en bij de aantoonbaarheid van voorlichting en onderricht.</p>
{cfg["na_tekst"]}
          </div>
          <p style="margin-top:var(--space-700)">
            {knop(cfg["vervolg_label"], cfg["vervolg_link"], "secondary")}
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 09 WAAROM HIER ================= -->
  <section class="content-block" id="s09-waarom">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Waarom hier</span>
            <h2 class="section-heading">Waarom een cursus bij MADEGRO?</h2>
          </div>
        </div>
      </div>
      <div class="panel-row panel-row--4">
{kaartrij(cfg["waarom"])}
      </div>
    </div>
  </section>

{quoteslider("10", "ervaringen", "Deelnemers", "Wat cursisten zeggen", cfg["testimonials"])}

  <!-- ================= 11 INFOPACK ================= -->
  <section class="band background--grey" id="s11-infopack">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle">Aanmelden</span>
          <h2 class="section-heading" style="margin:var(--space-500) 0">Het infopack</h2>
          <div class="article-body">
            <p>In het infopack staan het volledige programma, de leerdoelen, de kosten en de data waarop deze cursus draait.</p>
            <!-- TODO-CONTENT: infopack als PDF aanleveren. Zolang die er niet is,
                 loopt de aanvraag via dit formulier in plaats van een download. -->
            <p>Vraag hem hieronder aan, dan sturen we hem binnen {REACTIETIJD} toe.</p>
          </div>
        </div>
        <div class="col-lg-8 col-12">
          <div data-contactformulier data-onderwerp="cursus"></div>
          <noscript>
            <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons gerust op
              <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
          </noscript>
        </div>
      </div>
    </div>
  </section>

{faq_blok("12", cfg["faq"])}

{slotblok("13", "Vragen over deze cursus?")}
'''

    (UIT / cfg["bestand"]).write_text(pagina(
        bestand=cfg["bestand"],
        titel=cfg["titel"],
        omschrijving=cfg["omschrijving"],
        namespace=cfg["namespace"],
        pagina_css="cursus.css",
        css_naam="cursus",
        inhoud=inhoud,
        actief="cursusaanbod.html",
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "Course",
            "name": _plat(cfg["titel_kort"]),
            "description": cfg["omschrijving"],
            "provider": {"@type": "Organization", "name": "Madegro Advies B.V."},
            "hasCourseInstance": {
                "@type": "CourseInstance",
                "courseMode": "onsite",
                "courseWorkload": cfg["duur"],
            },
        }, ensure_ascii=False, indent=2) + "\n</script>\n<script type=\"application/ld+json\">\n" + faq_ld(cfg["faq"]),
    ), encoding="utf-8")
    print(cfg["bestand"], "geschreven")
