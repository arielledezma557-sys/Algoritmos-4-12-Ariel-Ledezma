#3. Se registran los nombres de 5 atletas y sus tiempos (en segundos) en una
#carrera de 100 metros. El programa debe cargar los datos en dos vectores
#paralelos, calcular y mostrar el promedio de los tiempos, mostrar el nombre del
#atleta con mejor y peor tiempo, y mostrar los nombres de quienes superaron el
#promedio.

atletas = []
tiempos = []

suma = 0

for i in range(5):
    nombre = input("Ingrese el nombre del atleta: ")
    tiempo = float(input("Ingrese el tiempo en segundos: "))
    atletas.append(nombre)
    tiempos.append(tiempo)
    suma += tiempo

promedio = suma / 5
mejortiempo = min(tiempos)
peortiempo = max(tiempos)

print("Resultados")
print("Promedio de tiempos:", promedio)
print("Mejor tiempo:")

for i in range(5):
    if tiempos[i] == mejortiempo:
        print(atletas[i], " ", tiempos[i])

print("Atletas que superaron el promedio:")
for i in range(5):
    if tiempos[i] == peortiempo:
        print(atletas[i], " ", tiempos[i])

print("Peor tiempo:")
for i in range(5):
    if tiempos[i] < promedio:
        print(atletas[i], " ", tiempos[i])



