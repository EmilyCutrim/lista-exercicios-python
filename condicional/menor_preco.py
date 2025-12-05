preco_um = (input('Digite o valor do primeiro produto: '))
preco_dois = (input('Digite o valor do segundo produto: '))
preco_tres = (input('Digite o valor do terceiro produto: '))

if preco_um <= preco_dois and preco_um <= preco_tres:
    print(f'O primeiro produto, com valor de R${preco_um}, é o mais barato.')

elif preco_dois <= preco_um and preco_dois <= preco_tres:
    print(f'O segundo produto, com valor de R${preco_dois}, é o mais barato.')

elif preco_tres <= preco_um and  preco_tres <= preco_dois:
    print(f'O terceiro produto, com valor de R${preco_tres}, é o mais barato.')
