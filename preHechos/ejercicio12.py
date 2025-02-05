#se define una función que recibe un entero como parametro
def es_primo(numero):
 if numero < 2:
    # si el numero es menor a 2, no es primo 
    return False
# recorre los numeros desde 2 hasta el numero
 for i in range(2, numero): 
    if numero % i == 0:
        # si el numero es divisible por i, no es primo
        return False
    # si no se cumple la condición anterior, el numero es primo
    return True

#imprime el resultado de la función es_primo con los siguientes argumentos
print(es_primo(11)) # True
print(es_primo(4)) # False