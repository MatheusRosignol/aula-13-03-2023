sair = "sair"




while True:
    numero1 = float(input ("Escreve o primeiro númmero: "))
    numero2 = float(input ("Escreve o segundo númmero: "))
    operador =input("Digite o operador (+_*/): ")
    
    
    try: # Tentar executar o código
        numero_valido = True
    
    except: # Caso tenha executar o código abaixo   
        numero_valido = False
        
    if numero_valido == False:
        print("Número inválido. ")
        continue        
        
        
    # operador_aceito = ("+-*/")
    # if operador not in operador_aceito:
    #     print("Operador não aceito")
    
    if operador == "+":
        print(f"Resultado: {numero1 + numero2}")
    elif operador == "-":
        print(f"Resultado: {numero1 - numero2}")
    elif operador == "*":
        print(f"Resultado: {numero1 * numero2}")
    elif operador == "/":
        print(f"Resultado: {numero1 / numero2}")        
    else:
        print("Operador inválido.")
        
    sair = input("Deseja sair? ").lower().startswith("s")
    if sair is True:
        break