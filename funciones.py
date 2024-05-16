def pedir_numero(mensaje):
    a = input(f"{mensaje}= ")
    while a.isalpha():
        a = input("Debe ingresar un numero =")
    return a
    
def esperar_usuario():
    import os
    os.system("Pause")

def limpiar_terminal():
    import os
    os.system('cls')

def sumar(a , b):
    return a+b

def restar(a , b):
    return a - b

def multiplicar (a , b):
    return a * b

def dividir(a , b):
    resultado = a / b
    return resultado
    

def resto_division(a ,b):
    resto = a % b
    return resto

def factorial(a):
    factorial = 1
    for i in range(1 , a + 1):
        factorial *= i
    return factorial

def pedir_opcion():
    opcion_elegida = input("Seleccione una opcion= ")
    return opcion_elegida

def interfaz():
    print("========== CALCULADORA ==========")
    print("1-Sumar")
    print("2-Restar")
    print("3-Multiplicar")
    print("4-Dividir")
    print("5-Factorial")