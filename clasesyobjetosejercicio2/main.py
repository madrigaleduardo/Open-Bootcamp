# clase llamada Alumno que tenga como atributos su nombre y su nota

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

# Definir los métodos para inicializar sus atributos, imprimirlos
    def imprimir_datos(self):
        print("Nombre del alumno:", self.nombre)
        print("Nota del alumno:", self.nota)

# Mostrar un mensaje con el resultado de la nota y si ha aprobado o ha reprobado

    def resultado(self):
        if self.nota >= 6:
            print("El alumno ha aprobado")
        else:
            print("El alumno ha reprobado")

# Creamos un objeto de la clase Alumno
alumno1 = Alumno("Eduardo", 9)

# Imprimimos los atributos del objeto
alumno1.imprimir_datos()

# Mostramos el resultado de la nota
alumno1.resultado()
