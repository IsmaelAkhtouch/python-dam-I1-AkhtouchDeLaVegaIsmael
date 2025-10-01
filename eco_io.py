while True:
    try:
        num1 = int(input("Introduce el primer número: "))
        num2 = int(input("Introduce el segundo número: "))
        num3 = int(input("Introduce el tercer número: "))
        suma = num1 + num2 + num3

        print(f"La suma de los 3 números es: {suma}.\nLa media es {suma/3}.\nEl mayor es {max(num1,num2,num3)}.\nEl menor es {min(num1,num2,num3)}.")
        break
    except ValueError:
        print("Debes introducir un número")
        continue