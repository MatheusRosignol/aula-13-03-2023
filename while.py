sistema = True

while sistema:
    nome = input ("Escreva o seu nome: ")
    print(f"O nome recebido foi{nome}")
    
    if nome == "sair":
        print("Finalizou o sistema")
        break