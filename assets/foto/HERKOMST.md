# Herkomst van de foto's

Alle foto's hieronder staan onder **CC0** of in het **publiek domein**: ze mogen
commercieel gebruikt worden en er is geen bronvermelding verplicht. Ze zijn
gevonden via [Openverse](https://openverse.org), bijgesneden en omgezet naar WebP.

Dit is opvulbeeld. Zodra Martin eigen foto's heeft van zijn opdrachtgevers,
projecten en cursussen, vervangen die deze bestanden een-op-een: zelfde
bestandsnamen, zelfde formaten.

| Bestand | Oorspronkelijke titel | Licentie | Bron | Pagina |
|---|---|---|---|---|
| `bouwplaats-*.webp` | HK SKD 日出康城 Lohas Park Road construction site buildings August 2024 R12S.02 | cc0 | wikimedia | https://commons.wikimedia.org/w/index.php?curid=152100483 |
| `productiehal-*.webp` | zonder titel | cc0 | rawpixel | https://www.rawpixel.com/image/5945466/free-public-domain-cc0-photo |
| `lassen-*.webp` | Staff Sgt. Elizabeth Germain welds | cc0 | rawpixel | https://www.rawpixel.com/image/8729603/photo-image-light-public-domain-person |
| `overleg-*.webp` | Business Team | cc0 | stocksnap | https://stocksnap.io/photo/business-team-W6PNBNYHM6 |
| `transport-*.webp` | zonder titel | cc0 | rawpixel | https://www.rawpixel.com/image/6065610/free-public-domain-cc0-photo |
| `haven-*.webp` | Boats Ships | cc0 | stocksnap | https://stocksnap.io/photo/boats-ships-27D9PQ26RJ |

## Formaten

Elke foto staat er twee keer in, voor `srcset`: een grote en een kleine variant.
De hero is 2400 en 1200 px breed; de overige beelden 1024 (of 960) en 640 px.
Bijsnijden gebeurde op 16:9 voor banden en 3:2 voor de kaarten, met het
zwaartepunt iets boven het midden.

## De illustratie

`assets/illustratie/madegro-terrein-*.webp` is **geen stockbeeld**: die is door de
opdrachtgever aangeleverd (`illustratie.png`, 4608 &times; 3072, met transparantie).
Hij staat in de huisstijlkleuren en wordt gebruikt in `s03-hoe-we-werken` op de
homepage. De eerste aangeleverde versie staat er nog naast als
`illustratie-v1.png`; die wordt nergens meer gebruikt en mag weg.

Bewerking: de doorzichtige rand eraf gesneden (4538 &times; 2965), daarna twee
WebP-formaten met `cwebp -q 82 -alpha_q 90`: 1520 &times; 993 en
800 &times; 523, samen 265 kB. Het bronbestand blijft ernaast staan, zodat er
opnieuw uit gesneden kan worden.

## martinv3.png en de martin-band-*.webp

Door de klant aangeleverd (1 september 2026), geen stockbeeld: Martin op een trap
voor het Viaduc de Passy in Parijs. Bron is 800x800 zonder balken, en hij zit
midden in beeld, anders dan de eerdere strandfoto, waar hij ver naar links stond.

De afgeleiden zijn de hele foto, verkleind naar 800 en 440 en geconverteerd met
`cwebp -q 78`. Die 78 is lager dan de 86 die we elders gebruiken: het steen van
de trap en de boog zit vol fijne structuur, en op 86 werd het bestand 206 kB.
Op 78 is dat 156 kB en is er op weergavegrootte niets van te zien.

De uitsnede zit niet in het bestand maar in de CSS: `object-fit: cover` met
`object-position: center 65%` in de modifier `.streamer--employee--portret`.
Onder 992px is de band liggend en zou Martin bij een beeldpunt van 50% te laag
uitvallen; op 65% toont hij de onderkant van de foto en staat Martin hoger in
het kader.

    python3 -c "
    from PIL import Image
    Image.open('martinv3.png').convert('RGB').save('/tmp/m.png')"
    cwebp -q 78 /tmp/m.png -o martin-band-800.webp

## martin.png (strandfoto)

**Niet meer in gebruik.** Vervangen door martinv3.png. De afgeleiden zijn
verwijderd; het origineel blijft staan.



## Cursusfoto's (aangeleverd, 3 september 2026)

Vier foto's, aangeleverd door Jesse als PNG en bewaard in `bron/`. **De licentie
is bij ons niet bekend**: het zijn professionele foto's die eruitzien als
stock- of persmateriaal. Voor het live gaat moet vaststaan dat MADEGRO ze mag
gebruiken; zie CONTENT-TODO.md.

| Bestand | Bron | Waar | Let op |
|---|---|---|---|
| `cursus-bewustzijn-bouw-*` | `Veiligheidsbewustzijn.png`, 1920x1280 | hero en kaart van Veiligheidsbewustzijn op de werkvloer | op de achtergrond een gebouw met kpn-belettering |
| `cursus-risico-lijn-*` | `riscios herkennen.png`, 3600x2400 | hero en kaart van Risico's herkennen en beoordelen | |
| `cursus-ladder-helmen-*` | `veiligheidsladder.png`, 3111x1746 | hero en kaart van Werken met de Veiligheidsladder | de witte helm draagt het logo van PILZ, een bestaand bedrijf in machineveiligheid |
| `cursus-rie-tablet-*` | `ri&e.png`, 700x525 | hero en kaart van RI&E in de praktijk | **te klein voor een hero**: 700px breed, wordt op een bureaublad tot 2400px opgerekt en is dan zacht |

Bewerking: niet bijgesneden (de hero's en kaarten snijden zelf met
`object-fit: cover`), alleen verkleind naar de breedtes in `MATEN` en gecodeerd
zonder metadata: WebP kwaliteit 82, AVIF kwaliteit 62. De browser kiest per
scherm de kleinste maat die scherp is.

## Dienstfoto's (aangeleverd, 3 september 2026)

Drie foto's, aangeleverd door Jesse als PNG en bewaard in `bron/`. Zelfde
voorbehoud als bij de cursusfoto's: **de licentie is bij ons niet bekend**; zie
CONTENT-TODO.md.

| Bestand | Bron | Waar | Let op |
|---|---|---|---|
| `dienst-gedrag-*` | `veiligheidsgedrag.png`, 1024x683 | hero van Veilig gedrag en de dienstkaart op de homepage | |
| `dienst-rie-*` | `ehs rie.png`, 1024x565 | hero van EHS RI&E en de dienstkaart op de homepage | het gele hesje draagt het logo en de slogan van EHS-services, een ander bedrijf |
| `dienst-checks-*` | `savety check.png`, 1200x670 | hero van Safety Checks en de dienstkaart op de homepage | Engelse bordteksten in beeld: SAFETY FIRST, MANDATORY PPE, EMERGENCY STOP en een klembord met RISK ASSESSMENT |

Alle drie zijn aan de krappe kant voor de hero. Die is op een bureaublad de
halve schermbreedte: 960 CSS-pixels op een scherm van 1920, en op een
retinascherm het dubbele daarvan. Boven de bronbreedte (1024 of 1200) rekt de
browser op. Op een telefoon en op een gewoon bureaublad is daar niets van te
zien; op een groot retinascherm zijn ze wat zachter dan de cursusfoto's.

Bewerking als bij de cursusfoto's: niet bijgesneden, verkleind naar 480, 800 en
de bronbreedte, WebP kwaliteit 82 en AVIF kwaliteit 62, zonder metadata. Samen
drie keer drie maten in twee formaten, 726 kB in totaal; per paginaweergave laadt
er daarvan één bestand van 13 tot 83 kB.

De CC0-foto's die op deze plekken stonden (`overleg`, `lassen`, `haven`)
blijven in gebruik op de cases, de cursuspagina's en in de dienstenkaart van het
menu.
