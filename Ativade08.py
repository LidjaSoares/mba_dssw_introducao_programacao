# Recebe dois números do usuário
numero1 = float(input("Digite o primeiro número: "))
numero2 = float(input("Digite o segundo número: "))

# Compara os dois números
if numero1 > numero2:
    print(f"O primeiro número ({numero1}) é maior que o segundo ({numero2}).")
elif numero2 > numero1:
    print(f"O segundo número ({numero2}) é maior que o primeiro ({numero1}).")
else:
    print("Os dois números são iguais.")
