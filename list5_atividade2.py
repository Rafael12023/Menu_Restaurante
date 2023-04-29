produto = []
valor = 0
menu = ""
realvalor = ""

produtos = [[1, 'COXINHA', 5.00],[2, 'PASTEL', 4.00],[3, 'EMPADA', 3.00],[4, 'KIBE', 2.00]]

while True:

    print('\n[1] ADICONAR PRODUTO\n[2] REMOVER PRODUTO\n[3] EXIBIR CARRINHO\n[4] SAIR')
    opcao = int(input('SELECIONE UMA OPÇÃO\t:'))

    if opcao == 1: #Adicionar Salgado Carrinho
        print('\n[1] COXINHA  R$5,00\n[2] PASTEL   R$3,00\n[3] EMPADA  R$3,00\n[4] KIBE     R$2,00')
        opcao1 = int(input('QUAL SALGADO VAI QUERER? ESCOLHA UMA OPÇÃO\t        :'))
        match opcao1:

            case 1:
                if len(produto) == 0:
                    produto.append([1, 'COXINHA', 5.00])
                    valor += 5.00
                elif len(produto) > 0:
                    codigo = len(produto)+1
                    produto.append([codigo, 'COXINHA', 5.00])
                    valor += 5.00

            case 2:
                if len(produto) == 0:
                    produto.append([1, 'PASTEL', 3.00])
                    valor += 3.00
                elif len(produto) > 0:
                    codigo = len(produto)+1
                    produto.append([codigo, 'PASTEL', 3.00])
                    valor += 3.00

            case 3:
                if len(produto) == 0:
                    produto.append([1, 'EMPADA', 3.00])
                    valor += 3.00
                elif len(produto) > 0:
                    codigo = len(produto)+1
                    produto.append([codigo, 'EMPADA', 3.00])
                    valor += 3.00

            case 4:
                if len(produto) == 0:
                    produto.append([1, 'KIBE', 2.00])
                    valor += 5.00
                elif len(produto) > 0:
                    codigo = len(produto)+1
                    produto.append([codigo, 'KIBE', 2.00])
                    valor += 2.00

    elif opcao == 2:
        x = int(input('QUAL PRODUTO DESEJA REMOVER, INFORME O NUMERO'))-1
        valor -= produto[x][2]
        del produto[x]



    elif opcao == 3:
        x = 0
        while x < len(produto):
            menu = str('PRODUTO:%s, PREÇO:R$%0.2f' % (produto[x][1], produto[x][2]))
            print(menu.replace(".",","))
            x += 1
        realvalor = str("%.2f" %valor)
        print("R$",realvalor.replace(".",","))


    elif opcao == 4: #Finalizar Programa
        print('\nOBRIGADO POR TER USADO O PROGRAMA')
        break





