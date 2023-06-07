# ejercicios basicos de python org
"""Try the exercises below
-Make a program that displays several numbers.
-Make a program that solves and shows the summation of 64 + 32.
-Do the same as in 2, but make it sum x + y.
"""


# 2

numb_1 = 64
numb_2 = 32
numb_1 = int(numb_1)
numb_2 = int(numb_2)
result = numb_1 + numb_2
print(f"el resultado es: {result}")

"""
-Try to print the word -lucky- inside s.
-Try to print the day, month, year in the form -Today is 2/2/2016-
"""

s = "My lucky number is %d, what is yours?" % 7
print(s[3:8])

fecha = "Today is %d %d %d" % (2, 2, 2016)
print(fecha)
