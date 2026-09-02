# -*- coding: utf-8 -*-
"""Bouwt alle twintig pagina's. Gebruik dit en niet de losse scripts: de
   service- en cursuspagina's worden gedreven door inhoud_*.py, niet door
   bouw_service.py / bouw_cursus.py, en die twee los draaien doet niets."""
import runpy, sys, pathlib
HIER = pathlib.Path(__file__).parent
sys.path.insert(0, str(HIER))

for naam in ["bouw_home", "inhoud_services", "inhoud_cursussen",
             "bouw_cases", "bouw_rest", "bouw_contact"]:
    print(f"--- {naam}")
    runpy.run_path(str(HIER / f"{naam}.py"), run_name="__main__")
