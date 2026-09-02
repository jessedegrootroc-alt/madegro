const http = require('http');
const fs = require('fs');
const path = require('path');
const zlib = require('zlib');

const ROOT = "/Users/jessevialuxury.nl/Library/CloudStorage/OneDrive-Advalley(2)/Documenten/Code/SERVICE.BASED.LANDINGSPAGE";
const PORT = 5500;

const TYPES = {
  '.html': 'text/html; charset=utf-8',
  '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8',
  '.json': 'application/json; charset=utf-8',
  '.svg': 'image/svg+xml',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.webp': 'image/webp',
  '.avif': 'image/avif',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.mp4': 'video/mp4',
  '.webm': 'video/webm',
  '.pdf': 'application/pdf',
};

// Tekstbestanden gaan gecomprimeerd over de lijn. Zonder dit is styleguide.css
// 96 kB en index.html 61 kB; met brotli is dat 20 en 10 kB. Afbeeldingen, video
// en woff2 zitten al in een gecomprimeerd formaat en gaan er ongemoeid doorheen:
// die nog eens door gzip halen kost tijd en levert niets op.
const COMPRIMEERBAAR = new Set([
  'text/html; charset=utf-8', 'text/css; charset=utf-8', 'text/javascript; charset=utf-8',
  'application/json; charset=utf-8', 'image/svg+xml', 'application/xml; charset=utf-8',
  'text/plain; charset=utf-8',
]);

// Hoe lang de browser een bestand mag bewaren. De namen van de afbeeldingen en
// van de video dragen hun maat in zich (logistiek-1200.webp); komt er een andere
// versie, dan komt er een andere naam, dus die mogen lang blijven staan.
// HTML, CSS en JS worden nog bewerkt en moeten elke keer opnieuw gecontroleerd
// worden, anders zie je je eigen wijziging niet.
//
// LET OP: dit is de ontwikkelserver. Voor productie horen CSS en JS ook lang
// gecachet te worden, maar dan met een versie in de bestandsnaam of in de query.
// Zie LEVERING.md voor de headers die daar horen te staan.
function cache(type) {
  if (type.startsWith('image/') || type.startsWith('video/') || type.startsWith('font/')) {
    return 'public, max-age=31536000, immutable';
  }
  return 'no-cache';
}

http.createServer((req, res) => {
  let rel = decodeURIComponent(req.url.split('?')[0]);
  if (rel.endsWith('/')) rel += 'index.html';
  const file = path.normalize(path.join(ROOT, rel));
  if (!file.startsWith(ROOT)) { res.writeHead(403); return res.end('Forbidden'); }
  fs.readFile(file, (err, data) => {
    if (err) {
      res.writeHead(404, {'Content-Type': 'text/html; charset=utf-8'});
      return res.end('<h1>404</h1><p>' + rel + '</p>');
    }
    const type = TYPES[path.extname(file).toLowerCase()] || 'application/octet-stream';
    const kop = {'Content-Type': type, 'Cache-Control': cache(type)};

    const mag = (req.headers['accept-encoding'] || '');
    if (COMPRIMEERBAAR.has(type) && data.length > 512) {
      if (/\bbr\b/.test(mag)) {
        kop['Content-Encoding'] = 'br';
        kop['Vary'] = 'Accept-Encoding';
        return zlib.brotliCompress(data, {
          params: {[zlib.constants.BROTLI_PARAM_QUALITY]: 5},
        }, (e, uit) => { res.writeHead(200, kop); res.end(e ? data : uit); });
      }
      if (/\bgzip\b/.test(mag)) {
        kop['Content-Encoding'] = 'gzip';
        kop['Vary'] = 'Accept-Encoding';
        return zlib.gzip(data, {level: 6}, (e, uit) => {
          res.writeHead(200, kop); res.end(e ? data : uit);
        });
      }
    }
    res.writeHead(200, kop);
    res.end(data);
  });
}).listen(PORT, () => console.log('Serving ' + ROOT + ' on http://localhost:' + PORT));
