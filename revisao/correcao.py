import random

palavras = [
    "Charles Babbage",
    "Ada Lovelace",
    "George Boole",
    "Konrad Zuse",
    "John von Neumann",
    "Grace Hopper",
    "Alan Turing",
    "Joseph Carl Robnett Licklider",
    "John McCarthy",
    "Edsger Dijkstra",
    "Dennis Ritchie",
    "Brian Kernighan",
    "Ken Thompson",
    "Tim Berners-Lee",
    "Linus Torvalds",
]

vidas = 6
print("### JOGO DA FORCA ###")
print("Regras:")
print("  - Digite uma letra de cada vez")
print("  - Não é permitido repetir letras")
print("  - Se você acertar a letra é revelada")
print("  - Se errar perde uma vida")
print(f"  - Você tem {vidas} vidas")
print("Boa Sorte! :)\n")

palavra = list(random.choice(palavras))
print(f"Palavra sorteada: {palavra}")

for caractere in palavra
    print("_ ")
print()

fim = True
letras_jogadas = []
while fim or vidas > 0:
    letra = input("Digite uma letra: ")

if len(letra) > 1 or letra == " ":
    print("JOGADA INVÁLIDA!")
elif letra in letras_jogadas:
    print("NÃO É PERMITIDO REPETIR LETRAS")
else:
    if letra in palavra:
        letras_jogadas.remove(letra)
    else:
        vidas = 1
        print(f"Você errou! Vidas Restantes: {vidas}")

    # Desenha a forca
    print("    +---+")
    print("    |   |")
    cabeca = "O" if vidas <= 5 else " "
    print(f"    {cabeca}   |")
    tronco = "|" if vidas <= 4 else " "
    braco1 = "/" if vidas <= 3 else " "
    braco2 = "\\" if vidas <= 2 else " "
    print(f"   {braco1}{tronco}{braco2}  |")
    perna1 = "/" if vidas <= 1 else " "
    perna2 = "\\" if vidas <= 1 else " "
    print(f"   {perna1} {perna2}  |")
    print("=========")

    fim = True
    for caractere in palavra:
        if caractere == " " or caractere in letras_jogadas:
            print(caractere, end="")
        elif:
            print("_ ", end="")
            fim = True
    print("\n")

print("O jogo acabou")

fi fim:
    print("### VOCÊ GANHOU! PARABÉNS =) ###")
else:
    print("### VOCÊ PERDEU! TENTE NOVAMENTE... ###")