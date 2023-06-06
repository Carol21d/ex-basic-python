""" INTRODUCCION A PYTHON"""
number_1 = input("ingresa el primer numero: ")
number_2 = input("ingresa el segundo numero: ")
number_1 = int(number_1)
number_2 = int(number_2)

# operaciones matematicas
suma = number_1 + number_2
resta = number_1-number_2
multiplicacion = number_1 * number_2
division = number_1/number_2

msg = f"""
los numeros usados son: {number_1} y {number_2},
la suma es {suma}.
la resta es {resta}.
la multiplicaion es {multiplicacion}.
la division es {division}.
"""
print(msg)
