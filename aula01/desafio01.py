#verificador de numero par ou impar
#crie um programa que verfique se um numero
#(informado pelo usuario) é par ou impar

#retornar a uma string (texto)
#o retorno dentro de uma variavel

numero = int(input('digite um numero: '))

if (numero % 2) == 0:
  print(f'0{numero} é par!')
else:
  print(f'0{numero} é impar!')



