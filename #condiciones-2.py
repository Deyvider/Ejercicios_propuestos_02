"""
Mejora el programa anterior haciendo que tenga en cuenta que no se puede
dividir por cero."""

while True:
    try:
        a = int(input("Ingrese el primer numero----> "))
    except ValueError:
        print("Debes escribir un numero")
        continue
    if a == 0:
        print("No debe ser 0")
        continue    

    try:
        b = int(input("Ingrese el segundo numero-----> "))
    except ValueError:
        print("Debes escribir un numero")
        continue
    if b == 0:
        print("No debe ser 0")
        continue    
    
    m = a%b 
    if m == 0:
        print("Su division es exacta ")
    else:
        print("Su division NO es exacta ")

