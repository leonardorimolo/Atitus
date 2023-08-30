class Piloto:
    def __init__(self,nome:str,breve:int,horas_voo:int):
        self.nome = nome
        self.breve = breve
        self.horas_voo = horas_voo


    def realizar_voo(self,horas_voadas:int):
        self.horas_voo = self.horas_voo + horas_voadas


    def __str__(self):
        return f'Piloto: {self.nome} , Breve: {self.breve}, Possui {self.horas_voo} horas de voo'



class Aviao:

    def __init__(self,marca:str,modelo:str,capacidade:int,minimo_horas:int):
        self.marca = marca
        self.modelo = modelo
        self.capacidade = capacidade
        self.minimo_horas = minimo_horas
        self.piloto = None


    def inserir_piloto(self,piloto:Piloto):
        if piloto.horas_voo >= self.minimo_horas: #Verifica se o piloto informado possui o m´ınimo de horas de voo necessarias para pilotar aquele avião
            self.piloto = piloto #Piloto é adicionado ao avião
            print(f"O piloto {piloto.nome} é o novo piloto do {self.marca}-{self.modelo}")
            return True
        else: #Caso o piloto não possua experiencia necessária para pilotar o avião
            print(f"O piloto {piloto.nome} não está autorizado a pilotar esse avião")
            return False
        
        
        
    def voar(self,tempo_voo:int):
        if self.piloto is not None: #Testando se tem um piloto no avião
            print(f"{self.marca} - {self.modelo} decolado com o Piloto {self.piloto.nome}")
            Piloto.realizar_voo(self.piloto,20)
        else:
            print("Impossível voar! Não tenho Piloto")
            
            
    def __str__(self):
        mensagem = f'Avião {self.marca} - {self.modelo} com capacidade para {self.capacidade} passageiros'
        if self.piloto is not None:
            return f'{mensagem} \n Pilotado por: {self.piloto.nome}'
        else:
            return f'{mensagem} \n Não possui piloto'
            
            



##############################################################################################################
print('\n')
print("---------- IMPRIMINDO AS INFORMAÇÕES DOS PILOTOS E DOS AVIÕES ----------")
print('\n')
#INFORMACAO DOS PILOTOS
print('Informações dos Pilotos!\n')
piloto1 = Piloto('José da Silva',123456,2000)
print(f'Piloto 1:  {piloto1}\n')
piloto2 = Piloto('Maria das Graças',456789,19350)
print(f'Piloto 2:  {piloto2}')
print('\n\n\n')


#INFORMAÇAO DOS AVIÕES
print('Informações dos Aviões!\n')
aviao1 = Aviao('Boeing','737',215,1000)
print(f'Avião 1:  {aviao1}\n')
aviao2 = Aviao('AirBus','A320',200,3000)
print(f'Avião 2:  {aviao2}\n')
aviao3 = Aviao('Northrop','f5',1,30000)
print(f'Avião 3:  {aviao3}\n\n')



#Fazendo com que o piloto 1 se torne piloto dos 3 aviões
print('\n\n')
print('------------------------------------------------------------------------\n\n')
print('--Fazendo com que o piloto 1 se torne piloto dos 3 aviões!--\n')
aviao1.inserir_piloto(piloto1)
aviao2.inserir_piloto(piloto1)
aviao3.inserir_piloto(piloto1)
print('\n\n')


#Fazendo com que o piloto 2 se torne piloto do avião 2 e 3
print('--Fazendo com que o piloto 2 se torne piloto do avião 2 e 3--\n')
aviao2.inserir_piloto(piloto2)
aviao3.inserir_piloto(piloto2)
print('\n\n\n')


#Imprimindo novamente as informações dos Aviões
print('--Imprimindo novamente as informações dos Aviões!--\n')
print(f'Avião 1:  {aviao1}\n')
print(f'Avião 2:  {aviao2}\n')
print(f'Avião 3:  {aviao3}\n\n')
print('------------------------------------------------------------------------\n\n')


#Fazendo os 3 aviões voarem por 20 horas
print('--Fazendo os 3 aviões voarem por 20 horas--\n')
aviao1.voar(20)
aviao2.voar(20)
aviao3.voar(20)
print('\n\n')

print('--Imprimindo os dados dos pilotos para conferir o aumento no número de horas de voo--\n\n')
print(f'Piloto 1:  {piloto1}\n')
print(f'Piloto 2:  {piloto2}\n\n')
print('------------------------------------------------------------------------\n\n')



print('--Aumentando o número de horas de voo de um dos Pilotos--\n\n')
piloto2.realizar_voo(12000)
aviao3.inserir_piloto(piloto2)
aviao3.voar(5)


                
