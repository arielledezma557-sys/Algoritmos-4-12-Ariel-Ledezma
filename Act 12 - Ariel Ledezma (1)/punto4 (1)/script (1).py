#Se realiza la carga de 10 valores enteros por teclado. Se desea conocer:
#a. La cantidad de valores ingresados negativos.
#b. La cantidad de valores ingresados positivos.
#c. La cantidad de múltiplos de 15.
#d. El valor acumulado de los números ingresados que son pares.


negativos=0
positivo=0
multiplo=0
pares=0

for i in range(10):
    numeros=int(input("ingresa en valores:"))

    if numeros<=0:
         negativos = negativos +1
 
    if numeros>=0:
         positivo = positivo +1

    if numeros % 15 ==0:
         multiplo = multiplo +1

    if numeros:
         pares = pares + numeros   

print("valores negativos ingresados:", negativos)
print("valores ingresados positivos:", positivo)
print("valor con multiplo de 15:", multiplo)
print("valores acumulados pares:", pares)



