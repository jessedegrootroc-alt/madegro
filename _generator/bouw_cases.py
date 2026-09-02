# -*- coding: utf-8 -*-
"""Het cases-overzicht met filters, en één template voor de detailpagina's."""
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
    return f'''        <div class="filter-groep" role="group" aria-label="{label}">
{chr(10).join(pillen)}
        </div>'''


def kaart(c):
    return f'''        <article class="case-kaart" data-dienst="{sleutelvorm(c["dienst"])}" data-branche="{sleutelvorm(c["branche"])}">
          <a class="case-kaart__link hover--icon" href="case-{c["slug"]}.html">
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
            <p>Zes trajecten uit de praktijk: wat de situatie was, wat we hebben gedaan en wat het opleverde. Filter op dienst of op branche om te zien wat het dichtst bij jouw situatie ligt.</p>
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
        omschrijving="Zes trajecten uit de praktijk: veilig gedrag, EHS RI&E en safety checks bij productie-, logistiek- en bouwbedrijven.",
        namespace="cases",
        pagina_css="cases.css",
        css_naam="cases",
        inhoud=inhoud,
        scripts=["cases.js"],
        extra_ld=faq_ld(FAQ),
    ), encoding="utf-8")
    print("cases.html geschreven")


# ==================================================================== detailblad
def detail(c):
    cijfers = "\n".join(f'''          <div class="kerncijfer">
            <span class="kerncijfer__label">{label}</span>
            <p class="kerncijfer__getal">{getal}<span class="kerncijfer__eenheid">{eenheid}</span></p>
          </div>''' for label, getal, eenheid in c["cijfers"])

    citaat, naam, functie = c["citaat"]
    verwant = [case(s) for s in c["verwant"]]
    verwante_rijen = "\n".join(f'''      <a class="cases-grid__row {'cases-grid__row--grey' if i % 2 == 0 else 'cases-grid__row--white'} hover--icon"
         href="case-{v["slug"]}.html" aria-label="{v["klant"]}: {_plat(v["titel"])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">
            <span class="cases-grid__meta-item">{v["dienst"]}</span>
            <span class="cases-grid__meta-item">{v["plaats"]}</span>
          </div>
          <h3 class="cases-grid__title">{v["klant"]}</h3>
          <div class="cases-grid__wrapper">
            <p class="cases-grid__text">{v["kort"]}</p>
            {icoonknop("button--icon--54", "button--secundair")}
          </div>
        </div>
        <figure class="cases-grid__image">
          {foto(v["beeld"], maten="(max-width: 991px) 100vw, 50vw")}
        </figure>
      </a>''' for i, v in enumerate(verwant))

    def punten(lijst):
        regels = "\n".join(f"          <li>{x}</li>" for x in lijst)
        return f'''        <ul class="case-lijst">
{regels}
        </ul>'''

    def bleed(sleutel, alt):
        return f'''  <figure class="case-bleed">
    {foto(sleutel, maten="100vw", alt=alt)}
  </figure>'''

    def blok(nr, ident, kop, tekst, lijst=None):
        extra = "\n" + punten(lijst) if lijst else ""
        return f'''  <section class="band background--white case-blok" id="s{nr}-{ident}">
    <div class="container">
      <div class="case-blok__inner">
        <h2 class="section-heading case-blok__kop">{kop}</h2>
        <div class="case-blok__body">
          <p>{tekst}</p>
        </div>{extra}
      </div>
    </div>
  </section>'''

    b1, b2 = c["bleed"]

    inhoud = f'''  <!-- ================= 01 KOP ================= -->
  <section class="service-hero" id="s01-introductie" data-header-theme="light">
    <div class="service-hero--beeld" aria-hidden="true">
      {foto(c["beeld"], laden="eager", maten="100vw", alt="")}
      <span class="service-hero--sluier"></span>
    </div>
    <div class="container">
      <div class="service-hero--inner">
        <span class="subtitle" style="color:var(--color-white)">{c["dienst"]} &middot; {c["branche"]}</span>
        <h1 class="service-hero--titel">{c["titel"]}</h1>
        <div class="hero--actions">
          {knop("Zelfde vraag? Neem contact op", "contact.html")}
          {knop("Alle cases", "cases.html", "secundair")}
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 02 KERNCIJFERS ================= -->
  <section class="band background--white" id="s02-kerncijfers">
    <div class="container">
      <div class="kerncijfers">
{cijfers}
      </div>
    </div>
  </section>

  <!-- ================= 03 INLEIDING ================= -->
  <section class="band background--white" id="s03-inleiding">
    <div class="container">
      <p class="case-lead">{c["situatie"]}</p>
    </div>
  </section>

{blok("04", "over", f'Over {c["klant"]}', c["over"])}

{bleed(b1, "")}

{blok("05", "uitdaging", "De uitdaging", c["uitdaging"], c["uitdaging_punten"])}

  <!-- ================= 06 CITAAT ================= -->
  <section class="band background--white" id="s06-citaat">
    <div class="container">
      <figure class="case-citaat">
        <blockquote><p>&ldquo;{c["citaat"][0]}&rdquo;</p></blockquote>
        <figcaption class="case-citaat__wie">
          <strong>{naam}</strong><span>{functie}, {c["klant"]}</span>
        </figcaption>
      </figure>
    </div>
  </section>

{blok("07", "aanpak", "De aanpak", c["oplossing"], c["aanpak_punten"])}

{bleed(b2, "")}

{blok("08", "resultaat", "Zelfde plek, ander resultaat", c["resultaat"])}

  <!-- ================= 09 VERWANTE CASES ================= -->
  <section class="cases-grid" id="s09-verwant">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">Andere trajecten</h2>
        {knop("Alle cases", "cases.html", "secundair")}
      </div>
      <div class="cases-grid__list">
{verwante_rijen}
      </div>
    </div>
  </section>

{slotblok("10", "Herken je dit?")}
'''

    (UIT / f'case-{c["slug"]}.html').write_text(pagina(
        bestand=f'case-{c["slug"]}.html',
        titel=f'{c["klant"]} | Case | MADEGRO',
        omschrijving=_plat(c["kort"])[:155],
        namespace=f'case-{c["slug"]}',
        pagina_css="cases.css",
        css_naam="cases",
        inhoud=inhoud,
        actief="cases.html",
        extra_ld=json.dumps({
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": _plat(c["titel"]),
            "about": _plat(c["dienst"]),
            "publisher": {"@type": "Organization", "name": "Madegro Advies B.V."},
        }, ensure_ascii=False, indent=2),
    ), encoding="utf-8")
    print(f'case-{c["slug"]}.html geschreven')


if __name__ == "__main__":
    overzicht()
    for c in CASES:
        detail(c)
