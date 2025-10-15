while True:
    try:
        celsius = int(input("Introduzca los grados: "))
    except ValueError:
        print("Tipo de dato incorrecto")
    conversion = input("Introduce el tipo d grados al que deseas convertirlo(Kelvin) k/f (Fahrenheit): ")
    if conversion == "k":
        print(f"La temperatura en kelvin es {celsius + 273.15}")
        break
    elif conversion == "f":
        print(f"La temperatura en fahrenheit es {(celsius + 9/5) + 32}")
        break
    else:
        print("Opción incorrecta")
    
