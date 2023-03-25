archivo = open("archivo.txt", "w")
archivo.write("Hola, este es mi archivo de texto.")
archivo.close()

archivo = open("archivo.txt", "a")
archivo.write("\n¡Acabo de añadir una nueva línea al archivo txt!")
archivo.close()

