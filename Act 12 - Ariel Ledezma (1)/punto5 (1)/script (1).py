#Realizar un programa que lea los lados de n triángulos, e informar:
#a. De cada uno de ellos, qué tipo de triángulo es: equilátero (tres lados iguales), isósceles (dos lados iguales), o escaleno (ningún lado igual)
#b. Cantidad de triángulos de cada tipo.


cantidad = int(input("¿Cuántos triángulos desea ingresar?: "))

equilatero = 0
isosceles = 0
escaleno = 0

for i in range(cantidad):

    print("Triángulo", i + 1)

    lado1 = int(input("Ingrese lado 1: "))
    lado2 = int(input("Ingrese lado 2: "))
    lado3 = int(input("Ingrese lado 3: "))

    if lado1 == lado2 and lado1 == lado3:
        print("Es un triángulo equilátero")
        equilatero += 1

    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Es un triángulo isósceles")
        isosceles += 1

    else:
        print("Es un triángulo escaleno")
        escaleno += 1

print("Cantidad de equiláteros:", equilatero)
print("Cantidad de isósceles:", isosceles)
print("Cantidad de escalenos:", escaleno)


