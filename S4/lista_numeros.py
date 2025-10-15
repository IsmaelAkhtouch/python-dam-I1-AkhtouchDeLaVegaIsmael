
try:
    cadena = input("Introduce los números divididos por comas: ")
    numeros = [float(i.strip()) for i in cadena.split(",")]
    duplicados = set( [ num for num in numeros if numeros.count(num)>1] )

    print(f"Suma: {sum(numeros)}")
    print(f"Media: {sum(numeros) / len(numeros)}")
    print(f"Número más alto: {max(numeros)}")
    print(f"Números que se han duplicado: {"No hay duplicados" if len(duplicados) == 0 else duplicados }")
except:
    ValueError()

