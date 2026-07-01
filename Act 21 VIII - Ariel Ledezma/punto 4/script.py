"""
4-
Se tiene que cargar los votos obtenidos por tres candidatos a una elección.
En una lista cargar en el primer componente el nombre del candidato y en la
segunda componente cargar una lista con componentes de tipo tupla con el
nombre de la provincia y la cantidad de votos obtenidos en dicha provincia.
Se deben cargar los datos por teclado.
1) Función para cargar todos los candidatos, sus nombres y las provincias con los
votos obtenidos.
2) Imprimir el nombre del candidato y la cantidad total de votos obtenidos en todas
las provincias.
"""

def cargar_candidatos():
    candidatos = []

    for i in range(3):
        nombre = input("Nombre del candidato: ")
        provincias = []

        cantidad = int(input("¿Cuántas provincias cargará?: "))

        for j in range(cantidad):
            provincia = input("Nombre de provincia: ")
            votos = int(input("Cantidad de votos: "))
            provincias.append((provincia, votos))

        candidatos.append([nombre, provincias])

    return candidatos


def total_votos(candidatos):
    for candidato in candidatos:
        total = 0

        for provincia in candidato[1]:
            total += provincia[1]

        print("Candidato:", candidato[0])
        print("Total votos:", total)

candidatos = cargar_candidatos()
total_votos(candidatos)


