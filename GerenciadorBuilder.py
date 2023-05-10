senhas = []

def gerar_senha():
    if len(senhas) == 0:
        novasenha = 1
    else:
        novasenha = senhas[-1] + 1
    
    senhas.append(novasenha)
    
    print("\nSENHA GERADA:", novasenha, "Aguarde a chamada")

def visualizar_painel():
    print("PROXIMAS SENHAS A SEREM CHAMADA ", senhas)

def verificar_senha_especifica(): 
 
     senhaatual = senhas[0]
     senhaesp = int(input("Informe sua senha: "))
     if senhaatual == senhaesp :

        print("Proximo a ser chamado")
     else:
        print("Você não é o proximo")
        print(senhas[0])
        print(senhaesp)

def atender_senha():
    if len(senhas) == 0:
        print("Não há senhas na fila.")
    else:
        senha_chamada = senhas.pop(0)
        print("\nA senha", senha_chamada, "foi chamada.")


while True:
    print("\nSISTEMA GERENCIADOR DE FILA")
    print("1 - NOVA SENHA")
    print("2 - VISUALIZAR PAINEL")
    print("3 - VERIFICAR SENHA ESPECIFICA")
    print("4 - CHAMAR PROXIMO DA FILA")
    print("5 - FECHAR O SISTEMA")
    op = int(input("\nESCOLHA UMA OPÇÃO: "))
    if op == 1:
        gerar_senha()
    elif op == 2:
        visualizar_painel()
    elif op == 3:
        verificar_senha_especifica()
    elif op == 4:
        atender_senha() 
    elif op == 5:
        break 
    else:
        print("\nOpção inválida.")