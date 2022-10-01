#Declarando una función 
def sumar(numero1, numero2):
    return numero1 + numero2

#Invocando la función
print(sumar(15,23))

#Funciones Lambda
#Simplemente otra forma de escribir otra función 

sumar_numeros = lambda numero1,numero2:numero1 + numero2 
print(sumar_numeros(75,23))