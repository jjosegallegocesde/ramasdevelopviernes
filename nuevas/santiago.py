def sumar(numero1,numero2): #Declarando la función
    return numero1+numero2

resultado=sumar(1,1) #Invocando la funcion
print(resultado)

#Funciones lambda
#Simplemente otra forma de escribir una funcion
sumar_numeros = lambda numero1,numero2:numero1+numero2

resultado=sumar_numeros(1,2) #Invocando la funcion
print(resultado)


