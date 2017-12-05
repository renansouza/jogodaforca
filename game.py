# Jogo da forca - Professor Tiago Menegaz
# Desenvolvido por: Renan, Elias e Karine

# Algoritmo do jogo

# Passo 1 -  Cadastrar o nome do jogador em arquivo
# Passo 2 - Solicitar ao jogador o tema de sua preferência
# Passo 3 - Para cada letra errada, desenhar um membro na forca, caso contrário não desenhar nada
# Passo 4 - Contar a quantidade de tentativas do jogador e armazenar em um arquivo
# Passo 5 - Salvar as palavras que o jogador acertou em seu arquivo

#!/usr/bin-/python
# -*- coding: utf-8 -*-

print ("#"*100)
print(" "*35, "BEM VINDO AO JOGO DA FORCA", " "*35)
print("#"*100)

# Solicita o nome do jogador, e armazena em um arquivo

print("Por favor, informe o seu nome: ")
player = input()

gravanome = open("players/" + player + ".txt", "w", encoding="utf-8")

# Escreve o nome do jogador dentro do arquivo criado

gravanome.write("O nome do jogador é: " + player + "\n\n")
gravanome.write("-" * 100 + "\n")

# Solicita o tema para o jogador e armazena o valor em uma variável

print("Qual o tema você prefere?\n")
print("1-) Tecnologia 2-) Futebol")

tema = input()

if tema == "1":
    tecnologia = open("temas/computacao.txt")
elif tema == "2":
    futebol = open("temas/futebol.txt")


