#Declarando la función 
def sumar(numero1, numero2):
    return numero1+ numero2

#Invocando la funcion
resultado=sumar(1,1)
print(resultado)

#funciones lambda
#simplemente otra forma de escribir una funcion 

sumarNumeros= lambda numero1, numero2: numero1 + numero2

resultado=sumarNumeros (1,2)
print(resultado)
