"""Escribe un programa que pida dos números y que conteste cuál es el menor y
cuál el mayor o que escriba que son iguales."""

a = int(input("Inrese el numero A ----> "))
b= int(input("Ingrese el numero B-----> "))

if a == b:
    print("Su numeros son Iguales")
if a<b :
    print(f"El numero {a} es Menor y el {b} es Mayor")
if b<a:
    print(f"El numero {b} es Menor y el {a} es Mayor")