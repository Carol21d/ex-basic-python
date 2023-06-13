age = input("Introduce la edad: ")
age = int(age)
msg = f"""
Tiene {age}
"""
if age > 21:
    print(msg+"Si, es mayor de edad")
else:
    print(msg+"No es mayor de edad")
