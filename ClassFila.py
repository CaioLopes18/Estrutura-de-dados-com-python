#atividade fila em python
#1 - cadastrar o pedido feito pelo cliente e adiciona este pedido á fila de pedidos
#2 - mostra o pedido assim que o usuário der um ok remove o pedido da fila e retorna o próximo pedido da fila para ser processado, se não houver pedidos na fila, deve retornar uma mensagem indicando que não há pedidos pendentes
#3 - exibe todos os pedidos pendentes 

import os
from collections import deque
os.system("cls")

class Queue:
    def __init__(self):
        self.queue= deque()
    
    def addOrder(self,order):
        self.queue.append(order)

    def processOrder(self):
        if len(self.queue) == 0:
            os.system("cls")
            print("Você está sem pedidos no momento, tente adicionando um\n")
        else:
            processedOrder = self.queue.popleft()
            print(f"Primeiro pedido da fila concluido, pedido:\n{processedOrder}")

            if len(self.queue) == 0:
                print("Você está sem pedidos no momento, você concluiu todos da fila\n")
            else:
                print(f"Proximo pedido a ser feito:\n{self.queue[0]}")

    def showOrders(self):
        if len(self.queue)==0:
              os.system("cls")
              print("Você está sem pedidos no momento :( ")
        else:
            print("Ordem dos pedidos:")
            for elemento in self.queue:
                print(f"{self.queue.index(elemento)+1}° - {elemento}")

queue = Queue()
while True:

    print("-------------------\n"
      "      CARDAPIO\n"
      "-------------------\n"
      "Hamburger - 10,90\n"
      "Batata - 04,90\n"
      "Refri 500ml 5,50\n"
      "-------------------")
    print("1 - Inserir pedido\n"
      "2 - Processar pedido\n"
      "3 - Mostrar pedidos\n"
      "0 - Fechar")
    funcao = int(input())

    if funcao==1:
        os.system("cls")
        order = input("Insira o pedido\n")
        queue.addOrder(order)

    elif funcao==2:
        os.system("cls")
        queue.processOrder()

    elif funcao==3:
        os.system("cls")
        queue.showOrders()

    elif funcao==0:
         os.system("cls")
         print("programa encerrado")
         break
    
    else:
         os.system("cls")
         print("entrada invalida,tente novamente")

