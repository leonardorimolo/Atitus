def media_valores(arquivo):
    soma = 0
    n = 0
    with open(arquivo, "r") as numeros:
        for linha in numeros.readlines():
            val = float(linha)
            soma += val
            n += 1
    return soma / n
            

med = media_valores("valores.txt")
print(f"A média dos valores é {med:.2f}")

'''
Considere o arquivo valores.txt contendo:

4
7
3
10
'''