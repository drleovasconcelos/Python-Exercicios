
pratos = {"Vegetaria": 180, "Peixe": 230, "Frango": 250, "Carne": 350}
sobremesas = {"Abacaxi": 75,"Sorvete Diet": 110, "Mousse Diet": 170, "Mousse Chocolate": 200}
bebidas = {"Cha" : 20, "Suco de Laranja": 70,"Suco de melão": 100, "Refrigerante Diet": 65}

print("*************MENU*************")

calorias=[]

while True:
    print('Escolha uma opção de prato:')

    for prato in pratos.keys():
        print(prato)

    print()
    choice1=input('')
    if choice1 in pratos.keys():
        print('Ótima escolha')
        print()
        print('Agora escolha uma opção de sobremesa:')

        for sobremesa in sobremesas.keys():
            print (sobremesa)

        choice2=input()
        if choice2 in sobremesas.keys():
            print('Òtima escolha!')
            print()
            print('Agora escolha uma opção de Bebida:')

            for bebida in bebidas.keys():
                print(bebida)

            print()
            choice3=input()
            if choice3 in bebidas.keys():
                print('Maravilha')
                calorias_totais=pratos[choice1]+sobremesas[choice2]+bebidas[choice3]
                print(f'O valor total de calorias do seu prato é {calorias_totais}')
                break


            else:
                print('Opção inválida!')


        else:
            print('Opção inválida.')



    else:
        print('Opção inválida!')
        print()
