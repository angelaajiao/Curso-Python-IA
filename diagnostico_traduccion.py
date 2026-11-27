"""Diagnóstico de la traducción. Ejecutar con:  python diagnostico_traduccion.py

No forma parte de la app: se puede borrar cuando terminemos.
"""

import traduccion

FRASE = "Heat the oil in a large pan."

for nombre, traductor in [("Google", traduccion._traductor_google("es")),
                          ("MyMemory", traduccion._traductor_mymemory("es"))]:
    try:
        print(f"{nombre:<9} OK   ->", traductor(FRASE))
    except Exception as error:
        print(f"{nombre:<9} FALLA ->", type(error).__name__, error)

traducidas, ok = traduccion.traducir_lista([FRASE, "Add the rice."])
print("\nLo que usa la app: ok =", ok, "|", traducidas)
