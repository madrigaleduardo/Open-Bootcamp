# Pedir al usuario una lista de países
paises = input("Ingrese una lista de países separados por comas: ")

# Convertir la cadena de entrada en una lista de países
lista_paises = paises.split(",")

# Crear un conjunto a partir de la lista de países para eliminar duplicados
conjunto_paises = set(lista_paises)

# Convertir el conjunto de países en una lista, eliminando espacios en blanco al principio o al final de cada país
lista_ordenada = sorted([pais.strip() for pais in conjunto_paises])

# Imprimir la lista de países ordenados alfabéticamente y separados por comas
print("Los países ingresados en orden alfabético son: " + ", ".join(lista_ordenada))

