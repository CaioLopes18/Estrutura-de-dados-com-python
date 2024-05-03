import os
lista = []
os.system("cls")
while True:
    print("1 - Inserir elementos na lista")
    print("2 - Pesquisar elementos na lista")
    print("3 - Excluir elementos de uma lista")
    print("4 - Imprimir a lista")
    print("0 - Encerrar o programa")

    Funcao = input("")
    
    #script para adicionar elementos
    if Funcao == "1":
        os.system("cls")
        print("A - Adicionar elemento pelo nome")
        print("B - Adicionar elemento pelo indice")
        
        Adicionar = input()
        if Adicionar == "a" or Adicionar == "A":
            Elemento = input("Insira o elemento desejado\n")
            lista.append(Elemento)
            print("Elemento inserido com sucesso")
        else:
            Elemento = input("Insira o elemento desejado\n")
            Indice = int(input("Insira o indice que deseja ser insirido\n"))
            lista.insert(Indice, Elemento)
            print("Elemento inserido com sucesso")


    #script para pesquisar elementos 
    elif Funcao == "2":
        os.system("cls")
        print("A - pesquisar elemento pelo nome")
        print("B - pesquisar elemento pelo indice")

        Pesquisa = input()
        if Pesquisa == "A" or Pesquisa == "a":
            Elemento = input("Insira o elemento que você deseja pesquisar\n")
            if Elemento in lista:
                print("Elemento ja está na lista no indice",lista.index(Elemento))
            else:
                print("O elemento não está na lista")
        else:
            IndiceDoElemento = int(input("Insira o indice que você deseja pesquisar o elemento\n"))
            if 0 >= IndiceDoElemento or IndiceDoElemento <= len(lista):
                print("O elemento encontrado foi este:",lista[IndiceDoElemento])
            else:
                print("Indice não encontrado")


    #script para deletar 
    elif Funcao == "3":
        os.system("cls")
        print("A - Deletar elemento pelo nome")
        print("B - Deletar elemento pelo indice")

        Deletar = input()
        if Deletar == "A" or Deletar == "a":

            ElementoDeletado = input("Insira o elemento que você deseja deletar\n")
            if ElementoDeletado in lista:
                lista.remove(ElementoDeletado)
                print("Elemento deletado com Sucesso")
            else:
                print("Elemento não encontrado, tente novamente")
        else:
            IndiceDeletado = int(input("Insira o indice que você deseja deletar\n"))
            if 0 >= IndiceDeletado or IndiceDeletado <= len(lista):
                lista.pop(IndiceDeletado)
                print("Elemento deletado com sucesso")
            else:
                print("Indice não encontrado")


    elif Funcao == "4":
        os.system("cls")
        print("Lista completa impressa:")
        for elemento in lista:  
            print(elemento)


    elif Funcao == "0":
        os.system("cls")
        print("Programa encerrado")   
        break
