#5. Crear y cargar en un lista los nombres de 5 países y en otra lista paralela
#la cantidad de habitantes del mismo. Ordenar alfabéticamente e imprimir
#los resultados. Por último ordenar con respecto a la cantidad de habitantes
#(de mayor a menor) e imprimir nuevamente.

paises = []
habitantes = []

for i in range(5):
    pais = input("Ingrese el nombre del país: ")
    cantidad = int(input("Ingrese la cantidad de habitantes: "))

    paises.append(pais)
    habitantes.append(cantidad)

for i in range(4):
    for j in range(i + 1, 5):

        if paises[i] > paises[j]:

            auxpais = paises[i]
            paises[i] = paises[j]
            paises[j] = auxpais

            auxhabitantes = habitantes[i]
            habitantes[i] = habitantes[j]
            habitantes[j] = auxhabitantes

print("Ordenados alfabéticamente:")

for i in range(5):
    print(paises[i], "-", habitantes[i])

for i in range(4):
    for j in range(i + 1, 5):

        if habitantes[i] < habitantes[j]:

            auxhabitantes = habitantes[i]
            habitantes[i] = habitantes[j]
            habitantes[j] = auxhabitantes

            auxpais = paises[i]
            paises[i] = paises[j]
            paises[j] = auxpais

print("Ordenados por habitantes:")

for i in range(5):
    print(paises[i], "-", habitantes[i])


