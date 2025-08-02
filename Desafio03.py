# Recebe os dados do usuário
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))

# Calcula o IMC
imc = peso / (altura ** 2)

# Exibe o resultado e a condição
print(f"Seu IMC é: {imc:.2f}")

# Classifica a condição de peso
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Peso normal.")
elif imc < 29.9:
    print("Sobrepeso.")
elif imc < 34.9:
    print("Obesidade grau I.")
elif imc < 39.9:
    print("Obesidade grau II.")
else:
    print("Obesidade grau III (mórbida).")
