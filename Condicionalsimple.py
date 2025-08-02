"""
las condicionales tiene estructuras simples y compuestas
ejemplo. if numero%2==0: par else impar
numero=0--- el valor del numero es cero
numero==0 --- el numero tiene como residuo un  cero se cuando es una condicion
numero===0-- tanto la variable numero como cero son del mismo tipo de datos.
if condicion:

"""
# ingresar y determina si el numero es par o impar
numero=float(input("Ingrese un numero :"))
if numero%2==0:
    print(f" El {numero} es par")
else:
    print(f" El {numero} es Impar")
print("-------------------------------------------")
# ingresar numero y determinar si es multiplo de 5 o no es
numero=int(input("Ingrese un numero :"))
if numero%5==0:
    print(f"El {numero} es Multiplo de 5")
else:
    print(f"El {numero} no es multiplo de 5")
# ingesar nombre y edad y determinar si la persona es mayor de edad o menor
print("---------------------------------------------")
nombre=input("Ingrese el nombre de la persona :")
edad=int(input("Ingrese  la edad persona :"))
if edad>=18:
    print(f"{nombre} tiene {edad} es mayor de edad")
else:
    print(f"{nombre} tiene {edad} es menor de edad")
