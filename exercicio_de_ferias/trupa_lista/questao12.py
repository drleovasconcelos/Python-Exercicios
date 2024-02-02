# A partir do arquivo criado na atividade anterior, crie um arquivo Python atividade12.py. Na
# sequência, após exibir a mensagem na tela (terminal) conforme o exemplo anterior, implemente
# um programa que, enquanto o turno de votação estiver aberto (turno = True), serão computados
# votos para os candidatos. No entanto, caso seja digitada a palavra 'encerrar', o turno deve ser
# encerrado (turno = True). Finalmente, exiba na tela (terminal) apenas a lista com os votos
# computados e confira se os votos foram adicionados corretamente à lista de votos.

lista_candidatos = ["Tião do Gás", "Zezinho 71", "Maria Marimar", "NULO", "BRANCO"]
lista_votos = [56, 71, 15, 0, 1]

for i, candidato in enumerate(lista_candidatos): ## loop, identificando os elementos da lista candidadatos de acordo com cada indice.
    voto = lista_votos[i] ## pegando os elementos da lista votos e colocando na variável voto
    print(candidato, "=", voto) 

qdeTiao = 0
qdeZezinho = 0
qdeMarimar = 0
qdeBranco = 0
qdeNulo = 0

iniciar = input("Você deseja votar: \n 1 - Sim; \n 2 - Não; \n")
while int(iniciar) == 1:
    voto1 = int(input("Digite seu Voto? \n 56 - Tião do Gás ;\n 71 - Zezinho 71; \n 15 - Maria Marimar; \n 0 - Nulo; \n 1 - Branco; \n"))
    if voto1 == 56:
        qdeTiao = qdeTiao + 1
    if voto1 == 71:
        qdeZezinho = qdeZezinho + 1
    if voto1 == 15:
        qdeMarimar = qdeMarimar + 1
    if voto1 == 0:
        qdeNulo = qdeNulo + 1
    if voto1 == 1:
        qdeBranco = qdeBranco + 1
    iniciar = input("Você deseja votar: \n 1 - Sim; \n 2 - Não; \n")

else:
    print(f"Contagem de Votos: \n"                               #\n é parágrafo
        f" Tião do Gás = {qdeTiao}\n"                                       
        f" Zezinho 71 = {qdeZezinho}\n"					#{  } substitui a concatenação 
        f" Maria Marimar = {qdeMarimar}\n" 
        f" Nulo = {qdeNulo}\n"
        f" Branco = {qdeBranco}")
