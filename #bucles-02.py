"""Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números y escriba cuántos negativos ha introducido."""

cont = 0
r = int(input("Cuantos numeros vas a ingresar"))

for i in range(r):
    n = int(input("Ingrese el un número"))
    if n < 0:
        cont += 1
print(f"Tienes {cont} numeros negativos")