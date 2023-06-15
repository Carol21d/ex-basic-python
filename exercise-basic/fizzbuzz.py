'''
Fizzbuzz:
Escribe un programa que muestre por consola(con print)
 los numeros 1-100 ambos incluidos con un salto de linea
-multiplos de 3 por la palabra"Fizz"
-multiplos de 5 por la palabra "Buzz"
- multiplos de 3 y 5 por la palabra "Fizzbuzz"
'''


def fizzbuzz(number):
    if number > 0:
        fizzbuzz(number - 1)
        print(number, end=' ')


print('Numbers from 1 to 100')
fizzbuzz(100)
