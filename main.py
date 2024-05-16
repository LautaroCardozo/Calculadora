from funciones import *
import os 

calcular = True

while calcular:
    interfaz()
    opcion =pedir_opcion()
    match opcion:
        case "1":
            a = pedir_numero("Ingrese el primer sumando")
            b = pedir_numero("Ingrese el segundo sumando")
            limpiar_terminal()
            print(f"La suma entre {a} y {b} da como resultado {sumar(int(a),int(b))}")
            esperar_usuario()
            limpiar_terminal()
        case "2": 
            a = pedir_numero("Ingrese el minuendo")
            b = pedir_numero("Ingrese el sustraendo")
            limpiar_terminal()
            print(f"La resta entre {a} y {b} da como resultado {restar(int(a),int(b))}")
            esperar_usuario()
            limpiar_terminal()
        case "3": 
            a = pedir_numero("Ingrese el multiplicando")
            b = pedir_numero("Ingrese el multiplicador")
            limpiar_terminal()
            print(f"La multiplicacion entre {a} y {b} da como resultado {multiplicar(int(a),int(b))}")
            esperar_usuario()
            limpiar_terminal()
        case "4": 
            a = pedir_numero("Ingrese el dividendo")
            b = pedir_numero("Ingrese el divisor")
            limpiar_terminal()
            try:
                print(f"la division entre {a} y {b} da como resultado {dividir(int(a),int(b))} y el resto es de {resto_division(int(a),int(b))}")
            except ZeroDivisionError:
                print("Error,no se puede dividir por cero")

            esperar_usuario()
            limpiar_terminal()
            
        case "5": 
            a = pedir_numero("Ingrese el numero a factorizar")
            limpiar_terminal()
            print(factorial(int(a)))
            esperar_usuario()
            limpiar_terminal()
            
        case "6":
            calcular = False
