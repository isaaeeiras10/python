senha = 'abacaxi'
for p in range (3):
    senha_digitada = input("Qual é a senha: ")
    if senha == senha_digitada:
        print ("Logado com sucesso!")
        break 
    else:
        if p==2:
            print("Senha incorreta! \nTentativas esgotadas.")
        else:
            print(f"Senha incorreta! \nVocê tem mais {2-p}")