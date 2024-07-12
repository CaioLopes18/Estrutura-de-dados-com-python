import os
os.system("cls")

class List:
    def __init__(self):
        self.list = []

    def insertItem(self):
        os.system("cls")
        print("A - Adicionar elemento")
        print("B - Adicionar elemento pelo indice")
        Add = input()
        if Add.upper() == "A":
            Element = input("Insira o elemento desejado\n")
            self.list.append(Element)
            print("Elemento inserido com sucesso")
        else:
            Element = input("Insira o elemento desejado\n")
            Index = int(input("Insira o indice que deseja ser insirido\n"))
            self.list.insert(Index, Element)
            print("Elemento inserido com sucesso")

    def searchItem(self):
        os.system("cls")
        print("A - pesquisar elemento pelo nome")
        print("B - pesquisar elemento pelo indice")
        Search = input()
        if Search.upper() == "A":
            Element = input("Insira o elemento que você deseja pesquisar\n")
            if Element in self.list:
                print(f"Elemento está na lista no indice {self.list.index(Element)}")
            else:
                print("O elemento não está na lista")
        else:
            IndexOfElement = int(input("Insira o indice que você deseja pesquisar o elemento\n"))
            if 0 >= IndexOfElement or IndexOfElement <= len(self.list):
                print(f"O elemento encontrado no indice {IndexOfElement} foi: {self.list[IndexOfElement]}")
            else:
                print("Indice maior do que a lista")


    def deleteItem(self):
        os.system("cls")
        print("A - Deletar elemento pelo nome")
        print("B - Deletar elemento pelo indice")

        Delete = input()
        if Delete.upper() == "A":

            DeletedElement = input("Insira o elemento que você deseja deletar\n")
            if DeletedElement in self.list:
                self.list.remove(DeletedElement)
                print("Elemento deletado com Sucesso")
            else:
                print("Elemento não encontrado, tente novamente")
        else:
            DeletedIndex = int(input("Insira o indice que você deseja deletar\n"))
            if 0 >= DeletedIndex or DeletedIndex <= len(self.list):
                self.list.pop(DeletedIndex)
                print("Elemento deletado com sucesso")
            else:
                print("Indice não encontrado")
        
    def printList(self):
        os.system("cls")
        if len(self.list) == 0:
            print("Lista vazia tente adicionar algo")
        else:
            print("Indice / Elemento")
            for i in self.list:
                print(      f"{self.list.index(i)}  -  {i}")

list = List()

while True:
    print("""
======Operações com lista======
1 - Inserir elementos na lista
2 - Pesquisar elementos na lista
3 - Excluir elementos de uma lista
4 - Imprimir a lista
0 - Encerrar o programa""")
    function = int(input("Insira o número da função que deseja executar\n"))

    if function == 1:
        list.insertItem()

    elif function == 2:
        list.searchItem()

    elif function == 3:
        list.deleteItem()

    elif function == 4:
        list.printList()

    elif function == 0:
        print("fechando...")
        break
    else:
        os.system("cls")
        print("entrada invalida,tente novamente")