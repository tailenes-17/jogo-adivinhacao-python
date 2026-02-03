import random
numero_secreto= random.randint(0,10)
chute = 0
tentativas = 0
max_tentativas = 3
while chute != numero_secreto:
    chute = int(input(' Qual seu palpite:'))
    tentativas += 1
    if chute == numero_secreto:
        print(f' Parabéns! voce acertou em {tentativas} tentativas.')
        break
    if tentativas == max_tentativas:
        print(f' Ops! voce atingiu o limite de tentativas. O numero secreto era: {numero_secreto}')
        break
    if chute > numero_secreto:
        print(' Voce errou, o numero secreto é menor.')
    elif chute < numero_secreto:
        print(' voce errou, o numero secreto é maior.')





