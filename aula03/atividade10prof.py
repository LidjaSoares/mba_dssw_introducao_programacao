from random import randint
import time

numero_aleatorio = randint(1,100)
parada = True

while parada:

    meu_numero = int(input('Digite um número de 1 a 100:'))

    if meu_numero == numero_aleatorio:
        print('Você acertou!')
        parada = False

    elif meu_numero < numero_aleatorio:
        print('Seu numero é MENOR! Tente um número mais alto')

    elif  meu_numero > numero_aleatorio:
        print('Seu número é MAIOR! Tente um número mais baixo')

    time.sleep(1)