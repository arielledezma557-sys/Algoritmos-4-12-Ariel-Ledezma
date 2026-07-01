"""""
4. Plantear una función que reciba un string en mayúsculas o minúsculas y
retorne la cantidad de letras &#39;a&#39; o &#39;A&#39;.
"""""

def contar_a(cadena):
    cantidad = 0

    for caracter in cadena:
        if caracter == 'a' or caracter == 'A':
            cantidad += 1

    return cantidad

texto = input("Ingrese un texto: ")

resultado = contar_a(texto)

print("Cantidad de letras 'a' o 'A':", resultado)




