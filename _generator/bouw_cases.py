# -*- coding: utf-8 -*-
"""Het cases-overzicht met filters, en de ene detailpagina case.html.

   De cases zelf staan in Supabase (tabel posts). cases.js vult het overzicht
   uit de database; de kaarten die hier uit CASES komen zijn het vertrekpunt
   en de terugval als de database niet antwoordt. case.js bouwt de
   detailpagina uit de rij met de slug uit ?slug=. Er worden geen losse
   case-<slug>.html-bestanden meer gebouwd; vercel.json stuurt oude links
   door naar case.html?slug=."""
import sys, pathlib, json, re, html
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from schil import _plat

UIT = pathlib.Path("/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE/madegro")

VINKJE = ('<span class="filter-pil__vink" aria-hidden="true">'
          '<svg viewBox="0 0 24 24" width="14" height="14" fill="currentColor">'
          '<path d="M10 15.2 19.2 6l1.4 1.4L10 18 3.6 11.6 5 10.2 10 15.2Z"/></svg></span>')


def sleutelvorm(waarde):
    """'EHS RIE' -> 'ehs-rie', zodat het in een data-attribuut past."""
    return re.sub(r'[^a-z0-9]+', '-', _plat(waarde).lower()).strip('-')


def filtergroep(label, naam, waarden, alles):
    pillen = [f'''          <button type="button" class="filter-pil is-actief" data-filter="{naam}" data-waarde="alles" aria-pressed="true">
            {VINKJE}<span>{alles}</span>
          </button>''']
    for w in waarden:
        pillen.append(f'''          <button type="button" class="filter-pil" data-filter="{naam}" data-waarde="{sleutelvorm(w)}" aria-pressed="false">
            {VINKJE}<span>{w}</span>
          </button>''')
    return f'''        <div class="filter-groep" role="group" aria-label="{label}" data-groep="{naam}">
{chr(10).join(pillen)}
        </div>'''


def kaart(c):
    return f'''        <article class="case-kaart" data-dienst="{sleutelvorm(c["dienst"])}" data-branche="{sleutelvorm(c["branche"])}">
          <a class="case-kaart__link hover--icon" href="case.html?slug=case-{c["slug"]}">
            <figure class="case-kaart__beeld">
              {foto(c["beeld"], maten="(max-width: 767px) 100vw, (max-width: 1199px) 50vw, 33vw", alt="")}
            </figure>
            <div class="case-kaart__inhoud">
              <div class="case-kaart__meta">
                <span class="case-kaart__label">{c["dienst"]}</span>
                <span class="case-kaart__label">{c["plaats"]}</span>
              </div>
              <h2 class="case-kaart__titel">{c["klant"]}</h2>
              <p class="case-kaart__tekst">{c["kort"]}</p>
              <div class="case-kaart__voet">
                <span class="case-kaart__lees">Lees de case</span>
                {icoonknop("", "button--secundair")}
              </div>
            </div>
          </a>
        </article>'''


# ====================================================================== overzicht
def overzicht():
    diensten = ["Veilig gedrag", "EHS RIE", "Safety Checks"]
    branches = ["Productie", "Logistiek", "Bouw"]

    FAQ = [
        ("Staat mijn branche er niet bij?", [
            "De aanpak verschilt minder per branche dan je zou denken. Of het nu om een productiehal, een magazijn of een bouwplaats gaat: de vraag is steeds of wat er op papier staat ook op de vloer gebeurt.",
            "Bel gerust om te vragen of we ervaring hebben met jouw type werk.",
        ]),
        ("Kan ik met een van deze bedrijven praten?", [
            "In overleg met de klant vaak wel. Voor een aantal opdrachtgevers verwijzen we door naar een contactpersoon die het traject van dichtbij heeft meegemaakt.",
        ]),
        ("Hoe lang duurt zo’n traject gemiddeld?", [
            "Een safety check is binnen een week rond. Een RI&amp;E met plan van aanpak kost twee tot zes weken. Een gedragstraject loopt maanden, omdat cultuur nu eenmaal niet in een maand verandert.",
        ]),
    ]

    inhoud = f'''{patroonhero("01", "cases", "Cases", "Cases")}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">Wat er verandert als je het serieus aanpakt</h2>
          <div class="article-body content-fit--half">
            <p>Trajecten uit de praktijk: wat de situatie was, wat we hebben gedaan en wat het opleverde. Filter op dienst of op branche om te zien wat het dichtst bij jouw situatie ligt.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="cases-overzicht" id="s03-cases">
    <div class="container">
      <div class="cases-overzicht__filters">
{filtergroep("Filter cases op dienst", "dienst", diensten, "Alle diensten")}
{filtergroep("Filter cases op branche", "branche", branches, "Alle branches")}
      </div>

      <p class="cases-overzicht__telling" role="status" aria-live="polite"></p>

      <div class="cases-overzicht__raster" id="caseRaster">
{chr(10).join(kaart(c) for c in CASES)}
      </div>

      <p class="cases-overzicht__leeg" hidden>Geen cases die aan beide filters voldoen. Zet er een terug op &lsquo;alle&rsquo;.</p>
    </div>
  </section>

{faq_blok("04", FAQ)}

{slotblok("05", "Zit jouw situatie hier tussen?")}
'''

    (UIT / "cases.html").write_text(pagina(
        bestand="cases.html",
        titel="Cases | MADEGRO",
        omschrijving="Trajecten uit de praktijk: veilig gedrag, EHS RI&E en safety checks bij productie-, logistiek- en bouwbedrijven.",
        namespace="cases",
        pagina_css="cases.css",
        css_naam="cases",
        inhoud=inhoud,
        scripts=["cases.js"],
        extra_ld=faq_ld(FAQ),
    ), encoding="utf-8")
    print("cases.html geschreven")


# ================================================================ detailpagina
def detailpagina():
    """case.html: de hero staat al in de HTML, met data-header-theme voor het
       witte logo, en wordt door case.js gevuld; de overige secties komen in
       #caseSecties. Zonder ?slug= of zonder gepubliceerde rij toont case.js
       een nette melding met een knop naar het overzicht."""
    inhoud = '''  <div id="caseDetail">
  <!-- ================= 01 KOP ================= -->
  <section class="service-hero" id="s01-introductie" data-header-theme="light">
    <div class="service-hero--beeld" aria-hidden="true">
      <img data-veld="beeld" alt="" hidden decoding="async" fetchpriority="high">
      <span class="service-hero--sluier"></span>
    </div>
    <div class="container">
      <div class="service-hero--inner">
        <span class="subtitle" style="color:var(--color-white)" data-veld="label">Case</span>
        <h1 class="service-hero--titel" data-veld="titel">Case laden&hellip;</h1>
        <div class="hero--actions" data-veld="acties"></div>
      </div>
    </div>
  </section>

  <div id="caseSecties" aria-live="polite"></div>
  </div>
'''
    (UIT / "case.html").write_text(pagina(
        bestand="case.html",
        titel="Case | MADEGRO",
        omschrijving="Een traject uit de praktijk van MADEGRO: de situatie, de aanpak en het resultaat.",
        namespace="case",
        pagina_css="cases.css",
        css_naam="cases",
        inhoud=inhoud,
        scripts=["case.js"],
        actief="cases.html",
    ), encoding="utf-8")
    print("case.html geschreven")


if __name__ == "__main__":
    overzicht()
    detailpagina()
