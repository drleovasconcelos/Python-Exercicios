# A partir do arquivo criado na atividade anterior, crie um arquivo Python exercicio03.py.
# Após, implemente o mesmo algoritimo do exercício anteriore, e utilize as funções
# .index() e .pop() para resolver o problema. Além disso, implemente uma nova variável
# do tipo lista (list) e adicione a ela todos os elementos removidos. Ao final, além de exibir
# a lista de compras atualizada, exiba a lista dos itens removidos. Dica: primeiro resolva
# o problema com as funções indicadas; após, implemente a lista de itens removidos.


# Carrega a lista de compras do exercicio02.py
from questao02 import lista_de_compras

# Inicializa a lista dos itens removidos
itens_removidos = []

# Pergunta ao usuário se deseja remover itens da lista
while True:
    item_remover = input("Digite um item para remover da lista (ou 'FIM' para encerrar): ")
    
    # Se o usuário digitar 'FIM', encerra o loop
    if item_remover.upper() == 'FIM':
        break
    
    # Tenta encontrar o índice do item na lista
    try:
        indice = lista_de_compras.index(item_remover)
        # Remove o item da lista e adiciona à lista de itens removidos
        item_removido = lista_de_compras.pop(indice)
        itens_removidos.append(item_removido)
        print(f"Item '{item_removido}' removido com sucesso!")
        
    except ValueError:
        print(f"Item '{item_remover}' não encontrado na lista.")

# Exibe a lista de compras atualizada
print("\nLista de Compras Atualizada:")
for item in lista_de_compras:
    print("-", item)

# Exibe a lista dos itens removidos
print("\nItens Removidos:")
for item in itens_removidos:
    print("-", item)
