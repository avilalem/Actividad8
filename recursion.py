def factorial(n):
    if n == 0:
       return 1
    else:
        return n*factorial(n-1)

def suma_naturales(n):
    if n == 0:
        return 0
    else:
        return n + suma_naturales(n-1)

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def letras(palabra, letra):
    if palabra=="":
        return 0
    if palabra[0]== letra:
        return 1+letras(palabra[1:], letra)
    else:
        return letras(palabra[1:], letra)

def voltear_palabra(palabra):
    if palabra=="":
        return ""
    else:
        return voltear_palabra(palabra[1:])+palabra[0]

def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

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
        opcion=input("Seleccione una opcion: ")
        if opcion=="1":
            n=int(input("Ingresa el numero: "))
            expresion = " * ".join(str(i) for i in range(1, n + 1))
            print(expresion)
            print(f"El factorial de {n} es: {factorial(n)}")
        elif opcion=="2":
            n=int(input("Ingresa el numero: "))
            print(f"La suma de los primeros {n} numeros es: {suma_naturales(n)}")
        elif opcion=="3":
            n=int(input("Ingresa el numero: "))
            print(f"El numero {n} de la secuencia es: {fibonacci(n)}")
        elif opcion=="4":
            palabra=input("Ingresa la palabra: ")
            letra=input("Ingresa la letra: ")
            resultado=letras(palabra, letra)
            if resultado==0:
                print(f"La letra {letra} no aparece en {palabra}")
            print(f"La letra {letra} aparece: {resultado} veces en {palabra}")
        elif opcion=="5":
            palabra=input("Ingresa la palabra: ")
            invertida=voltear_palabra(palabra)
            print(f"La palabra invertida es: {invertida}")
        elif opcion=="6":
            base=int(input("Ingresa la base: "))
            exponente=int(input("Ingresa el exponente: "))
            print(f"{base} elevado a la {exponente} es: {potencia(base, exponente)}")
        elif opcion=="7":
            print("Gracias por usar el programa")
            break
        else:
            print("Opcion invalida")

menu()