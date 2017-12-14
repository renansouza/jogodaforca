# Jogo da forca - Professor Tiago Menegaz
# Desenvolvido por: Renan, Elias e Karine

# Algoritmo do jogo

# Passo 1 - Cadastrar o nome do jogador em arquivo
# Passo 2 - Solicitar ao jogador o tema de sua preferência
# Passo 3 - Para cada letra errada, desenhar um membro na forca, caso contrário não desenhar nada
# Passo 4 - Contar a quantidade de tentativas do jogador e armazenar em um arquivo
# Passo 5 - Salvar as palavras que o jogador acertou em seu arquivo

#!/usr/bin-/python
# -*- coding: utf-8 -*-

import random

# Solicita o nome do jogador, e armazena em um arquivo

def player():

    player = input("Por favor, informe o seu nome:\n")

# Escreve o nome do jogador dentro do arquivo criado

    gravanome = open("players/" + player + ".txt", "w", encoding="utf-8")
    gravanome.write("O nome do jogador é: " + player + "\n\n")
    gravanome.write("-" * 100 + "\n")
    gravanome.close()
    return player

# Solicita o tema para o jogador e armazena o valor em uma variável

def theme(player):


    tema = input("Qual o tema você prefere?\n "
                 "1-) Tecnologia 2-) Futebol\n")

    if tema == "1":

        tecnologia = open("temas/computacao.txt", encoding="utf-8")
        gravanome = open("players/" + player + ".txt", "a", encoding="utf-8")

        gravanome.write("\nO tema escolhido é tecnologia\n")

        busca = [] ## guarda as perguntas de computação
        tentativas = 0
        resposta = []

        perguntas = tecnologia.readlines()

        for e in range(0, len(perguntas), 2):
            busca.append(str(perguntas[e])[:-1])

        # ajuste para a 1ª posição
        busca[0] = busca[0][1:]
        pergunta = list(random.choice((busca)))
        pergunta = (''.join(pergunta)).strip()
        print(pergunta, end="\t")

        for i, v in enumerate(perguntas):
            if str(v).strip() == pergunta:
                resposta = perguntas[i+1][:-1]

                for l in range(len(resposta)):
                    print('#', sep='', end="")
                # cont = 0
                # while cont <= len(resposta):
                #     teste = input()




    elif tema == "2":

        futebol = open("temas/futebol.txt")
        gravanome = open("players/" + player + ".txt", "a", encoding="utf-8")
        gravanome.write("\n")
        gravanome.write("O tema escolhido é futebol ")
        gravanome.write("\n")
        gravanome.close()

def game():

    print ("#"*100)
    print(" "*35, "BEM VINDO AO JOGO DA FORCA", " "*35)
    print("#"*100)

    theme(player())

# Chama game

if __name__ == '__main__':
    game()