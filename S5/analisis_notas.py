# Pedimos la lista de notas al usuario como un string
entrada = input("Introduce las calificaciones separadas por comas: ")

notas_str = [nota.strip() for nota in entrada.split(',')]

notas = []
for n in notas_str:
    try:
        nota = float(n)
        if 0 > nota or nota > 10:
            print(f"Nota {nota} descartada. Las notas introducidas deben estar entre 0 y 10.")
            continue
        notas.append(nota)
    except ValueError:
        print(f"\nValor inválido encontrado y descartado: '{n}'")

# Media, máxima y minima
total_notas = len(notas)
media = round(sum(notas) / total_notas, 2) if total_notas > 0 else 0
nota_min = min(notas) if total_notas > 0 else 0
nota_max = max(notas) if total_notas > 0 else 0

# Porcentajes de aprobados y sobresalientes
aprobados = len([n for n in notas if n >= 5])
sobresalientes = len([n for n in notas if n >= 9])

# Contar manualmente cuántas veces aparece cada nota
# {clave:valor}
frecuencias = {}
for nota in notas:
    if nota in frecuencias:
        frecuencias[nota] += 1
    else:
        frecuencias[nota] = 1

# Buscar la frecuencia máxima
max_repeticiones = max(frecuencias.values()) if frecuencias else 0

# Buscar todas las notas que tienen esa frecuencia máxima (puede haber empate)
modas = [nota for nota, rep in frecuencias.items() if rep == max_repeticiones]

# Porcentajes
porc_aprobados = round((aprobados / total_notas) * 100, 2) if total_notas > 0 else 0
porc_sobresalientes = round((sobresalientes / total_notas) * 100, 2) if total_notas > 0 else 0

# Mensaje final según la media
if media >= 8:
    mensaje = "Nivel excelente"
elif 5 <= media < 8:
    mensaje = "Nivel medio"
else:
    mensaje = "Necesita refuerzo"

# Mostrar resultados
print("\n--- Resumen estadístico ---")
print(f"Número total de notas: {total_notas}")
print(f"Media: {media}")
print(f"Nota mínima: {nota_min}")
print(f"Nota máxima: {nota_max}")
print(f"Moda: {modas}")
print(f"Porcentaje de aprobados (≥5): {porc_aprobados}%")
print(f"Porcentaje de sobresalientes (≥9): {porc_sobresalientes}%")
print(f"Mensaje final: {mensaje}")