"""
Faça uma lista de compras com list
o usuário deve ter a possibilidade de
inserir, apagar e listar valores da lista.
 Não permitir que o programa quebre com erros de indices inexistentes
"""
lista = []

while True:

    opcao = input('[I]nserir [A]pagar [L]istar [S]air: ').upper()

    if opcao == 'I':
        item = input('Insira um item: ')
        lista.append(item)

    elif opcao == 'A':
        posicao = int(input('Insira a posicao: '))
        if posicao not in lista:
            print('Posição inválida')
        else:
            lista.pop(posicao)

    elif opcao == 'L':
        if not lista:
            print('Nenhum item encontrado na lista')
        else:
            for item in enumerate(lista):
                print(item)

    elif opcao == 'S':
        print('Saindo...')
        break
    else:
        print('Opção invalida, tente novamente.')
