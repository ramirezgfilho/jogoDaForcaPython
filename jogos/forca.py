import random




def jogar():

    imprime_mensagem_abertura()

    palava_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palava_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0


    #Enquanto nao enforcou e nao acertou o jogo continua!!
    while(not enforcou and not acertou):

        chute = pede_chute()

        if(chute in palava_secreta):
            marca_chute_correto(chute, palava_secreta, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)

        enforcou = erros == 7

        acertou = "_" not in letras_acertadas

        print(letras_acertadas)

    if(acertou):
        imprime_mensagem_vitoria()
    else:
        imprime_mensagem_derrota(palava_secreta)



def imprime_mensagem_abertura():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    numero_palavra = random.randrange(0, len(palavras))
    palava_secreta = palavras[numero_palavra].upper()
    return palava_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra]

def pede_chute():
    chute = input("Qual a letra? ")
    chute = chute.strip()
    chute = chute.upper()
    return chute

def marca_chute_correto(chute, palava_secreta, letras_acertadas):
    index = 0
    for letra in palava_secreta:
        if (chute == letra):
            print("Encontrei a letra {} na posição {}".format(letra, index))
            letras_acertadas[index] = letra
        index += 1


def imprime_mensagem_derrota(palavra_secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


def imprime_mensagem_vitoria():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if (erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if (erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if (erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if (erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if (erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if (erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()

if(__name__ == "__main__"):
    jogar()
