cpf = input('CPF: ')
senha = input('Senha: ')

menu = {
    1: '1: Consultar saldo',
    2: '2: Consultar Extrato',
    3: '3: Depositar',
    4: '4: Sacar',
    5: '5: Comprar criptomoedas',
    6: '6: Vender criptomoedas',
    7: '7: Atualizar cotação',
    8: '8: Sair',
}


if cpf == '12345678900' and senha == '123456':
    for valor in menu.values():
        print(valor)
else:
    print('CPF e/ou senha inválidos.')

escolha = input('Digite o que deseja acessar: ')
senha2 = input('Senha: ')

saldo = {
    1: 'Reais: ',
    2: 'Bitcoin: ',
    3: 'Etherum: ',
    4: 'Ripple: '
}

if escolha == 1 and senha2 == '123456':
    for valor in saldo.values():
        print(valor)
elif senha2 != '123456':
    print('Senha incorreta.')

