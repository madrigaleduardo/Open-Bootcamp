#Crea una clase Persona con las siguientes variables: La edad, El nombre y El teléfono

class Persona:
    def __init__(self, edad, nombre, telefono):
        self._edad = edad
        self._nombre = nombre
        self._telefono = telefono

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

# Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.

class Cliente(Persona):
    def __init__(self, edad, nombre, telefono, credito):
        super().__init__(edad, nombre, telefono)
        self._credito = credito

    def get_credito(self):
        return self._credito

    def set_credito(self, credito):
        self._credito = credito


class Trabajador(Persona):
    def __init__(self, edad, nombre, telefono, salario):
        super().__init__(edad, nombre, telefono)
        self._salario = salario

    def get_salario(self):
        return self._salario

    def set_salario(self, salario):
        self._salario = salario


# Crea ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.
c = Cliente(32, "Eduardo", "5529723499", 1000)
# Mostramos las propiedades
print("Edad: ", c.get_edad())
print("Nombre: ", c.get_nombre())
print("Teléfono: ", c.get_telefono())
print("Crédito: ", c.get_credito())

# Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.

t = Trabajador(30, "Natalia", "7724342432", 2000)
# Mostramos las propiedades
print("Edad: ", t.get_edad())
print("Nombre: ", t.get_nombre())
print("Teléfono: ", t.get_telefono())
print("Salario: ", t.get_salario())
