import os
os.system("cls")
class staticStack:
    def __init__(self,size):
        self.maxSize = size
        self.stack = [None] * size
        self.top = -1

    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.maxSize- 1
    
    def stackUp(self,item):
        os.system("cls")
        if self.isFull():
            print("Erro: a pilha está cheia\n")
        else: 
            self.top += 1
            self.stack[self.top] = item

    def unstack(self):
        os.system("cls")
        if self.isEmpty():
            print("Erro: a pilha está vazia\n")
        else:
            value = self.stack[self.top]
            self.top -= 1
            print(f"Item desempilhado: {value}")

    def printTopStack(self):
        os.system("cls")
        if self.isEmpty():
            print("Erro: a pilha está vazia\n")
        else:
            print(f"Topo da Pilha: {self.stack[self.top]}")


print("Defina um tamanho para sua pilha\n")
size = int(input(""))
stack = staticStack(size)

while True:
    
    print("""
1 - Inserir item na pilha
2 - Printar topo da pilha
3 - Desempilhar pilha
""")
    f = int(input(""))
    if f == 1:
        item = input("insira um item\n")
        stack.stackUp(item)
    elif f == 2:
        stack.printTopStack()
    elif f == 3:
        stack.unstack()
    
    elif f == 0:
        print("encerrando...\n")
        break