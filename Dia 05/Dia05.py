#Projeto gerador de senhas
import random
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
simbolos = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem vindo ao gerador de senhas!")
qtd_letras = int(input(f"Quantas letras você quer incluir na sua senha?\n")) 
qtd_simbolos = int(input(f"Quantos símbolos especiais?\n"))
qtd_numeros = int(input(f"E quantos números?\n"))

#zerada inicialmente
senha = ''
novo_carac = ''

while(qtd_letras > 0 or qtd_simbolos > 0 or qtd_numeros > 0):
    categoria = random.randrange(0,3)
    if(categoria==0):
        if(qtd_letras == 0):
            continue
        else:
            index_sorteio = random.randrange(0,len(letras)+1)
            novo_carac = letras[index_sorteio]
            qtd_letras-=1
    elif(categoria==1):
        if(qtd_simbolos == 0):
            continue
        else:
            index_sorteio = random.randrange(0,len(simbolos)+1)
            novo_carac = simbolos[index_sorteio]
            qtd_simbolos-=1
    elif(categoria==2):
        if(qtd_numeros == 0):
            continue
        else:
            index_sorteio = random.randrange(0,len(numeros)+1)
            novo_carac = numeros[index_sorteio]
            qtd_numeros-=1
    senha += novo_carac

print(f"Sua senha gerada é: {senha}")


