
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
-Try to print the word ‘lucky’ inside s.
-Try to print the day, month, year in the form “Today is 2/2/2016”.
"""
s = "My lucky number is %d, what is yours?" % 7
print(s[3:8])

fecha = "Today is %d %d %d" % (2, 2, 2016)
print(fecha)

# 3
"""
Exercises below

Try the replace program
Can a string be replaced twice?
Does replace only work with words or also phrases?
"""

sv = "Hello World World World"
sv = sv.replace("World","on Chaos",2)
print(sv)

#4
"""
a)Find out if string find is case sensitive
b)What if a query string appers twice in the string?
c)Write a program that asks console input and searches for a query.
"""


phrase = "Find out if string G find is case sensitive"
if phrase.count('G') == 1:
    print("Aparece una vez")
else:
    print("Aparece mas de una vez ")
print(phrase.count('G'))
print(phrase.find('NOT FOUND'))


 #version mejorada del ejercicio de arriba
phrase_2 = "Write a program that asks console input and searches for a query"
if phrase_2.count('a') >1:
    print("La letra 'a' aparece más de una vez en el string")
else:
    print("La letra 'a' solo aparece una vez en el string")


#4.c
print("Introduce una palabra o frase: ")
find_word= input("")
if find_word.count("o") >1:
    print(f"la frase es: {find_word} ")
    print("letra 'o' fue encontrada más de una vez")
else:
    print(f"la frase es: {find_word} ")
    print("la letra 'o' fue encontrada una vez en la frase")
