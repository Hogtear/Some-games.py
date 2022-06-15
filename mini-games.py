
#Rock paper scissors
def rps():
    while True:
        try:
            
            def play():
                user = input("Qual a sua escolha?\n\n'r' para Pedra, 'p' para Papel e 's' para Tesoura: \n\n")
                computer = random.choice(['r', 'p', 's'])

                if user == computer:
                    print("Empate!")

                if is_win(user, computer):
                    print("Você ganhou!")
                
                return 'Você perdeu!'

                def is_win(player, opponent):
                    if (player == 'r' and opponent == 's') or (player == 'p' and opponent == 'r') or (player == 's' and opponent == 'p'):
                        return True
                print((play()))                        
            break

        except ValueError:
            print('Digite APENAS caracteres! Tente novamente')

#Acerte o número
def rand_number():
    while True:
        try:
            random_number = random.randint(1, 100)
            guess = 0
            while guess != random_number:
                guess = int(input(f'Adivinhe o número entre 1 e 100: '))
                if guess > random_number:
                    print('Errou! O número é menor!')
                elif guess < random_number:
                    print('Errou! O número é maior!')
            print('Parabéns! Você acertou! o número era:', random_number)
            break
        except ValueError:
            print('Digite APENAS valores numéricos! Tente novamente')

#Programa principal
while True:

    import random
    global volume

    print('\n======================BEM VINDO=====================\n')
    print('Digite um dos seguintes números para escolher a opção desejada:\n')
    escolha = int(input('Escolha uma opção:\n'
                        '1 - Pedra, papel e Tesoura\n'
                        '2 - Acerte o número\n'
                        '4 - Sair do programa\n'))

    if escolha == 1:
        rps()

    elif escolha == 2:
        rand_number()

    elif escolha == 4:
        print('Saindo do programa...')
        break

    else:
        print('Opção inválida! Tente novamente')
