import pickle

class Vehiculo:
    def __init__(self, marca, modelo, year):
        self.marca = marca
        self.modelo = modelo
        self.year = year

vehiculo = Vehiculo("Ford", "Mustang", 2022)

# Guardar el objeto en un archivo
with open("vehiculo.pickle", "wb") as archivo:
    pickle.dump(vehiculo, archivo)

# Cargar el objeto desde el archivo
with open("vehiculo.pickle", "rb") as archivo:
    vehiculo_cargado = pickle.load(archivo)

print(f"Marca: {vehiculo_cargado.marca}")
print(f"Modelo: {vehiculo_cargado.modelo}")
print(f"Año: {vehiculo_cargado.year}")
