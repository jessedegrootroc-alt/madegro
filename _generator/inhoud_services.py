# -*- coding: utf-8 -*-
"""De inhoud van de drie servicepagina's. Het skelet staat in bouw_service.py."""
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from bouw_service import servicepagina

PARTNER_EHS = ("EHS-Services", "Environment, Health &amp; Safety",
               "Vaste partner voor vraagstukken rond milieu, arbeidshygi&euml;ne en gecertificeerde toetsing. Waar een kerndeskundige nodig is, schakelen we hen in.",
               "https://www.ehs-services.nl")
# TODO-CONTENT: de twee partners hieronder zijn verzonnen. Vervang naam, tekst
# en link zodra duidelijk is met wie er echt wordt samengewerkt.
PARTNER_2 = ("Waalzicht Arbo", "Arbodienst",
             "Voor bedrijfsartsen, verzuimbegeleiding en de toetsing die daarbij hoort. Handig als de RI&amp;E ook een gezondheidskundige blik nodig heeft.",
             "#")
PARTNER_3 = ("Delta Opleidingen", "Opleidingsinstituut",
             "Voor trajecten die met een extern erkend certificaat moeten worden afgesloten, bijvoorbeeld bij aanbestedingen.",
             "#")

# ============================================================ Veilig gedrag
servicepagina({
    "bestand": "veilig-gedrag.html",
    "service_naam_kort": "Veilig gedrag",
    "namespace": "veilig-gedrag",
    "onderwerp": "veilig-gedrag",
    "titel": "Veilig gedrag | MADEGRO",
    "omschrijving": "Veiligheidscultuur die op de werkvloer standhoudt. MADEGRO begeleidt bedrijven langs de treden van de Veiligheidsladder, van reactief naar vooruitstrevend.",
    "service_type": "Veiligheidscultuur en gedragsverandering",
    "service_naam": "Veilig gedrag",
    "hero_foto": "dienst-gedrag",
    "hero_positie": "links",
    "eyebrow": "Dienst 01",
    "h1": "Veilig gedrag",
    "intro": '''          <p>De regels staan op papier, de instructies zijn gegeven, en toch zie je op de vloer iets anders gebeuren. Dat is zelden onwil. Meestal is het gewoonte, tijdsdruk, of een procedure die in de praktijk niet werkt.</p>
          <p>Veilig gedrag gaat over dat gat dichten: het gedrag laten aansluiten op wat er is afgesproken. We kijken naar mens, systeem &eacute;n techniek, want als de techniek onveilig werken uitlokt, verandert er van een toolbox niets.</p>''',
    "wanneer_intro": "Een gedragstraject is geen standaardpakket. Deze drie situaties komen het vaakst voorbij; herken je er een, dan is het gesprek waarschijnlijk de moeite waard.",
    "herkenning": [
        ("Je bedrijf groeit snel",
         "Er komen mensen bij, er draaien ploegen die elkaar nauwelijks zien, en de manier van werken die vroeger vanzelf ging moet nu expliciet gemaakt worden."),
        ("Je hebt behoefte aan effici&euml;ntere processen",
         "Incidenten en bijna-ongevallen kosten stilstand en herstelwerk. Wie dat terugdringt, wint tijd. Veiligheid en productiviteit trekken hier dezelfde kant op."),
        ("Je wilt kosten besparen",
         "Verzuim, schade en het herstellen van fouten drukken op je marge. Een hoger veiligheidsniveau vertaalt zich direct naar minder van alle drie."),
    ],
    "aanpak_kop": "De Veiligheidsladder als meetlat",
    "aanpak_intro": "We beginnen met een nulmeting: op welke trede staat de organisatie nu, en waar wil je heen? Daarna werken we per trede, met de leidinggevenden als kartrekkers. De begeleiding stopt niet bij de oplevering; we blijven aangehaakt tot het gedrag ook zonder ons blijft staan.",
    "stappen": [
        ("Pathologisch", "Veiligheid wordt gezien als iets dat van buitenaf wordt opgelegd. Er wordt vooral gekeken naar wat er nodig is om niet in de problemen te komen.",
         "&ldquo;Zolang we niet gepakt worden is het goed.&rdquo; Incidenten worden binnenskamers gehouden."),
        ("Reactief", "Er wordt gehandeld n&aacute; een incident. De organisatie kan snel schakelen als het misgaat, maar komt niet toe aan voorkomen.",
         "Na elk ongeval een maatregel, tot de aandacht wegzakt en het weer stil wordt."),
        ("Berekenend", "Veiligheid is vastgelegd in systemen, procedures en registraties. Het gebeurt omdat het moet, en het is aantoonbaar.",
         "De map is op orde en de audit wordt gehaald, maar op de vloer leeft het niet."),
        ("Proactief", "Men denkt vooruit, herkent risico&rsquo;s v&oacute;&oacute;rdat er iets gebeurt en spreekt elkaar erop aan. Leidinggevenden vragen ernaar.",
         "Een monteur legt het werk stil omdat het niet klopt, en dat wordt gewaardeerd in plaats van bestraft."),
        ("Vooruitstrevend", "Veiligheid zit in het DNA van de organisatie. Continu verbeteren is vanzelfsprekend en gaat verder dan de eigen poort.",
         "Medewerkers komen zelf met verbeteringen en delen die met leveranciers en klanten."),
    ],
    "voordelen_kop": "Wat een gedragstraject oplevert",
    "voordelen": [
        ("mensen", "Mensen spreken elkaar aan", "Aanspreken wordt normaal in plaats van vervelend. Dat is de belangrijkste graadmeter: het gebeurt ook als jij er niet bij bent."),
        ("grafiek", "Minder stilstand en herstelwerk", "Bijna-ongevallen komen boven tafel voordat ze incidenten worden, en dat scheelt direct productietijd."),
        ("schild", "Aantoonbaar niveau", "Je kunt richting opdrachtgevers en verzekeraars onderbouwen waar je staat en wat je eraan doet."),
        ("trap", "Een niveau dat blijft", "Werkwijzen worden overgedragen aan je eigen leidinggevenden, zodat het niet met ons vertrek weer wegzakt."),
    ],
    "partners": [PARTNER_EHS, PARTNER_2, PARTNER_3],
    "projecten": [
        ("Van reactief naar proactief in drie blokken", "Van Deursen Metaal B.V.", "Maart 2026", "Gorinchem",
         "Nulmeting wees uit dat de organisatie op trede twee zat. Met de voormannen als kartrekkers is in drie blokken toegewerkt naar het gedrag dat bij trede vier hoort.", "overleg"),
        ("Twee ploegen, &eacute;&eacute;n manier van werken", "Rivierpoort Logistiek", "September 2025", "Hardinxveld-Giessendam",
         "Na een samenvoeging liepen de werkafspraken uiteen. De verschillen zijn benoemd en teruggebracht tot afspraken die beide ploegen herkenden.", "productiehal"),
    ],
    "contact_kop": "Benieuwd op welke trede je staat?",
    "faq": [
        ("Hoe meten jullie op welke trede we staan?", [
            "Met observaties op de werkvloer en gesprekken op alle niveaus: directie, leidinggevenden en uitvoerenden. Wat mensen zeggen en wat ze doen verschilt vaak, en juist dat verschil is de informatie.",
            "Je krijgt een nulmeting met de trede per onderdeel, zodat duidelijk is waar de winst zit.",
        ]),
        ("Kunnen we een trede overslaan?", [
            "In de praktijk niet. Een organisatie die nog reactief werkt kun je geen proactief gedrag opleggen; dat wordt afvinkgedrag. Wel gaat de ene stap sneller dan de andere.",
        ]),
        ("Wat vragen jullie van onze eigen mensen?", [
            "Tijd van de leidinggevenden, vooral. Zij zijn degenen die het gedrag dragen; wij begeleiden hen daarin. Reken op een dagdeel per blok, plus de gesprekken op de vloer.",
        ]),
    ],
})

# ================================================================= EHS RIE
servicepagina({
    "bestand": "ehs-rie.html",
    "service_naam_kort": "EHS RIE",
    "namespace": "ehs-rie",
    "onderwerp": "ehs-rie",
    "titel": "EHS RI&amp;E | MADEGRO",
    "omschrijving": "De wettelijk verplichte risico-inventarisatie en -evaluatie, opgesteld of getoetst door MADEGRO, met een plan van aanpak dat uitvoerbaar is.",
    "service_type": "Risico-inventarisatie en -evaluatie",
    "service_naam": "EHS RI&E",
    # Zelfde beeld als de dienstkaart op de homepage, zodat je na een klik
    # ziet waar je vandaan komt.
    "hero_foto": "dienst-rie",
    # Midden: de adviseur staat rechts van het midden, links uitlijnen zou hem
    # half wegsnijden.
    "eyebrow": "Dienst 02",
    "h1": "EHS RI&amp;E",
    "intro": '''          <p>De risico-inventarisatie en -evaluatie is voor vrijwel elke werkgever in Nederland verplicht (Arbowet, artikel 5), inclusief een plan van aanpak. Heb je meer dan 25 medewerkers, dan moet een gecertificeerde kerndeskundige de RI&amp;E toetsen.</p>
          <p>MADEGRO stelt de RI&amp;E op, herziet of toetst een bestaande, en vertaalt hem naar maatregelen die je daadwerkelijk kunt uitvoeren. Environment, Health &amp; Safety in samenhang: milieu, gezondheid en veiligheid komen op dezelfde werkvloer samen.</p>''',
    "wanneer_intro": "Een RI&amp;E is geen document dat je &eacute;&eacute;n keer maakt. Bij deze drie situaties is een nieuwe of herziene inventarisatie meestal aan de orde.",
    "herkenning": [
        ("Je bedrijf groeit snel",
         "Nieuwe machines, een nieuwe hal of een nieuwe ploeg betekent nieuwe risico&rsquo;s. Een RI&amp;E van drie jaar geleden beschrijft een bedrijf dat niet meer bestaat."),
        ("Je hebt behoefte aan effici&euml;ntere processen",
         "Een goede inventarisatie legt bloot waar dubbel werk, onnodige handelingen en improvisatie zitten. Dat zijn precies de plekken waar het misgaat."),
        ("Je wilt kosten besparen",
         "Zonder actuele RI&amp;E loop je een boete en aansprakelijkheid. Belangrijker: maatregelen die je vooraf plant zijn goedkoper dan schade achteraf."),
    ],
    "aanpak_kop": "Van inventarisatie naar plan van aanpak",
    "aanpak_intro": "We lopen de vloer op, spreken met de mensen die het werk doen en toetsen aan de wettelijke eisen. Het resultaat is geen boekwerk maar een lijst waar prioriteiten in staan: wat moet nu, wat kan later, en wat kost het.",
    "stappen_comment": '<!-- TODO-CONTENT: de exacte drie stappen van het servicemodel moeten door Martin worden aangeleverd. Onderstaande is een werkbare invulling. -->',
    "stappen": [
        ("Inventarisatie", "We brengen in kaart welke risico&rsquo;s er zijn op het gebied van milieu, gezondheid en veiligheid: per afdeling, per werkplek en per machine, inclusief de taken die maar zelden voorkomen.",
         ""),
        ("Evaluatie &amp; prioritering", "Elk risico krijgt een weging naar kans en effect. Daarmee ontstaat een volgorde: wat vraagt direct om een maatregel en wat kan mee in het reguliere onderhoud.",
         ""),
        ("Plan van aanpak", "De maatregelen komen in een plan met verantwoordelijken, termijnen en een indicatie van de kosten. Dat is het document waar de arbeidsinspectie naar vraagt, en waar jij mee kunt sturen.",
         ""),
    ],
    "voordelen_kop": "Wat een RI&amp;E je oplevert",
    "voordelen": [
        ("document", "Je voldoet aantoonbaar", "Een actuele RI&amp;E met plan van aanpak is het eerste waar de arbeidsinspectie naar vraagt."),
        ("lijst", "Een werkbare prioritering", "Geen lijst van tweehonderd punten, maar een volgorde waarin je zaken kunt oppakken."),
        ("klok", "Minder verrassingen", "Risico&rsquo;s die je vooraf kent, kun je inplannen. De rest komt op het slechtste moment langs."),
        ("schild", "Klaar voor toetsing", "Boven 25 medewerkers is toetsing door een kerndeskundige verplicht; we leveren de RI&amp;E toetsklaar op."),
    ],
    "partners": [PARTNER_EHS, PARTNER_2, PARTNER_3],
    "projecten": [
        ("RI&amp;E en plan van aanpak voor een nieuwe hal", "Rivierpoort Logistiek", "November 2025", "Hardinxveld-Giessendam",
         "Bij de ingebruikname van een nieuwe hal de risico&rsquo;s in kaart gebracht en vertaald naar maatregelen die binnen het bouwbudget pasten.", "productiehal"),
        ("Herziening na uitbreiding van de productielijn", "Van Deursen Metaal B.V.", "Mei 2025", "Gorinchem",
         "De bestaande RI&amp;E dekte de nieuwe lijn niet. Herzien, getoetst en teruggebracht tot twaalf maatregelen met een termijn.", "lassen"),
    ],
    "contact_kop": "Is jullie RI&amp;E nog actueel?",
    "faq": [
        ("Hoe vaak moet een RI&amp;E herzien worden?", [
            "De wet noemt geen vaste termijn, maar zegt: bij elke belangrijke wijziging. Nieuwe machines, een verbouwing, een andere werkwijze of een flinke groei zijn allemaal aanleiding.",
            "In de praktijk komt dat neer op eens per drie tot vier jaar, of eerder als er iets verandert.",
        ]),
        ("Moet onze RI&amp;E getoetst worden?", [
            "Boven de 25 medewerkers wel, door een gecertificeerde kerndeskundige. Daaronder geldt in veel gevallen een vrijstelling, zeker als je een erkend branche-instrument gebruikt.",
            "We kijken samen wat in jouw situatie geldt, zodat je geen toetsing betaalt die niet hoeft.",
        ]),
        ("Wat als er al een RI&amp;E ligt?", [
            "Dan beginnen we niet opnieuw. We toetsen wat er ligt, vullen aan wat ontbreekt en werken het plan van aanpak bij. Dat is sneller en goedkoper dan een nieuw document.",
        ]),
    ],
})

# =========================================================== Safety Checks
servicepagina({
    "bestand": "safety-checks.html",
    "service_naam_kort": "Safety Checks",
    "namespace": "safety-checks",
    "onderwerp": "safety-checks",
    "titel": "Safety Checks | MADEGRO",
    "omschrijving": "Periodieke controles op de werkvloer: voldoet de praktijk aan de kwaliteits- en veiligheidseisen? MADEGRO levert een rapportage met concrete verbeterpunten.",
    "service_type": "Veiligheidsinspectie en audit",
    "service_naam": "Safety Checks",
    "hero_foto": "dienst-checks",
    "hero_positie": "links",
    "eyebrow": "Dienst 03",
    "h1": "Safety Checks",
    "intro": '''          <p>Een safety check is een controle op de werkvloer: voldoet wat er in de praktijk gebeurt aan de kwaliteits- en veiligheidseisen die voor jouw bedrijf gelden? Niet vanuit de kantoortafel, maar lopend, kijkend en vragend.</p>
          <p>Je krijgt een rapportage met bevindingen en concrete verbeterpunten. Geen lijst met tekortkomingen om af te vinken, maar een paar dingen waar je maandag mee kunt beginnen.</p>''',
    "wanneer_intro": "Een check is nuttig als je wilt weten hoe je ervoor staat, zonder dat er meteen een audit of incident aan te pas komt.",
    "herkenning": [
        ("Je bedrijf groeit snel",
         "Wat bij dertig man vanzelf ging, ontglipt bij tachtig. Een externe blik legt vast waar de rek eruit is."),
        ("Je hebt behoefte aan effici&euml;ntere processen",
         "Improvisatie op de vloer is bijna altijd een teken dat het proces ergens niet klopt. Een check maakt zichtbaar waar dat zit."),
        ("Je wilt kosten besparen",
         "Een certificeringsaudit die misgaat kost je een hertoetsing en tijd. Vooraf checken is goedkoper dan achteraf herstellen."),
    ],
    "aanpak_kop": "Kijken wat er echt gebeurt",
    "aanpak_intro": "We spreken vooraf af waar de check over gaat en waar de grens ligt. Op locatie lopen we mee met het werk in plaats van alleen documenten te lezen. De rapportage is kort en benoemt wat er goed gaat, want dat is even belangrijk om vast te houden.",
    "stappen_comment": '<!-- TODO-CONTENT: de exacte drie stappen van het servicemodel moeten door Martin worden aangeleverd. Onderstaande is een werkbare invulling. -->',
    "stappen": [
        ("Voorbereiding &amp; scope", "We bepalen samen wat er getoetst wordt: welke locaties, welke normen of certificeringen, en welke onderdelen buiten beschouwing blijven. Zo weet iedereen vooraf waar de check over gaat.",
         ""),
        ("Check op locatie", "Op de vloer, tijdens het werk. We kijken naar de uitvoering, spreken met medewerkers en toetsen aan de afgesproken eisen. Wat opvalt leggen we ter plekke vast met foto&rsquo;s.",
         ""),
        ("Rapportage &amp; opvolging", "Je krijgt een rapportage met bevindingen, prioriteiten en concrete verbeterpunten. We lopen hem samen door en spreken af wie wat oppakt. Een vervolgcheck laat zien of het beklijft.",
         ""),
    ],
    "voordelen_kop": "Wat een check je oplevert",
    "voordelen": [
        ("lijst", "Een eerlijk beeld", "Van iemand die er niet elke dag rondloopt en dus ziet wat jij niet meer opmerkt."),
        ("document", "Concrete verbeterpunten", "Geen abstracte aanbevelingen, maar punten met een verantwoordelijke en een termijn."),
        ("schild", "Geen verrassingen bij een audit", "Je weet vooraf waar een externe auditor op zou aanslaan."),
        ("grafiek", "Vergelijkbaar over locaties", "Meerdere vestigingen langs dezelfde meetlat, zodat je kunt zien waar het schuurt."),
    ],
    "partners": [PARTNER_EHS, PARTNER_2, PARTNER_3],
    "projecten": [
        ("Safety checks op vier locaties", "Merwede Bouwgroep", "Juni 2025", "Regio Rotterdam",
         "Vier vestigingen langs dezelfde meetlat gelegd, zodat het management voor het eerst kon vergelijken waar het echt schuurde.", "transport"),
        ("Check voorafgaand aan certificering", "Van Deursen Metaal B.V.", "Februari 2025", "Gorinchem",
         "Twee weken voor de externe audit meegelopen. De vijf punten die naar boven kwamen waren op tijd opgelost.", "haven"),
    ],
    "contact_kop": "Wil je weten hoe je ervoor staat?",
    "faq": [
        ("Hoe lang duurt een safety check?", [
            "Voor &eacute;&eacute;n locatie meestal een dag op de vloer, plus een dag voor de rapportage. Bij meerdere vestigingen plannen we ze achter elkaar, zodat de vergelijking klopt.",
        ]),
        ("Komt er een lijst met tekortkomingen uit?", [
            "Nee. Een lijst van honderd punten leest niemand. Je krijgt de punten die er echt toe doen, met een prioriteit, plus wat er goed gaat.",
        ]),
        ("Is dit hetzelfde als een audit?", [
            "Niet helemaal. Een audit toetst formeel aan een norm en leidt tot een certificaat. Een safety check is een praktijkcontrole zonder die formele status, vaak juist gebruikt om een audit voor te bereiden.",
        ]),
    ],
})
