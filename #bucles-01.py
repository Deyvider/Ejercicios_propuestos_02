"""
1.- Escribe una función que reciba una lista de 6 números enteros ingresados por
teclado e imprima cuales son pares, impares y a su vez si son primos o no.
al final retorna la suma de todos los números."""

numeros = []
pares = []
impares = []
primos = []
sumar = []
def primo(num):
    for n in range(2, num):
        if num % n == 0:
            print("No es primo", n, "es divisor")
            return False
    print("Es primo")
    primos.append(nn)
    return True

def sumalista(listaNumeros):
    laSuma = 0
    for i in listaNumeros:
        laSuma = laSuma + i
    return laSuma

for i in range(6):
    nn = int(input("Ingrese un numero---> "))
    if nn % 2 == 0:
        pares.append(nn)
    else:
        impares.append(nn)
    primo(nn)
    numeros.append(nn)
    primo(nn)
    sumar.append(nn)
    

print(f"Los numeros pares son: {pares}")

print(f"Los numeros impares son: {impares}")

print(f"Los numeros Primos son: {primos}")

print(f"La suma es: {sumalista(sumar)}")