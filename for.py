# con indice
for numbers in range(5):
    print(numbers)

# con indice y final
for numbers_two in range(0, 11):
    print(numbers_two)

# con una busqueda de un numero
found = 11
for numero in range(21):
    print(numero)
    if numero == found:
        print("Encontrado")
        break
    else:
        print("No fue encontrado el numero")


for k in range(3):
    for j in range(2):
        print(f"{k} , {j}")
