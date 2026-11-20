"""Módulo 1 - Ejercicio 3: código con estilo. SOLUCIÓN."""

IVA_GENERAL = 21

<<<<<<< HEAD
IVA_GENERAL = 21

def precio_final(precio, iva=IVA_GENERAL, descuento=0):
  """Devuelve el precio final aplicando el descuento y después el IVA."""
  precio_con_descuento = precio - precio * descuento / 100
  precio_con_iva = precio_con_descuento + precio_con_descuento * iva / 100
  return round(precio_con_iva, 2)
=======

def precio_final(precio, iva=IVA_GENERAL, descuento=0):
    """Devuelve el precio tras aplicar el descuento y después el IVA.

    ``iva`` y ``descuento`` son porcentajes. El resultado se redondea a dos
    decimales.
    """
    precio_con_descuento = precio - precio * descuento / 100
    precio_con_iva = precio_con_descuento + precio_con_descuento * iva / 100
    return round(precio_con_iva, 2)
>>>>>>> c67e6ab911f0511b15210cc127f0d3c5623470b5
