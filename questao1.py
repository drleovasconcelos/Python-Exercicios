sair = False
while sair != True:
    codigo = int(input("Qual peso você quer descobrir em outro planeta: \n 1 - Mercurio; \n 2 - Vênus; \n 3 - Marte; \n 4 - Júpiter; \n 5 - Saturno; \n 6 - Urano; \n 0 - Sair; \n"))
    if codigo == 1:
        PT = int(input("Digite o seu peso na terra: "))
        G = 0.37
        PP = PT / (10 * G)
        print(f"Peso na Terra: {PT}")
        print (f"Código: {codigo}")
        print (f"Peso em mercurio: {PP}")
    
    elif codigo == 2:
        PT = int(input("Digite o seu peso na terra: "))
        G = 0.88
        PP = PT / (10 * G)
        print(f"Peso na Terra: {PT}")
        print (f"Código: {codigo}")
        print (f"Peso em Vênus: {PP}")

    elif codigo == 3:
        PT = int(input("Digite o seu peso na terra: "))
        G = 0.38
        PP = PT / (10 * G)
        print(f"Peso na Terra: {PT}")
        print (f"Código: {codigo}")
        print (f"Peso em Marte: {PP}")
    elif codigo == 4:
        PT = int(input("Digite o seu peso na terra: "))
        G = 2.64
        PP = PT / (10 * G)
        print(f"Peso na Terra: {PT}")
        print (f"Código: {codigo}")
        print (f"Peso em Júpiter: {PP}")
    elif codigo == 5:
        PT = int(input("Digite o seu peso na terra: "))
        G = 1.15
        PP = PT / (10 * G)
        print(f"Peso na Terra: {PT}")
        print (f"Código: {codigo}")
        print (f"Peso em Saturno: {PP}")
    elif codigo == 6:
        PT = int(input("Digite o seu peso na terra: "))
        G = 1.17
        PP = PT / (10 * G)
        print(f"Peso na Terra: {PT}")
        print (f"Código: {codigo}")
        print (f"Peso em Urano: {PP}")
    else:
        print ("Obrigado")
        break

