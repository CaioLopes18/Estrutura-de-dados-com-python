from tkinter import * 
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

root = Tk()

root.title("Endereço")
root.geometry("700x500")

#Criando o frame e estabelecendo configurações
arq = Frame(root)
arq.place(relx=0.05,rely=0.05,relwidth=0.9,relheight=0.9)
arq.pack(fill='both', expand=True)

#Criando texto
text = Label(arq, font = "Quicksand 12",text="Cidades:\n0 - Criciúma  1 - Forquilinha  2 - Maracajá\n3 - Araranguá  4 - Meleiro  5 - Sombrio  6 - Turvo\n7 - Jacinto Machado  8 - Timbé do Sul")
text.place(relx=0.27,rely=0.1,)

#Criando espaço para input no frame
inp = Entry(arq)
inp.configure(font = "Quicksand 12", bg = "white")
inp.place(relx=0.37,rely=0.3,relwidth=0.3,relheight=0.05)

inp2 = Entry(arq)
inp2.configure(font = "Quicksand 12", bg = "white")
inp2.place(relx=0.37,rely=0.4,relwidth=0.3,relheight=0.05)

#função que chama o grafo com networkx
def grafos():
   no_inicial = int(inp.get())
   no_final = int(inp2.get())

   distancias = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
               [4, 0, 4, 0, 0, 0, 0, 10, 7 ],
               [0, 4, 0, 5, 0, 16, 0, 0, 2 ],
               [0, 0, 5, 0, 9, 12, 0, 0, 0],
               [0, 0, 0, 9, 0, 10, 0, 0, 0],
               [0, 0, 16, 12, 10, 0, 2, 0, 0],
               [0, 0, 0, 0, 0, 2, 0, 1, 6 ],
               [8, 10, 0, 0, 0, 0, 1, 0, 7],
               [0, 7, 2, 0, 0, 0, 6, 7, 0]]

   posi = {0:[0,1],1:[1,2] ,2:[2,2] ,3:[3,2] ,4:[4,1] ,5:[3,0] ,6:[2,0] ,7:[1,0],8:[2,1]}

   G = nx.from_numpy_array(np.array(distancias))
   nx.draw_networkx(G,posi,node_color="white",edgecolors= "black")

   caminho_minimo = nx.dijkstra_path(G,no_inicial,no_final)
   arcos_caminho = [(caminho_minimo[i],caminho_minimo[i+1]) for i in range (len(caminho_minimo)-1)]

   cor_dos_arcos = []
   for arco in G.edges():
      rev = []
      rev = arco[1],arco[0]
      if arco in arcos_caminho or rev in arcos_caminho:
         cor_dos_arcos.append("red")
      else:
         cor_dos_arcos.append("black")

   posiCidades = {0:[0,1.15],1:[1,2.15] ,2:[2,2.15] ,3:[3,2.15] ,4:[4,1.15] ,5:[3,-0.15] ,6:[2,-0.15] ,7:[1,-0.15],8:[2,-1.015]}
   cidades={0:"Criciúma",1:"Forquilinha",2:"Maracajá",3:"Araranguá",4:"Meleiro",5:"Sombrio", 6:"Turvo",7:"Jacinto Machado",8:"Timbé do Sul"}
   nx.draw_networkx_labels(G,pos=posiCidades, labels=cidades,font_size=10,font_color="black")

   grafo_labels = nx.get_edge_attributes(G,'weight')
   nx.draw_networkx_edge_labels(G, pos=posi,edge_labels = grafo_labels)#valores distancias



   nx.draw_networkx(G,posi,node_color="white",edgecolors= "black", edge_color=cor_dos_arcos)
   plt.title("Grafo")
   plt.show()
#Criando botão para imprimir
botao_enviar = Button(arq,text="Calcular Distancia",command=grafos)
botao_enviar.place(relx=0.36,rely=0.8,relwidth=0.3,relheight=0.1)
root.mainloop()