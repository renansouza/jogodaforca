# Jogo da forca - Professor Tiago Menegaz
# Desenvolvido por: Renan, Elias e Karine

# Algoritmo do jogo

# Passo 1 -  Cadastrar o nome do jogador em arquivo
# Passo 2 - Solicitar ao jogador o tema de sua preferência
# Passo 3 - Para cada letra errada, desenhar um membro na forca, caso contrário não desenhar nada
# Passo 4 - Contar a quantidade de tentativas do jogador e armazenar em um arquivo
# Passo 5 - Salvar as palavras que o jogador acertou em seu arquivo

print ("#"*100)
print(" "*35, "BEM VINDO AO JOGO DA FORCA", " "*35)
print("#"*100)

# Solicita o nome do jogador, e armazena em um arquivo

print("\n")
player = input("Por favor, informe seu nome: \n")

gravanome = open("players/"+player+".txt", "a")

theme = input("Escolha entre os temas seguintes: 1 - Computação 2- Matemática: \n")

