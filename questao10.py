# 10. Utilize a lista de compras do programa anterior para identificar 
# qual o produto mais barato e qual o produto mais caro da lista de compras.

# Dicionário de produtos e preços
produtos = {}
qdeItens = int(input("Quantidade de Itens: "))
for i in range(qdeItens):
    produto = input("Informe o produto: ")
    preco = float(input("Informe o preço: "))
    produtos[produto] = preco

# Inicializa as variáveis para armazenar o produto mais barato e mais caro
produto_mais_barato = 0
preco_mais_barato = float('inf')  # Inicializa com o maior valor possível
produto_mais_caro = 0
preco_mais_caro = float('-inf')  # Inicializa com o menor valor possível

# Loop pelos produtos e compara os preços
for produto, preco in produtos.items():
    if preco < preco_mais_barato:
        produto_mais_barato = produto
        preco_mais_barato = preco

    if preco > preco_mais_caro:
        produto_mais_caro = produto
        preco_mais_caro = preco

# Verifica se há um produto mais barato
if produto_mais_barato != 0:
    print(f"O produto mais barato é {produto_mais_barato} com o preço de R${preco_mais_barato}")
else:
    print("Não há produtos na lista.")

# Verifica se há um produto mais caro
if produto_mais_caro != 0:
    print(f"O produto mais caro é {produto_mais_caro} com o preço de R${preco_mais_caro}")
else:
    print("Não há produtos na lista.")