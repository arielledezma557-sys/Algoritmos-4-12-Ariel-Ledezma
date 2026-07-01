"""""
2. Se desea saber la temperatura media trimestral de cuatro países. Para ello se
tiene como dato las temperaturas medias mensuales de dichos países. Se debe
ingresar el nombre del país y seguidamente las tres temperaturas medias
mensuales.
Seleccionar las estructuras de datos adecuadas para el almacenamiento de los
datos en memoria.

● Cargar por teclado los nombres de los países y las temperaturas
medias mensuales.
● Imprimir los nombres de los países y las temperaturas medias
mensuales de las mismas.
● Calcular la temperatura media trimestral de cada país.
● Imprimir los nombres de los países y las temperaturas medias
trimestrales.
● Imprimir el nombre del país con la temperatura media trimestral
mayor.
"""""

paises = []
temperaturas = []

for i in range(4):
    nombre = input("Ingrese nombre del país: ")
    paises.append(nombre)

    temps = []
    for j in range(3):
        temp = float(input("Ingrese temperatura del mes: "))
        temps.append(temp)

    temperaturas.append(temp)

print("Países y temperaturas mensuales:")

for i in range(4):
    print(paises[i], temperaturas[i])

print("Temperaturas medias trimestrales:")

promedios = []

for i in range(4):
    promedio = float(temperaturas[i]) / 3
    promedios.append(promedio)
    print(paises[i], "  ", promedio)

mayor = promedios[0]
posicion = 0

for i in range(1, 4):
    if promedios[i] > mayor:
        mayor = promedios[i]
        posicion = i

print("país con mayor temperatura media trimestral:")
print(paises[posicion], " ", mayor)


