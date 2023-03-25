import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('alumnos.db')

# Crear la tabla Alumnos
conn.execute('''CREATE TABLE Alumnos
                (id INTEGER PRIMARY KEY,
                 nombre TEXT,
                 apellido TEXT);''')

# Insertar 8 alumnos
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("Eduardo", "Madrigal"))
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("Luis", "Loaeza"))
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("Juan", "Ochoa"))
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("Tanya", "Ceballos"))
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("David", "Ruiz"))
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("Laura", "Mendoza"))
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("Brenda", "Olincan"))
conn.execute("INSERT INTO Alumnos (nombre, apellido) VALUES (?, ?)", ("Ana", "Leyva"))

# Guardar los cambios
conn.commit()

# Buscar un alumno por nombre
nombre_buscado = input("Introduce el nombre del alumno a buscar: ")
cursor = conn.execute("SELECT * FROM Alumnos WHERE nombre = ?", (nombre_buscado,))
for fila in cursor:
    print(f"ID: {fila[0]}")
    print(f"Nombre: {fila[1]}")
    print(f"Apellido: {fila[2]}")

# Cerrar la conexión a la base de datos
conn.close()
