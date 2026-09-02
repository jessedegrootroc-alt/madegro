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

