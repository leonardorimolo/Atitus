import random

palavras = ['algoritmo', 'bigdata', 'cibersegurança', 'digitalização', 'inteligência artificial', 'html']

palavra = random.choice(palavras)

lista_caracter = list(palavra)
lista_caracter_jogada = []

print(lista_caracter)

jogada = "a"
vida = 6
while len(jogada) == 1:
    if jogada.isalpha() == True:
        jogada = str(input("Digite uma letra"))
        
        if jogada in lista_caracter:
            lista_caracter_jogada.append(jogada)
            print(lista_caracter_jogada)

        else:
            vida = vida - 1
            print(f'Voce tem {vida} vidas restantes')
            if vida == 0:
                jogada = 'aa'
                print('Voce perdeu!')
                