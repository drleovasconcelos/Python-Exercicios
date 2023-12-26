# Exercício 04
# Faça um programa que calcule o desconto de 10% em um produto e exiba o valor com
# desconto.
# Saída de Dados (terminal):
# Digite o valor do produto: 80.0
# O valor com desconto é: 72.0

produto = float(input("Digite o valor do produto: "))
desconto = float(input("Digite o valor do desconto: "))

valor_do_desconto = (produto * desconto) / 100
preco_do_produto = produto - valor_do_desconto
print("Valor do Produto: ", produto)
print("Valor do produto com desconto: ", preco_do_produto) 

