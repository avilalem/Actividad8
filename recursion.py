def factorial(n):
    if n == 0:
       return 1
    else:
        return n*factorial(n-1)
    n = int(input("Ingrese un numero: "))
    factorial(n)
    print(f"El factorial es: {factorial(n)}")

def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n-1)
    n = int(input("Ingrese un numero: "))
    print(f"La suma naturales es: {suma_naturales(n)}")

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    n = int(input("Ingrese un numero: "))
    print(f"El numero de la secuencia fibonacci #{n} es: {fibonacci(n)}")

def letras(palabra, letra):
    if palabra=="":
        return 0
    if palabra[0]== letra:
        return 1+letras(palabra[1:], letra)
    else:
        return letras(palabra[1:], letra)
    palabra=input("Ingrese un palabra: ")
    letra=input("Ingrese un letra: ")
    resultado=letras(palabra, letra)
    print(f"La letra {letra} aparece: {resultado} veces en {palabra}")

def voltear_palabra(palabra):
    if palabra=="":
        return 0


def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

    base=int(input("Ingrese una base: "))
    exponente=int(input("Ingrese una exponente: "))
    print(f"La potencia es: {potencia(base, exponente)}")



def menu():
    while True:
        print("___MENU___")
        print("1. Factorial")
        print("2. Suma de los primeros N numeros naturales")
        print("3. Enesimo numero Fibonacci")
        print("4. Cuantas veces aparece una letra en una palabra")
        print("5. Invertir cadena de texto")
        print("6. Exponencia")
        print("7. Salir")