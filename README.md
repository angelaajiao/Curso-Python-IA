# 🍳 ¿Qué cocino con lo que tengo?

Página web que propone recetas a partir de los ingredientes que tienes en casa.
Usa la API gratuita de [TheMealDB](https://www.themealdb.com).

## Qué hace

- Escribes tus ingredientes separados por comas (en español o en inglés).
- Te muestra las recetas ordenadas por cuántos de tus ingredientes usan, con foto.
- Al abrir una receta ves los ingredientes, lo que **te falta comprar** y los pasos.
- Marcas con casillas lo que tienes en casa (o todo de golpe) y la página te dice qué te falta.
- Botón "Sorpréndeme" para una receta al azar.
- Recetas favoritas: se guardan con el corazón y tienen su propio apartado. Se guardan en `favoritos.json`, así que siguen ahí al cerrar la app.
- Interfaz en español o inglés (selector con banderas). En español, las recetas se traducen automáticamente.
- Vídeo de la receta; si TheMealDB no lo tiene, botón para buscarlo en YouTube.

## Estructura

| Fichero | Qué contiene |
| --- | --- |
| `logica.py` | Toda la lógica: limpiar y traducir ingredientes, combinar y ordenar resultados, qué falta. Sin internet, con tests |
| `api.py` | Las llamadas a TheMealDB con `requests` |
| `app.py` | La página web con Streamlit. Solo muestra y recoge datos |
| `favoritos.py` | Guardar, quitar y leer las recetas favoritas (fichero `favoritos.json`) |
| `textos.py` | Todos los textos de la interfaz en español e inglés |
| `traduccion.py` | Traducción automática de las recetas con el traductor de Google |
| `.streamlit/config.toml` | Colores de la página |
| `tests/` | Tests con pytest (no necesitan internet) |

La API gratuita solo filtra por **un** ingrediente a la vez, así que se hace una
petición por ingrediente y `logica.combinar_resultados` cuenta en cuántas
búsquedas aparece cada receta.

## Cómo ejecutarlo

```bash
python -m venv .venv
.venv\Scripts\Activate.ps1        # Windows (PowerShell)
pip install -r requirements.txt

pytest                            # tests
python api.py                     # prueba rápida de la API
streamlit run app.py              # la página web
```
