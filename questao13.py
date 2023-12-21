# 14. Faça um programa que inicialize uma lista vazia, depois disso solicite 5 nomes diferentes ao usuário 
# (utilize laço de repetição). 
#Cada nome digitado deve ser adicionado à lista e por fim, todos os nomes devem ser escritos no console. 
# Utilize uma função para solicitar e retornar o nome digitado, uma função para adicionar o nome à lista 
# (passando o nome e a lista por parâmetro) 
# e outra função para escrever todos os nomes no console.

lista = []
nome = 0

def nomes(nome):
        lista.append(nome)
        return lista

for i in range (5):
    nome = input("Digite o nome: ")
    lista = nomes(nome)
print("Nomes da lista: ", lista)