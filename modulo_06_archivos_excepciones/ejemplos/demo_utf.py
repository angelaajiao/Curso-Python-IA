texto = "Añadir contraseña"
print(texto)
datos = texto.encode("utf-8")
datos
print(datos)
datos.decode("utf-8")
print(datos)
datos.decode("latin-1")  
print(datos)        # lo que se ve al abrir mal un fichero
len(texto), len(datos)
