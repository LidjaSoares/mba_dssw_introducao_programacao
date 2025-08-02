# Recebe os comprimentos dos lados
lado1 = float(input("Digite o comprimento do primeiro lado: "))
lado2 = float(input("Digite o comprimento do segundo lado: "))
lado3 = float(input("Digite o comprimento do terceiro lado: "))

# Verifica se os lados formam um triângulo válido
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    # Classifica o triângulo
    if lado1 == lado2 == lado3:
        print("Triângulo Equilátero")
    elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
        print("Triângulo Isósceles")
    else:
        print("Triângulo Escaleno")
else:
    print("Os lados fornecidos não formam um triângulo válido.")
