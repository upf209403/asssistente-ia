numero = 8

def define_numero():
    global numero 
    numero = 5
    return numero
    
rodando = True

while rodando:
    nome = input("Digite um nome: ")

    if(nome):
        print(nome)

        if(nome.lower()[0] == "z"):
            rodando = False
            print("Programa finalizado")
    else:
        print("String vazia")