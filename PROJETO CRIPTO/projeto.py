def loginUser():
    cpf = input('CPF: ')
    senha = input('Senha: ')
    return cpf, senha


Bitcoin = 0.0158
Ethereum = 1.03
Ripple = 200.35
Reais = 580.00
historico_tr = []

def menu():
    print("\n1. Consultar saldo")
    print("2. Consultar extrato")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Comprar criptomoedas")
    print("6. Vender criptomoedas")
    print("7. Atualizar cotação")
    print("8. Sair")

def saldo():
    print('\nSaldo:')
    print('Reais:', Reais)
    print('Bitcoins:', Bitcoin)
    print('Ripple:', Ripple)
    print('Ethereum:', Ethereum)
    


def registrar_tr( valor, tipo, cripto, quantidade, taxa, reaisSaldo, bitcoinSaldo, rippleSaldo, etherumSaldo):
    pass

    
    
#def consultar_ex():


def sacar():
    global Reais
    saqueValor = float(input('Por favor, digite o valor do saque:'))
    if saqueValor > Reais:
        print('Saldo insuficiente para realização do saque.')
    else:
        Reais -= saqueValor
        registrar_tr(saqueValor, '-', 0.0, 0.0, 0.0, Reais, Bitcoin, Ripple, Ethereum)
        print('Seu saque foi realizado com sucesso!')
        print('Novo saldo em Reais: R$', Reais)
    


def depositar():
    global Reais
    depositoValor = float(input('Por favor, digite o valor do depósito:'))
    Reais += depositoValor
    registrar_tr(depositoValor, '+', 0.0, 0.0, 0.0, Reais, Bitcoin, Ripple, Ethereum)
    print('Seu depósito foi realizado com sucesso!')
    print('Novo saldo em Reais: R$', Reais)
    

def saida():
    print('Saindo, muito obrigado pelo seu acesso!')


#def comprar_criptom():


#def vender_criptom():


cpf, senha = loginUser()
while True:
    menu()
    escolha = input("Digite a opção desejada: ")
    senha2 = input('Senha: ')

    if escolha == '1' and senha2 == '123456':
        saldo()

    elif escolha == '3'and senha2 == '123456':
        depositar()

    elif escolha == '4'and senha2 == '123456':
        sacar()
    
    elif escolha == '8' and senha2 == '123456':
        saida()
        break
    
    elif senha2 != '123456':
        print('Senha incorreta, tente novamente.')




