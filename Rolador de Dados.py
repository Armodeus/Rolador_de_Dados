from random import randint

print('')
print('>>>>Rolando um Dado de 6 lados<<<<')
print('')

a = input('Pressione (1) rolar o dado (2) Sair: ')

# valida variável (a)
while a not in '1 2':
    print('Você escolheu a opção', a)
    print('Opção inválida, tente novamente.')
    a = input('Pressione (1) rolar o dado (2) Sair: ')
# Se a for 1 fazer a jogada.
if a == '1':
    print('Você escolheu a opção', a)
    b = randint(1, 6)
    print(b)
    jogar = str(input('Deseja jogar novamente? (S) Sim  (N) Não: ')).strip().upper()[0]

    # Validação variável jogar.
    while jogar not in 'S N':
        print('Opção inválida.')
        jogar = str(input('Deseja jogar novamente? (S) Sim  (N) Não: ')).strip().upper()[0]

    # Enquanto a variável jogar for sim.
    while jogar == 'S':
        print('Você escolheu jogar novamente!')
        b = randint(1, 6)
        print(b)
        jogar = str(input('Deseja jogar novamente? (S) Sim  (N) Não: ')).strip().upper()[0]
        while jogar not in 'S N':
            print('Opção inválida.')
            jogar = str(input('Deseja jogar novamente? (S) Sim  (N) Não: ')).strip().upper()[0]

    if jogar == 'N':
        print('Fim do jogo!')

# Se (a) for 2 sair do jogo.
elif a == '2':
    print('Você escolheu a opção', a)
    print('Você saiu do programa!')
