# Lista de compras com itens duplicados
lista_compras = ['Lápis', 'Borracha', 'Apontador', 'Pacote Folhas A4', 'Lápis', 'Caneta Bic', 'Clips de Metal', 'Grampos', 'Post It', 
        'Suporte p/ Notebook', 'Borracha', 'Lápis', 'Lápis', 'Caneta Bic','Grampos', 'Clips de Metal']

# Dicionário para armazenar a contagem de cada item
contagem_itens = {}

# Contar a quantidade de cada item
for item in lista_compras:
    if item in contagem_itens:
        contagem_itens[item] += 1
    else:
        contagem_itens[item] = 1

# Exibir os resultados
print("Lista de compras: ")
for item, quantidade in contagem_itens.items():
    print(f"{quantidade}x {item}")