# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *

UIT = pathlib.Path("/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE/madegro")

# ===================================================== cursusaanbod.html
FAQ_AANBOD = [
    ("Draaien de cursussen op vaste data?", [
        "We plannen in overleg, zodat het in de productieplanning past. Bij ploegendiensten draaien we dezelfde cursus meerdere keren op een dag.",
    ]),
    ("Kunnen we een cursus op maat laten maken?", [
        "Ja. De opzet ligt vast, maar de voorbeelden en de eindopdracht komen het liefst uit je eigen bedrijf. Dat kost weinig extra en levert veel meer op.",
    ]),
    ("Hoeveel deelnemers kunnen er mee?", [
        "Maximaal twaalf per groep. Bij meer mensen draaien we de cursus vaker, zodat er ruimte blijft voor vragen uit de eigen praktijk.",
    ]),
]

kaarten = "\n".join(cursuskaart(i, c) for i, c in enumerate(CURSUSSEN))

inhoud_aanbod = f'''{patroonhero("01", "cursusaanbod", "Cursusaanbod", "Cursusaanbod")}

  <section class="band background--white" id="s02-introductie">
    <div class="container">
      <div class="row">
        <div class="col-lg-8 col-12">
          <h2 class="section-heading" style="margin:0 0 var(--space-500)">Kennis die op de vloer blijft</h2>
          <div class="article-body content-fit--half">
            <p>Een cursus is pas geslaagd als je er de volgende dag iets mee doet. Daarom zijn onze cursussen kort, praktisch en zoveel mogelijk op locatie: de voorbeelden staan dan letterlijk om je heen.</p>
            <p>Elke cursus sluit af met een opdracht uit je eigen bedrijf. Deelnemers gaan naar huis met iets bruikbaars in plaats van met een map.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s03-cursussen">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Vier cursussen</span>
            <h2 class="section-heading">Van bewustzijn tot beoordeling</h2>
          </div>
        </div>
      </div>
      <!-- TODO-CONTENT: cursusnamen, doelgroepen, duur en prijzen bevestigen door Martin -->
      <div class="panel-row panel-row--4">
{kaarten}
      </div>
    </div>
  </section>

{faq_blok("04", FAQ_AANBOD)}

{slotblok("05", "Welke cursus past bij jullie?")}
'''

(UIT / "cursusaanbod.html").write_text(pagina(
    bestand="cursusaanbod.html",
    titel="Cursusaanbod | MADEGRO",
    omschrijving="Vier praktische cursussen over veiligheid op de werkvloer: van veiligheidsbewustzijn tot RI&E in de praktijk.",
    namespace="cursusaanbod",
    pagina_css="cursus.css",
    css_naam="cursus",
    inhoud=inhoud_aanbod,
    extra_ld=faq_ld(FAQ_AANBOD),
), encoding="utf-8")
print("cursusaanbod.html geschreven")

# ========================================================= over-ons.html
FAQ_OVER = [
    ("Werkt Martin alleen?", [
        "Voor het advieswerk wel: je hebt &eacute;&eacute;n aanspreekpunt, van het eerste gesprek tot de oplevering. Waar specialisme nodig is, bijvoorbeeld toetsing door een kerndeskundige, schakelen we een partner in.",
    ]),
    ("In welke regio werken jullie?", [
        "Vanuit Hardinxveld-Giessendam, met de meeste klanten in de Drechtsteden, de Alblasserwaard en de regio Rotterdam. Verder weg kan ook; dan kijken we naar reistijd.",
    ]),
    ("Hoe zit het met tarieven?", [
        "Advieswerk gaat op dagtarief, trajecten en cursussen op een vaste prijs vooraf.",
    ]),
]

# ---- waarden: vier vlakken, in de opzet van de referentie -------------------
# TODO-CONTENT: deze vier waarden zijn afgeleid uit wat er al op de site staat
# (nuchter, de vloer op, maatwerk, overdragen), maar Martin heeft ze nooit zo
# opgeschreven. Laat hem ze bevestigen of herschrijven.
WAARDEN = [
    ("Nuchter",
     "Geen bangmakerij en geen rapport van tachtig pagina&rsquo;s. Wat er speelt, in taal die je voormannen begrijpen."),
    ("Op de vloer",
     "Elk traject begint bij de mensen die het werk doen. Wat in het handboek staat weten we snel genoeg."),
    ("Praktisch",
     "Een maatregel die niet in de planning past, wordt niet uitgevoerd. We kijken naar wat er haalbaar is."),
    ("Overdraagbaar",
     "Het doel is dat je het zelf kunt. Kennisoverdracht is geen bijproduct maar de opdracht."),
]

# ---- werkwijze als beeld-en-tekstraster, twee per rij -----------------------
# De kleuren lopen als een schaakbord (grijs, wit, wit, grijs). Groen zou hier
# botsen: de medewerkersband eronder is ook groen en dan lopen de twee in elkaar
# over zonder zichtbare naad.
WERKWIJZE = [
    ("Eerst kijken",
     "Elk traject begint op de vloer. Wat er in het handboek staat weten we snel genoeg; wat er gebeurt is de vraag.",
     "productiehal", "Productiehal waar de werkwijze in de praktijk bekeken wordt", "grey"),
    ("Mens, systeem en techniek",
     "Als de techniek onveilig werken uitlokt, verandert er van een toolbox niets. Alle drie tegelijk, of het houdt geen stand.",
     "lassen", "Lasser aan het werk aan een constructie", "white"),
    ("Maatwerk, geen pakket",
     "Een bedrijf van vijftien man vraagt iets anders dan een fabriek met ploegendiensten. De aanpak schaalt mee.",
     "transport", "Industri&euml;le installatie op locatie", "white"),
    ("Overdragen",
     "Werkwijzen gaan naar je eigen mensen. Het doel is dat je ons daarna niet meer nodig hebt.",
     "overleg", "Werkoverleg waarin de werkwijze wordt overgedragen", "grey"),
]

kaarten = "\n".join(
    beeldkaart(kop, tekst, beeld, alt=alt, kleur=kleur)
    for kop, tekst, beeld, alt, kleur in WERKWIJZE
)

inhoud_over = f'''{paginahero("01", "verhaal", "Over MADEGRO", "Over MADEGRO", "bouwplaats",
             alt="Bouwplaats met torenkraan, een van de werkomgevingen van MADEGRO")}

  <section class="content-text-side-cta" id="s02-statement">
    <div class="container">
      <div class="content-text-side-cta--container">
        <div class="content-text-side-cta--body">
          <p>MADEGRO is het adviesbureau van Martin de Groot en bestaat sinds 2002. We ondersteunen bedrijven op het gebied van kwaliteit, arbo en milieu: toetsen of een organisatie aan de eisen voldoet, en haar daarna een niveau hoger brengen. Flexibel maatwerk, zonder verplichte urenafname.</p>
        </div>
      </div>
    </div>
  </section>

{vlakkenrij("03", "waarden", "Waar we voor staan", WAARDEN, subtitel="Onze waarden")}

  <section class="content-block" id="s04-werkwijze">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Werkwijze</span>
            <h2 class="section-heading">Waar we op letten</h2>
          </div>
        </div>
      </div>
      <div class="row g-0">
{kaarten}
      </div>
    </div>
  </section>

  <section class="streamer streamer--employee streamer--employee--portret background--groen" id="s05-martin">
    <div class="container">
      <div class="streamer--employee-row">
        <figure class="streamer--employee-portrait">
          {foto("martin-band", maten="(max-width: 991px) 100vw, 40vw")}
        </figure>
        <div class="streamer--employee-panel band">
          <span class="subtitle" style="color:var(--color-white)">Eigenaar &middot; EHSQ-specialist</span>
          <h2 class="streamer--employee-name">Martin de Groot</h2>
          <div class="article-body content-fit--half">
            <p>EHSQ-specialist: veiligheid, kwaliteitsmanagementsystemen en projectmanagement. Opgeleid aan de Hogeschool van Amsterdam, en sinds 2002 zelfstandig met MADEGRO. Werkte als HSE-manager bij onder meer Cosun Beet Company en Huhtamaki, en is op dit moment ook actief voor AEB Amsterdam en GE Vernova.</p>
            <p>Het uitgangspunt van elk traject: je moet het daarna zelf kunnen. Kennisoverdracht is geen bijproduct maar het doel: klanten worden zelfstandiger, niet afhankelijker.</p>
          </div>
          <div>
            {knop("Contact opnemen", "contact.html")}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="content-block" id="s06-samenwerking">
    <div class="container">
      <div class="content-block--container background--white" style="padding-bottom:var(--space-700)">
        <div class="row">
          <div class="col-md-8 col-12">
            <span class="subtitle" style="margin-bottom:var(--space-500)">Samenwerking</span>
            <h2 class="section-heading">Partners</h2>
            <p class="article-body" style="margin-top:var(--space-500); max-width:var(--content-max-half)">
              Waar specialisme nodig is werken we samen met vaste partners, zodat je niet zelf op zoek hoeft.
            </p>
          </div>
        </div>
      </div>
      <!-- TODO-CONTENT: Waalzicht Arbo en Delta Opleidingen zijn verzonnen namen;
           vervangen zodra duidelijk is met wie er echt wordt samengewerkt. -->
      <div class="panel-row panel-row--3">
        <div>
          <div class="panel panel--grey">
            <span class="panel__meta">Environment, Health &amp; Safety</span>
            <h3 class="panel__title">EHS-Services</h3>
            <p class="panel__body">Vaste partner voor vraagstukken rond milieu, arbeidshygi&euml;ne en gecertificeerde toetsing.</p>
            <p class="panel__actie"><a class="button button--link" href="https://www.ehs-services.nl" target="_blank" rel="noopener">Naar de website</a></p>
          </div>
        </div>
        <div>
          <div class="panel">
            <span class="panel__meta">Arbodienst</span>
            <h3 class="panel__title">Waalzicht Arbo</h3>
            <p class="panel__body">Voor bedrijfsartsen, verzuimbegeleiding en de toetsing die daarbij hoort.</p>
          </div>
        </div>
        <div>
          <div class="panel panel--grey">
            <span class="panel__meta">Opleidingsinstituut</span>
            <h3 class="panel__title">Delta Opleidingen</h3>
            <p class="panel__body">Voor trajecten die met een extern erkend certificaat moeten worden afgesloten.</p>
          </div>
        </div>
      </div>
    </div>
  </section>

{faq_blok("07", FAQ_OVER)}

{slotblok("08", "Even kennismaken?")}
'''

(UIT / "over-ons.html").write_text(pagina(
    bestand="over-ons.html",
    titel="Over ons | MADEGRO",
    omschrijving="MADEGRO is het adviesbureau van Martin de Groot: veiligheidskundige en kwaliteitscontroleur voor productie, bouw, techniek en logistiek.",
    namespace="over-ons",
    pagina_css="over-ons.css",
    css_naam="over-ons",
    inhoud=inhoud_over,
    extra_ld=faq_ld(FAQ_OVER),
), encoding="utf-8")
print("over-ons.html geschreven")
