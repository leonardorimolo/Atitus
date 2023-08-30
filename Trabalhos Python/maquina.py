class Maquina:
    def __init__(self, preco_ticket):
        self.preco_ticket = preco_ticket
        self.total_arrecadado = 0
        self.valor_inserido = 0

    def inserir_dinheiro(self):

        moedas = 5

        while moedas != -1:
            moedas = int(input("Informe a moeda [-1 para parar]: "))
            if moedas != -1:
                self.valor_inserido = self.valor_inserido + moedas

    def imprimir_ticket(self):
        if self.valor_inserido == self.preco_ticket:
            self.total_arrecadado = self.valor_inserido
            self.valor_inserido = 0
            print("###################")
            print("      TICKET       ")
            print("###################")
            print(f"   {self.preco_ticket} centavos   ")


        elif self.valor_inserido > self.preco_ticket:
            troco = self.valor_inserido - self.preco_ticket
            self.total_arrecadado = self.valor_inserido - troco
            print("###################")
            print("      TICKET       ")
            print(f"   {self.preco_ticket} centavos   ")
            print(f"Troco: {troco} centavos ")
            print("###################")

            self.valor_inserido = 0




        elif self.valor_inserido < self.preco_ticket:
            print(
                f"O dinheiro inserido na máquina ({self.valor_inserido} centavos) é insuficiente. Preço do Ticket: {self.preco_ticket} centavos")


def Menu(valor_inserido):
    print(f"MÁQUINA DE TICKETS: [possuo {valor_inserido} centavos]")
    print('[a] Inserir Moedas')
    print("[b] Imprimir Ticket")
    print("[x] Encerrar Operação")
    opcao = input("?")

    return opcao


# MAIN

preco_ticket = int(input("Informe o preco do ticket:"))
main = Maquina(preco_ticket)

opcao = 'z'
while opcao != 'x':
    opcao = Menu(main.valor_inserido)

    match opcao:
        case "a":
            main.inserir_dinheiro()
            print(main.valor_inserido)

        case 'b':
            main.imprimir_ticket()

        case 'x':
            print(f'Total Arrecadado: {main.total_arrecadado}')
