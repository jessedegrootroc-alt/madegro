# _generator

De twintig HTML-pagina's in de hoofdmap worden hier gemaakt en zijn dus
**gegenereerde bestanden**. Pas je een pagina met de hand aan, dan is die
wijziging weg zodra hier iets opnieuw draait.

```
python3 bouw_alles.py
```

Dat schrijft alle pagina's opnieuw. `bouw_alles.py` roept de andere scripts aan:

| bestand | wat het maakt |
|---|---|
| `schil.py` | de gedeelde onderdelen: balk, voettekst, hero's, knoppen, beeld |
| `bouw_home.py` | `index.html` |
| `inhoud_services.py` | de drie dienstpagina's, via `bouw_service.py` |
| `inhoud_cursussen.py` | de vier cursuspagina's, via `bouw_cursus.py` |
| `bouw_cases.py` | het case-overzicht en de zes casepagina's |
| `bouw_rest.py` | cursusaanbod en over-ons |
| `bouw_contact.py` | contact, privacybeleid en cookies |

De CSS, de JavaScript en alles in `assets/` worden **niet** gegenereerd; die
bewerk je rechtstreeks.

## Let op: het uitvoerpad staat hard in de scripts

Bovenin elk bouwscript staat een absoluut pad naar de map waar de HTML
terechtkomt, van de machine waarop dit gebouwd is. Draai je dit ergens anders,
pas dan die `UIT = pathlib.Path(...)` regels aan.

## server.js

De ontwikkelserver, hier meegenomen omdat de metingen ermee gedaan zijn. Hij
comprimeert met brotli of gzip en zet cachetijden, net als een productieserver
hoort te doen. Bovenin staat een absoluut pad naar de map die hij uitserveert;
pas dat aan en start hem met `node server.js`.

Wat een echte server moet doen staat in `../LEVERING.md`.
