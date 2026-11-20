"""Módulo 2 - Práctica 2, parte B: calculadora de nómina. SOLUCIÓN DE REFERENCIA."""

# plantilla: inicio-quitar define aquí las constantes SEGURIDAD_SOCIAL y PAGAS
SEGURIDAD_SOCIAL = 6.35
PAGAS = 12
# plantilla: fin-quitar


def calcular_irpf(bruto_anual: float) -> float:
    """Calcula la retención anual de IRPF con una escala progresiva.

    Cada tramo se aplica solo a la parte del salario que cae dentro de él.

    >>> calcular_irpf(30000)
    7165.5
    """
    # Solución con lo visto en el módulo 2: se recorre la escala de arriba
    # abajo y se grava en cada tramo lo que excede de su límite inferior.
    # En el módulo 4 se puede reescribir con una lista de tuplas y un bucle.
    retencion = 0.0
    restante = bruto_anual

    if restante > 60000:
        retencion += (restante - 60000) * 0.45
        restante = 60000
    if restante > 35200:
        retencion += (restante - 35200) * 0.37
        restante = 35200
    if restante > 20200:
        retencion += (restante - 20200) * 0.30
        restante = 20200
    if restante > 12450:
        retencion += (restante - 12450) * 0.24
        restante = 12450
    if restante > 0:
        retencion += restante * 0.19

    return round(retencion, 2)


def calcular_seguridad_social(bruto_anual: float) -> float:
    """Calcula la cotización anual del trabajador a la Seguridad Social.

    >>> calcular_seguridad_social(30000)
    1905.0
    """
    return round(bruto_anual * SEGURIDAD_SOCIAL / 100, 2)


def calcular_neto_anual(bruto_anual: float) -> float:
    """Devuelve el salario neto anual: bruto menos IRPF y Seguridad Social.

    >>> calcular_neto_anual(30000)
    20929.5
    """
    neto = bruto_anual - calcular_irpf(bruto_anual) - calcular_seguridad_social(bruto_anual)
    return round(neto, 2)


def tipo_efectivo(bruto_anual: float) -> float:
    """Devuelve el porcentaje de IRPF sobre el bruto, con dos decimales.

    Si el bruto es cero o negativo devuelve 0.0.

    >>> tipo_efectivo(30000)
    23.89
    """
    if bruto_anual <= 0:
        return 0.0
    return round(calcular_irpf(bruto_anual) / bruto_anual * 100, 2)


def formatear_nomina(bruto_anual: float) -> str:
    """Devuelve el resumen de la nómina en cinco líneas alineadas.

    >>> print(formatear_nomina(30000))
    Bruto anual            30,000.00
    IRPF (23.89 %)         -7,165.50
    Seguridad Social       -1,905.00
    Neto anual             20,929.50
    Neto mensual            1,744.12
    """
    irpf = calcular_irpf(bruto_anual)
    seguridad_social = calcular_seguridad_social(bruto_anual)
    neto = calcular_neto_anual(bruto_anual)
    etiqueta_irpf = f"IRPF ({tipo_efectivo(bruto_anual):.2f} %)"

    return (
        f"{'Bruto anual':<20}{bruto_anual:>12,.2f}\n"
        f"{etiqueta_irpf:<20}{-irpf:>12,.2f}\n"
        f"{'Seguridad Social':<20}{-seguridad_social:>12,.2f}\n"
        f"{'Neto anual':<20}{neto:>12,.2f}\n"
        f"{'Neto mensual':<20}{neto / PAGAS:>12,.2f}"
    )


def main() -> None:
    """Pide el salario bruto anual y muestra la nómina."""
    texto = input("Salario bruto anual: ").strip()
    if not texto.replace(".", "", 1).isdigit():
        print("Importe no válido")
        return
    print(formatear_nomina(float(texto)))


if __name__ == "__main__":
    main()
