#Usando un if, crear una condición que compare si la variable numeroIf es positivo, negativo, o 0.
#Pista: Los números inferiores a 0 son negativos y los superiores, positivos.

numeroIf = 4

if numeroIf > 0:
    print("El número es positivo")
elif numeroIf < 0:
    print("El número es negativo")
else:
    print("El número es cero")

#Crea un bucle While, este bucle tendrá que tener como condición que la variable numeroWhile sea inferior a 3, el bloque de código que tendrá el bucle deberá:

#Incrementar el valor de la variable en uno cada vez que se ejecute.

#Mostrarlo por pantalla cada vez que se ejecute.

numeroWhile = 0

while numeroWhile < 3:
    numeroWhile += 1
    print(numeroWhile)

#Para el bucle Do While, deberás crear la misma estructura que en el While, pero solo se debe ejecutar una vez.
#Comentario: En Python no hay una estructura do-while como tal, pero se puede simular usando un bucle while y una condición que siempre se cumpla en la primera iteración.

numeroDoWhile = 0

while True:
    numeroDoWhile += 1
    print(numeroDoWhile)
    if numeroDoWhile >= 3:
        break

#Para el bucle For, crea una variable numeroFor, esta variable tendrá como valor 0 y su condición será que la variable sea igual o menor que 3, se irá incrementando en 1 su valor cada vez que se ejecute y deberá mostrarse por pantalla.

for numeroFor in range(4):
    print(numeroFor)

#Por último, para el Switch, deberás crear la variable estacion, y distintos case para las cuatro estaciones del año. Dependiendo del valor de la variable estacion se deberá mandar un mensaje por consola informando de la estación en la que está. También habrá que poner un default para cuando el valor de la variable no sea una estación.
#Comentario: En Python no hay una estructura switch como tal, pero se puede simular usando un diccionario y una función que devuelve el valor correspondiente al caso que se esté evaluando.

def switch(estacion):
    estaciones = {
        "invierno": "La estación es invierno",
        "primavera": "La estación es primavera",
        "verano": "La estación es verano",
        "otoño": "La estación es otoño"
    }

    if estacion in estaciones:
        return estaciones[estacion]
    else:
        return "No es una estación"


estacion = "otoño"
print(switch(estacion))

estacion = "cualquiera"
print(switch(estacion))

