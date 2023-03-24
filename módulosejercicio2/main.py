import time

hora_actual = time.localtime().tm_hour
minuto_actual = time.localtime().tm_min

minutos_restantes = 0

if hora_actual >= 19:
    print("¡Hora de ir a casa!")
else:
    minutos_restantes = (19 - hora_actual) * 60 - minuto_actual
    print(f"Todavía quedan {minutos_restantes} minutos de trabajo.")
