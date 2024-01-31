# A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade10.py.
# Aproveite todo o códico implementado anteriores. Dessa vez, além de exibir a lista na tela
# (terminal), você deverá exibir a quantidade de itens. Para isso, criei uma lista 'quantidade_itens'
# e adicione a ela a quantidade de cada item. Para isso, você deverá comparar a 'lista_final' (sem
# elementos repetidos) com a lista original (com os itens duplicados).

lista_compras = ['Lápis', 'Borracha', 'Apontador', 'Pacote Folhas A4', 'Lápis', 'Caneta Bic', 'Clips de Metal', 'Grampos', 'Post It', 
        'Suporte p/ Notebook', 'Borracha', 'Lápis', 'Lápis', 'Caneta Bic','Grampos', 'Clips de Metal']

# quantidade_itens = []
# for i, item in enumerate(lista):
#     print(i + 1, " ==> ", item)
# print("Quantidade de itens na lista = ", len(lista))
# Lista final sem elementos duplicados
lista_final = []

# Lista para armazenar a quantidade de cada item
quantidade_itens = []

# Iterar sobre os elementos da lista de compras
for item in lista_compras:
    # Verificar se o item já está na lista final
    if item not in lista_final:
        # Adicionar o item à lista final
        lista_final.append(item)
        # Contar quantas vezes o item aparece na lista original
        quantidade = lista_compras.count(item)
        # Adicionar a quantidade na lista de quantidade de itens
        quantidade_itens.append(quantidade)

# Exibir a lista final
print("Lista de compras:", lista_final)

# Exibir a quantidade de cada item
print("Quantidade de itens:", quantidade_itens)
