# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *
from schil import _plat

UIT = pathlib.Path("/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE/madegro")

FAQ = [
    ("Werken jullie ook voor kleinere bedrijven?", [
        "Ja. De aanpak schaalt mee: bij een bedrijf van vijftien man ziet een traject er anders uit dan bij een fabriek met tweehonderd medewerkers, maar de vragen zijn dezelfde.",
        "Bij minder dan 25 medewerkers hoeft een RI&amp;E in veel gevallen niet getoetst te worden door een kerndeskundige. Dat scheelt tijd en geld; we kijken samen wat er in jouw situatie wel en niet moet.",
    ]),
    ("Hoe lang duurt een traject?", [
        "Een safety check is meestal binnen een week rond, inclusief rapportage. Een RI&amp;E met plan van aanpak kost twee tot zes weken, afhankelijk van de omvang en het aantal locaties.",
        "Een gedragstraject loopt langer: cultuur verandert niet in een maand. We werken daar in blokken, met vaste meetmomenten.",
    ]),
    ("Blijven jullie betrokken na afloop?", [
        "Ja. Het doel is dat je het zelf kunt, niet dat je ons nodig blijft hebben. Daarom dragen we werkwijzen over aan je eigen mensen en blijven we daarna bereikbaar voor vragen.",
        "Veel klanten kiezen voor een periodieke check om scherp te blijven.",
    ]),
]

# De drie cijfers komen uit Martins eigen LinkedIn-profiel: MADEGRO staat daar
# als eigen bedrijf sinds juli 2002, met achttien opdrachtgevers bij naam.
# Het aantal branches is uit diezelfde lijst geteld.
# TODO-CONTENT: laat Martin ze bevestigen. Er stond hier eerder "450 cursisten
# opgeleid"; dat cijfer was verzonnen en is nergens op terug te voeren.
USPS = [
    ("24", "jaar zelfstandig", "MADEGRO bestaat sinds 2002. De adviezen komen uit ervaring op de vloer, niet uit een handboek."),
    ("18", "opdrachtgevers", "Van constructiebedrijf tot energiecentrale, van verpakkingsfabriek tot afvalverwerker."),
    ("6", "branches", "Industrie, energie, bouw en infra, voedingsmiddelen, verpakking en afvalverwerking."),
]

# De projectrijen komen uit dezelfde lijst als het cases-overzicht (schil.py),
# zodat een wijziging niet op twee plekken hoeft.
PROJECTEN = CASES[:3]

def projectkaart(c, grijs):
    return f'''      <a class="cases-grid__row {'cases-grid__row--grey' if grijs else 'cases-grid__row--white'} hover--icon"
         href="case-{c["slug"]}.html" aria-label="{c["klant"]}: {_plat(c["titel"])}">
        <div class="cases-grid__body">
          <div class="cases-grid__meta">
            <span class="cases-grid__meta-item">{c["dienst"]}</span>
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
      </a>'''


projecten = "\n".join(projectkaart(c, grijs=(i % 2 == 0)) for i, c in enumerate(PROJECTEN))

usps = "\n".join(f'''        <div>
          <div class="panel panel--{'grey' if i % 2 == 0 else 'wit'}">
            <p class="usp__getal" data-telop="{getal}">{getal}</p>
            <p class="usp__label">{label}</p>
            <p class="panel__body">{tekst}</p>
          </div>
        </div>''' for i, (getal, label, tekst) in enumerate(USPS))

INTROS_DIENSTEN = [
    "Het gedrag op de werkvloer laten aansluiten op wat er op papier staat, met de Veiligheidsladder als meetlat.",
    "De wettelijk verplichte risico-inventarisatie, vertaald naar een plan van aanpak dat je echt kunt uitvoeren.",
    "Periodiek toetsen of de praktijk nog klopt met de eisen, met een rapportage waar concrete punten in staan.",
]
diensten = "\n".join(dienstkaart(i, d, intro)
                     for i, (d, intro) in enumerate(zip(SERVICES, INTROS_DIENSTEN)))

cursussen = "\n".join(cursuskaart(i, c) for i, c in enumerate(CURSUSSEN))

# De vierde waarde is de foto naast het citaat, de vijfde het logo van de
# opdrachtgever. Dat is bewust een werkplek en
# geen portret: van deze mensen hebben we geen foto, en een willekeurig gezicht
# naast een naam zetten maakt er een bestaand persoon van die dit nooit gezegd
# heeft.
TESTIMONIALS = [
    # TODO-CONTENT: echte getuigenissen aanleveren; onderstaande namen zijn fictief
    ("De rapportage was de eerste die onze ploegleiders uit zichzelf hebben doorgelezen. Geen lijst met tekortkomingen, maar een paar dingen die je maandag kunt aanpakken.",
     "Karin Vermeer", "KAM-co&ouml;rdinator, Van Deursen Metaal B.V.", "productiehal", "van-deursen-metaal"),
    ("We dachten dat we op trede vier zaten. Na de nulmeting bleek het drie te zijn, en dat gesprek was precies wat we nodig hadden.",
     "Stefan de Bruin", "Operationeel manager, Rivierpoort Logistiek", "transport", "rivierpoort-logistiek"),
    ("Martin praat met de mensen op de vloer, niet alleen met de directie. Dat merk je aan wat er daarna verandert.",
     "Hans Molenaar", "Directeur, Merwede Bouwgroep", "bouwplaats", "merwede-bouwgroep"),
]


inhoud = f'''  <!-- ================= 01 INTRODUCTIE ================= -->
  <section class="hero" id="s01-introductie" data-header-theme="light">
    <div class="hero--beeld" aria-hidden="true">
      {foto("logistiek", laden="eager", maten="100vw")}
      <!-- De film ligt over het stilstaande beeld heen en komt pas in beeld als
           hij speelt. site.js hangt de bron er pas in op een breed scherm en
           alleen als beweging aan staat: zonder script, op een telefoon of met
           prefers-reduced-motion blijft het bij de foto hierboven, en dat is
           het eerste beeldje van dezelfde film. -->
      <video class="hero--video" data-herovideo="assets/video/hero-logistiek.mp4"
             width="1600" height="900" muted loop playsinline preload="none"></video>
      <span class="hero--sluier"></span>
    </div>
    <div class="container hero--container">
      <div class="hero--content">
        <span class="subtitle" style="color:var(--color-white)">Veiligheidskunde en kwaliteit</span>
        <h1 class="hero--title">Veiligheid die niet alleen op papier klopt</h1>
        <div class="hero--intro article-body">
          <p>MADEGRO helpt productie-, bouw-, techniek- en logistiekbedrijven om het veiligheidsniveau echt omhoog te brengen. Niet met een map in de kast, maar met werkwijzen die op de vloer standhouden.</p>
          <p>Veiligheid is geen kostenpost. Het is een verbeterdimensie naast kwaliteit, productiviteit en kosten. Meestal zie je het effect het eerst terug in minder stilstand en minder herstelwerk.</p>
        </div>
        <div class="hero--actions">
          {knop("Contact opnemen", "contact.html")}
          {knop("Over ons", "over-ons.html", "secondary")}
        </div>
      </div>
    </div>
  </section>

  <!-- ================= 02 WAT MADEGRO DOET ================= -->
  <section class="content-text-side-cta" id="s02-wat-we-doen">
    <div class="container">
      <div class="content-text-side-cta--container background--grey">
        <div class="row gx-0">
          <div class="col-lg-8 col-12">
            <div class="content-text-side-cta--body">
              <p>Veiligheid is geen papieren oefening. Met wisselende ploegen, nieuwe machines en een inspectie die zomaar langs kan komen, wil je weten waar je staat. MADEGRO brengt dat in beeld en zorgt dat het niveau omhoog gaat, van de werkvloer tot het plan van aanpak.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-text-side-visual background--white" id="s03-hoe-we-werken">
    <div class="container">
      <div class="row gx-0">
        <article class="col-lg-4 col-12">
          <div class="content-text-side-visual--stack content-text-side-visual--article">
            <h2>De regie over veiligheid op je eigen terrein</h2>
            <div class="content-text-side-visual--body content-fit--quarter">
              <p>We lopen je terrein af zoals een inspecteur dat zou doen: bij de poort, op de laadkuil, in de hal en op kantoor. Wat we zien leggen we vast in taal die je voormannen begrijpen, met maatregelen die in de planning passen.</p>
              <p>Daarna dragen we het over. Je eigen mensen houden de RI&amp;E bij, herkennen de risico&rsquo;s en spreken elkaar aan. Wij blijven bereikbaar, maar je hebt ons niet meer nodig om het draaiende te houden.</p>
            </div>
            {knop("Plan een kennismaking", "contact.html")}
          </div>
        </article>
      </div>
    </div>
    <div class="content-text-side-visual--visual added-distance">
      {foto("terrein", maten="(max-width: 991px) calc(100vw - 32px), (max-width: 1199px) calc(100vw - 96px), (max-width: 1352px) 940px, 70vw")}
    </div>
  </section>

  <!-- ================= 04 DE DRIE DIENSTEN ================= -->
  <section class="content-block" id="s04-diensten">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Wat we doen</span>
            <h2 class="section-heading">Drie manieren om het veiligheidsniveau te verhogen</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              De drie diensten grijpen op elkaar in: een safety check laat zien waar je staat, een RI&amp;E legt de risico&rsquo;s en de maatregelen vast, en een gedragstraject zorgt dat het ook zo blijft. Je kunt met elk van de drie beginnen.
            </p>
          </div>
        </div>
      </div>
      <div class="row g-0">
{diensten}
      </div>
    </div>
  </section>

  <!-- ================= 05 PROJECTEN ================= -->
  <section class="cases-grid" id="s05-projecten">
    <div class="container">
      <div class="cases-grid__header">
        <h2 class="cases-grid__heading">Recente trajecten</h2>
        {knop("Alle cases", "cases.html", "secundair")}
      </div>
      <!-- TODO-CONTENT: echte projecten, data en locaties aanleveren door Martin -->
      <div class="cases-grid__list">
{projecten}
      </div>
    </div>
  </section>

  <!-- ================= 06 USP'S ================= -->
  <section class="content-block" id="s06-usps">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">In cijfers</span>
            <h2 class="section-heading">Waar we vandaan komen</h2>
          </div>
        </div>
      </div>
      <!-- TODO-CONTENT: de drie getallen aanleveren door Martin -->
      <div class="panel-row panel-row--3">
{usps}
      </div>
    </div>
  </section>

  <!-- ================= 07 CURSUSAANBOD ================= -->
  <section class="content-block" id="s07-cursusaanbod">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Cursussen</span>
            <h2 class="section-heading">Kennis die op de vloer blijft</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              De cursussen zijn kort en praktisch. Deelnemers werken met situaties uit hun eigen bedrijf, zodat wat ze leren de volgende dag al bruikbaar is.
            </p>
          </div>
          <div class="col-md-4 col-12 text-md-end">
            {knop("Hele aanbod", "cursusaanbod.html")}
          </div>
        </div>
      </div>
      <!-- TODO-CONTENT: cursusnamen, doelgroepen, duur en prijzen bevestigen -->
      <div class="panel-row panel-row--4">
{cursussen}
      </div>
    </div>
  </section>

{quoteslider("08", "testimonials", "Wat klanten zeggen", "Uit de praktijk", TESTIMONIALS)}

{faq_blok("09", FAQ, "Wat mensen meestal eerst vragen")}

  <!-- ================= 10 WIE JE SPREEKT ================= -->
  <section class="streamer streamer--employee streamer--employee--portret background--groen" id="s10-martin">
    <div class="container">
      <div class="streamer--employee-row">
        <figure class="streamer--employee-portrait">
          {foto("martin-band", maten="(max-width: 991px) 100vw, 40vw")}
        </figure>
        <div class="streamer--employee-panel band">
          <span class="subtitle" style="color:var(--color-white)">Wie je spreekt</span>
          <h2 class="streamer--employee-name">Martin de Groot</h2>
          <div class="article-body content-fit--half">
            <p>MADEGRO bestaat sinds 2002. In die ruim twintig jaar werkte Martin als veiligheidskundige en HSE-manager bij onder meer Cosun Beet Company, Huhtamaki, Stork, Ballast Nedam en GE Vernova: in de industrie, de energiesector en de bouw.</p>
            <p>Buiten het werk loopt hij ultramarathons en doet hij ironmans; bij de atletiekvereniging in Monnickendam was hij jeugdtrainer en voorzitter. Honderd kilometer haal je niet met een goed plan alleen, maar met gewoontes die het houden als het tegenzit. Precies wat een veiligheidscultuur ook nodig heeft.</p>
          </div>
          <div>
            {knop("Meer over MADEGRO", "over-ons.html")}
          </div>
        </div>
      </div>
    </div>
  </section>

{slotblok("11", "Even sparren over waar je staat?")}
'''

(UIT / "index.html").write_text(pagina(
    bestand="index.html",
    titel="MADEGRO | Veiligheidskunde en kwaliteit voor productie, bouw en techniek",
    omschrijving="MADEGRO brengt het veiligheidsniveau van bedrijven omhoog: veilig gedrag, EHS RI&E en safety checks. Praktisch, met kennisoverdracht aan je eigen mensen.",
    namespace="home",
    pagina_css="index.css",
    css_naam="index",
    inhoud=inhoud,
    scripts=["index.js"],
    extra_ld=faq_ld(FAQ),
), encoding="utf-8")

print("index.html geschreven")
