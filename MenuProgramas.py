while True:
    print("Menu \n"
          "1) Contador ciclo del 1 a la 10 y sumar \n"
          "2) Contador cicli del 1 al 20 pares \n"
          "3) Tabla de Multiplicar con limite \n"
          "4) Descuento 20% sobre el precio del Producto \n"
          "5) Salir ")
    opcion=int(input(" Selecione una opcion(1-5) :"))
    suma=0
    if opcion==1:
        for i in range(1,11):
            print(i)
            suma+=i # suma=suma+i
        print(f"La suma es :{suma}")
    elif opcion==2:
        for i in range(0,21,2):
            print(i)
    elif opcion==3:
        tabla=int(input("Digite la tabla que desea :"))
        limite=int(input("Ingrese el limite :"))
        for i in range(1,limite+1):
            resultado=tabla*i
            print(f"{tabla}*{i}={resultado}")
    elif opcion==4:
        nombreProducto=input("Ingrese el nombre producto :")
        precio=int(input("Ingrese el precio del producto :"))
        descuento=precio*0.30
        precioFinal=precio-descuento
        print(f"{nombreProducto} tiene un descuento de {descuento}\n"
              f"un precio final de :{precioFinal}")
    elif opcion==5:
        print("Listo salio del programa ")
        break


