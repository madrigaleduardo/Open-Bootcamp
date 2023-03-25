from functools import reduce

# Definir una lista de numeros
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Usar filter para obtener los elementos impares de la lista
impares = list(filter(lambda x: x % 2 != 0, lista_numeros))

# Usar reduce para sumar los elementos impares obtenidos anteriormente
suma_impares = reduce(lambda x, y: x + y, impares)

# Imprimir los resultados
print("Lista números:", lista_numeros)
print("Elementos impares:", impares)
print("Suma de los elementos impares:", suma_impares)
