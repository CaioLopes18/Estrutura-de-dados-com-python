#atividade fila em python
#1 - cadastrar o pedido feito pelo cliente e adiciona este pedido á fila de pedidos
#2 - mostra o pedido assim que o usuário der um ok remove o pedido da fila e retorna o próximo pedido da fila para ser processado, se não houver pedidos na fila, deve retornar uma mensagem indicando que não há pedidos pendentes
#3 - exibe todos os pedidos pendentes 

import os
from collections import deque
Fila = deque()
os.system("cls")
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
        pedido = input("Insira o pedido\n")
        Fila.append(pedido)
    elif funcao==2:
        os.system("cls")
        if len(Fila)==0:
            os.system("cls")
            print("Você está sem pedidos no momento, tente adicionando um\n")
        else:
            PedidoRemovido = Fila.popleft()
            print(f"Primeiro pedido da fila concluido, pedido:\n{PedidoRemovido}")
            if len(Fila)==0:
                print("Você está sem pedidos no momento, você concluiu todos da fila\n")
            else:
                print(f"Proximo pedido a ser feito:\n{Fila[0]}")
    elif funcao==3:
        os.system("cls")
        if len(Fila)==0:
              os.system("cls")
              print("Você está sem pedidos no momento :( ")
        else:
            print("Ordem dos pedidos:")
            for elemento in Fila:
                print(f"{Fila.index(elemento)+1}° - {elemento}")
    elif funcao==0:
         os.system("cls")
         print("programa encerrado")
         break
    else:
         os.system("cls")
         print("entrada invalida,tente novamente")

