#Se ingresan un conjunto de n alturas de personas por teclado. Mostrar la altura promedio de las personas.

suma=0
cantidad=int(input("ingresa la cantidad de las perosnas:"))
for Y in range(cantidad):
    altura=int(input("ingrese la alturas de las personas:"))
    suma+=altura
    
    promedio=altura/cantidad
print("Mostrar la altura promedio de las personas es:", altura/cantidad)

