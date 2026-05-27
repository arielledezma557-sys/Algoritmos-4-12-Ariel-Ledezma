#Escribir un programa que solicite ingresar 10 notas de alumnos y nos informe cuántos tienen notas mayores o iguales a 7 y cuántos menores.

notas1=int(input("ingrese la primera nota:"))
notas2=int(input("ingrese la segunda nota:"))
notas3=int(input("ingrese la tercera nota:"))
notas4=int(input("ingrese la cuarta nota:"))
notas5=int(input("ingrese la quinta nota:"))
notas6=int(input("ingrese la sexta nota:"))
notas7=int(input("ingrese la septima nota:"))
notas8=int(input("ingrese la octava nota:"))
notas9=int(input("ingrese la novena nota:"))
notas10=int(input("ingrese la decima nota:"))

notas=[notas1,notas2,notas3,notas4,notas5,notas6,notas7,notas8,notas9,notas10]

mayor=0
menor=0

for i in notas:
    if i >= 7:
          mayor +=1
    else: 
       menor += 1

print("Algunas notas con mayor o igual a 7:", mayor)
print("algunas notas con menor a 7:", menor)

