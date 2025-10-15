numero = int(input("Introduce un número: "))

if numero <= 1:
    print(f"El numero {numero} no es primo")
if numero == 2:
    print(f"El numero {numero} es primo")
if numero % 2 == 0:
    print(f"El numero {numero} no es primo")
for i in range(3, int(numero**0.5) + 1, 2):
    if numero % i == 0:
        print(f"El numero {numero} no es primo")
print(f"El numero {numero} es primo")

