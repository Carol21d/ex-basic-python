import random


def pc_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(
            f'If {guess} too high (h), too low(l) or correctly (c)')
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
    print(f'The pc guessed your number , It´s was {guess}')


pc_guess(10)
