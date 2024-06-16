import math

# 1. Imprimir Nombre
def imprimir_nombre(nombre="Diego Saavedra"):
    if (__name__ == "__main__"):
        nombre = input("Ingrese su nombre: ")
        print(nombre)
    else:
        print(nombre)
        return nombre

# 2. Suma de los Números del 1 al 10
def suma_1_al_10():
    suma = sum(range(1, 11))
    print(suma)
    return suma

# 3. Datos Personales
def imprimir_datos_personales(nombre, edad, estatura):
    print("Nombre: " + nombre)
    print("Edad: " + str(edad))
    print("Estatura: " + str(estatura))

# 4. Par o Impar
def par_o_impar(numero=0):
    if numero == 0:
        num = int(input("Ingrese un número: "))
        if num % 2 == 0:
            print("par")
            return "par"
        else:
            print("impar")
            return "impar"
    else:
        if numero % 2 == 0:
            print("par")
            return "par"
        else:
            print("impar")
            return "impar"

# 5. Área de un Círculo
def area_circulo(radio):
    area = math.pi * radio ** 2
    print("Área del círculo:", area)
    return area

# 6. Suma de Dos Números
def suma(a, b):
    resultado = a + b
    print("La suma es:", resultado)
    return resultado

# 7. Área de un Círculo con Parámetro
def area_circulo_param(radio):
    area = math.pi * radio ** 2
    print("El área del círculo es:", area)
    return area

# 8. Conversión de Temperatura
def celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    print("Temperatura en Fahrenheit:", fahrenheit)
    return fahrenheit

def fahrenheit_a_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print("Temperatura en Celsius:", celsius)
    return celsius

if __name__ == "__main__":
    # Ejecución de cada ejercicio
    print("\n1. Imprimir Nombre")
    imprimir_nombre()

    print("\n2. Suma de los Números del 1 al 10")
    suma_1_al_10()

    print("\n3. Datos Personales")
    nombre = "Gabriel"
    edad = 20
    estatura = 1.6
    imprimir_datos_personales(nombre, edad, estatura)

    print("\n4. Par o Impar")
    par_o_impar()

    print("\n5. Área de un Círculo")
    radio = float(input("Ingrese el radio del círculo: "))
    area_circulo(radio)

    print("\n6. Suma de Dos Números")
    a = int(input("Ingrese el primer número: "))
    b = int(input("Ingrese el segundo número: "))
    suma(a, b)

    print("\n7. Área de un Círculo con Parámetro")
    radio = float(input("Ingrese el radio del círculo: "))
    area_circulo_param(radio)

    print("\n8. Conversión de Temperatura")
    celsius = float(input("Ingrese la temperatura en grados Celsius: "))
    celsius_a_fahrenheit(celsius)
    fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))
    fahrenheit_a_celsius(fahrenheit)
