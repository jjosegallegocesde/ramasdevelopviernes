# Declarando la función

def sumar(numero1,numero2):
    return numero1 + numero2

# Invocando la función    

resultado = sumar(2,4)

print(resultado)

# Funciones lambda

sumarNumeros = lambda numero1,numero2: numero1 + numero2

resultado = sumarNumeros(2,7)

print(resultado)