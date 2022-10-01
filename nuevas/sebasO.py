# Declarando la funcion
def sumar(numUno, numDos):
    return numUno+numDos

# Llamar la funcion ingresandola en una variable
res = sumar(5,5)

# Imprimir la variable con el resultado
print(res)

# Funciones Lambda, otra forma de escribir una funcion
sumarNumeros = lambda numeroUno, numeroDos:numeroUno+numeroDos
res = sumarNumeros(10,5)
print(res)