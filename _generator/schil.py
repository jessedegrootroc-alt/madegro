# -*- coding: utf-8 -*-
import pathlib
"""
Gedeelde paginaschil voor de MADEGRO-site.

Dit script schrijft platte HTML-bestanden weg. De site zelf heeft geen build-stap:
wat hier uitkomt is gewone HTML die je met een statische server serveert. Dit
bestand hoort dan ook niet bij de site, het is gereedschap om de dertien pagina's
identiek te houden terwijl ze gebouwd worden.
"""

BASIS = "https://www.madegro.nl"

# Het hoofdmenu. Een item is óf een gewone link, óf een uitklapper met sublinks
# en een kaart ernaast. De drie diensten en de vier cursussen stonden hier
# eerder allemaal los naast elkaar; dat waren zeven items op één balk.
#
# De sublinks komen uit SERVICES en CURSUSSEN verderop in dit bestand, zodat een
# wijziging daar meteen in het menu, de voet en de overzichtspagina's landt.
# Daarom wordt NAV pas onderaan opgebouwd, in bouw_nav().
NAV = []

# Het vijfde veld is de sleutel uit FOTOS voor het beeld op de kaart.
# TODO-CONTENT: dit is opvulbeeld uit de stockmap. Er zijn zes foto's voor
# zeven kaarten (vier cursussen plus drie diensten), dus er zit een herhaling
# in. Zodra Martin foto's van zijn eigen cursussen heeft, vervangen die deze.
CURSUSSEN = [
    ("cursus-veiligheidsbewustzijn.html", "Veiligheidsbewustzijn op de werkvloer",
     "Voor operators en uitvoerenden", "1 dagdeel", "cursus-bewustzijn-bouw"),
    ("cursus-risicobeoordeling.html", "Risico&rsquo;s herkennen en beoordelen",
     "Voor voormannen en teamleiders", "2 dagdelen", "cursus-risico-lijn"),
    ("cursus-veiligheidsladder.html", "Werken met de Veiligheidsladder",
     "Voor KAM- en HSE-co&ouml;rdinatoren", "3 dagdelen", "cursus-ladder-helmen"),
    ("cursus-rie-praktijk.html", "RI&amp;E in de praktijk",
     "Voor preventiemedewerkers", "2 dagdelen", "cursus-rie-tablet"),
]


# TODO-CONTENT: alle zes de cases zijn verzonnen om het template te vullen.
# Bedrijfsnamen, cijfers, citaten en jaartallen moeten door Martin worden
# vervangen voordat de site live gaat.
CASES = [
    {
        "slug": "van-deursen-metaal",
        "titel": "Van reactief naar proactief in drie blokken",
        "klant": "Van Deursen Metaal B.V.",
        "dienst": "Veilig gedrag",
        "branche": "Productie",
        "plaats": "Gorinchem",
        "datum": "Maart 2026",
        "beeld": "lassen",
        "kort": "Twee ploegen die na een reorganisatie anders werkten, teruggebracht naar één manier van doen. De voormannen trokken de kar.",
        "cijfers": [("Trede bij de nulmeting", "2", "van 5"),
                    ("Trede na het traject", "4", "van 5"),
                    ("Doorlooptijd", "7", "maanden"),
                    ("Meldingen bijna-ongevallen", "3x", "meer")],
        "situatie": "Na een samenvoeging van twee productiehallen liepen de werkafspraken uiteen. Wat in de ene ploeg vanzelfsprekend was, gold in de andere niet, en niemand sprak elkaar erop aan.",
        "over": "Van Deursen Metaal maakt constructiedelen voor de scheepsbouw. Zestig medewerkers, twee ploegen, een machinepark dat in tien jaar flink is uitgebreid.",
        "uitdaging": "De directie wilde één veiligheidsniveau over beide hallen. Op papier lag alles vast, maar op de vloer werkte iedere ploeg naar eigen inzicht. Een nulmeting langs de Veiligheidsladder liet zien dat de organisatie op trede twee stond: er werd pas gehandeld ná een incident.",
        "citaat": ("De rapportage was de eerste die onze ploegleiders uit zichzelf hebben doorgelezen. Geen lijst met tekortkomingen, maar een paar dingen die je maandag kunt aanpakken.", "Karin Vermeer", "KAM-coördinator"),
        "oplossing": "In drie blokken van elk twee maanden hebben we met de voormannen gewerkt aan het gedrag dat bij trede vier hoort. Elk blok begon op de vloer, met observaties, en eindigde met afspraken die de voormannen zelf opschreven. Wij begeleidden, zij voerden uit.",
        "resultaat": "Bij de hermeting stond de organisatie op trede vier. Belangrijker: het aantal gemelde bijna-ongevallen verdrievoudigde. Dat klinkt verkeerd, maar het betekent dat mensen dingen melden die ze eerder lieten lopen.",
        "bleed": ['productiehal', 'overleg'],
        "uitdaging_punten": [
            "Twee hallen die na de samenvoeging elk hun eigen werkafspraken hadden aangehouden.",
            "Een nulmeting op trede twee: er werd pas gehandeld n&aacute;dat er iets was gebeurd.",
        ],
        "aanpak_punten": [
            "Drie blokken van twee maanden, elk beginnend met observaties op de vloer.",
            "De voormannen schreven de afspraken zelf op; wij begeleidden alleen.",
            "Een hermeting langs dezelfde meetlat als de nulmeting.",
        ],
        "verwant": ["rivierpoort-logistiek", "merwede-bouwgroep"],
    },
    {
        "slug": "rivierpoort-logistiek",
        "titel": "RI&amp;E en plan van aanpak voor een nieuwe hal",
        "klant": "Rivierpoort Logistiek",
        "dienst": "EHS RIE",
        "branche": "Logistiek",
        "plaats": "Hardinxveld-Giessendam",
        "datum": "November 2025",
        "beeld": "productiehal",
        "kort": "Bij de ingebruikname van een nieuwe hal de risico’s in kaart gebracht en vertaald naar maatregelen die binnen het bouwbudget pasten.",
        "cijfers": [("Werkplekken beoordeeld", "34", ""),
                    ("Maatregelen in het plan", "18", ""),
                    ("Daarvan binnen een maand af", "11", ""),
                    ("Doorlooptijd", "5", "weken")],
        "situatie": "Een nieuwe hal van 4.000 m² ging in gebruik. De bestaande RI&amp;E beschreef een bedrijf dat niet meer bestond.",
        "over": "Rivierpoort Logistiek doet opslag en distributie voor de maakindustrie. Tachtig medewerkers, drie ploegen, veel intern transport.",
        "uitdaging": "De oplevering stond gepland, de eerste pallets zouden binnen twee maanden binnenkomen, en er lag nog geen actuele risico-inventarisatie. Boven de 25 medewerkers is toetsing door een gecertificeerde kerndeskundige verplicht, dus het document moest ook toetsklaar zijn.",
        "citaat": ("We dachten dat we het wel wisten. De rondgang liet zien dat de drukste kruising in de hal nergens op papier stond.", "Stefan de Bruin", "Operationeel manager"),
        "oplossing": "We hebben de hal in gebruik genomen zoals hij bedoeld was en meegelopen met het werk: laden, lossen, orderpicken, heftruckverkeer. Elke werkplek is beoordeeld op kans en effect. Het plan van aanpak kreeg per maatregel een eigenaar, een termijn en een kostenindicatie.",
        "resultaat": "Achttien maatregelen, waarvan elf binnen een maand uitgevoerd. De RI&amp;E is getoetst zonder aanvullende opmerkingen. De verkeersroutes in de hal zijn vóór ingebruikname aangepast, wat achteraf een stuk duurder was geweest.",
        "bleed": ['transport', 'overleg'],
        "uitdaging_punten": [
            "Een nieuwe hal van 4.000 m&sup2; die over twee maanden in gebruik ging.",
            "Een RI&amp;E die een bedrijf beschreef dat niet meer bestond.",
            "Boven de 25 medewerkers moet het document toetsklaar zijn voor een kerndeskundige.",
        ],
        "aanpak_punten": [
            "Meegelopen met laden, lossen, orderpicken en heftruckverkeer in de hal zelf.",
            "Vierendertig werkplekken beoordeeld op kans en effect.",
            "Per maatregel een eigenaar, een termijn en een kostenindicatie.",
        ],
        "verwant": ["van-deursen-metaal", "merwede-bouwgroep"],
    },
    {
        "slug": "merwede-bouwgroep",
        "titel": "Safety checks op vier locaties langs dezelfde meetlat",
        "klant": "Merwede Bouwgroep",
        "dienst": "Safety Checks",
        "branche": "Bouw",
        "plaats": "Regio Rotterdam",
        "datum": "Juni 2025",
        "beeld": "bouwplaats",
        "kort": "Vier vestigingen op dezelfde manier getoetst, zodat het management voor het eerst kon vergelijken waar het echt schuurde.",
        "cijfers": [("Locaties getoetst", "4", ""),
                    ("Bevindingen totaal", "27", ""),
                    ("Met prioriteit hoog", "6", ""),
                    ("Tijd op locatie", "1", "dag per vestiging")],
        "situatie": "Vier vestigingen, vier manieren van werken, en een directie die geen idee had waar de grootste risico’s zaten.",
        "over": "Merwede Bouwgroep werkt aan utiliteitsbouw en renovatie. Honderdtwintig medewerkers verdeeld over vier vestigingen.",
        "uitdaging": "Elke vestiging rapporteerde zijn eigen cijfers, in zijn eigen format. Vergelijken was onmogelijk, dus ging de aandacht naar de vestiging die het hardst riep in plaats van naar die met het grootste risico.",
        "citaat": ("Martin praat met de mensen op de vloer, niet alleen met de directie. Dat merk je aan wat er daarna verandert.", "Hans Molenaar", "Directeur"),
        "oplossing": "Vier checks in dezelfde week, met dezelfde meetlat en dezelfde vragen. Per vestiging een dag meelopen tijdens het werk, foto’s bij de bevindingen, en één rapportage waarin de vier naast elkaar staan.",
        "resultaat": "Zevenentwintig bevindingen, waarvan zes met prioriteit hoog. Twee daarvan zaten op de vestiging die het minst geklaagd had. Sindsdien draait de check twee keer per jaar op alle vier de locaties.",
        "bleed": ['overleg', 'lassen'],
        "uitdaging_punten": [
            "Vier vestigingen die elk in hun eigen format rapporteerden.",
            "De aandacht ging naar wie het hardst riep, niet naar het grootste risico.",
        ],
        "aanpak_punten": [
            "Vier checks in dezelfde week, met dezelfde vragen en dezelfde meetlat.",
            "Per vestiging een dag meelopen tijdens het werk, met foto&rsquo;s bij elke bevinding.",
            "&Eacute;&eacute;n rapportage waarin de vier vestigingen naast elkaar staan.",
        ],
        "verwant": ["van-deursen-metaal", "rivierpoort-logistiek"],
    },
    {
        "slug": "hollands-diep-transport",
        "titel": "Aanspreken normaal maken in een ploegendienst",
        "klant": "Hollands Diep Transport",
        "dienst": "Veilig gedrag",
        "branche": "Logistiek",
        "plaats": "Dordrecht",
        "datum": "Januari 2026",
        "beeld": "transport",
        "kort": "Chauffeurs die elkaar nooit zagen, toch één werkwijze laten delen. Het begon met vijf minuten aan het begin van elke dienst.",
        "cijfers": [("Chauffeurs betrokken", "45", ""),
                    ("Ploegen", "3", ""),
                    ("Schademeldingen", "40", "% minder"),
                    ("Doorlooptijd", "5", "maanden")],
        "situatie": "Drie ploegen die elkaar op de wisseling van vijf minuten na nooit spraken. Afspraken bleven hangen in de ploeg waar ze gemaakt waren.",
        "over": "Hollands Diep Transport rijdt bulk- en stukgoed door de Benelux. Vijfenveertig chauffeurs, drie ploegen, een eigen werkplaats.",
        "uitdaging": "Iedere ploeg had zijn eigen gewoontes rond laden, zekeren en manoeuvreren op het terrein. De schadecijfers verschilden een factor drie tussen de ploegen, zonder dat iemand kon uitleggen waarom.",
        "citaat": ("Het gekke is: we hebben niets nieuws bedacht. We hebben opgeschreven wat de beste ploeg al deed.", "Ellen Rietveld", "Planner"),
        "oplossing": "Vijf minuten aan het begin van elke dienst, met één vast onderwerp per week, aangedragen door de chauffeurs zelf. Wij hebben de eerste zes weken meegedraaid en daarna de planners opgeleid om het over te nemen.",
        "resultaat": "Na vijf maanden zaten de drie ploegen op vergelijkbare schadecijfers, veertig procent onder het oude gemiddelde. De vijf minuten staan nog steeds in de dienstplanning.",
        "bleed": ['haven', 'overleg'],
        "uitdaging_punten": [
            "Drie ploegen met elk eigen gewoontes rond laden, zekeren en manoeuvreren.",
            "Schadecijfers die een factor drie uiteenliepen, zonder dat iemand wist waarom.",
        ],
        "aanpak_punten": [
            "Vijf minuten aan het begin van elke dienst, met &eacute;&eacute;n onderwerp per week.",
            "De onderwerpen kwamen van de chauffeurs zelf.",
            "Zes weken meegedraaid, daarna de planners opgeleid om het over te nemen.",
        ],
        "verwant": ["van-deursen-metaal", "rivierpoort-logistiek"],
    },
    {
        "slug": "waalhaven-terminal",
        "titel": "Een check twee weken vóór de certificeringsaudit",
        "klant": "Waalhaven Terminal",
        "dienst": "Safety Checks",
        "branche": "Logistiek",
        "plaats": "Rotterdam",
        "datum": "Februari 2025",
        "beeld": "haven",
        "kort": "Meegelopen alsof het de echte audit was. De vijf punten die naar boven kwamen waren op tijd opgelost.",
        "cijfers": [("Bevindingen", "5", ""),
                    ("Opgelost voor de audit", "5", ""),
                    ("Afwijkingen bij de audit", "0", ""),
                    ("Tijd op locatie", "2", "dagen")],
        "situatie": "Over twee weken kwam de externe auditor langs. Niemand wist zeker of het zou lukken.",
        "over": "Waalhaven Terminal doet overslag van stukgoed. Vijfendertig medewerkers, ploegendienst, veel bezoekende chauffeurs op het terrein.",
        "uitdaging": "De vorige audit had drie afwijkingen opgeleverd en een hertoetsing gekost. De directie wilde dat niet nog een keer, maar had geen zicht op wat er nu nog open stond.",
        "citaat": ("Twee dagen meelopen was genoeg. Hij zag dingen die wij al jaren niet meer zien.", "Peter Vonk", "Terminalmanager"),
        "oplossing": "Twee dagen op locatie, met de norm ernaast, precies zoals een auditor het zou doen. Bevindingen dezelfde dag gedeeld, zodat er meteen aan gewerkt kon worden in plaats van na een rapport van twee weken later.",
        "resultaat": "Vijf bevindingen, alle vijf opgelost voordat de auditor kwam. De audit sloot zonder afwijkingen.",
        "bleed": ['transport', 'bouwplaats'],
        "uitdaging_punten": [
            "Een vorige audit met drie afwijkingen en een hertoetsing als gevolg.",
            "Geen zicht op wat er van die punten nog open stond.",
        ],
        "aanpak_punten": [
            "Twee dagen op locatie met de norm ernaast, zoals een auditor het zou doen.",
            "Bevindingen dezelfde dag gedeeld in plaats van na twee weken.",
            "Een korte lijst met wat v&oacute;&oacute;r de audit af moest en wat kon wachten.",
        ],
        "verwant": ["merwede-bouwgroep", "rivierpoort-logistiek"],
    },
    {
        "slug": "de-groot-bouwstoffen",
        "titel": "Een RI&amp;E die eindelijk gebruikt wordt",
        "klant": "De Groot Bouwstoffen",
        "dienst": "EHS RIE",
        "branche": "Bouw",
        "plaats": "Sliedrecht",
        "datum": "September 2025",
        "beeld": "overleg",
        "kort": "Een bestaand document van 90 pagina’s teruggebracht tot twaalf maatregelen waar iemand verantwoordelijk voor is.",
        "cijfers": [("Pagina’s in het oude document", "90", ""),
                    ("Maatregelen na herziening", "12", ""),
                    ("Met eigenaar en termijn", "12", ""),
                    ("Doorlooptijd", "3", "weken")],
        "situatie": "Er lág een RI&amp;E. Negentig pagina’s, drie jaar oud, en niemand die hem ooit had opengeslagen.",
        "over": "De Groot Bouwstoffen levert bouwmaterialen aan aannemers in de regio. Vijfentwintig medewerkers, een buitenterrein en een eigen bezorgdienst.",
        "uitdaging": "Het document was compleet maar onbruikbaar: geen prioriteiten, geen eigenaren, geen termijnen. Bij de laatste inspectie was dat precies het punt waar het op vastliep.",
        "citaat": ("We hadden een RI&amp;E om te hebben. Nu hebben we er een om mee te werken.", "Joke van Wijk", "Preventiemedewerker"),
        "oplossing": "Niet opnieuw beginnen, maar herzien. We hebben getoetst wat er lag, aangevuld wat ontbrak rond het buitenterrein, en het plan van aanpak teruggebracht tot twaalf maatregelen met een naam en een datum erbij.",
        "resultaat": "Twaalf maatregelen, allemaal belegd. Het plan wordt nu elk kwartaal in het werkoverleg doorgenomen, en dat kost een kwartier.",
        "bleed": ['bouwplaats', 'transport'],
        "uitdaging_punten": [
            "Een compleet document zonder prioriteiten, eigenaren of termijnen.",
            "Precies het punt waarop de laatste inspectie vastliep.",
        ],
        "aanpak_punten": [
            "Niet opnieuw beginnen: getoetst wat er lag en aangevuld wat ontbrak.",
            "Het buitenterrein alsnog in kaart gebracht.",
            "Het plan van aanpak terug naar twaalf maatregelen met een naam en een datum.",
        ],
        "verwant": ["rivierpoort-logistiek", "van-deursen-metaal"],
    },
]


def case(slug):
    return next(c for c in CASES if c["slug"] == slug)

# Vierde veld: de beeldsleutel, net als bij CURSUSSEN.
SERVICES = [
    ("veilig-gedrag.html", "Veilig gedrag", "Van papier naar werkvloer", "overleg"),
    ("ehs-rie.html", "EHS RIE", "Risico&rsquo;s in kaart, met een plan dat werkt", "lassen"),
    ("safety-checks.html", "Safety Checks", "Periodiek toetsen wat er echt gebeurt", "haven"),
]

def bouw_nav():
    """NAV invullen zodra SERVICES en CURSUSSEN bekend zijn."""
    NAV.extend([
        {"soort": "link", "href": "index.html", "label": "Home"},
        {
            "soort": "uitklap", "id": "diensten", "label": "Diensten",
            "links": [(b, t, o) for b, t, o, _ in SERVICES],
            "kaart": {
                "kop": "Weten waar je staat?",
                "tekst": "In een gesprek van een halfuur brengen we in beeld welke van de drie het meest oplevert in jouw situatie.",
                "knop": "Plan een gesprek",
                "href": "contact.html",
                "foto": "overleg",
            },
        },
        {
            "soort": "uitklap", "id": "cursussen", "label": "Cursussen",
            "links": ([("cursusaanbod.html", "Alle cursussen", "Het volledige aanbod op een rij")]
                      + [(b, t, o) for b, t, o, _, _ in CURSUSSEN]),
            "kaart": {
                "kop": "Twijfel je welke cursus past?",
                "tekst": "Vertel kort wie er meedoet en waar het werk om draait; we denken mee over de volgorde.",
                "knop": "Plan een gesprek",
                "href": "contact.html",
                "foto": "productiehal",
            },
        },
        {"soort": "link", "href": "cases.html", "label": "Cases"},
        {"soort": "link", "href": "over-ons.html", "label": "Over ons"},
    ])


# TODO-CONTENT: contactgegevens laten bevestigen door Martin
TELEFOON_WEERGAVE = "0184 00 00 00"
TELEFOON_LINK = "+31184000000"
EMAIL = "info@madegro.nl"
ADRES = "Wieling 39, 3371 PB Hardinxveld-Giessendam"
KVK = "81812892"
REACTIETIJD = "twee werkdagen"

# Praktische gegevens van de cursussen. Ze stonden alleen in de FAQ-antwoorden;
# als los veld kunnen ze ook in de kerncijfers boven aan de pagina staan.
# TODO-CONTENT: het tarief is een aanname en moet door Martin bevestigd worden.
GROEP = "12"
PRIJS = "&euro; 750"
PRIJS_EENHEID = "per dagdeel"


# (naam, groot, groothoogte, klein, kleinhoogte, alt, map, midden)
#
# Middenmaat staat op None voor alle foto's, en dat is een bewuste keuze. Er
# hebben tussenmaten van 800px in gezeten, want op een telefoon van 412 CSS-
# pixels met dpr 1,75 is 721px nodig en dan slaat de browser 640 over en neemt
# 1200. Op papier drie keer zoveel pixels als er te zien is.
#
# In beeld pakte dat verkeerd uit. Een kandidaat die net boven de gevraagde
# breedte ligt wordt door de browser met een goedkoper filter verkleind dan een
# kandidaat die er ruim boven ligt: 800 naar 720 werd zichtbaar zachter dan 1200
# naar 720. Vergeleken op schermafdrukken van voor en na, en nagerekend: de
# scherpte van het gebied zakte met ruim zestig procent. Dat is precies wat we
# niet wilden inleveren, dus de tussenmaten zijn eruit.
#
# Bij de patronen staat wel een tussenmaat, want daar zit geen fijn detail in
# dat zachter kan worden; het zijn vloeiende verlopen.
FOTOS = {
    'bouwplaats':   ('bouwplaats', 2400, 1350, 1200, 675, 'Bouwplaats met torenkraan', 'foto', None),
    # Het eerste beeldje van de herovideo, zodat het stilstaande beeld en de
    # eerste frame van de film op elkaar aansluiten.
    'logistiek':    ('logistiek', 2400, 1350, 1200, 675, 'Vrachtwagen op een dijkweg langs het water', 'foto', None),
    'productiehal': ('productiehal', 1024, 309, 640, 193, 'Productiehal met medewerkers aan de lijn', 'foto', None),
    'lassen':       ('lassen', 1024, 683, 640, 427, 'Lasser aan het werk aan een constructie', 'foto', None),
    'overleg':      ('overleg', 960, 640, 640, 427, 'Werkoverleg met een klein team', 'foto', None),
    'transport':    ('transport', 1024, 683, 640, 427, 'Industri\u00eble transportbrug en constructie', 'foto', None),
    'haven':        ('haven', 960, 540, 640, 360, 'Zeeschip aan de kade van een containerterminal', 'foto', None),
    'martin-band':  ('martin-band', 800, 800, 440, 440,
                     'Martin de Groot, zittend op een trap voor het Viaduc de Passy in Parijs', 'foto', None),
    'terrein':      ('madegro-terrein', 1520, 993, 800, 523,
                     'Bedrijfsterrein van boven: een vrachtwagen rijdt door de scanpoort naar de slagboom, bij de portiersloge en het tourniquet controleren medewerkers de toegang, en camera&rsquo;s houden het hek en de laadkuil in de gaten',
                     'illustratie', None),
    # Cursusfoto's, aangeleverd door Jesse op 3 september 2026 (assets/foto/bron/).
    # De maten staan in MATEN; width/height hier zijn die van de grootste maat.
    'cursus-bewustzijn-bouw': ('cursus-bewustzijn-bouw', 1920, 1280, 480, 320,
                     'Uitvoerder in oranje veiligheidsjas kijkt toe terwijl twee bouwvakkers wapening vlechten op een bouwplaats', 'foto', 1200),
    'cursus-risico-lijn':     ('cursus-risico-lijn', 2400, 1600, 480, 320,
                     'Medewerker in blauwe overall en gele helm bedient een machine aan een productielijn vol slangen en kabels', 'foto', 1200),
    'cursus-ladder-helmen':   ('cursus-ladder-helmen', 2400, 1347, 480, 269,
                     'Twee medewerkers met helm en hesje kijken omhoog in een installatie, een van hen met een tekening in de hand', 'foto', 1200),
    'cursus-rie-tablet':      ('cursus-rie-tablet', 700, 525, 480, 360,
                     'Man met tablet op een bordes boven een productielijn met robotarmen', 'foto', None),
}


# Hoe breed een kaart werkelijk is, voor het sizes-attribuut. Zonder dit haalt
# de browser het grootste bestand op voor een kaart van een kwart pagina breed.
BEELD_MATEN_4 = "(max-width: 767px) 100vw, (max-width: 991px) 50vw, 25vw"
BEELD_MATEN_3 = "(max-width: 991px) 100vw, 33vw"


def foto(sleutel, klasse='', laden='lazy', maten='100vw', alt=None):
    """Eén beeld, in AVIF met WebP als terugval, in meerdere breedtes.

       <picture> met een AVIF-bron en een WebP-<img>. AVIF is bij gelijke
       kwaliteit ruwweg een derde tot de helft kleiner dan WebP; elke browser van
       de laatste jaren kan het lezen, en wie het niet kan krijgt de WebP. De
       browser kiest de breedte zelf, op grond van sizes en de pixeldichtheid.

       De breedtes komen uit MATEN[sleutel] als die er is, anders uit de tuple
       (kleine, middel, grote maat). Bestanden heten <naam>-<breedte>.<ext>.
       width en height zijn die van de grootste maat; ze leggen de verhouding
       vast, zodat er niets verspringt terwijl het beeld nog laadt.

       De alt-tekst beschrijft wat er te zien is; bij puur decoratief beeld geef
       je alt='' mee."""
    naam, gb, gh, kb, kh, standaard_alt, map_, mb = FOTOS[sleutel]
    tekst = standaard_alt if alt is None else alt
    prioriteit = ' fetchpriority="high" decoding="async"' if laden == 'eager' else ' decoding="async"'
    breedtes = sorted(MATEN.get(sleutel) or ({kb, gb} | ({mb} if mb else set())))
    bron = lambda ext: ', '.join(f'assets/{map_}/{naam}-{b}.{ext} {b}w' for b in breedtes)
    klasse_attr = f' class="{klasse}"' if klasse else ''

    # Vangnet. Een <source> naar een bestand dat er niet is, is erger dan geen
    # <source>: de browser kiest de AVIF-bron op type, en valt bij een 404 NIET
    # terug op de WebP. Je krijgt dan een kapot beeld. Dat is precies wat er
    # gebeurde toen zes foto's wel een WebP hadden en nog geen AVIF. Dus: alleen
    # een AVIF-bron als elk bestand in die srcset ook echt op schijf staat, en
    # anders hard stoppen als ook de WebP ontbreekt, want dan is de build fout.
    wortel = pathlib.Path(__file__).resolve().parent.parent
    ontbreekt = [b for b in breedtes if not (wortel / f'assets/{map_}/{naam}-{b}.webp').exists()]
    if ontbreekt:
        raise FileNotFoundError(f'foto {sleutel!r}: WebP ontbreekt voor breedte(s) {ontbreekt}')
    avif_compleet = all((wortel / f'assets/{map_}/{naam}-{b}.avif').exists() for b in breedtes)
    avif_bron = f'<source type="image/avif" srcset="{bron("avif")}" sizes="{maten}">' if avif_compleet else ''

    return (f'<picture>{avif_bron}'
            f'<img src="assets/{map_}/{naam}-{gb}.webp" srcset="{bron("webp")}" sizes="{maten}" '
            f'width="{gb}" height="{gh}" alt="{tekst}" loading="{laden}"{prioriteit}{klasse_attr}>'
            f'</picture>')


# Per fotosleutel de breedtes die er als bestand van bestaan. Staat een sleutel
# hier niet in, dan gelden de maten uit de FOTOS-tuple. De ladder is afgestemd
# op waar het beeld staat: een band over de volle breedte gaat tot 2400, een
# kaart van een derde pagina hoeft niet verder dan 960.
MATEN = {
    'cursus-bewustzijn-bouw': [480, 800, 1200, 1800, 1920],
    'cursus-risico-lijn':     [480, 800, 1200, 1800, 2400],
    'cursus-ladder-helmen':   [480, 800, 1200, 1800, 2400],
    'cursus-rie-tablet':      [480, 700],
}


PIJL = ('<svg class="arrow--animation is-{n}" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true">'
        '<path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/></svg>')


SPOOR = ('<span class="button__spoor" aria-hidden="true">'
         + PIJL.format(n=1).replace('width="16" height="16"', 'width="14" height="14"')
         + PIJL.format(n=2).replace('width="16" height="16"', 'width="14" height="14"')
         + '</span>')


def _inhoud(label):
    return f'<span class="button__inhoud">{label}{SPOOR}</span>'


def knop(label, href, soort='primary', extra=''):
    """De grote CTA-knop met dezelfde pijlwissel als de ronde icoonknop."""
    attr = f' {extra}' if extra else ''
    return f'<a href="{href}" class="button button--{soort}"{attr}>{_inhoud(label)}</a>'


def icoonknop(maat="", soort=""):
    """De ronde icoonknop uit §6.6.2. Decoratief: de hele kaart is de link.

       soort="button--secundair" geeft de diepgroene variant; die is voor de
       cases, die naast diensten en cursussen de tweede keus zijn."""
    klasse = f"button--icon {maat} {soort}".strip()
    return (f'<span class="{klasse}" aria-hidden="true" inert>'
            f'<span class="button--circle"><span class="circle-container">'
            f'{PIJL.format(n=1)}{PIJL.format(n=2)}'
            f'</span></span></span>')


CHEVRON = ('<svg class="submenu--chevron" width="12" height="12" viewBox="0 0 24 24" aria-hidden="true">'
           '<path d="M12 15.4 5.6 9 7 7.6l5 5 5-5L18.4 9 12 15.4Z"/></svg>')


def header(actief):
    """De balk met het logo, het hoofdmenu en de hamburger, plus de uitklappers
       en het mobiele paneel.

       De uitklappers staan buiten .header--container: ze lopen over de volle
       breedte onder de balk door, en dat kan niet binnen een flexrij. De balk
       is position:fixed en dus het ankerpunt voor hun position:absolute."""

    def is_actief(item):
        if item["soort"] == "link":
            return item["href"] == actief
        return any(b == actief for b, _, _ in item["links"])

    def bureau_item(item):
        aan = is_actief(item)
        klasse = "submenu--link is-actief" if aan else "submenu--link"
        if item["soort"] == "link":
            huidig = ' aria-current="page"' if aan else ""
            return f'      <a class="{klasse}" href="{item["href"]}"{huidig}>{item["label"]}</a>'
        return (f'      <button type="button" class="{klasse} submenu--trigger" '
                f'data-uitklap="{item["id"]}" aria-expanded="false" '
                f'aria-controls="uitklap-{item["id"]}">{item["label"]}{CHEVRON}</button>')

    def paneel(item):
        if item["soort"] != "uitklap":
            return ""
        k = item["kaart"]
        links = "\n".join(
            f'          <li><a class="uitklap__link" href="{b}">'
            f'<span class="uitklap__naam">{titel}</span>'
            f'<span class="uitklap__uitleg">{onder}</span></a></li>'
            for b, titel, onder in item["links"])
        return f'''  <div class="uitklap" id="uitklap-{item["id"]}" data-uitklap-paneel="{item["id"]}" inert>
    <div class="uitklap__inner">
      <div class="uitklap__kolom">
        <span class="subtitle">{item["label"]}</span>
        <ul class="uitklap__lijst" role="list">
{links}
        </ul>
      </div>
      <div class="uitklap__kaart">
        {foto(k["foto"], maten="(max-width: 1199px) 0px, 40vw", alt="")}
        <span class="uitklap__sluier" aria-hidden="true"></span>
        <div class="uitklap__kaart-tekst">
          <p class="uitklap__kaart-kop">{k["kop"]}</p>
          <p class="uitklap__kaart-body">{k["tekst"]}</p>
          {knop(k["knop"], k["href"])}
        </div>
      </div>
    </div>
  </div>'''

    def mobiel_item(item, i):
        vertraging = f'style="transition-delay:{i * 60}ms"'
        rol = (f'<span class="mobile-panel--text-slide"><span class="mobile-panel--text-slide-inner">'
               f'<span>{item["label"]}</span><span>{item["label"]}</span></span></span>')
        if item["soort"] == "link":
            return (f'      <li><a class="mobile-panel--nav-link" href="{item["href"]}" '
                    f'data-panel-sluit {vertraging}>{rol}</a></li>')
        sub = "\n".join(
            f'          <li><a class="mobile-panel--sublink" href="{b}" data-panel-sluit>{titel}</a></li>'
            for b, titel, _ in item["links"])
        return f'''      <li>
        <button type="button" class="mobile-panel--nav-link mobile-panel--nav-knop"
                data-mobiel-uitklap="{item["id"]}" aria-expanded="false"
                aria-controls="mobiel-{item["id"]}" {vertraging}>{rol}{CHEVRON}</button>
        <ul class="mobile-panel--sublijst" id="mobiel-{item["id"]}" role="list" hidden>
{sub}
        </ul>
      </li>'''

    links = "\n".join(bureau_item(n) for n in NAV)
    panelen = "\n".join(filter(None, (paneel(n) for n in NAV)))
    paneel_links = "\n".join(mobiel_item(n, i) for i, n in enumerate(NAV))

    return f'''<header class="header header--scrolled" id="siteHeader">
  <div class="header--container">
    <a href="index.html" class="header--logo" aria-label="MADEGRO, naar de homepage">
      <img class="header--logo-kleur" src="assets/logo/madegro-logo.svg" alt="MADEGRO" width="227" height="40">
      <img class="header--logo-wit" src="assets/logo/madegro-logo-wit.svg" alt="" aria-hidden="true" width="227" height="40">
    </a>

    <nav class="submenu" aria-label="Hoofdmenu">
{links}
      <a class="submenu--link highlight" href="contact.html">Contact</a>
    </nav>

    <button type="button" id="hamburger" class="hamburger" aria-expanded="false" aria-controls="mobilePanel">
      Menu
      <svg width="16" height="16" viewBox="0 0 24 24" aria-hidden="true"><path d="M2 5h20v2H2V5Zm0 6h20v2H2v-2Zm0 6h20v2H2v-2Z"/></svg>
    </button>
  </div>

{panelen}
</header>

<div class="mobile-panel--overlay" id="panelOverlay" hidden></div>
<div class="mobile-panel" id="mobilePanel" role="dialog" aria-modal="true" aria-label="Menu">
  <div class="mobile-panel--topbar">
    <a class="mobile-panel--chip" href="contact.html">Contact</a>
    <button type="button" class="mobile-panel--chip is-close" id="panelSluit">
      Sluiten
      <svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M19 6.4 17.6 5 12 10.6 6.4 5 5 6.4 10.6 12 5 17.6 6.4 19l5.6-5.6 5.6 5.6 1.4-1.4-5.6-5.6L19 6.4Z"/></svg>
    </button>
  </div>
  <nav class="mobile-panel--nav" aria-label="Hoofdmenu">
    <span class="mobile-panel--label">Menu</span>
    <ul class="mobile-panel--list" role="list">
{paneel_links}
    </ul>
  </nav>
  <div class="mobile-panel--cta button__mobile-width">
    {knop("Contact opnemen", "contact.html")}
  </div>
</div>'''


def footer():
    services = "\n".join(f'            <li><a href="{b}">{t}</a></li>' for b, t, _, _ in SERVICES)
    cursussen = "\n".join(f'            <li><a href="{b}">{t}</a></li>' for b, t, _, _, _ in CURSUSSEN)
    return f'''<footer class="footer">
  <div class="container">
    <div class="footer--widgets">
      <div class="row footer--gap">
        <div class="col-lg-3 col-md-4 col-12 widget">
          <img src="assets/logo/madegro-logo.svg" alt="MADEGRO" width="227" height="40" style="margin-bottom:var(--space-500)">
          <p class="footer--intro">Advies en begeleiding op het gebied van veiligheid en kwaliteit, voor bedrijven die verder willen dan het vinkje.</p>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h4>Diensten</h4>
          <ul role="list">
{services}
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h4>Cursussen</h4>
          <ul role="list">
{cursussen}
          </ul>
        </div>
        <div class="col-lg-3 col-md-4 col-12 widget">
          <h4>Contact</h4>
          <ul role="list">
            <li><a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a></li>
            <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
          </ul>
          <p class="footer--adres">{ADRES}<br>KvK {KVK}</p>
        </div>
      </div>
    </div>
    <div class="footer--line"></div>
    <div class="footer--copyright">
      <span>&copy; 2026 Madegro Advies B.V.</span>
      <a href="privacybeleid.html">Privacybeleid</a>
      <a href="cookies.html">Cookies</a>
    </div>
  </div>
</footer>'''


COOKIEBALK = '''<!-- ================= COOKIEMELDING ================= -->
<aside id="cookiebalk" class="cookiebalk" hidden aria-label="Cookiemelding">
  <h2>Cookie-instellingen</h2>
  <p>Deze site plaatst alleen wat nodig is om hem te laten werken. Zet je analytische cookies aan, dan help je ons te zien wat werkt en wat niet. Lees het <a href="cookies.html">cookiebeleid</a>.</p>

  <div id="cookieKeuzes" class="cookie-keuzes" hidden>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" checked disabled aria-label="Functionele cookies, altijd aan">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Functioneel</span>
        <p>Nodig om de site te laten werken. Staat altijd aan.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieAnalytisch" aria-label="Analytische cookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Analytisch</span>
        <p>Laat ons zien welke pagina&rsquo;s bezocht worden, zodat we de site kunnen verbeteren.</p>
      </div>
    </div>
    <div class="cookie-optie">
      <label class="cookie-schakelaar">
        <input type="checkbox" id="cookieMarketing" aria-label="Marketingcookies">
        <span aria-hidden="true"></span>
      </label>
      <div>
        <span class="cookie-optie-naam">Marketing</span>
        <p>Voor advertenties en het meten daarvan. Nu niet in gebruik.</p>
      </div>
    </div>
  </div>

  <div class="cookie-knoppen">
    <button type="button" class="cookie-knop" data-cookie="weigeren">Weigeren</button>
    <button type="button" class="cookie-knop" data-cookie="aanpassen">Aanpassen</button>
    <button type="button" class="cookie-knop cookie-knop--donker" data-cookie="toestaan">Toestaan</button>
  </div>
</aside>'''


ORGANISATIE_LD = f'''{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Madegro Advies B.V.",
  "alternateName": "MADEGRO",
  "foundingDate": "2002-07",
  "url": "{BASIS}/",
  "logo": "{BASIS}/assets/logo/madegro-logo.svg",
  "email": "{EMAIL}",
  "telephone": "{TELEFOON_LINK}",
  "vatID": null,
  "identifier": {{ "@type": "PropertyValue", "name": "KvK", "value": "{KVK}" }},
  "address": {{
    "@type": "PostalAddress",
    "streetAddress": "Wieling 39",
    "postalCode": "3371 PB",
    "addressLocality": "Hardinxveld-Giessendam",
    "addressCountry": "NL"
  }}
}}'''


def pagina(bestand, titel, omschrijving, namespace, pagina_css, css_naam,
           inhoud, scripts=(), extra_ld=None, actief=None, body_klasse=""):
    """Zet één complete HTML-pagina in elkaar."""
    ld_blokken = f'<script type="application/ld+json">\n{ORGANISATIE_LD}\n</script>'
    if extra_ld:
        ld_blokken += f'\n<script type="application/ld+json">\n{extra_ld}\n</script>'

    script_regels = "\n".join(f'<script src="{s}"></script>' for s in scripts)
    body_attr = f' class="{body_klasse}"' if body_klasse else ""

    return f'''<!DOCTYPE html>
<html lang="nl">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>{titel}</title>
<meta name="description" content="{omschrijving}" />
<link rel="canonical" href="{BASIS}/{bestand}" />
<meta name="robots" content="index, follow, max-image-preview:large" />
<meta name="author" content="Madegro Advies B.V." />
<meta name="theme-color" content="#FFFFFF" />
<meta name="color-scheme" content="light" />

<!-- GSAP en Barba komen van jsDelivr. Het opzetten van die verbinding (dns,
     tcp, tls) kost op een telefoon een paar honderd ms en begint nu al terwijl
     de HTML nog binnenkomt, in plaats van pas onderaan de pagina. -->
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin />

<!-- Het lettertype staat in de kop van de pagina en is dus onderdeel van de
     LCP. Zonder preload vindt de browser het pas nadat styleguide.css binnen is
     en ontleed is. crossorigin moet erbij, ook al staat het bestand op dezelfde
     server: een font wordt altijd in CORS-modus opgehaald, en zonder dat woord
     haalt de browser het twee keer op. -->
<link rel="preload" href="assets/fonts/inter-tight-latin.woff2" as="font" type="font/woff2" crossorigin />

<link rel="stylesheet" href="styleguide.css" />
<link rel="stylesheet" href="transitions.css" />
<!-- De cookiebalk verschijnt pas als cookiebalk.js hem opbouwt, dus zijn stijl
     hoeft de eerste weergave niet op te houden. media="print" laat de browser
     hem buiten het kritieke pad ophalen; onload zet hem daarna alsnog aan. De
     noscript-regel vangt op dat zonder JavaScript ook die onload niet afgaat. -->
<link rel="stylesheet" href="cookiebalk.css" media="print" onload="this.media='all'" />
<noscript><link rel="stylesheet" href="cookiebalk.css" /></noscript>
<link rel="stylesheet" href="{pagina_css}" data-page-css="{css_naam}" />

<link rel="icon" href="assets/favicon/favicon.svg" type="image/svg+xml" />
<link rel="apple-touch-icon" href="assets/favicon/apple-touch-icon.png" />

<meta property="og:type" content="website" />
<meta property="og:site_name" content="MADEGRO" />
<meta property="og:locale" content="nl_NL" />
<meta property="og:url" content="{BASIS}/{bestand}" />
<meta property="og:title" content="{titel}" />
<meta property="og:description" content="{omschrijving}" />
<meta property="og:image" content="{BASIS}/assets/social/madegro-deelafbeelding.png" />
<meta name="twitter:card" content="summary_large_image" />
<meta name="twitter:title" content="{titel}" />
<meta name="twitter:description" content="{omschrijving}" />

{ld_blokken}
</head>

<body{body_attr}>
<a class="skip-link" href="#main-content">Naar de inhoud</a>

<!-- De header en het mobiele paneel staan bewust BUITEN #smooth-wrapper.
     ScrollSmoother verschuift de inhoud met een transform, en onder een
     transform hangt position:fixed aan dat element in plaats van aan het
     scherm. Ze blijven daardoor ook staan bij een pagina-overgang; welke
     menulink actief is wordt in page-transitions.js bijgewerkt. -->
{header(actief or bestand)}

<div id="smooth-wrapper">
<div id="smooth-content">

<div data-barba="wrapper">
<div class="app__wrapper" data-barba="container" data-barba-namespace="{namespace}">
<div class="content__wrapper">

<main id="main-content">

{inhoud}

</main>

{footer()}

<script src="site.js"></script>
<script src="contactformulier.js"></script>
{script_regels}
</div><!-- /.content__wrapper -->
</div><!-- /[data-barba=container] -->
</div><!-- /[data-barba=wrapper] -->

</div><!-- /#smooth-content -->
</div><!-- /#smooth-wrapper -->

{COOKIEBALK}

<!-- ================= PAGINA-OVERGANGEN =================
     Barba wisselt alleen de container hierboven om, GSAP animeert de wissel. -->
<!-- defer: de browser haalt ze op terwijl hij de pagina nog aan het ontleden is
     en voert ze daarna uit, in deze volgorde. Die volgorde is nodig, want
     ScrollTrigger heeft gsap nodig en page-transitions.js heeft Barba nodig. -->
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/gsap.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollTrigger.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/gsap@3.13.0/dist/ScrollSmoother.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/@barba/core@2.10.3/dist/barba.umd.js"></script>
<script defer src="cookiebalk.js"></script>
<script defer src="analytics.js"></script>
<script defer src="smooth-scroll.js"></script>
<script defer src="page-transitions.js"></script>

</body>
</html>
'''


# Logo's van de bedrijven onder de logoslider. LET OP: dit zijn logo's van
# bestaande, herkenbare bedrijven, overgenomen uit de referentie. Het zijn dus
# niet de klanten van MADEGRO. Ze staan hier als opvulmateriaal voor de layout
# en moeten voor livegang vervangen worden door echte opdrachtgevers, met
# toestemming. Zie CONTENT-TODO.md.
# De opdrachtgevers uit Martins LinkedIn-profiel, met de logo's die hij heeft
# aangeleverd. Breedte is de echte breedte van het bestand op 96px hoog; die
# staat in de HTML zodat er geen sprong in de band zit terwijl ze laden.
#
# Van vijf opdrachtgevers die hij noemt is geen logo aangeleverd: BAM Infra,
# NEM Standaard Kessel, Fisia Babcock, AEB Amsterdam en Fitweld. Die staan dus
# niet in de band; een band met logo's en losse namen door elkaar leest rommelig.
#
# TODO-CONTENT: dit zijn beeldmerken van bestaande bedrijven. Laat Martin per
# opdrachtgever bevestigen dat hij hun logo mag tonen. Bij de meeste klanten is
# dat een formaliteit, bij sommige ligt er een geheimhoudingsafspraak.
OPDRACHTGEVERS = [
    ("alstom",        "Alstom",                       408),
    ("ballast-nedam", "Ballast Nedam",                452),
    ("bilfinger",     "Bilfinger",                    210),
    ("cosun",         "Cosun Beet Company",           345),
    ("ebert-hera",    "Ebert Hera",                   389),
    ("electrabel",    "Electrabel / GDF Suez",        203),
    ("freesmij",      "Freesmij",                     309),
    ("ge-vernova",    "GE Vernova",                   362),
    ("huhtamaki",     "Huhtamaki",                    478),
    ("ivens",         "Ivens",                        237),
    ("ooms",          "Ooms Bouw &amp; Ontwikkeling", 248),
    ("stork",         "Stork",                        197),
    ("tes",           "TES Industrial Systems",       160),
]


def _logoset(verborgen=False, plat=False):
    """De logo's van de opdrachtgevers. Het tweede exemplaar van de reeks is
       aria-hidden, dus een schermlezer hoort de namen een keer.

       Het adres staat in data-src en niet in src, en site.js zet het om zodra de
       band in de buurt van het scherm komt. Dat scheelt 118 kB bij het openen
       van elke pagina; de band staat altijd onderaan.

       loading="lazy" werkt hier niet, dat is gemeten: het venster knipt af met
       overflow:hidden, waardoor de browser alles rechts van de rand als "niet in
       beeld" ziet. Van de 26 afbeeldingen laadden er drie, ook na doorscrollen
       naar de band toe. Vandaar een waarnemer op de sectie zelf: die zet ze alle
       26 tegelijk aan, ruim voordat je ze ziet.

       plat=True geeft dezelfde reeks met een gewone src, voor de noscript."""
    extra = ' aria-hidden="true"' if verborgen else ''
    bron = 'src' if plat else 'data-src'
    regels = "\n".join(
        '          <li class="logo-slider__logo">'
        f'<img {bron}="assets/partners/{slug}.webp" alt="{naam}" '
        f'width="{breedte}" height="80" decoding="async"></li>'
        for slug, naam, breedte in OPDRACHTGEVERS)
    return f'        <ul class="logo-slider__set"{extra}>\n{regels}\n        </ul>'


def logoslider(nr):
    """De doorlopende logoband. De reeks staat er twee keer in: de animatie
       schuift precies de helft op, zodat het naadloos doorloopt. Het tweede
       exemplaar is aria-hidden, dus een schermlezer hoort de namen een keer.
       De band pauzeert bij hover en staat stil bij prefers-reduced-motion."""
    return (f'  <section class="logo-slider" id="s{nr}-partners" aria-label="Opdrachtgevers" data-logoband>\n'
            '    <div class="logo-slider__venster">\n'
            '      <div class="logo-slider__spoor">\n'
            f'{_logoset()}\n{_logoset(verborgen=True)}\n'
            '      </div>\n'
            '    </div>\n'
            '    <noscript>\n'
            '      <div class="logo-slider__venster">\n'
            '        <div class="logo-slider__spoor">\n'
            f'{_logoset(plat=True)}\n{_logoset(verborgen=True, plat=True)}\n'
            '        </div>\n'
            '      </div>\n'
            '    </noscript>\n'
            '  </section>')


def ctablok(nr, kop, tekst=None):
    """Verwijst naar de contactpagina in plaats van zelf een formulier te tonen.
       Het formulier zelf staat nog op contact.html; dit is de aanloop erheen.

       Eén groen vlak over de volle breedte, alles gecentreerd. De contactkaart
       met Martins gegevens stond hier eerder naast en is eruit gehaald: die
       gegevens staan op de contactpagina waar deze knop naartoe wijst."""
    regel = tekst or f'Vertel kort waar je tegenaan loopt. We reageren binnen {REACTIETIJD}.'
    return (f'  <section class="cta-slot" id="s{nr}-contact">\n'
            '    <div class="container">\n'
            '      <div class="cta-slot__hoofd">\n'
            '        <span class="subtitle cta-slot__label">Contact</span>\n'
            f'        <h2 class="cta-slot__kop">{kop}</h2>\n'
            f'        <p class="cta-slot__tekst">{regel}</p>\n'
            '        <div class="cta-slot__actie">\n'
            f'          {knop("Neem contact op", "contact.html")}\n'
            '        </div>\n'
            '      </div>\n'
            '    </div>\n'
            '  </section>')

def paginahero(nr, ident, label, titel, beeld, alt=None, positie=None):
    """De hero met links de kop op grijs en rechts een foto. De <h1> staat in de
       HTML voor het beeld; onder 768px zet de CSS het beeld met order bovenaan,
       zodat de leesvolgorde blijft kloppen."""
    stijl = f' style="object-position:{positie}"' if positie else ""
    beeldtag = foto(beeld, laden="eager", maten="(max-width: 767px) 100vw, 50vw", alt=alt)
    if stijl:
        beeldtag = beeldtag.replace("<img ", f"<img{stijl} ")
    return (f'  <section class="paginahero" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld">\n'
            f'      {beeldtag}\n'
            '    </div>\n'
            '  </section>')


def patroonhero(nr, ident, label, titel):
    """Dezelfde hero, maar met het merkpatroon in plaats van een foto.

       Twee bestanden, want de compositie verschilt: op breed scherm staat het
       patroon rechts in een liggend vak, op een telefoon als brede band boven de
       titel. <picture> kiest ze op dezelfde grens als de layout zelf omslaat
       (768px), zodat er nooit een verkeerde uitsnede te zien is.

       Hoe hoog die band is, staat in de stylesheet en niet in het bestand: 7:3
       plus de hoogte van de vaste balk, want die ligt eroverheen. Het
       bronbestand is daarom vierkant en niet al op 7:3 gesneden; cover heeft
       verticaal wat over nodig.

       Het patroon is versiering en zegt niets wat de kop niet al zegt, dus
       alt="" en aria-hidden: een schermlezer slaat het over."""
    return (f'  <section class="paginahero paginahero--patroon" id="s{nr}-{ident}">\n'
            '    <div class="paginahero__kop">\n'
            f'      <span class="subtitle">{label}</span>\n'
            f'      <h1 class="paginahero__titel">{titel}</h1>\n'
            '    </div>\n'
            '    <div class="paginahero__beeld" aria-hidden="true">\n'
            '      <picture>\n'
            '        <source media="(max-width: 767px)" srcset="assets/patronen/hero-patroon-mobiel-720.webp 720w, assets/patronen/hero-patroon-mobiel-800.webp 800w, assets/patronen/hero-patroon-mobiel-1440.webp 1440w" sizes="100vw" width="1440" height="1440">\n'
            '        <img src="assets/patronen/hero-patroon-1440.webp" srcset="assets/patronen/hero-patroon-720.webp 720w, assets/patronen/hero-patroon-1000.webp 1000w, assets/patronen/hero-patroon-1440.webp 1440w" sizes="50vw" width="1440" height="940" alt="" loading="eager" fetchpriority="high" decoding="async">\n'
            '      </picture>\n'
            '    </div>\n'
            '  </section>')


KLEURENRIJ = ("geel", "grijs", "wit", "groen")


def vlakkenrij(nr, ident, kop, vlakken, subtitel=None):
    """Kop met daaronder vier gekleurde vlakken over de volle breedte. vlakken is
       een lijst van (kop, tekst); de kleuren lopen vast in dezelfde volgorde,
       zodat de rij op elke pagina hetzelfde ritme heeft."""
    label = f'        <span class="subtitle" style="margin-bottom:var(--space-500)">{subtitel}</span>\n' if subtitel else ""
    items = "\n".join(
        f'      <li class="vlak vlak--{KLEURENRIJ[i % 4]}">\n'
        f'        <h3 class="vlak__kop">{titel}</h3>\n'
        f'        <p class="vlak__tekst">{tekst}</p>\n'
        '      </li>'
        for i, (titel, tekst) in enumerate(vlakken)
    )
    return (f'  <section class="vlakkenband" id="s{nr}-{ident}">\n'
            '    <div class="container">\n'
            '      <div class="vlakkenband__kop">\n'
            f'{label}'
            f'        <h2 class="section-heading">{kop}</h2>\n'
            '      </div>\n'
            '    </div>\n'
            '    <ul class="vlakkenrij">\n'
            f'{items}\n'
            '    </ul>\n'
            '  </section>')


def beeldkaart(kop, tekst, beeld, alt=None, kleur="grey", href=None):
    """Een kaart met de foto erboven en de tekst eronder, twee per rij. Dit is de
       verticale variant van .cta-blocks-advanced."""
    binnen = (f'      <figure class="cta-blocks-advanced__banner">\n'
              f'        {foto(beeld, maten="(max-width: 991px) 100vw, 50vw", alt=alt)}\n'
              '        <span class="cta-blocks-advanced__backdrop" aria-hidden="true"></span>\n'
              '      </figure>\n'
              f'      <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{kleur}">\n'
              f'        <h3 class="cta-blocks-advanced__title">{kop}</h3>\n'
              '        <div class="cta-blocks-advanced__wrapper">\n'
              f'          <div class="cta-blocks-advanced__content"><p>{tekst}</p></div>\n'
              '        </div>\n'
              '      </div>')
    if href:
        omhulsel = (f'    <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" '
                    f'href="{href}">\n{binnen}\n    </a>')
    else:
        omhulsel = f'    <div class="cta-blocks-advanced__card">\n{binnen}\n    </div>'
    return f'  <div class="col-lg-6 col-12 kolom--vullend">\n{omhulsel}\n  </div>'

def cursuskaart(i, cursus):
    """Eén cursus als paneel met de foto erboven. Staat hier en niet in de twee
       bouwbestanden, want de kaart komt op de homepage en op het cursus-
       overzicht voor; zo blijft het één definitie.

       De alt is leeg: de foto zegt niets wat de link niet al zegt, en een
       schermlezer zou anders eerst een beschrijving van een productiehal
       voorlezen voordat hij bij de cursusnaam is."""
    bestand, titel, doelgroep, duur, beeld = cursus
    return f'''        <div>
          <a class="panel panel--{'grey' if i % 2 else 'wit'} panel--beeld panel--link hover--icon" href="{bestand}">
            <figure class="panel__beeld">
              {foto(beeld, maten=BEELD_MATEN_4, alt="")}
            </figure>
            <span class="panel__meta">{doelgroep}</span>
            <h3 class="panel__title">{titel}</h3>
            <p class="panel__body">{duur}</p>
            <span class="panel__actie">{icoonknop()}</span>
          </a>
        </div>'''


def dienstkaart(i, dienst, intro):
    """Eén dienst als kaart met de foto erboven. Alleen de homepage gebruikt hem,
       maar hij staat hier bij cursuskaart() omdat het dezelfde soort kaart is."""
    bestand, titel, sub, beeld = dienst
    return f'''        <div class="col-lg-4 col-12 kolom--vullend">
          <a class="cta-blocks-advanced__card cta-blocks-advanced__card--linked hover--icon" href="{bestand}"
             aria-label="{titel}: {sub}">
            <figure class="cta-blocks-advanced__banner cta-blocks-advanced__banner--verhouding">
              {foto(beeld, maten=BEELD_MATEN_3, alt="")}
            </figure>
            <div class="cta-blocks-advanced__body cta-blocks-advanced__body--bg-{'grey' if i % 2 == 0 else 'white'}">
              <span class="subtitle">Dienst 0{i + 1}</span>
              <div class="cta-blocks-advanced__wrapper">
                <div>
                  <h3 class="cta-blocks-advanced__title" style="margin-bottom:var(--space-500)">{titel}</h3>
                  <div class="cta-blocks-advanced__content"><p>{sub}</p><p>{intro}</p></div>
                </div>
                {icoonknop("button--icon--56")}
              </div>
            </div>
          </a>
        </div>'''


# Voorlopige woordmerken voor de verzonnen opdrachtgevers bij de citaten.
# TODO-CONTENT: dit zijn geen echte logo's. Ze zijn hier gemaakt als grijze
# letters in een websafe schreefloze, zodat de opmaak af is. Een logo van een
# van de dertien echte opdrachtgevers kan hier niet staan: dan hangt er een
# aanbeveling van Alstom of Stork onder een citaat dat niemand heeft gegeven.
# Zie CONTENT-TODO.md.
PLAATSHOUDER_LOGOS = {
    "van-deursen-metaal":    ("Van Deursen Metaal", 317),
    "rivierpoort-logistiek": ("Rivierpoort Logistiek", 317),
    "merwede-bouwgroep":     ("Merwede Bouwgroep", 275),
}


def quotelogo(slug):
    """Het logo van de opdrachtgever onder de naam bij een citaat.

       slug is een sleutel uit OPDRACHTGEVERS (een echt logo), een sleutel uit
       PLAATSHOUDER_LOGOS (een voorlopig woordmerk), of None voor een geel
       invulveld."""
    if slug is None:
        return ('<p class="quote__logo quote__logo--leeg">'
                '<span class="invulveld">Logo opdrachtgever</span></p>')
    if slug in PLAATSHOUDER_LOGOS:
        naam, breedte = PLAATSHOUDER_LOGOS[slug]
        return (f'<p class="quote__logo quote__logo--plaatshouder">'
                f'<img src="assets/partners/{slug}.svg" alt="{naam}" '
                f'width="{breedte}" height="80" loading="lazy" decoding="async"></p>')
    naam, breedte = next((n, b) for sl, n, b in OPDRACHTGEVERS if sl == slug)
    return (f'<p class="quote__logo"><img src="assets/partners/{slug}.webp" '
            f'alt="{naam}" width="{breedte}" height="80" loading="lazy" decoding="async"></p>')


def quoteslider(nr, ident, subtitel, kop, items):
    """Een quote per keer, groot uitgelicht: beeld links, citaat rechts, met een
       streepje boven de naam, daaronder het logo van de opdrachtgever. Pijlen
       eronder om te bladeren.

       items is een lijst van (citaat, naam, functie, fotosleutel, logoslug). De
       foto is een werkplek en geen portret: van deze mensen hebben we geen foto,
       en een willekeurig gezicht naast een naam zetten maakt er een bestaand
       persoon van die dit nooit gezegd heeft. Voor logoslug: zie quotelogo()."""
    dias = "\n".join(f'''        <figure class="quote" role="group" aria-roledescription="citaat"
               aria-label="Citaat {i + 1} van {len(items)}">
          <div class="quote__beeld">
            {foto(sleutel, maten="(max-width: 767px) 100vw, 40vw")}
          </div>
          <div class="quote__body">
            <blockquote class="quote__tekst"><p>{citaat}</p></blockquote>
            <hr class="quote__streep">
            <figcaption class="quote__naam">{naam}, {functie}</figcaption>
            {quotelogo(logo)}
          </div>
        </figure>''' for i, (citaat, naam, functie, sleutel, logo) in enumerate(items))

    return f'''  <section class="quotes" id="s{nr}-{ident}">
    <div class="container">
      <div class="quotes__kop">
        <span class="subtitle">{subtitel}</span>
        <h2 class="section-heading">{kop}</h2>
      </div>
      <!-- TODO-CONTENT: echte getuigenissen met naam en toestemming; deze zijn fictief -->
      <div class="quotes__venster" data-quoteslider aria-live="polite">
{dias}
      </div>
      <!-- De pijlen staan hidden en worden door site.js zichtbaar gemaakt.
           Zonder JavaScript staan alle citaten gewoon onder elkaar en zou je
           op knoppen klikken die niets doen. -->
      <div class="quotes__nav" hidden>
        <button type="button" class="button--icon button--icon--56 button--grijs quotes__pijl" data-quote="vorige" aria-label="Vorige quote">
          <span class="button--circle"><span class="circle-container">{_pijl_paar("links")}</span></span>
        </button>
        <button type="button" class="button--icon button--icon--56 button--grijs quotes__pijl" data-quote="volgende" aria-label="Volgende quote">
          <span class="button--circle"><span class="circle-container">{_pijl_paar("rechts")}</span></span>
        </button>
        <p class="quotes__teller" data-quote-teller>1 / {len(items)}</p>
      </div>
    </div>
  </section>'''


def _pijl_paar(richting):
    """De pijl uit de icoonknop, twee keer, zodat de bestaande hover-animatie
       (de ene schuift weg, de andere komt binnen) blijft werken."""
    draai = ' style="transform:scaleX(-1)"' if richting == "links" else ""
    pad = ('<path d="M13.2 4.6 20.6 12l-7.4 7.4-1.4-1.4 5-5H3.4v-2h13.4l-5-5 1.4-1.4Z"/>')
    return "".join(
        f'<svg class="arrow--animation is-{n}" width="16" height="16" viewBox="0 0 24 24"'
        f' aria-hidden="true"{draai}>{pad}</svg>' for n in (1, 2))


def slotblok(nr, kop, tekst=None):
    """De logoband met daaronder de CTA, zoals in de referentie. Het zijn twee
       secties, dus ook twee nummers: de band krijgt nr, het contactblok nr+1."""
    return logoslider(nr) + "\n\n" + ctablok(f"{int(nr) + 1:02d}", kop, tekst)


def contactblok(onderwerp, kop="Neem contact op",
                intro="Vertel kort waar je tegenaan loopt. We reageren binnen "
                      f"{REACTIETIJD}."):
    """Het gedeelde formulier. De HTML wordt door contactformulier.js gerenderd;
       hier staat alleen de haak plus een terugval voor bezoekers zonder JS."""
    return f'''  <section class="band background--grey" id="s{onderwerp["nr"]}-contact">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <span class="subtitle">Contact</span>
          <h2 class="section-heading" style="margin:var(--space-500) 0">{kop}</h2>
          <p class="article-body">{intro}</p>
          <p class="article-body" style="margin-top:var(--space-500)">
            Liever bellen? <a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a>
          </p>
        </div>
        <div class="col-lg-8 col-12">
          <div data-contactformulier data-onderwerp="{onderwerp["waarde"]}"></div>
          <noscript>
            <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons gerust op
              <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
          </noscript>
        </div>
      </div>
    </div>
  </section>'''


def faq_blok(nr, items, titel="Veelgestelde vragen"):
    """Drie FAQ-items als accordeon plus de bijbehorende FAQPage-structuurdata."""
    regels = []
    for i, (vraag, antwoorden) in enumerate(items):
        alineas = "".join(f"<p>{a}</p>" for a in antwoorden)
        regels.append(f'''          <div class="accordion__item">
            <button type="button" class="accordion__header" aria-expanded="false" aria-controls="faq-{nr}-{i}">
              <span class="accordion__number">{i + 1:02d}</span>
              <span class="accordion__title">{vraag}</span>
              <span class="accordion__suffix" aria-hidden="true"><span class="accordion__icon"></span></span>
            </button>
            <div class="accordion__details" id="faq-{nr}-{i}">
              <div class="accordion__details-inner article-body">{alineas}</div>
            </div>
          </div>''')
    return f'''  <section class="band background--white" id="s{nr}-faq">
    <div class="container">
      <div class="row">
        <div class="col-md-4 col-12">
          <span class="subtitle">FAQ</span>
          <h2 class="font-size--lg" style="margin-top:var(--space-500)">{titel}</h2>
        </div>
        <div class="col-md-8 col-12">
          <div class="accordion">
{chr(10).join(regels)}
          </div>
        </div>
      </div>
    </div>
  </section>'''


def faq_ld(items):
    import json
    return json.dumps({
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {"@type": "Question", "name": _plat(v),
             "acceptedAnswer": {"@type": "Answer", "text": " ".join(_plat(a) for a in ant)}}
            for v, ant in items
        ],
    }, ensure_ascii=False, indent=2)


def _plat(tekst):
    import re, html
    return html.unescape(re.sub(r"<[^>]+>", "", tekst))


# NAV verwijst naar SERVICES, CURSUSSEN en foto(); die staan hierboven, dus de
# lijst wordt hier pas gevuld. header() leest hem daarna.
bouw_nav()
