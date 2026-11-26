# Módulo 7. Ejercicios

Sustituye cada `raise NotImplementedError` por tu código y comprueba el resultado con:

```bash
pytest modulo_07_ciencia_datos -v
pytest modulo_07_ciencia_datos -v -k ej2        # solo un ejercicio
```

Necesitas `numpy`, `pandas` y `matplotlib`. Si los tests fallan con `ModuleNotFoundError`, activa el entorno virtual y ejecuta `pip install -r requirements.txt`.

Tres normas para todo el módulo:

- **Sin bucles.** Las operaciones se hacen sobre el array o la columna completos. Si escribes un `for` para recorrer filas, busca el método que lo hace.
- **Sin modificar lo que recibes.** Todas las funciones devuelven un objeto nuevo y dejan el original como estaba.
- **Sin `print` ni `plt.show()`.** Las funciones devuelven datos o figuras.

Para probar a mano, abre un intérprete o un cuaderno en la carpeta del módulo y carga los datos:

```python
import pandas as pd
ventas = pd.read_csv("datos/ventas_2026.csv", parse_dates=["fecha"])
```

## Ejercicio guiado: EDA del Titanic

Abre `eda_titanic.ipynb` y ejecuta sus celdas en orden. El cuaderno usa el
CSV incluido en `datos/titanic.csv` y propone preguntas para practicar
inspección, valores ausentes, visualización e interpretación. Es independiente
de los ejercicios evaluados con pytest.

## Ejercicio 1. NumPy

Fichero: `m7_ej1_numpy.py`

| Función | Qué practica |
| --- | --- |
| `crear_rango(inicio, fin, paso)` | `np.arange` |
| `estadisticas(valores)` | Agregaciones y conversión a `float` de Python |
| `aplicar_iva(precios, tipo)` | Aritmética vectorizada y `np.round` |
| `normalizar(valores)` | Operar con el mínimo y el máximo del propio array |
| `mayores_que_la_media(valores)` | Máscaras booleanas |
| `reemplazar_negativos(valores, sustituto)` | `np.where` |
| `totales(matriz)` | El parámetro `axis` |
| `importes(unidades, precios)` | Operación entre dos arrays y comprobación de la forma |
| `media_movil(valores, ventana)` | Reto: sin bucles |

Pista para `media_movil`: busca `np.convolve` y su modo `"valid"`. Una media es una suma con todos los pesos iguales.

## Ejercicio 2. pandas: cargar, inspeccionar y seleccionar

Fichero: `m7_ej2_pandas.py`

| Función | Qué practica |
| --- | --- |
| `crear_dataframe(ventas)` | De la lista de diccionarios del Módulo 4 a un DataFrame |
| `cargar_ventas(ruta)` | `read_csv` y `parse_dates` |
| `con_importe(df)` | Columna calculada sin tocar el original |
| `resumen(df)` | `len`, `columns`, `min`, `max` y `sum` |
| `ventas_de(df, vendedor)` | Filtro con una condición |
| `filtrar(df, region, categorias, unidades_minimas)` | Combinar condiciones opcionales con `&` e `isin` |
| `mayores_ventas(df, n)` | `nlargest` y selección de columnas |
| `productos(df)` | `unique` |
| `precio_medio_por_categoria(df)` | Un primer `groupby` |

Pista para `filtrar`: empieza con una máscara que siempre se cumple y ve estrechándola con `&=` solo cuando el criterio venga indicado.

## Ejercicio 3. Limpieza de datos

Fichero: `m7_ej3_limpieza.py`
Datos: `datos/ventas_sucias.csv`, con 63 filas de las que 54 son aprovechables

| Función | Qué practica |
| --- | --- |
| `cargar_en_bruto(ruta)` | `dtype=str` |
| `contar_ausentes(df)` | `isna().sum()` |
| `normalizar_texto(df, columnas)` | El accesor `.str` |
| `convertir_tipos(df)` | `to_datetime` y `to_numeric` con `errors="coerce"` |
| `quitar_duplicados(df)` | `drop_duplicates` |
| `rellenar_region(df, valor)` | `fillna` |
| `limpiar(df)` | Encadenar todo lo anterior en el orden correcto |

Antes de escribir nada, abre el fichero y busca los defectos a ojo. Hay de seis tipos.

Pista para `normalizar_texto`: usa `capitalize`, no `title`. Mira qué le pasaría a «Licencia ofimática».

## Ejercicio 4. Agrupar, agregar y combinar

Fichero: `m7_ej4_agrupacion.py`

| Función | Qué practica |
| --- | --- |
| `importe_por(df, columna)` | `groupby`, `sum` y `sort_values` |
| `cuota(df, columna)` | Operar con el resultado de un `groupby` |
| `resumen_por_vendedor(df)` | `agg` con varias medidas con nombre |
| `importe_mensual(df)` | Agrupar por una columna derivada de la fecha |
| `tabla_region_categoria(df)` | `pivot_table` |
| `producto_estrella(df)` | Reto: agrupar por dos columnas |
| `con_objetivos(resumen, objetivos)` | `merge` con `how="left"` |

Compara `importe_por(df, "region")` con el `agrupar_por` que escribiste en el Módulo 4. Hacen lo mismo.

## Ejercicio 5. Visualización

Fichero: `m7_ej5_graficos.py`

| Función | Qué practica |
| --- | --- |
| `grafico_barras(serie, titulo, etiqueta_y)` | `plt.subplots`, `bar`, título y etiquetas |
| `grafico_lineas(serie, titulo, etiqueta_y)` | `plot` con marcadores y rejilla |
| `histograma(valores, titulo, intervalos)` | `hist` |
| `panel(por_vendedor, mensual, titulo)` | Dos ejes en una figura y `suptitle` |
| `guardar(figura, ruta)` | `savefig` y `plt.close` |

Los tests no miran los colores ni el tamaño: comprueban que la figura tiene los ejes, las barras, las líneas y los textos que se piden. Para ver tus gráficos, guárdalos y abre el PNG:

```python
from m7_ej5_graficos import grafico_barras, guardar
guardar(grafico_barras(serie, "Prueba"), "prueba.png")
```

## Práctica 7

Enunciado en [`PRACTICA_7.md`](PRACTICA_7.md).

## Para quien termine antes

- Completa el apartado «Tu turno» del cuaderno `ejemplos/07_cuaderno_exploracion.ipynb`.
- Reescribe con pandas el informe de la Práctica 4 y comprueba que salen las mismas cifras.
- Mide con `%timeit`, en un cuaderno, cuánto tarda `importe_por` y cuánto tu `agrupar_por` del Módulo 4 con las 320 ventas repetidas mil veces: `pd.concat([ventas] * 1000)`.
