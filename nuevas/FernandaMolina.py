#declarando la funcion
def sumar(numero1, numero2):
  return numero1 + numero2

#las funciones se declaran y se llaman
#invocando la funcion
resultado=sumar(2,7)
print (resultado)

#FUNCIONES LAMBDA
#Simplemente otra forma de escribir una funcion
sumar_numeros = lambda numero1,numero2: numero1+numero2
resultado=sumar_numeros(2,7)
print (resultado)
