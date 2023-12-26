# Faça um programa que conte a quantidade de vogais e de consoantes de uma palavra.
# Dica: utilize o operador relacional in.

palavra = input('Digite a palavra: ')
qdadeVogais = 0
qdadeConsoante = 0
vogais = "aeiouAEIOU"
for letra in palavra:
    if letra in vogais:
        qdadeVogais += 1
    else: 
        qdadeConsoante += 1
print(f'A palavra {palavra} tem {qdadeVogais} vogais e {qdadeConsoante} consoantes.')