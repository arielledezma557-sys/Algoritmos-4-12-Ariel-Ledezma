"""
3. Confeccionar una función que reciba entre 2 y 5 enteros. La misma nos
debe retornar la suma de dichos valores. Debe tener tres parámetros por
defecto.
"""

def sumar(a, b, c=0, d=0, e=0):
    return a + b + c + d + e

print(sumar(5, 8))
print(sumar(5, 8, 2))
print(sumar(5, 8, 2, 6))
print(sumar(5, 8, 2, 6, 1))


