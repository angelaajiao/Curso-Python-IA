"""Módulo 2 - Práctica 2, parte B: calculadora de nómina."""

# TODO: define aquí las constantes SEGURIDAD_SOCIAL y PAGAS
SEGURIDAD_SOCIAL = 6.35
PAGAS = 12

#Tramos de IRPF
TRAMOS_IRPF = [
    (12_450, 19),
    (20_200, 24),
    (35_200, 30),
    (60_000, 37),
    (float("inf"), 45),
]

def calcular_irpf(bruto_anual: float) -> float:
    """Calcula la retención anual de IRPF con una escala progresiva.

    Cada tramo se aplica solo a la parte del salario que cae dentro de él.

    >>> calcular_irpf(30000)
    7165.5
    """
    retencion = 0
    limite_anterior = 0
    for limite, tipo in TRAMOS_IRPF:
        if bruto_anual <= limite:
            retencion += (bruto_anual - limite_anterior) * tipo / 100
            break
        parte_en_tramo = min(bruto_anual, limite) - limite_anterior
        retencion += parte_en_tramo * tipo / 100
        limite_anterior = limite
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
    irpf = calcular_irpf(bruto_anual)
    seguridad_social = calcular_seguridad_social(bruto_anual)
    return round(bruto_anual - irpf - seguridad_social, 2)

def tipo_efectivo(bruto_anual: float) -> float:
    """Devuelve el porcentaje de IRPF sobre el bruto, con dos decimales.

    Si el bruto es cero o negativo devuelve 0.0.

    >>> tipo_efectivo(30000)
    23.89
    """
    if bruto_anual <= 0:
        return 0.0
    irpf = calcular_irpf(bruto_anual)
    return round(irpf / bruto_anual * 100, 2)


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
    neto_anual = calcular_neto_anual(bruto_anual)
    neto_mensual = round(neto_anual / PAGAS, 2)
    etiqueta_irpf = f"IRPF ({tipo_efectivo(bruto_anual):.2f} %)"

    lineas = [
        f"{'Bruto anual':<20}{bruto_anual:>12,.2f}",
        f"{etiqueta_irpf:<20}{-irpf:>12,.2f}",
        f"{'Seguridad Social':<20}{-seguridad_social:>12,.2f}",
        f"{'Neto anual':<20}{neto_anual:>12,.2f}",
        f"{'Neto mensual':<20}{neto_mensual:>12,.2f}",
    ]
    return "\n".join(lineas)

def main() -> None:
    """Pide el salario bruto anual y muestra la nómina."""
    try:
        bruto_anual = float(input("Salario bruto anual: "))
    except ValueError:
        print("Importe no válido")
        return
    if bruto_anual <= 0:
        print("Importe no válido")
        return
    print(formatear_nomina(bruto_anual))

if __name__ == "__main__":
    main()
