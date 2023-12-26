# Faça um programa que verifique quantas letras 'a' têm em uma palavra qualquer. Para
# isso, utilize o laço FOR para percorrer as letras da palavra e verifique se a letra é igual
# à letra 'a'. Se sim, implemente um contador para armazenar o total de letras. Dica: crie
# uma variável chamada 'quantidade' e atribua zero como valor inicial. Sempre que uma
# letra verificada da palavra for igual à letra 'a', a variável 'quantidade' deve receber o
# próprio valor mais um, conforme o exemplo a seguir:

palavra = input ('Digite a palavra: ')
quantidade = 0
for letra in palavra:
    if letra == "a":
        quantidade = quantidade + 1
print ('Quantas letras a quem na palavra: ', quantidade)