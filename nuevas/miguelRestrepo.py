""" Declarando la funcion """
def sumar(numero1, numero2): 
    return numero1 + numero2

""" invocando la funcion """
resultado=sumar(1,1)

print(resultado)

#funciones lambda
#Simplemente otra forma de escribir una funcion
#la funcion lambda solo se escribe en una linea

sumarNumeros= lambda numero1, numero2: numero1+numero2
resultado=sumarNumeros(1,1)

print(resultado)


