LETRAS_DNI = "TRWAGMYFPDXBNJZSQVHLCKE"

def esta_vacio(texto):
    return texto is None or texto.strip() == ""

def normalizar_nombre(nombre):
    palabras = nombre.split()
    return " ".join(palabra.capitalize() for palabra in palabras)

def es_email(texto):
    if " " in texto or texto.count("@") != 1:
        return False
    usuario, dominio = texto.split("@")
    if not usuario or "." not in dominio:
        return False
    return not dominio.startswith(".") and not dominio.endswith(".")

def es_dni(texto):
    texto = texto.strip().upper()
    if len(texto) != 9:
        return False
    numero, letra = texto[:8], texto[8]
    if not (numero.isascii() and numero.isdigit()):
        return False
    return LETRAS_DNI[int(numero) % 23] == letra