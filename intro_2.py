print("Bienvenidos a la calculadora 2.0")
print("escribe salir para salir")
print("elige suma,resta, div, multi")


result = ""

while True:
    if not result:
        result = input("ingresa el numero: ")
        if result.lower() == "salir":
            break
        result = int(result)
    op = input("ingresa una operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa el siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        result += n2
    elif op.lower() == "resta":
        result -= n2
    elif op.lower() == "div":
        result /= n2
    elif op.lower() == "multi":
        result *= n2
    else:
        print("Operacion no valida")
        break
    print(f"el resultado es : {result}")
