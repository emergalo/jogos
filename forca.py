import random

def jogar():

    imprime_mensagem_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_corretas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_corretas)

    while(not enforcou and not acertou):

        chute = input("Qual a letra?  ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            posicao = 0
            for letra in palavra_secreta:
                if(chute.upper() == letra.upper()):
                    letras_corretas[posicao] = letra
                posicao += 1
        else:
            erros += 1

        enforcou = erros == 6
        acertou = "_" not in letras_corretas
        print(letras_corretas)

    if(acertou):
        print("Voce acertou a palavra!!!")
    else:
        print("Voce Perdeu!!!")

    print("Fim de jogo")


def imprime_mensagem_abertura():
    print("*************************************")
    print("***Ola, bem vindo ao jogo de Forca***")
    print("*************************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()

    numero = random.randrange(0, len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

if(__name__ == "__main__"):
    jogar()