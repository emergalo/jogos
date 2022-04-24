import random

def jogar():
    print("*************************************")
    print("Ola, bem vindo ao jogo de adivinhacao")
    print("*************************************")

    numero_secreto = random.randrange(1,101)
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nivel de dificuldade?")
    print("(1) Facil (2) Medio (3) Dificil")

    nivel = int(input("Defina o nivel: "))

    while(nivel < 1 or nivel > 3):
        print("Erro!!!")
        print("Defina o nivel de dificuldade (1) Facil (2) Medio (3) Dificil")
        nivel = int(input("Defina o nivel: "))

    if(nivel == 1):
        total_de_tentativas = 10
    elif(nivel == 2):
        total_de_tentativas = 6
    else:
        total_de_tentativas = 3

    for rodada in range(1 , total_de_tentativas + 1):
        print("Tentativa {} de {}" . format(rodada, total_de_tentativas))
        chute_str = input("Digite um numero entre o 1 a 100:  ")
        print("Voce digitou:  ", chute_str)
        chute = int(chute_str)

        if (chute < 1 or chute > 100):
            print("Voce deve digitar um numero entre 1 a 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        if(acertou):
            print("Voce Acertou")
            print("Sua pontuacao foi {} pontos".format(pontos))
            break
        else:
            if(maior):
                print("Seu numero é maior que o numero secreto")
            elif(menor):
                print("Seu numero é menor que o numero secreto")

            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim de jogo")

if(__name__ == "__main__"):
    jogar()