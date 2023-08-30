import csv

    
def calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos):
    for linha in csv_reader:
        #CRIME VIOLENTOS
        pontos_violentos = pontos_violentos + (int(linha['Vitimas de Homicidio Doloso']) * 10)
        pontos_violentos = pontos_violentos + (int(linha["Vitimas de Latrocinio"]) * 10)
        pontos_violentos = pontos_violentos + (int(linha["Vitimas de Lesao Corp Seg Morte"]) * 10)
        pontos_violentos = pontos_violentos + (int(linha[" Roubo de Veiculo"]) * 3)
        pontos_violentos = pontos_violentos + (int(linha[" Roubos"]) * 2 )
        pontos_violentos = pontos_violentos + (int(linha[" Delitos Relacionados a Armas e Municoes"]) * 2)
        pontos_violentos = pontos_violentos + (int(linha[" Entorpecentes Trafico"]) * 5)

        #CRIMES NAO VIOLENTOS
        pontos_nao_violentos = pontos_nao_violentos + (int(linha[" Entorpecentes Posse"]) * 2)
        
        pontos_nao_violentos = pontos_nao_violentos + (int(linha["Furto de Veiculo "]) * 3)
        pontos_nao_violentos = pontos_nao_violentos + (int(linha[" Furtos"]) * 3)
        pontos_nao_violentos = pontos_nao_violentos + (int(linha[" Estelionato"]) * 1)

    return pontos_violentos,pontos_nao_violentos


#ARQUIVO JAN 2021
with open("jan-21.csv", "r", encoding="utf-8") as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=";")
    pontos_violentos = 0
    pontos_nao_violentos = 0
    pontos_violentos,pontos_nao_violentos = calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos)
    crimes_violentos_2021 = pontos_violentos
    crimes_nao_violentos_2021 = pontos_nao_violentos 
 

#ARQUIVO JAN 2022
with open("jan-22.csv", "r", encoding="utf-8") as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=";")
    pontos_violentos = 0
    pontos_nao_violentos = 0
    pontos_violentos,pontos_nao_violentos = calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos)
    crimes_violentos_2022 = pontos_violentos
    crimes_nao_violentos_2022 = pontos_nao_violentos 
   

#ARQUIVO JAN 2023
with open("jan-23.csv", "r", encoding="utf-8") as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=";")
    pontos_violentos = 0
    pontos_nao_violentos = 0
    pontos_violentos,pontos_nao_violentos = calc_crimes(csv_reader,pontos_violentos,pontos_nao_violentos)
    crimes_violentos_2023 = pontos_violentos
    crimes_nao_violentos_2023 = pontos_nao_violentos 


crimes_violentos = {"2021":crimes_violentos_2021, "2022": crimes_violentos_2022, "2023": crimes_violentos_2023}
crimes_nao_violentos = {"2021":crimes_nao_violentos_2021, "2022": crimes_nao_violentos_2022, "2023": crimes_nao_violentos_2023}
print("---------------------------------------------------")
print("Indicadores globais por ano")
print("---------------------------------------------------")
print("Crimes Violentos")
print("- 2021:",crimes_violentos["2021"])
print("- 2022:",crimes_violentos["2022"])
print("- 2023:",crimes_violentos["2023"])
print()
print("Crimes Não Violentos")
print("- 2021:",crimes_nao_violentos["2021"])
print("- 2022:",crimes_nao_violentos["2022"])
print("- 2023:",crimes_nao_violentos["2023"])


def calc_pontos_cidades(csv_reader,cidade_pontos_nao_violentos,cidade_pontos_violentos):
    
    for linha in csv_reader:
        pontos_violentos = (
            int(linha['Vitimas de Homicidio Doloso']) * 10 +
            int(linha['Vitimas de Latrocinio']) * 10 +
            int(linha['Vitimas de Lesao Corp Seg Morte']) * 10 +
            int(linha[' Roubo de Veiculo']) * 3 +
            int(linha[' Roubos']) * 2 +
            int(linha[' Delitos Relacionados a Armas e Municoes']) * 2 +
            int(linha[' Entorpecentes Trafico']) * 5
        )
        
        pontos_nao_violentos = (
            int(linha[' Entorpecentes Posse']) * 2 +
            int(linha['Furto de Veiculo ']) * 3 +
            int(linha[' Furtos']) * 3 +
            int(linha[' Estelionato']) * 1
        )
        
        cidade = linha['Municipios']
        
        cidade_pontos_violentos = pontos_violentos, cidade
        cidade_pontos_nao_violentos = pontos_nao_violentos

    return cidade_pontos_nao_violentos, cidade_pontos_violentos


def imprime_dados(top_n_cidades_violentos,top_n_cidades_nao_violentos,cidade_pontos_nao_violentos,cidade_pontos_violentos):
    
    top_n_cidades_violentos = sorted(cidade_pontos_violentos, key=cidade_pontos_violentos.get, reverse=True)[:top_n_cidades_violentos]
    top_n_cidades_nao_violentos = sorted(cidade_pontos_nao_violentos, key=cidade_pontos_nao_violentos.get, reverse=True)[:top_n_cidades_nao_violentos]
    
    return top_n_cidades_violentos,top_n_cidades_nao_violentos



with open('jan-21.csv', 'r', encoding='utf-8') as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=";")
    cidade_pontos_nao_violentos = []
    cidade_pontos_violentos = []
    top_n_cidades_violentos = 20
    top_n_cidades_nao_violentos = 7
  

    cidade_pontos_nao_violentos, cidade_pontos_violentos = calc_pontos_cidades(csv_reader,cidade_pontos_nao_violentos,cidade_pontos_violentos)
    top_n_cidades_violentos,top_n_cidades_nao_violentos = imprime_dados(top_n_cidades_violentos,top_n_cidades_nao_violentos,cidade_pontos_nao_violentos,cidade_pontos_violentos)
    
with open('jan-22.csv', 'r', encoding='utf-8') as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=";")
    cidade_pontos_nao_violentos = {}
    cidade_pontos_violentos = {}
    top_n_cidades_violentos = 20
    top_n_cidades_nao_violentos = 7
  

    cidade_pontos_nao_violentos1, cidade_pontos_violentos1 = calc_pontos_cidades(csv_reader,cidade_pontos_nao_violentos,cidade_pontos_violentos)
    top_n_cidades_violentos,top_n_cidades_nao_violentos = imprime_dados(top_n_cidades_violentos,top_n_cidades_nao_violentos,cidade_pontos_nao_violentos,cidade_pontos_violentos)
    

with open('jan-23.csv', 'r', encoding='utf-8') as arquivo:
    csv_reader = csv.DictReader(arquivo, delimiter=";")
    cidade_pontos_nao_violentos = {}
    cidade_pontos_violentos = {}
    top_n_cidades_violentos = 20
    top_n_cidades_nao_violentos = 7
  

    cidade_pontos_nao_violentos2, cidade_pontos_violentos2 = calc_pontos_cidades(csv_reader,cidade_pontos_nao_violentos,cidade_pontos_violentos)
    top_n_cidades_violentos,top_n_cidades_nao_violentos = imprime_dados(top_n_cidades_violentos,top_n_cidades_nao_violentos,cidade_pontos_nao_violentos,cidade_pontos_violentos)
    
  

x = 0

for cidade in (top_n_cidades_violentos):
    pontos_violentos = cidade_pontos_violentos[1] + cidade_pontos_violentos1[1] + cidade_pontos_nao_violentos2[1]
    print(f'{x+1} - {cidade}: {pontos_violentos}')
    x += 1


x = 0
for cidade in top_n_cidades_nao_violentos:
    pontos_nao_violentos = cidade_pontos_nao_violentos[1] 
    print(f'{x+1} - {cidade}: {pontos_nao_violentos}')
    x += 1