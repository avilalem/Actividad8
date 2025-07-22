def factorial(n):
    if n == 0:
       return 1
    else:
        print(n)
        return n*factorial(n-1)
n=int(input("Ingrese un numero: "))
factorial(n)
print(f"El factorial es: {factorial(n)}")
#########

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

base=int(input("Ingrese una base: "))
exponente=int(input("Ingrese una exponente: "))

print(f"La potencia es: {potencia(base, exponente)}")
