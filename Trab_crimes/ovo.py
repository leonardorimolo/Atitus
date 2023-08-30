import csv


def calcular_pontos(linha):
    pontos_violentos = (
        int(linha['Vitimas de Homicidio Doloso']) * 10
        + int(linha['Vitimas de Latrocinio']) * 10
        + int(linha['Vitimas de Lesao Corp Seg Morte']) * 10
        + int(linha[' Roubo de Veiculo']) * 3
        + int(linha[' Roubos']) * 2
        + int(linha[' Delitos Relacionados a Armas e Municoes']) * 2
        + int(linha[' Entorpecentes Trafico']) * 5
    )
    pontos_nao_violentos = (
        int(linha[' Entorpecentes Posse']) * 2
        + int(linha['Furto de Veiculo ']) * 3
        + int(linha[' Furtos']) * 3
        + int(linha[' Estelionato'])
    )
    return pontos_violentos, pontos_nao_violentos


def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
        csv_reader = csv.DictReader(arquivo, delimiter=';')
        pontos_violentos = 0
        pontos_nao_violentos = 0
        for linha in csv_reader:
            pontos_violentos1, pontos_nao_violentos1 = calcular_pontos(linha)
            pontos_violentos += pontos_violentos1
            pontos_nao_violentos += pontos_nao_violentos1
        return pontos_violentos, pontos_nao_violentos


# Dados por ano
arquivos = ['jan-21.csv', 'jan-22.csv', 'jan-23.csv']
crimes_violentos = {}
crimes_nao_violentos = {}

for arquivo in arquivos:
    pontos_violentos, pontos_nao_violentos = ler_arquivo(arquivo)
    crimes_violentos = pontos_violentos
    crimes_nao_violentos = pontos_nao_violentos

# Resultados globais
print('---------------------------------------------------')
print('Indicadores globais por ano')
print('---------------------------------------------------')
print('Crimes Violentos')
ano = [2021,2022,2023]
for ano in range(3):
    pontos = pontos_violentos
    print(f'- {ano}: {pontos}')
print()
print('Crimes Não Violentos')
for ano in range(3):
    pontos = pontos_nao_violentos
    print(f'- {ano}: {pontos}')
