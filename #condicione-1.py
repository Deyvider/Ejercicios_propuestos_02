"""Escribe un programa que pida dos números 
enteros y que calcule su división,
escribiendo si la división es exacta o no."""

a = int(input("Ingrese el primer numero ---->  "))

b = int(input("Ingrese el segundo numero ---->"))

m = a%b

if m == 0:
    print("Su division es exacta ")
else:
    print("Su division NO es exacta ")
