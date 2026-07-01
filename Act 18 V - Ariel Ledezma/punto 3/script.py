"""""
3. Confeccionar una función que calcule la superficie de un rectángulo y la
retorne, la función recibe como parámetros los valores de dos de sus lados:
def retornar_superficie(lado1,lado2):
En el bloque principal del programa cargar los lados de dos rectángulos y
luego mostrar cuál de los dos tiene una superficie mayor.
"""""

def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

print("Rectángulo 1")
lado1 = float(input("Ingrese lado 1: "))
lado2 = float(input("Ingrese lado 2: "))

print("Rectángulo 2")
lado3 = float(input("Ingrese lado 1: "))
lado4 = float(input("Ingrese lado 2: "))

superficie1 = retornar_superficie(lado1, lado2)
superficie2 = retornar_superficie(lado3, lado4)

print("Superficie del rectángulo 1:", superficie1)
print("Superficie del rectángulo 2:", superficie2)

if superficie1 > superficie2:
    print("El rectángulo 1 tiene mayor superficie.")

elif superficie2 > superficie1:
    print("El rectángulo 2 tiene mayor superficie.")

else:
    print("Los dos rectángulos tienen la misma superficie.")


