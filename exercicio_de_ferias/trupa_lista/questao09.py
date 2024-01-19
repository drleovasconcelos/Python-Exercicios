# A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade09.py. Na
# sequência, exiba a lista de itens para escritório sem os itens duplicados. Para isso, a partir da
# lista original (com todos os duplicados) e da lista auxiliar (apenas com os itens duplicados) crie
# uma terceira lista chamada 'lista_final' e adicione a ela os itens tratados. Ainda, organize a lista
# em ordem crescente com a função .sort(). Dica: consulte a tabela de métodos manipuladores
# de lista para criar a lista final e exibir ao usuário sem os itens duplicados.

# importar lista anterior
# from questao07 import itens_lista
# from questao07 import itens_repetidos

# itens_lista = ['Lápis', 'Borracha', 'Apontador', 'Pacote Folhas A4', 'Lápis', 'Caneta Bic', 'Clips de Metal', 'Grampos', 'Post It', 
#         'Suporte p/ Notebook', 'Borracha', 'Lápis', 'Lápis', 'Caneta Bic','Grampos', 'Clips de Metal']
# itens_repetidos:  ['Lápis', 'Borracha', 'Caneta Bic', 'Clips de Metal', 'Grampos']
#p1 - na sequência, exiba a lista de itens para escritório sem os itens duplicados. crie uma terceira lista com os dados tratados
#p2 - organize a lista em ordem crescente com a função .sort().
# atividade09.py

# Importar o arquivo exercicio07.py que contém a lista
from questao08 import itens_lista

# Exibir a lista original na tela
print("Itens na Lista Original:", itens_lista)

# Criar uma lista auxiliar para armazenar itens duplicados
itens_duplicados = []
itens_sem_duplicados = []

# Preencher a lista auxiliar e a lista sem duplicados
for item in itens_lista:
    if itens_lista.count(item) > 1 and item not in itens_duplicados:
        itens_duplicados.append(item)
    elif itens_lista.count(item) == 1:
        itens_sem_duplicados.append(item)

# Criar a lista final combinando itens sem duplicados e ordenando em ordem crescente
lista_final = itens_sem_duplicados + itens_duplicados
lista_final.sort()

# Exibir a lista final ao usuário
print("Lista Final (sem duplicados e ordenada):", lista_final)