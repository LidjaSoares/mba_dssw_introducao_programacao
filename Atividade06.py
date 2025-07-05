PI = 3.14 #VALORES DE CONSTANTES SEMPRE EM CAIXA ALTA
altura = float(input('digite o valor da altura: '))
raio = float(input('digite o valor do raio: '))

area_lateral = 2 * PI * altura * raio
base = altura * (raio ** 2)
area_cilindro = area_cilindro = area_lateral + base
qtd_litros = area_cilindro / 3
qtd_latas = qtd_litros / 5
custo_total = qtd_latas * 50

print(f' o custo total da pintura é R${custo_total:2f}')


#quantidades de latas de tinta e o custo para pintar um cilindro de combustivel
#valor da lata = 50
#capac da lata = 5
#pintura = 1l pinta 3m quadrados


#comecar de baixo p cima