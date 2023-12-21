# 11. Faça um programa que solicite ao usuário três números diferentes e exiba o dobro do maior número. 
# Para fazer isso separe seu código em duas funções diferentes: 
# Uma função para retornar o maior dos três números e outra função para dobrar o número

def maior_num (num1, num2, num3):
    if num1<num2<num3:
        print(f'Maior número é o terceiro, e o dobro é {num3 * 2}')
    if num2<num3<num1:
        print(f'Maior número é o primeiro, e o dobro é {num1 * 2}')
    if num3<num1<num2:
        print(f'Maior número é o segundo, e o dobro é {num2 * 2}')
    return ()


num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))
num3 = float(input("Digite o terceiro numero: "))
x = maior_num(num1, num2, num3) 




# def encontrar_maior(num1, num2, num3):
#     """Retorna o maior entre três números."""
#     return max(num1, num2, num3)

# def dobrar_numero(numero):
#     """Retorna o dobro de um número."""
#     return numero * 2

# # Solicitar ao usuário três números diferentes
# num1 = float(input("Digite o primeiro número: "))
# num2 = float(input("Digite o segundo número: "))
# num3 = float(input("Digite o terceiro número: "))

# # Encontrar o maior número
# maior_numero = encontrar_maior(num1, num2, num3)

# # Dobrar o maior número
# resultado = dobrar_numero(maior_numero)

# # Exibir o resultado
# print(f"O dobro do maior número ({maior_numero}) é: {resultado}")
