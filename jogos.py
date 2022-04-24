import forca
import adivinhaca

def escolha_jogo():
    print("*************************************")
    print("***Escolha o seu jogo****************")
    print("*************************************")

    print("Escolha o jogo = Forca (1) Adivinhacao (2)")
    jogo = int(input("Qual o jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhacao")
        adivinhaca.jogar()

if(__name__ == "__main__"):
    escolha_jogo()




