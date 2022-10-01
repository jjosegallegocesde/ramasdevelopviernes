def sumar(numero1,numero2): #Declarando la funcion
    return numero1 + numero2

suma = sumar(2,3)#invocando la funcion
print(suma)



#funciones lambda
#simplemente otra forma de escribir una funcion

sumarNumeros = lambda numero3,numero4:numero3+numero4

suma = sumarNumeros(2,3)#invocando la funcion
print(suma)

Saludar = lambda : print("Hola")

Saludar()