#Declarando la función
def sumarNumeros(numero1,numero2):
    return numero1 + numero2

#Impriendo la función
print(sumarNumeros(12,3))

#FUNCIONES LAMBDA - OTRA FORMA DE ESCRIBIR UNA FUNCIÓN 
sumar_numeros = lambda number1,number2: number1 + number2

print(sumar_numeros(2,3))