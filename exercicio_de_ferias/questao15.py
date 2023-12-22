# Faça um programa que exiba todos os números ímpares de 1 a 100 com o FOR e a
# função RANGE. Após, faça o mesmo exercício utilizando o WHILE.

num = 1
while num <= 100:
    if num % 2 != 0:
        print(num)
    num += 1
        

for i in range (1, 101):
    if i % 2 != 0:
        print(i)
   