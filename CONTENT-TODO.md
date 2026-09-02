# CONTENT-TODO: wat er nog vervangen moet worden

De site is helemaal ingevuld: er staat nergens meer een `[TOKEN]` of een
`TODO-CONTENT` in de zichtbare tekst. **Maar een deel van wat er staat is
verzonnen.** Dit bestand vertelt precies wat.

In de HTML staat bij elk verzonnen blok een `<!-- TODO-CONTENT: ... -->` boven het
element. Zoek daarop en je vindt de plek. Er staan er nu 29.

> **Voor de site live gaat.** Alles onder "Verzonnen" moet nagelopen worden.
> Klantnamen, cijfers en getuigenissen die niet kloppen zijn niet alleen
> misleidend richting bezoekers, ze zijn ook een risico richting de
> opdrachtgevers die erin genoemd worden.

---

## Verzonnen: controleren of vervangen

### Bedrijfsgegevens

| Wat | Staat er nu | Waar |
|---|---|---|
| Telefoonnummer | `0184 00 00 00` | header, footer, contactpagina, foutmelding van het formulier |
| E-mailadres | `info@madegro.nl` | idem |
| Reactietijd | twee werkdagen | contactblokken |

Het telefoonnummer is bewust een niet-bestaand patroon gebleven. Een verzonnen
nummer dat er echt uitziet komt bijna zeker bij iemand anders uit.

### Opdrachtgevers in de logoband: nu met echte logo's

Hier stond een blokker: de band toonde vijftien logo's van bedrijven die uit de
referentiesite kwamen en geen klant van MADEGRO zijn. Die zijn weg.

De band toont nu dertien echte opdrachtgevers met hun eigen beeldmerk: Alstom,
Ballast Nedam, Bilfinger, Cosun Beet Company, Ebert Hera, Electrabel/GDF Suez,
Freesmij, GE Vernova, Huhtamaki, Ivens, Ooms Bouw &amp; Ontwikkeling, Stork en TES
Industrial Systems.

**Wat nog geregeld moet worden:** dit zijn beeldmerken van bestaande bedrijven.
Laat Martin per opdrachtgever bevestigen dat hij hun logo op zijn site mag tonen.
Bij de meeste klanten is dat een formaliteit, bij sommige ligt er een
geheimhoudingsafspraak over de opdracht of over het noemen van de naam. Dat geldt
ook voor het noemen van de namen zelf, los van het logo.

Van vijf opdrachtgevers die hij op LinkedIn noemt is geen logo aangeleverd: BAM
Infra, NEM Standaard Kessel, Fisia Babcock, AEB Amsterdam en Fitweld. Die staan
niet in de band. Lever hun logo aan als ze erbij horen, of laat het zo.

Zie `assets/partners/HERKOMST.md` voor hoe de bestanden gemaakt zijn.

### Klanten en cases

**Dit is nu urgenter geworden.** Sinds de opdrachtgevers uit LinkedIn op de site
staan, staan er echte bedrijfsnamen naast zes verzonnen cases. Een bezoeker die
&ldquo;Cosun Beet Company&rdquo; in de band ziet en daarna een casepagina over
&ldquo;Van Deursen Metaal B.V.&rdquo; leest, gaat ervan uit dat die tweede ook echt is.
Vervang de cases door echte trajecten of haal ze weg, en schrijf ze in geen
geval om naar de echte klantnamen zonder hun toestemming en zonder echte cijfers.

Zes verzonnen opdrachtgevers, elk met een eigen detailpagina:

| Case | Dienst | Branche | Plaats |
|---|---|---|---|
| Van Deursen Metaal B.V. | Veilig gedrag | Productie | Gorinchem |
| Rivierpoort Logistiek | EHS RIE | Logistiek | Hardinxveld-Giessendam |
| Merwede Bouwgroep | Safety Checks | Bouw | Regio Rotterdam |
| Hollands Diep Transport | Veilig gedrag | Logistiek | Dordrecht |
| Waalhaven Terminal | Safety Checks | Logistiek | Rotterdam |
| De Groot Bouwstoffen | EHS RIE | Bouw | Sliedrecht |

Per case zijn verzonnen: de titel, de situatie, de uitdaging, de aanpak, het
resultaat, vier kerncijfers, een citaat met naam en functie, en de twee
opsommingen onder &lsquo;De uitdaging&rsquo; en &lsquo;De aanpak&rsquo;. Ze staan ook in
de projectrijen op de homepage en de servicepagina's; dat komt uit dezelfde
lijst, dus je hoeft het maar op één plek te vervangen.

De detailpagina toont per case twee beelden over de volle breedte. Daar staat nu
opvulbeeld van 1024px breed in; op een scherm van 1920px wordt dat bijna twee keer
opgerekt en is het zichtbaar zacht. Voor die twee plekken zijn foto&rsquo;s van
minstens 2400px breed nodig, liefst van de opdrachtgever zelf.

**De kerncijfers zijn het meest riskant.** &ldquo;Trede 2 naar 4&rdquo;,
&ldquo;40% minder schade&rdquo;, &ldquo;0 afwijkingen bij de audit&rdquo;: dat
zijn claims over resultaten die niet zijn behaald. Haal ze weg of vervang ze
voordat de site live gaat.

### Getuigenissen: nu veel prominenter

Zes verzonnen citaten van verzonnen mensen bij verzonnen bedrijven: drie op de
homepage, drie op elke cursuspagina.

**Dit is urgenter geworden.** Ze stonden als drie kleine kaartjes naast elkaar en
staan nu &eacute;&eacute;n voor &eacute;&eacute;n groot uitgelicht, met een foto ernaast en een naam eronder.
Dezelfde verzonnen tekst krijgt daarmee veel meer gewicht, en naast de echte
opdrachtgeverslogo's in de band eronder leest het als iets wat gecontroleerd is.

De foto naast een citaat is met opzet een werkplek en geen portret. Een
willekeurig gezicht naast &ldquo;Rob van Dijk, Voorman&rdquo; maakt er een bestaand persoon
van die dit nooit gezegd heeft. Komen er echte citaten met toestemming, dan kan
er ook een echt portret bij; de fotosleutel staat per citaat in de lijst.

### Cijfers

Op de homepage staan nu 24 jaar zelfstandig, 18 opdrachtgevers en 6 branches.
Alle drie zijn ze afgeleid uit het LinkedIn-profiel en dus controleerbaar; laat
Martin ze wel bevestigen. Er stond hier eerder 14 jaar, 60 bedrijven en 450
cursisten. Die drie waren verzonnen.

### Cursussen

De vier cursussen zijn bedacht om het template te kunnen vullen:

1. Veiligheidsbewustzijn op de werkvloer (1 dagdeel)
2. Risico's herkennen en beoordelen (2 dagdelen)
3. Werken met de Veiligheidsladder (3 dagdelen)
4. RI&E in de praktijk (2 dagdelen)

Verandert een naam, dan verandert ook `cursus-[slug].html` en de links in de
header, footer, homepage en op `cursusaanbod.html`.

Ook aangenomen: het tarief van € 750 per dagdeel, maximaal twaalf deelnemers, en
het **MADEGRO-deelnamecertificaat** (eigen certificaat, geen extern erkend
diploma, twee jaar geldig).

### Partners

**EHS-Services** komt uit de projectbrief en klopt. **Waalzicht Arbo** en **Delta
Opleidingen** zijn verzonnen, inclusief hun omschrijving; hun links staan op `#`.

### Tarieven

Op `over-ons.html`: dagtarief voor advies, vaste prijs per traject, safety check
vanaf € 1.450. Aannames.

### Stappenplannen

Bij **EHS RIE** (Inventarisatie → Evaluatie & prioritering → Plan van aanpak) en
**Safety Checks** (Voorbereiding & scope → Check op locatie → Rapportage &
opvolging) zijn de drie stappen een werkbare invulling. De brief zegt dat Martin
de echte stappen aanlevert.

---

## Klopt wel

Deze dingen komen uit de projectbrief of uit de wet en zijn niet verzonnen:

- Madegro Advies B.V., Wieling 39, 3371 PB Hardinxveld-Giessendam, KvK 81812892.
- Martin de Groot, eigenaar, veiligheidskundige en kwaliteitscontroleur.
  **Let op het jaartal:** de projectbrief zei &ldquo;algemeen directeur sinds 2021&rdquo;,
  zijn LinkedIn-profiel zegt &ldquo;Owner MADEGRO, jul. 2002 &ndash; heden&rdquo;. Dat scheelt
  negentien jaar en allebei komt het van Martin zelf. De site volgt nu 2002.
  De meest waarschijnlijke verklaring is dat MADEGRO als bedrijf uit 2002 komt
  en Madegro Advies **B.V.** pas in 2021 is opgericht; het KvK-nummer past
  daarbij. Dit moet hij zelf uitspreken voordat de site live gaat.
- De drie diensten en het cursusaanbod als indeling.
- De vijf treden van de Veiligheidsladder en het gedrag dat erbij hoort.
- RI&E verplicht op grond van Arbowet artikel 5, inclusief plan van aanpak;
  toetsing door een gecertificeerde kerndeskundige verplicht boven 25 werknemers.
- EHS-Services als partner.

---

## Beeld

De foto's zijn **CC0 of publiek domein**, commercieel bruikbaar en zonder
bronvermelding. Herkomst per bestand staat in `assets/foto/HERKOMST.md`.

Het is opvulbeeld: algemene industrie, geen MADEGRO-projecten. Vervang de
bestanden een-op-een zodra er eigen foto's zijn (zelfde namen, zelfde maten).

## Het logo bij de citaten is een voorlopig woordmerk

Onder elk citaat staat het logo van de opdrachtgever. Wat er nu staat is geen
echt logo: het zijn drie zelfgemaakte woordmerken in
`assets/partners/van-deursen-metaal.svg`, `rivierpoort-logistiek.svg` en
`merwede-bouwgroep.svg`: grijze letters in een websafe schreefloze, geen
vormgegeven merk. Ze staan er zodat de opmaak af is.

De drie citaten op de homepage en de drie op de cursuspagina&rsquo;s komen van
Van Deursen Metaal, Rivierpoort Logistiek en Merwede Bouwgroep. Die bedrijven
bestaan niet; ze zijn bedacht om het template te vullen. Er is dus ook geen
logo. En een logo van een van de dertien echte opdrachtgevers eronder zetten kan
niet: dan staat er een aanbeveling van Alstom of Stork die niemand heeft
gegeven.

Wat er moet gebeuren: echte getuigenissen bij Martin ophalen, met naam, functie,
bedrijf en schriftelijke toestemming om te publiceren, inclusief het
logo. Vul daarna de vijfde waarde in `TESTIMONIALS` (`bouw_home.py`) en
`TESTIMONIALS_BASIS` (`inhoud_cursussen.py`) met de sleutel uit
`OPDRACHTGEVERS`, bijvoorbeeld `"stork"`, en het echte logo staat er. Staat het
bedrijf nog niet in die lijst, dan moet het logo er eerst bij; zie het kopje over
de logoband hierboven. Gooi de drie SVG&rsquo;s daarna weg.

**Laat deze drie woordmerken niet live gaan.** Ze zien er van een afstand uit als
een echt logo, en dat is precies het risico: een bezoeker leest het als een
opdrachtgever die dit gezegd heeft.

## Zeven kaarten, zes foto&rsquo;s

De vier cursuskaarten en de drie dienstkaarten hebben nu een foto erboven. Dat
zijn zeven plekken, en er staan zes bruikbare stockfoto&rsquo;s in
`assets/foto/`. E&eacute;n foto komt dus twee keer voor: `overleg` staat bij Dienst 01
en bij RI&amp;E in de praktijk. Op de homepage zitten daar drie secties tussen,
dus het valt niet meteen op, maar het is wel een gat.

Daar komt bij dat de zes foto&rsquo;s ook al de hero&rsquo;s, de caserijen en de
citaten vullen. Op de homepage staat `bouwplaats` nu zes keer in de bron (hero,
citaat, casekaart) en `productiehal` zes keer. Het is opvulbeeld en het ziet er
verzorgd uit, maar het is niet MADEGRO.

Twee manieren om dit op te lossen:

- **Eigen foto&rsquo;s van Martin.** Dat is de bedoeling en het beste antwoord:
  foto&rsquo;s van echte cursussen en van werk bij opdrachtgevers. Ze vervangen
  de bestaande bestanden een-op-een: zelfde namen, zelfde formaten, dus
  er hoeft niets aan de code te veranderen. Let bij foto&rsquo;s van deelnemers
  op toestemming voor publicatie.
- **Meer stockbeeld erbij zoeken.** Kan ook, maar dan moet ik nieuwe CC0-foto&rsquo;s
  downloaden. Zeg het als je dat wilt; ik doe het niet uit mezelf.

## De homepagehero: de donkere laag kan niet weg

De groene gradient is er op verzoek af; de film houdt zijn eigen kleuren. Wat er
nog ligt is een zwarte aanloop van 30% boven naar 70% onder. Dat is geen filter
over het beeld maar het temmen ervan waar de tekst staat.

Die laag kan niet weg zonder de kop onleesbaar te maken. Er zit een fel
verlichte loods in de film en op die beeldjes haalt wit **1,00:1**: wit op wit,
de kop is dan letterlijk niet te zien. Met de laag erop staat de kop op 4,37:1,
de introtekst op 5,83:1 en de knoppen op 7,32:1. 30% is de lichtste stand
waarop dat lukt.

Wil je toch een kalere film, dan is de weg: een ander fragment kiezen zonder die
loods, of de tekst uit het beeld halen en op een vlak eronder zetten.

## Het contactvlak is niet leesbaar genoeg

Het patroon staat daar op volle sterkte, zonder waas. Dat is een keuze, geen
vergissing, maar de witte tekst haalt de contrasteis niet: label 1,76:1 (nodig
4,5), kop 2,03:1 (nodig 3) en introtekst 3,15:1 (nodig 4,5). Iemand die slecht
ziet, of die op een telefoon in de zon staat, leest dat vlak niet.

Twee manieren om het op te lossen met behoud van het patroon: de waas
terugzetten (de regel staat in `styleguide.css`), of de tekst uit het midden
halen naar de donkere hoek linksonder. Beide zijn een paar regels werk.

## Het merkpatroon: het paars staat naast de huisstijl

De patronen staan op contact, cases, cursusaanbod (hero) en in het contactvlak
van elke pagina. Ze zijn opgebouwd uit petrol en geel, wat klopt, maar er zit
donkerpaars in als donkerste tint. Dat zit niet in de huisstijl: het donkerste
vlak op de site is `#014144`, diep petrol, afgeleid uit het logo.

In versie 2 is dat paars een stuk minder prominent dan in de eerste versie, en
op de telefoonband is het door de uitsnede helemaal weg. Op breed scherm en in
het contactvlak staat het er nog, al valt het in het contactvlak nauwelijks op
door de petrolwaas eroverheen.

Te beslissen: het paars laten staan als donkerste tint, of de patronen opnieuw
exporteren met het diepe petrol daar. Zie `assets/patronen/HERKOMST.md`.

## De herovideo: licentie onbekend

De homepage-hero draait sinds 2 september 2026 een film in plaats van een foto
(`assets/video/hero-logistiek.mp4`: vrachtwagen, loods, terminal, schip). Die is
aangeleverd zonder bron. Twee dingen om na te gaan voor het live gaat:

1. **De licentie.** Er zat geen bron bij; ga na of het commercieel gebruikt mag
   worden.
2. **De belettering op de vrachtwagen ("A6").** Als dat een bestaand bedrijf is,
   staat er een herkenbare partij in beeld die daar niet om gevraagd heeft.

Zie `assets/video/HERKOMST.md`. Liever nog eigen dronebeeld van een
opdrachtgever: dan staat er een terrein waar MADEGRO ook echt geweest is.

## Het logo: geplaatst, maar drie dingen om te beslissen

Het echte logo staat er (`assets/logo/madegro-logo.svg`, met het onveranderde
origineel ernaast als `madegro-logo-orgineel.svg`). Het placeholderwoordmerk is
weg. Drie dingen die daarmee boven tafel komen:

**1. De huisstijlkleuren zijn naar het logo getrokken. OPGELOST (2 september 2026.)**
De site stond in groen `#0C8653`, een aanname uit de projectbrief, terwijl het
logo petrol `#017E84` is. Dat wringde in de balk. Op jouw aanwijzing is het
merkgroen nu de kleur van het logo; de twee donkerdere tonen zijn afgeleid van
dezelfde tint (182,7&deg;) en verzadiging, dus de hele ramp is &eacute;&eacute;n kleur:

| token | was | is |
|---|---|---|
| `--color-groen` | `#0C8653` | `#017E84` |
| `--color-groen-diep` | `#075E3B` | `#01575B` |
| `--color-groen-diepst` | `#06442C` | `#014144` |

Nog te beslissen: het logo draagt ook een bleekgeel `#EBE184` en de site een fel
`#FFFC58`. Dat verschil staat er nog. En het geel heeft nog geen ingedrukt-kleur
zoals het groen die nu wel heeft. Zeg het als je die erbij wilt, dat is &eacute;&eacute;n
token.

De favicon (`assets/favicon/favicon.svg`) en de deelafbeelding
(`assets/social/madegro-deelafbeelding.png`) staan nog in de oude
placeholderkleuren en horen bij dezelfde beslissing.

**2. De ondertitel is in de balk onleesbaar.** Het logo is 5,68:1 en draagt
&ldquo;Kwaliteit | Arbo | Milieu&rdquo; in de onderste helft. Op 32 px hoog wordt die regel
6 px; ik heb de balk daarom op 40 px gezet, maar dan is het nog 8 px. Wat een
balk eigenlijk nodig heeft is een **compacte variant zonder ondertitel**. Vraag
die op bij wie het logo gemaakt heeft; het volledige logo kan dan in de voet
blijven staan, waar wel ruimte is.

**3. Op een fotohero verliest het logo contrast: opgelost.** De letters
MADEGRO zijn uitgespaard, niet gevuld: ze nemen de kleur aan van wat erachter
zit. Op wit en op het grijs van de gescrolde balk gaat dat goed, maar op de
fotohero's van de homepage, de drie diensten en de vier cursussen hing het ervan
af hoe donker de foto op die plek was. Op `veilig-gedrag.html` is de foto
linksboven licht en liepen de letters bijna weg tegen het petrol.

Martin heeft daarvoor een witte variant aangeleverd
(`assets/logo/madegro-logo-wit.svg`): witte letterromp met de ondertitel in
petrol. Die staat nu in de balk zodra de header op een donkere ondergrond zit,
en het petrolkleurige logo staat er zodra hij op wit of grijs staat. Er is dus
geen wit plaatje of filter meer nodig. Blijft alleen punt 2 open: een compacte
variant zonder ondertitel, en die is er dan dus in twee kleuren nodig.

---

## Wat er uit Martins LinkedIn-profiel is overgenomen

Uit `linkedin.com/in/martin-de-groot-5b197415`:

| Op de site | Uit het profiel |
|---|---|
| &ldquo;MADEGRO bestaat sinds 2002&rdquo; | Owner MADEGRO, jul. 2002 &ndash; heden |
| &ldquo;24 jaar zelfstandig&rdquo; | idem, 24 jr 3 mnd |
| &ldquo;18 opdrachtgevers&rdquo; en de namen in de band | de lijst onder &ldquo;Opdrachtgevers&rdquo; |
| &ldquo;6 branches&rdquo; | geteld uit diezelfde lijst |
| EHSQ-specialist, Hogeschool van Amsterdam | kop en opleiding |
| Cosun Beet Company, Huhtamaki, AEB Amsterdam, GE Vernova | de functies in het profiel |
| jeugdtrainer en voorzitter bij de atletiekvereniging | vrijwilligerswerk, AV Monnickendam |

**Er stond eerder dat MADEGRO in 2021 begon.** Dat was verzonnen en het scheelde
negentien jaar. Het is overal rechtgezet.

**Let op de KvK-inschrijving.** Op de site staat Madegro Advies B.V. met KvK
81812892. Als de B.V. van recenter datum is dan 2002, dan is &ldquo;bestaat sinds
2002&rdquo; waar voor het bedrijf maar niet voor deze rechtspersoon. Laat Martin
zeggen hoe hij dat geformuleerd wil hebben.

**Nog niet gebruikt, wel de moeite waard:** Martin geeft aantoonbaar VCA
Basis-trainingen (zie zijn bericht over de training in Leeuwarden) en bezocht
het Safety Culture Ladder-event. VCA staat niet in het cursusaanbod, terwijl het
de best onderbouwde cursus zou zijn die er staat. Overweeg die toe te voegen en
een van de verzonnen cursussen te laten vallen.

---

## Het aantal deelnemers: staat als geel invulveld op vier pagina's

Onder de knoppen in de kop van elke cursuspagina staat &ldquo;Al [aantal nog
invullen] deelnemers gingen je voor.&rdquo; Het getal ontbreekt met opzet: er stond
eerder &ldquo;450 cursisten opgeleid&rdquo; op de homepage en dat was verzonnen. Op de
plek waar het nu staat, direct onder de belangrijkste knop, zou een
verzonnen getal het meeste gewicht krijgen van alles op de pagina.

Zet het per cursus in `deelnemers` in het inhoudsbestand; zonder waarde blijft
het gele veld staan, dat kan niet per ongeluk live.

Heeft Martin geen telling, dan is er een alternatief dat wel klopt: noem in
plaats van een aantal de opdrachtgevers waar de cursus al gegeven is. Die namen
staan al in de logoband.

---

## De cursuspagina's

Twee dingen die bij het herindelen van de layout uit de FAQ naar boven zijn
gehaald en nu prominenter staan dan eerst:

- **Het tarief.** &euro; 750 per dagdeel stond alleen in een FAQ-antwoord en staat
  nu als kerncijfer boven aan elke cursuspagina. Het bedrag was al een aanname;
  op die plek valt het veel meer op, dus laat Martin het bevestigen v&oacute;&oacute;r
  publicatie.
- **De doelgroepbeschrijving.** De sectie &ldquo;Voor wie&rdquo; is samengesteld uit de regel
  op `cursusaanbod.html` en de FAQ-antwoorden. Voor de cursus
  Veiligheidsbewustzijn stond die tekst er al; voor de andere drie heb ik hem
  geschreven op basis van het bestaande materiaal.

---

## De waarden op `over-ons.html`

De vier vlakken onder &ldquo;Waar we voor staan&rdquo; (Nuchter, Op de vloer, Praktisch,
Overdraagbaar) zijn door mij afgeleid uit wat er al op de site stond, niet door
Martin opgeschreven. Ze klinken als zijn woorden omdat ze uit zijn teksten komen,
maar hij heeft ze nooit zo benoemd. Laat hem ze bevestigen of herschrijven.

---

## De sectie over Martin (homepage en over-ons)

Wat hij zelf heeft aangeleverd: dat hij ultramarathons loopt, ironmans doet en
reist. De rest komt nu uit zijn LinkedIn-profiel; zie de tabel hierboven.

Twee zinnen zijn nog van mij en geen citaat:

- de laatste zin van de sportalinea, die de sport doortrekt naar
  veiligheidscultuur;
- &ldquo;Kennisoverdracht is geen bijproduct maar het doel: klanten worden
  zelfstandiger, niet afhankelijker.&rdquo;

Allebei passen ze bij wat hij op LinkedIn schrijft, maar hij heeft ze niet zo
gezegd.

## Juridische pagina's

`privacybeleid.html` en `cookies.html` hebben opzettelijk gaten, gemarkeerd met de
gele blokken. Daar hoort niets verzonnen te worden:

- datum van laatste wijziging
- welke gegevens bij een cursusaanmelding worden vastgelegd, en hoe lang
- hostingpartij en certificerende instantie, en of er een verwerkersovereenkomst ligt
- welke beveiligingsmaatregelen er echt zijn ingericht
- welke statistiekentool gebruikt gaat worden

---

## Techniek

- **Het contactformulier verstuurt niets.** Zet het endpoint in
  `contactformulier.js` (`ENDPOINT`).
- **Statistieken laden niet.** Zet het meet-ID in `analytics.js` (`META_ID`).
- **Het logo** is een voorlopig woordmerk in `assets/logo/madegro-logo.svg`.
- **De domeinnaam** staat als `https://www.madegro.nl` in de canonical-tags,
  `sitemap.xml` en `robots.txt`. Aanpassen als dat anders wordt.
