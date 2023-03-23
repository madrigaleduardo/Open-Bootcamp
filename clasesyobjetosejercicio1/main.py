# Crear la clase Vehículo la cual tendrá los siguientes atributos: Color, Ruedas y Puertas

class Vehiculo:
    def __init__(self, color, ruedas, puertas):
        self.color = color
        self.ruedas = ruedas
        self.puertas = puertas

# Crear clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos: Velocidad y Cilindrada

class Coche(Vehiculo):
    def __init__(self, color, ruedas, puertas, velocidad, cilindrada):
        super().__init__(color, ruedas, puertas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

#  Crear un objeto de la clase Coche y mostrarlo por consola

mi_coche = Coche("Negro", 4, 4, 300, 1970)


print("Color:", mi_coche.color)
print("Ruedas:", mi_coche.ruedas)
print("Puertas:", mi_coche.puertas)
print("Velocidad:", mi_coche.velocidad)
print("Cilindrada:", mi_coche.cilindrada)
