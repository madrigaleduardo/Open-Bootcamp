# Pedir al usuario su peso en kg y su estatura en metros
peso = float(input("Ingresa tu peso en kg: "))
estatura = float(input("Ingresa tu estatura en metros: "))

# Calcular el índice de masa corporal (IMC)
imc = peso / (estatura ** 2)

# Redondear el valor del IMC a dos decimales
imc_redondeado = round(imc, 2)

# Mostrar el valor del IMC al usuario
print("Tu índice de masa corporal es", imc_redondeado)
