valor_produto = float(input("digite o valor do produto: "))
desconto = float(input('digite o desconto:'))
valor_desconto = (valor_produto * desconto) / 100
valor_final = valor_produto - valor_desconto

print(f'o valor final é {valor_final:.2f}')

