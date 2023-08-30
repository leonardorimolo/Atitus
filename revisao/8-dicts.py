dicionario = {'Yan': '1234-5678', 
              'Pedro': '9999-9999', 
              'Ana': '8765-4321',
              'Marina': '8877-7788'}

print(dicionario['Pedro'])

dicionario['Joao'] = "1234-4567"

del dicionario["Yan"]

dicionario.pop('Ana')

for nome in dicionario:
    print(f"{nome} == {dicionario[nome]}")