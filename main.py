#Crear una función con tres parámetros que sean números que se suman entre sí

def sumar_numeros(num1, num2, num3):
    suma = num1 + num2 + num3
    return suma

# Llamar a la función en el main y darle valores

resultado = sumar_numeros(1, 2, 3)
print("La suma de los números es", resultado)

# Crear una clase coche
# Dentro de la clase coche, una variable numérica que almacene el número de puertas que tiene
# la clase Coche, que tiene un constructor __init__() que recibe como parámetro el número de puertas del coche, y un método añadir_puerta() que incrementa en uno el número de puertas

class Coche:
    def __init__(self, num_puertas):
        self.num_puertas = num_puertas

    def añadir_puerta(self):
        self.num_puertas += 1


#Crear un objeto miCoche en el main y añadirle una puerta
#Mostrar el número de puertas que tiene el objeto

miCoche = Coche(4)
miCoche.añadir_puerta()
print("El coche tiene", miCoche.num_puertas, "puertas")
