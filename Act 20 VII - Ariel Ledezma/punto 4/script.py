"""
4. Confeccionar una función que reciba una serie de edades y me retorne la
cantidad que son mayores o iguales a 18 (como mínimo se envía un entero
a la función)
"""
def mayores_edad(*edades):
    contador = 0

    for edad in edades:
        if edad >= 18:
            contador += 1

    return contador

print("Mayores de edad:", mayores_edad(12, 18, 25, 30, 16, 20))

