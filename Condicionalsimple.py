def par_impar():
    numero = float(input("Ingrese un número: "))
    if numero % 2 == 0:
        print(f"El {numero} es par")
    else:
        print(f"El {numero} es impar")

def multiplo_de_5():
    numero = int(input("Ingrese un número: "))
    if numero % 5 == 0:
        print(f"El {numero} es múltiplo de 5")
    else:
        print(f"El {numero} no es múltiplo de 5")

def mayor_o_menor():
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    if edad >= 18:
        print(f"{nombre} tiene {edad} años y es mayor de edad")
    else:
        print(f"{nombre} tiene {edad} años y es menor de edad")

# Menú principal
while True:
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Determinar si un número es par o impar")
    print("2. Determinar si un número es múltiplo de 5")
    print("3. Determinar si una persona es mayor o menor de edad")
    print("4. Salir")

    opcion = input("Seleccione una opción (1-4): ")

    if opcion == "1":
        par_impar()
    elif opcion == "2":
        multiplo_de_5()
    elif opcion == "3":
        mayor_o_menor()
    elif opcion == "4":
        print("Gracias por usar el programa. ¡Hasta luego!")
        break
    else:
        print("Opción no válida. Intente de nuevo.")
