# -*- coding: utf-8 -*-
import sys, pathlib
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import *

UIT = pathlib.Path("/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE/madegro")

# ============================================================ contact.html
inhoud = f'''{patroonhero("01", "contact", "Contact", "Contact")}

  <section class="band background--white" id="s02-formulier">
    <div class="container">
      <div class="row">
        <div class="col-lg-4 col-12">
          <div class="article-body">
            <p>Vertel kort waar je tegenaan loopt. Of dat nu een RI&amp;E is die verlopen is, een audit die eraan komt of het gevoel dat de regels op papier niet terugkomen op de vloer.</p>
            <p>We reageren binnen {REACTIETIJD}.</p>
          </div>
          <p class="contact-direct">Liever meteen iemand spreken? Bel
            <a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a> of mail naar
            <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>
        </div>

        <div class="col-lg-8 col-12">
          <div class="contact-formulier-wikkel">
            <div data-contactformulier data-onderwerp="overig"></div>
            <noscript>
              <p class="article-body">Het formulier heeft JavaScript nodig. Mail ons gerust op
                <a href="mailto:{EMAIL}">{EMAIL}</a> of bel {TELEFOON_WEERGAVE}.</p>
            </noscript>
          </div>
        </div>
      </div>
    </div>
  </section>

{vlakkenrij("03", "gegevens", "Onze gegevens", [
    ("Telefoon",
     f'<a href="tel:{TELEFOON_LINK}">{TELEFOON_WEERGAVE}</a><br>Op werkdagen bereikbaar'),
    ("E-mail",
     f'<a href="mailto:{EMAIL}">{EMAIL}</a><br>Antwoord binnen {REACTIETIJD}'),
    ("Adres",
     "Wieling 39<br>3371 PB Hardinxveld-Giessendam"),
    ("Madegro Advies B.V.",
     f"KvK {KVK}"),
])}
'''

(UIT / "contact.html").write_text(pagina(
    bestand="contact.html",
    titel="Contact | MADEGRO",
    omschrijving="Neem contact op met MADEGRO over veilig gedrag, een EHS RI&E, een safety check of een cursus. We reageren binnen twee werkdagen.",
    namespace="contact",
    pagina_css="contact.css",
    css_naam="contact",
    inhoud=inhoud,
), encoding="utf-8")

# ======================================================= tekstpagina's
PRIVACY = '''  <section class="tekstband" id="s01-privacybeleid">
    <div class="container">
      <div class="tekst">
        <p class="meta">Juridisch</p>
        <h1>Privacybeleid</h1>
        <p class="meta">Laatst bijgewerkt: <span class="invulveld">nog invullen</span></p>

        <h2>Wie verwerkt je gegevens</h2>
        <p>Madegro Advies B.V., Wieling 39, 3371 PB Hardinxveld-Giessendam, KvK ''' + KVK + f'''. Voor vragen over dit beleid kun je terecht bij <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

        <h2>Welke gegevens en waarom</h2>
        <h3>Contactformulier</h3>
        <p>Vul je het formulier in, dan verwerken we je naam, bedrijfsnaam, e-mailadres, telefoonnummer, het gekozen onderwerp en je bericht. Die gegevens gebruiken we alleen om je vraag te beantwoorden en, als dat tot een opdracht leidt, om die uit te voeren.</p>
        <p>Grondslag: je toestemming, en bij een lopende opdracht de uitvoering van de overeenkomst.</p>

        <h3>Cursusaanmeldingen</h3>
        <p>Meld je je aan voor een cursus, dan verwerken we daarnaast de gegevens die nodig zijn voor deelname en het certificaat.</p>
        <div class="invulblok">
          <p>Welke gegevens er bij een cursusaanmelding precies worden vastgelegd, en hoe lang ze bewaard blijven, moet hier nog ingevuld worden.</p>
        </div>

        <h3>Bezoekgegevens</h3>
        <p>De site plaatst geen analytische of marketingcookies zolang je daar geen toestemming voor geeft. Je keuze zelf bewaren we in de lokale opslag van je browser onder de naam <span class="invulveld">madegro-cookies-v1</span>. Dat is geen cookie: het gaat niet mee naar de server.</p>

        <h2>Hoe lang we het bewaren</h2>
        <p>Berichten via het formulier bewaren we tot twee jaar na het laatste contact. Gegevens die bij een opdracht horen bewaren we zolang de wet dat vraagt, voor de administratie zeven jaar.</p>

        <h2>Met wie we het delen</h2>
        <p>We verkopen geen gegevens. We delen ze alleen met partijen die nodig zijn om te leveren: de partij die deze site host, en bij een cursus de instantie die het certificaat uitgeeft.</p>
        <div class="invulblok">
          <p>De hostingpartij en de eventuele certificerende instantie moeten hier met naam genoemd worden, met de vermelding of er een verwerkersovereenkomst ligt.</p>
        </div>

        <h2>Je rechten</h2>
        <p>Je mag je gegevens inzien, corrigeren of laten verwijderen, en je mag bezwaar maken tegen de verwerking. Stuur een mail naar <a href="mailto:{EMAIL}">{EMAIL}</a>; we reageren binnen een maand. Ben je het niet eens met hoe we ermee omgaan, dan kun je klagen bij de Autoriteit Persoonsgegevens.</p>

        <h2>Beveiliging</h2>
        <p>De site gaat over https en de gegevens uit het formulier komen alleen terecht bij wie ze nodig heeft.</p>
        <div class="invulblok">
          <p>Beschrijf hier alleen de maatregelen die daadwerkelijk zijn ingericht. Wat er nog niet is, hoort er niet in te staan.</p>
        </div>
      </div>
    </div>
  </section>'''

(UIT / "privacybeleid.html").write_text(pagina(
    bestand="privacybeleid.html",
    titel="Privacybeleid | MADEGRO",
    omschrijving="Hoe MADEGRO omgaat met je gegevens.",
    namespace="privacybeleid",
    pagina_css="tekstpagina.css",
    css_naam="tekst",
    inhoud=PRIVACY,
    body_klasse="tekstpagina",
), encoding="utf-8")

COOKIES = f'''  <section class="tekstband" id="s01-cookies">
    <div class="container">
      <div class="tekst">
        <p class="meta">Juridisch</p>
        <h1>Cookies</h1>
        <p class="meta">Laatst bijgewerkt: <span class="invulveld">nog invullen</span></p>

        <h2>Wat deze site plaatst</h2>
        <p>Op dit moment plaatst deze website geen analytische of marketingcookies. Er draait geen statistiekentool en er staat geen advertentiepixel op de pagina.</p>
        <p>Het enige dat wordt opgeslagen is je eigen keuze in de cookiemelding. Die bewaren we in de lokale opslag van je browser onder de naam <span class="invulveld">madegro-cookies-v1</span>, zodat je de vraag niet bij elk bezoek opnieuw krijgt.</p>

        <h2>De drie categorie&euml;n</h2>
        <h3>Functioneel</h3>
        <p>Nodig om de site te laten werken, waaronder het onthouden van je keuze. Hiervoor is geen toestemming vereist.</p>
        <h3>Analytisch</h3>
        <p>Bedoeld om te zien welke pagina&rsquo;s bezocht worden, zodat de site verbeterd kan worden. Er staat een statistiekentool klaar die pas laadt nadat je analytische cookies hebt aangezet.</p>
        <div class="invulblok">
          <p>Welke statistiekentool er gebruikt gaat worden en welk meet-ID daarbij hoort, moet hier nog ingevuld worden. Zolang dat veld leeg is, laadt er niets.</p>
        </div>
        <h3>Marketing</h3>
        <p>Voor advertenties en het meten van het effect daarvan. Op dit moment niet in gebruik.</p>

        <h2>Je keuze wijzigen</h2>
        <p>Je kunt je keuze op elk moment aanpassen of intrekken.</p>
        <p><button type="button" class="cookie-knop cookie-knop--donker" data-cookie-instellingen>Cookie-instellingen openen</button></p>

        <h2>Wat er verder gebeurt</h2>
        <p>De pagina laadt de scripts voor de pagina-overgangen van een extern adres. Dat zet geen cookies, maar ontvangt wel het IP-adres van je bezoeker:</p>
        <ul>
          <li>cdn.jsdelivr.net</li>
        </ul>
        <p>De lettertypen staan op onze eigen server; daar gaat dus niets naartoe. Meer over gegevens staat in het <a href="privacybeleid.html">privacybeleid</a>.</p>
      </div>
    </div>
  </section>'''

(UIT / "cookies.html").write_text(pagina(
    bestand="cookies.html",
    titel="Cookies | MADEGRO",
    omschrijving="Welke cookies MADEGRO gebruikt en hoe je je keuze aanpast.",
    namespace="cookies",
    pagina_css="tekstpagina.css",
    css_naam="tekst",
    inhoud=COOKIES,
    body_klasse="tekstpagina",
), encoding="utf-8")

print("contact.html, privacybeleid.html en cookies.html geschreven")
