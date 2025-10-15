texto = input("Introduce una cadena de texto: ")    
vocales = "aeiouAEIOU"
contador_vocales = 0
contador_consonantes = 0
contador_mayusculas = 0
total_caracteres = 0

for char in texto:
    if char.isalpha():
        total_caracteres += 1
        if char in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1
        if char.isupper():
            contador_mayusculas += 1



print(f"Vocales: {contador_vocales}")
print(f"Consonantes: {contador_consonantes}")
print(f"Mayúsculas: {contador_mayusculas}")
print(f"Total de caracteres: {total_caracteres}")