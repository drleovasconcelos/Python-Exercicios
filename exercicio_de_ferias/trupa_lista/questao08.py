# A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade08.py. Na
# sequência, exiba a lista na tela (terminal) e pergunte ao usuário se ele deseja saber se há
# elementos repetidos na lista. Se sim, crie uma lista nova e adicione a ela todos os itens repetidos.
# Ao final, exiba ao usuário a lista de itens repetidos. Dica: utilize a função .count().

# p1 - usar lista anteriormente
# p2 - exibir na tela a lista
# p3 - perguntar se deseja saber se tem elementos repetidos na tabela
# p4 - se sim, crie uma nova lista com os elementos repetidos 
# p5 - exibir a lista de itens repetidos

itens_lista = ['Lápis', 'Borracha', 'Apontador', 'Pacote Folhas A4', 'Lápis', 'Caneta Bic', 'Clips de Metal', 'Grampos', 'Post It', 
        'Suporte p/ Notebook', 'Borracha', 'Lápis', 'Lápis', 'Caneta Bic','Grampos', 'Clips de Metal']
print("Material de Escritório: ", itens_lista)

opcao_repetidos = input("Deseja saber se tem elementos repetidos na lista? Sim ou Não = ")
if opcao_repetidos.lower() == "sim":
    itens_repetidos = []
    for item in itens_lista:
        if itens_lista.count(item) > 1 and item not in itens_repetidos: ## se ele aparecer mais de 1 vez e não estiver na lista de repetidos, ele e adcionado na lista nova
            itens_repetidos.append(item)
    print("Lista dos itens repetidos: ", itens_repetidos)
    print("Quantidade de itens duplicados: ", len(itens_repetidos))

else:
    print("Fim")