#Realizar un programa que solicite la carga por teclado de dos números, si el primero es mayor al segundo informar su suma y diferencia, en caso contrario informar el producto y la división del primero respecto al segundo.

num1=int(input("ingrese el primero valor:"))
num2=int(input("ingrese el segundo valor:"))
suma = num1+num2
producto=num1*num2
div=num1/num2
print("la suma de los dos valores es", suma)
print("el producto de los dos valores es", producto)
print("la division de los dos valores es", div)
