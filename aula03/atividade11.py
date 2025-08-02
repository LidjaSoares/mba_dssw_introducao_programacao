def gerar_tabuada():
    try:
        numero = int(input("Digite o número para ver a tabuada: "))
        print(f"\n📊 Tabuada do {numero}:\n")
        for i in range(1, 11):
            resultado = numero * i
            print(f"{numero} x {i} = {resultado}")
    except ValueError:
        print("⚠️ Por favor, digite um número inteiro válido.")
