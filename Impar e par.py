#Faça um Programa Python que leia uma frase (caracteres), e diga quantas vogais e consoantes foram lidas. Mostre a lista ao final.

ListaVogais = ["U","O","I","E","A"]

Frase = str(input("Insira uma frase: \n"))
Vogais = []
Consoantes = []
for elemento in Frase:
    if elemento == " ":
        None
    else:
        if elemento.upper() in ListaVogais:
            Vogais.append(elemento)
        else:
            Consoantes.append(elemento)

print(f"Quandidade de vogais: {len(Vogais)}")

print(f"Quandidade de consoantes: {len(Consoantes)}")