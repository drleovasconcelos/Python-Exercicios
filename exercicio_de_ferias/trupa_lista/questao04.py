# Exercício 04
# A partir do arquivo criado na atividade anterior, crie um arquivo Python exercicio04.py.
# Após, pergunte ao usuário se ele deseja exibir a lista em ordem alfabética. Se sim,
# ordene a lista com a função .sort() e exiba a lista ordena. Ao final da lista, exiba a
# quantidade de itens adicionados à lista (tamanho da lista) com a seguinte mensagem:
# "Sua lista de compras tem {quantidade} itens".

# Carrega a lista de compras do exercicio03.py
from questao03 import lista_de_compras

# Pergunta ao usuário se deseja exibir a lista em ordem alfabética
ordenar = input("Deseja exibir a lista em ordem alfabética? (S/N): ")

# Se o usuário digitar 'S', ordena a lista
if ordenar.upper() == 'S':
    lista_de_compras.sort()

# Exibe a lista de compras
print("\nLista de Compras:")
for item in lista_de_compras:
    print("-", item)

# Exibe a quantidade de itens na lista
quantidade_itens = len(lista_de_compras)
print(f"\nSua lista de compras tem {quantidade_itens} itens.")