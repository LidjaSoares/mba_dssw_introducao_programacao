import random

print("🎯 Bem-vindo ao jogo de adivinhação!")
print("O computador pensou em um número entre 1 e 100. Tente adivinhar!")

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    chute = int(input("Digite seu palpite: "))
    tentativas += 1

    if chute < numero_secreto:
        print("🔼 Muito baixo! Tente um número maior.")
    elif chute > numero_secreto:
        print("🔽 Muito alto! Tente um número menor.")
    else:
        print(f"🎉 Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
        break
