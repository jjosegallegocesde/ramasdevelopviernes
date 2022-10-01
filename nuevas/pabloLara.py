#declarando la función
def sumar(numeroUno, numeroDos):
    return numeroUno + numeroDos


""" resultado = sumar(10,10)

print(resultado)
 """
#Funciones lambda
#Simplemente es otra forma de escribir una funcion 

sumarNumeros = lambda numeroUno, numeroDos: numeroUno + numeroDos

resultado = sumarNumeros(10,10)
print(resultado)


