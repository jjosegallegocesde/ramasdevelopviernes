def sumar (numero1,numero2): #Declarar la funcion
    return (numero1+numero2)

resultado=sumar(1,1) #Invoncando la funcion
print(resultado)

#Funciones lambda
#Simplemente otra forma de escribir una funcion
sumar_numeros = lambda numero1,numero2:numero1+numero2

resultado=sumar_numeros(2,2) #Invoncando la funcion
print(resultado)