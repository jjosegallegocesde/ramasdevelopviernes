def sumar_num (numero1, numero2):
   #declarando la función
    return numero1,numero2

resultado=sumar_num(1,2) # invocando la funcion    
print(resultado) 

#funciones lambda
#simplemente otra forma de escribir una funcion 

sumar_numeros = lambda numero1,numero2: numero1+numero2

resultado=sumar_numeros(1,2) # invocando la funcion
print(resultado)