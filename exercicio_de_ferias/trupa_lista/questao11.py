# Na sequência, defina duas variável do tipo lista (list):
# 'lista_candidatos' e 'lista_votos'. Na primeira, adicione manualmente os seguintes candidatos:
# Tião do Gás, Zezinho 71 e Maria Marimar. Na segunda, reserve com 0 os espaços para
# computador os votos de cada candidato. Assim, o índice 0 da lista 'lista_votos' deve conter os
# votos do índice 0 da 'lista_candidatos'. Finalmente, exiba na tela (terminal) a mensagem
# conforme o exemplo abaixo:


lista_candidatos = ["Tião do Gás", "Zezinho 71", "Maria Marimar", "NULO", "BRANCO"]
lista_votos = [56, 71, 15, 0, 1]

for i, candidato in enumerate(lista_candidatos): ## loop, identificando os elementos da lista candidadatos de acordo com cada indice.
    voto = lista_votos[i] ## pegando os elementos da lista votos e colocando na variável voto
    print(candidato, "=", voto) 

