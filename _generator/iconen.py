# -*- coding: utf-8 -*-
"""De iconen van de site komen uit de iconenset in assets/iconen/ (lijniconen,
   24x24, lijndikte 2, vierkante uiteinden). Ze worden inline in de HTML gezet,
   met stroke="currentColor", zodat ze de tekstkleur volgen en met CSS te
   kleuren zijn. De set zelf gaat niet mee naar de server (.vercelignore).

   Welk icoon waar staat:
     arrow-right          pijl in knoppen en de ronde icoonknop
     chevron-down         uitklapmenu
     menu / xmark         hamburger en sluitknop van het mobiele menu
     check                vinkjes in filterpillen en lijsten
     shield-check, list-check, stairs, clock, users, chart-bar-trend-up,
     file-check           de voordelen op de dienstpagina's"""
import pathlib, re

MAP = pathlib.Path(__file__).resolve().parent.parent / "assets" / "iconen"


def icoon(naam, klasse="", maat=None, extra=""):
    """Eén icoon als inline <svg>. maat is de weergavebreedte in pixels;
       zonder maat bepaalt de CSS de grootte."""
    bron = (MAP / f"{naam} 1.svg").read_text(encoding="utf-8")
    binnen = re.search(r"<svg[^>]*>(.*)</svg>", bron, re.S).group(1)
    binnen = re.sub(r'(stroke|fill)="#[0-9A-Fa-f]{3,6}"', r'\1="currentColor"', binnen)
    binnen = re.sub(r"\s*\n\s*", "", binnen).strip()
    k = f' class="{klasse}"' if klasse else ""
    m = f' width="{maat}" height="{maat}"' if maat else ""
    e = f" {extra}" if extra else ""
    return f'<svg{k}{m} viewBox="0 0 24 24" fill="none" aria-hidden="true"{e}>{binnen}</svg>'


if __name__ == "__main__":
    for n in ["arrow-right", "check"]:
        print(n, icoon(n, maat=16))
