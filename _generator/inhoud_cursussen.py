# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bouw_cursus import cursuspagina

WAAROM_BASIS = [
    ("USP 01", "Je krijgt een certificaat", "Na afloop ontvang je het MADEGRO-deelnamecertificaat, waarmee je richting opdrachtgevers en auditors kunt aantonen dat de stof is doorlopen."),
    ("USP 02", "Uit de praktijk, niet uit een boek", "De voorbeelden komen van echte werkvloeren. Waar het kan werken we met situaties uit je eigen bedrijf."),
    ("USP 03", "Kleine groepen", "Maximaal twaalf deelnemers, zodat er ruimte is voor de vragen die er in jouw situatie echt toe doen."),
    ("USP 04", "Op locatie of bij ons", "We komen naar je toe als dat handiger is. Dat scheelt reistijd en de voorbeelden staan dan letterlijk om je heen."),
]

# Vierde waarde is de foto naast het citaat: een werkplek, geen portret.
# Vijfde is het logo van de opdrachtgever; None geeft een geel invulveld.
TESTIMONIALS_BASIS = [
    ("Geen powerpoint van drie uur, maar de vloer op en kijken. Dat blijft veel beter hangen.",
     "Rob van Dijk", "Voorman, Van Deursen Metaal B.V.", "lassen", "van-deursen-metaal"),
    ("Ik dacht dat ik dit allemaal wel wist. De helft van de voorbeelden herkende ik uit onze eigen hal.",
     "Marieke Bakker", "Preventiemedewerker, Rivierpoort Logistiek", "productiehal", "rivierpoort-logistiek"),
    ("Nuchter gebracht, zonder opgeheven vinger. Dat werkt bij onze mensen een stuk beter.",
     "Tim Willemse", "Bedrijfsleider, Merwede Bouwgroep", "haven", "merwede-bouwgroep"),
]

# TODO-CONTENT: cursusnamen, inhoud, tarieven en data laten bevestigen door Martin.
# De vier cursussen hieronder zijn bedacht om het template te vullen; het tarief
# van 750 euro per dagdeel is een aanname.
cursuspagina({
    "bestand": "cursus-veiligheidsbewustzijn.html",
    "doelgroep": "Voor operators en uitvoerenden",
    # TODO-CONTENT: deze doelgroepbeschrijving is samengesteld uit de regel op
    # cursusaanbod.html en de FAQ; laat Martin hem nakijken.
    "voor_wie": "Voor iedereen die het werk zelf uitvoert: operators, monteurs, chauffeurs, bouwvakkers. Er is geen voorkennis nodig en er wordt niets van je verwacht op papier. Draai je in ploegen, dan draaien we de cursus meerdere keren op een dag, zodat elke ploeg aan de beurt komt zonder dat de productie stilvalt.",
    "voor_wie_foto": "productiehal",
    "inhoud_foto": "lassen",
    "hero_foto": "cursus-bewustzijn-bouw",
    "namespace": "cursus-veiligheidsbewustzijn",
    "titel": "Cursus Veiligheidsbewustzijn op de werkvloer | MADEGRO",
    "titel_kort": "Veiligheidsbewustzijn op de werkvloer",
    "omschrijving": "Korte praktijkcursus voor operators en uitvoerenden: risico's herkennen in je eigen werk en elkaar erop aanspreken.",
    "duur": "1 dagdeel",
    "doorlooptijd": "één dag",
    "doorlooptijd_getal": "1",
    "doorlooptijd_eenheid": "dag",
    "intro_kort": '''          <p>De meeste ongevallen gebeuren niet bij het bijzondere werk, maar bij de handeling die je al duizend keer hebt gedaan. Deze cursus maakt dat zichtbaar.</p>''',
    "statement": '''          <p>In &eacute;&eacute;n dagdeel gaan we van &lsquo;dat is nu eenmaal zo&rsquo; naar het herkennen van risico&rsquo;s in je eigen werk, en naar het gesprek erover met je collega&rsquo;s.</p>''',
    "waarom": WAAROM_BASIS,
    "opzet": '''            <p>We beginnen op de werkvloer, niet in het leslokaal. Deelnemers lopen hun eigen werkplek langs met een andere bril op en benoemen wat ze zien.</p>
            <p>Daarna gaan we in gesprek over wat er opviel: waarom werken we zoals we werken, en wat zou er moeten veranderen om het veiliger te maken zonder het onwerkbaar te maken?</p>''',
    "resultaten": [
        "risico&rsquo;s in je eigen werk benoemen voordat er iets gebeurt",
        "het verschil uitleggen tussen een onveilige situatie en onveilig gedrag",
        "een collega aanspreken zonder dat het een conflict wordt",
        "een bijna-ongeval melden en uitleggen waarom dat nut heeft",
    ],
    "tijdlijn": [
        ("Rondgang op de werkvloer", "In tweetallen de eigen werkplek langs, met een kijkopdracht. Wat je elke dag ziet, zie je nu bewust.", "45 minuten"),
        ("Terugkoppeling en gesprek", "We leggen de observaties naast elkaar. Meestal komen dezelfde drie of vier dingen bij iedereen terug.", "60 minuten"),
        ("Aanspreken oefenen", "Het lastigste onderdeel: hoe zeg je er iets van zonder dat het botst? We oefenen met situaties uit de rondgang.", "45 minuten"),
        ("Afspraken en afsluiting", "Wat nemen we mee naar maandag? Drie concrete afspraken, opgeschreven door de deelnemers zelf.", "30 minuten"),
    ],
    "na_kop": "En daarna?",
    "na_tekst": '''              <p>Deelnemers gaan terug naar hun eigen ploeg met drie afspraken die ze zelf hebben opgeschreven. De ervaring is dat die alleen standhouden als de leidinggevende erop terugkomt.</p>
              <p>Daarom raden we aan om de cursus te combineren met een gedragstraject, of op zijn minst met een terugkommoment na een paar maanden.</p>''',
    "vervolg_link": "veilig-gedrag.html",
    "vervolg_label": "Naar Veilig gedrag",
    "testimonials": TESTIMONIALS_BASIS,
    "faq": [
        ("Voor wie is deze cursus bedoeld?", ["Voor iedereen die het werk uitvoert: operators, monteurs, chauffeurs, bouwvakkers. Er is geen voorkennis nodig."]),
        ("Kan het in ploegendienst?", ["Ja. We draaien de cursus meerdere keren op een dag, zodat elke ploeg aan de beurt komt zonder dat de productie stilvalt."]),
        ("Wat kost het?", ["Op locatie bij jou, voor een groep tot twaalf deelnemers: € 750 per dagdeel, exclusief btw en reiskosten."]),
    ],
})

cursuspagina({
    "bestand": "cursus-risicobeoordeling.html",
    "doelgroep": "Voor voormannen en teamleiders",
    # TODO-CONTENT: deze doelgroepbeschrijving is samengesteld uit de regel op
    # cursusaanbod.html en de FAQ; laat Martin hem nakijken.
    "voor_wie": "Voor wie een ploeg aanstuurt en beslist hoe het werk wordt aangepakt: voormannen, teamleiders en werkvoorbereiders. Enige ervaring op de werkvloer is genoeg. Het helpt als je al eens met een RI&amp;E of een werkplekinspectie te maken hebt gehad, maar het hoeft niet.",
    "voor_wie_foto": "overleg",
    "inhoud_foto": "transport",
    "hero_foto": "cursus-risico-lijn",
    "namespace": "cursus-risicobeoordeling",
    "titel": "Cursus Risico&rsquo;s herkennen en beoordelen | MADEGRO",
    "titel_kort": "Risico&rsquo;s herkennen en beoordelen",
    "omschrijving": "Voor voormannen en teamleiders: risico's systematisch beoordelen op kans en effect, en beslissen welke maatregel past.",
    "duur": "2 dagdelen",
    "doorlooptijd": "twee weken",
    "doorlooptijd_getal": "2",
    "doorlooptijd_eenheid": "weken",
    "intro_kort": '''          <p>Een risico zien is &eacute;&eacute;n ding. Beoordelen hoe erg het is, en beslissen welke maatregel erbij past, is een vak apart.</p>''',
    "statement": '''          <p>In twee dagdelen leer je werken met kans en effect, en met de arbeidshygi&euml;nische strategie: bronaanpak eerst, persoonlijke beschermingsmiddelen als laatste redmiddel.</p>''',
    "waarom": WAAROM_BASIS,
    "opzet": '''            <p>Het eerste dagdeel gaat over beoordelen: hoe weeg je kans tegen effect, en hoe voorkom je dat alles &lsquo;hoog&rsquo; wordt? Deelnemers scoren echte situaties uit hun eigen bedrijf.</p>
            <p>Het tweede dagdeel gaat over maatregelen. Welke oplossing past bij welk risico, en waarom is een instructie meestal de zwakste maatregel die er is?</p>''',
    "resultaten": [
        "een risico onderbouwd scoren op kans en effect",
        "de arbeidshygi&euml;nische strategie toepassen bij het kiezen van een maatregel",
        "onderscheid maken tussen een maatregel die werkt en een die alleen aantoonbaar is",
        "je beoordeling uitleggen aan collega&rsquo;s en aan de directie",
    ],
    "tijdlijn": [
        ("Kans en effect", "De systematiek, met genoeg voorbeelden om het gevoel te krijgen. Waar zit het verschil tussen zelden-ernstig en vaak-licht?", "Dagdeel 1"),
        ("Zelf scoren", "Deelnemers beoordelen situaties uit hun eigen werk en verdedigen hun score tegenover de groep.", "Dagdeel 1"),
        ("Maatregelen kiezen", "De arbeidshygi&euml;nische strategie, van bronaanpak tot persoonlijke bescherming, met de kosten en de praktijk erbij.", "Dagdeel 2"),
        ("Eindopdracht", "Een risico uit het eigen bedrijf volledig uitwerken: beoordeling, maatregel, verantwoordelijke en termijn.", "Dagdeel 2"),
    ],
    "na_kop": "En daarna?",
    "na_tekst": '''              <p>Deelnemers kunnen na afloop meedraaien bij het opstellen of bijwerken van de RI&amp;E. Veel bedrijven laten hun voormannen daarna zelf de jaarlijkse actualisatie doen.</p>
              <p>Wil je die stap in &eacute;&eacute;n keer goed zetten, dan is de cursus RI&amp;E in de praktijk het logische vervolg.</p>''',
    "vervolg_link": "cursus-rie-praktijk.html",
    "vervolg_label": "Naar RI&amp;E in de praktijk",
    "testimonials": TESTIMONIALS_BASIS,
    "faq": [
        ("Moet ik voorkennis hebben?", ["Enige ervaring op de werkvloer is genoeg. Het helpt als je al eens met een RI&amp;E of een werkplekinspectie te maken hebt gehad, maar het hoeft niet."]),
        ("Kunnen we onze eigen RI&amp;E meenemen?", ["Graag zelfs. Dan werken we in het tweede dagdeel met jullie eigen risico&rsquo;s in plaats van met voorbeelden."]),
        ("Wat kost het?", ["Op locatie bij jou, voor een groep tot twaalf deelnemers: € 750 per dagdeel, exclusief btw en reiskosten."]),
    ],
})

cursuspagina({
    "bestand": "cursus-veiligheidsladder.html",
    "doelgroep": "Voor KAM- en HSE-co&ouml;rdinatoren",
    # TODO-CONTENT: deze doelgroepbeschrijving is samengesteld uit de regel op
    # cursusaanbod.html en de FAQ; laat Martin hem nakijken.
    "voor_wie": "Voor wie binnen de organisatie verantwoordelijk is voor veiligheid en kwaliteit: KAM- en HSE-co&ouml;rdinatoren, en de leidinggevenden die met hen meelopen. Je hoeft de Veiligheidsladder niet te kennen; wel helpt het als je weet hoe het er bij jullie op de vloer aan toegaat.",
    "voor_wie_foto": "bouwplaats",
    "inhoud_foto": "overleg",
    "hero_foto": "cursus-ladder-helmen",
    "namespace": "cursus-veiligheidsladder",
    "titel": "Cursus Werken met de Veiligheidsladder | MADEGRO",
    "titel_kort": "Werken met de Veiligheidsladder",
    "omschrijving": "Voor KAM- en HSE-coördinatoren: de treden van de Veiligheidsladder, een nulmeting uitvoeren en een verbeterplan opstellen.",
    "duur": "3 dagdelen",
    "doorlooptijd": "zes weken",
    "doorlooptijd_getal": "6",
    "doorlooptijd_eenheid": "weken",
    "intro_kort": '''          <p>De Veiligheidsladder wordt steeds vaker gevraagd door opdrachtgevers. Maar een trede halen is iets anders dan er ook echt op staan.</p>''',
    "statement": '''          <p>In drie dagdelen leer je de treden herkennen, een nulmeting uitvoeren in je eigen organisatie en een verbeterplan opstellen dat verder komt dan een certificaat.</p>''',
    "waarom": WAAROM_BASIS,
    "opzet": '''            <p>We doorlopen de vijf treden, van pathologisch tot vooruitstrevend, met het gedrag dat bij elke trede hoort. Het herkennen van dat gedrag is de kern: niet wat er in het handboek staat, maar wat er gebeurt.</p>
            <p>Tussen de dagdelen door voer je een nulmeting uit in je eigen organisatie. De resultaten daarvan zijn het materiaal voor het derde dagdeel.</p>''',
    "resultaten": [
        "de vijf treden herkennen aan concreet gedrag in plaats van aan documenten",
        "een nulmeting uitvoeren met gesprekken en observaties",
        "bepalen welke trede realistisch is als volgende stap",
        "een verbeterplan opstellen dat de leidinggevenden meeneemt",
    ],
    "tijdlijn": [
        ("De vijf treden", "Wat kenmerkt elke trede, en waaraan zie je op de vloer waar een organisatie staat?", "Dagdeel 1"),
        ("Meten", "Hoe voer je gesprekken die iets opleveren, en hoe observeer je zonder dat mensen ander gedrag laten zien?", "Dagdeel 2"),
        ("Nulmeting in eigen huis", "Tussen de dagdelen door voer je zelf een meting uit. Wij zijn op afstand beschikbaar voor vragen.", "Twee weken"),
        ("Verbeterplan", "De resultaten op tafel, de volgende trede bepalen en het plan opstellen. Je gaat naar huis met een concept dat af is.", "Dagdeel 3"),
    ],
    "na_kop": "En daarna?",
    "na_tekst": '''              <p>Je hebt een nulmeting en een verbeterplan. De uitvoering daarvan is waar het lastig wordt: dat vraagt om leidinggevenden die het dragen.</p>
              <p>Wil je daar begeleiding bij, dan sluit het gedragstraject naadloos aan op wat je in deze cursus hebt opgezet.</p>''',
    "vervolg_link": "veilig-gedrag.html",
    "vervolg_label": "Naar Veilig gedrag",
    "testimonials": TESTIMONIALS_BASIS,
    "faq": [
        ("Is dit een gecertificeerde opleiding?", ["Nee, dit is geen opleiding onder een extern schema. Deelnemers ontvangen het MADEGRO-deelnamecertificaat. Wil je een traject dat wél onder een erkend schema valt, dan verwijzen we door naar Delta Opleidingen."]),
        ("Hoeveel tijd kost de nulmeting?", ["Reken op twee tot drie dagdelen, verspreid over twee weken. Bij een grotere organisatie meer, omdat je met meer ploegen moet spreken."]),
        ("Wat kost het?", ["Op locatie bij jou, voor een groep tot twaalf deelnemers: € 750 per dagdeel, exclusief btw en reiskosten."]),
    ],
})

cursuspagina({
    "bestand": "cursus-rie-praktijk.html",
    "doelgroep": "Voor preventiemedewerkers",
    # TODO-CONTENT: deze doelgroepbeschrijving is samengesteld uit de regel op
    # cursusaanbod.html en de FAQ; laat Martin hem nakijken.
    "voor_wie": "Voor preventiemedewerkers en voor wie de RI&amp;E in het eigen bedrijf beheert. Dit is een praktijkcursus over de RI&amp;E zelf, geen volledige opleiding tot preventiemedewerker. Je eigen RI&amp;E mag mee; dan ga je naar huis met een geactualiseerd document in plaats van met een oefening.",
    "voor_wie_foto": "transport",
    "inhoud_foto": "haven",
    "hero_foto": "cursus-rie-tablet",
    "namespace": "cursus-rie-praktijk",
    "titel": "Cursus RI&amp;E in de praktijk | MADEGRO",
    "titel_kort": "RI&amp;E in de praktijk",
    "omschrijving": "Voor preventiemedewerkers: zelf een RI&E opstellen of actualiseren, en er een plan van aanpak van maken dat uitvoerbaar is.",
    "duur": "2 dagdelen",
    "doorlooptijd": "drie weken",
    "doorlooptijd_getal": "3",
    "doorlooptijd_eenheid": "weken",
    "intro_kort": '''          <p>De RI&amp;E is verplicht, maar te vaak een document dat na oplevering in de kast verdwijnt. Zonde, want het is het enige overzicht van alles wat er in je bedrijf mis kan gaan.</p>''',
    "statement": '''          <p>In twee dagdelen leer je er zelf mee werken: opstellen, actualiseren, en vertalen naar een plan van aanpak waar je op kunt sturen.</p>''',
    "waarom": WAAROM_BASIS,
    "opzet": '''            <p>Het eerste dagdeel gaat over de inventarisatie: welke bronnen gebruik je, hoe zorg je dat je niets vergeet, en hoe betrek je de mensen die het werk doen?</p>
            <p>Het tweede dagdeel gaat over het plan van aanpak. Dat is waar de meeste RI&amp;E&rsquo;s stranden: een lijst zonder eigenaar en zonder termijn verandert niets.</p>''',
    "resultaten": [
        "een RI&amp;E opstellen of actualiseren voor je eigen organisatie",
        "beoordelen of een bestaande RI&amp;E nog dekkend is",
        "een plan van aanpak maken met eigenaren, termijnen en kosten",
        "uitleggen wanneer toetsing door een kerndeskundige verplicht is",
    ],
    "tijdlijn": [
        ("Inventariseren", "Bronnen, methodes en de valkuil van het overslaan van taken die maar zelden voorkomen.", "Dagdeel 1"),
        ("Eigen inventarisatie", "Tussen de dagdelen door breng je een afdeling van je eigen bedrijf in kaart.", "Twee weken"),
        ("Plan van aanpak", "Van lijst naar planning: prioriteren, eigenaren aanwijzen en kosten inschatten.", "Dagdeel 2"),
        ("Toetsing en vervolg", "Wanneer moet het getoetst worden, en hoe houd je het document daarna actueel?", "Dagdeel 2"),
    ],
    "na_kop": "En daarna?",
    "na_tekst": '''              <p>Je kunt de RI&amp;E van je eigen organisatie zelf bijhouden. Voor de eerste keer opstellen, of bij een toetsingsplicht, is een extra paar ogen vaak wel prettig.</p>
              <p>We kijken graag mee met wat je hebt gemaakt voordat het definitief wordt.</p>''',
    "vervolg_link": "ehs-rie.html",
    "vervolg_label": "Naar EHS RI&amp;E",
    "testimonials": TESTIMONIALS_BASIS,
    "faq": [
        ("Vervangt deze cursus de opleiding tot preventiemedewerker?", ["Nee. Dit is een praktijkcursus over de RI&amp;E specifiek, geen volledige opleiding tot preventiemedewerker. Voor die bredere opleiding verwijzen we door."]),
        ("Kunnen we met onze eigen RI&amp;E werken?", ["Ja, dat heeft de voorkeur. Je gaat dan naar huis met een geactualiseerd document in plaats van met een oefening."]),
        ("Wat kost het?", ["Op locatie bij jou, voor een groep tot twaalf deelnemers: € 750 per dagdeel, exclusief btw en reiskosten."]),
    ],
})
