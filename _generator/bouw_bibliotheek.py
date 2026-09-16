# -*- coding: utf-8 -*-
"""Schrijft assets/foto/bibliotheek.json: de foto's die het beheer (admin.html)
   in zijn fotokiezer laat zien, met per foto een groot pad (hero, sfeerfoto),
   een klein pad (kaart) en de alt-tekst. Alleen echte foto's; het portret van
   Martin en de illustratie horen niet in een case."""
import sys, pathlib, json
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from schil import FOTOS, MATEN

UIT = pathlib.Path(__file__).resolve().parent.parent

def bibliotheek():
    lijst = []
    for sleutel, (naam, gb, gh, kb, kh, alt, map_, mb) in FOTOS.items():
        if map_ != "foto" or sleutel == "martin-band":
            continue
        maten = sorted(MATEN.get(sleutel) or ({kb, gb} | ({mb} if mb else set())))
        # Groot: de kleinste maat van minstens 1024, anders de grootste die er is.
        groot = next((m for m in maten if m >= 1024), maten[-1])
        klein = next((m for m in maten if m >= 480), maten[0])
        lijst.append({
            "sleutel": sleutel,
            "naam": sleutel.replace("-", " ").capitalize(),
            "groot": f"assets/{map_}/{naam}-{groot}.webp",
            "klein": f"assets/{map_}/{naam}-{klein}.webp",
            "alt": alt.replace("&rsquo;", "’"),
        })
    return lijst

if __name__ == "__main__":
    pad = UIT / "assets/foto/bibliotheek.json"
    pad.write_text(json.dumps(bibliotheek(), ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"bibliotheek.json geschreven ({len(bibliotheek())} foto's)")
