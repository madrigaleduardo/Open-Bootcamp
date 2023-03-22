#Crear clase Persona.

class Persona:
    def __init__(self):
        self._edad = None
        self._nombre = None
        self._telefono = None

#Crear variables edad, nombre y telefono de la clase Persona.

    def get_edad(self):
        return self._edad

    def set_edad(self, edad):
        self._edad = edad

    def get_nombre(self):
        return self._nombre

    def set_nombre(self, nombre):
        self._nombre = nombre

    def get_telefono(self):
        return self._telefono

    def set_telefono(self, telefono):
        self._telefono = telefono


# Crear un objeto persona en el main.
p = Persona()

# Utiliza los gets y sets para darle valores a las propiedades edad, nombre y telefono, por último muéstralas por consola
p.set_edad(32)
p.set_nombre("Eduardo")
p.set_telefono("5529412379")

# Mostramos los valores de las propiedades con los gets
print("Edad: ", p.get_edad())
print("Nombre: ", p.get_nombre())
print("Teléfono: ", p.get_telefono())
