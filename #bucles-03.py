"""
Escriba un programa que pregunte cuántos números se van a introducir, pida
esos números, y escriba el mayor, el menor y la media aritmética."""

numeros = []

r = int(input("Cuantos numeros vas a ingresar--->"))

def promedio(datos):
    sumatoria = sum(datos)

    longitud = float(len(datos))
    
    resultado = sumatoria / longitud
    print('El promeio es: ', resultado)
    

for i in range(r):
    n = int(input("Ingrese el un número---->"))
    numeros.append(n)
    
promedio(numeros)    
max_item = max(numeros)
min_item = min(numeros)

print(f"El mayor es: {max_item}")
print(f"El menor es: {min_item}")

