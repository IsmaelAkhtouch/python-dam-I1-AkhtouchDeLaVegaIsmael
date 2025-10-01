from datetime import datetime

def pedir_nombre_y_anio_nacimiento():
    anio_actual = datetime.now().year
    nombre = input("Introduzca su nombre: ")

    try:
        anio_nacimiento = int(input("Introduce tu año de nacimiento: "))
    except ValueError:
        print("Debes introducir un número")
        return
    
    edad = anio_actual - anio_nacimiento
    if edad < 0:
        raise ValueError("Tu año de nacimiento no puede ser mayor al año actual")
    
    elif edad < 18:
        print("Te llamas",nombre,"y eres un niño")

    elif edad < 66:
        print("Te llamas",nombre," y eres un adulto")

    else:
        print("Te llamas",nombre," y eres un anciano")
        
    return

print(f"\n{'*'*100}")
pedir_nombre_y_anio_nacimiento()
print(f"{'*'*100}")