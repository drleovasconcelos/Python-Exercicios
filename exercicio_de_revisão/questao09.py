# 09. Faça um programa que inicialize uma lista de compras com 5 itens diferentes, 
# onde cada item é um dicionário contendo a descrição e preço do produto.
# Depois disso, percorra a lista e exiba as informações de cada item.

lista_de_compra = []

qdeItens = int(input("Quantidade de Itens: "))
for i in range(qdeItens):
    produto = input("Informe o produto: ")
    preço = float(input("Informe o preço: "))
    item = {"Produto": produto, "Preço": preço}
    lista_de_compra.append(item)
for item in lista_de_compra:
    print("Produto:", item["Produto"])
    print("Preço:", item["Preço"])
    print("\n")
# print("Lista de Compra: ", lista_de_compra)

# qdeItens = int(input("Quantidade de Itens: "))
# for i in range(qdeItens):
#     item = input("Digite os itens das compras: ")
#     lista_de_compra.append(item)
# print("Lista de Compras:", lista_de_compra)


# d = {
#     "nome": "Leo",
#     "idade":15,
#     "telefone": 85985449394
# }

# for x,y in d.items():
#     print({x:y})



