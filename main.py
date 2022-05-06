from ia import*
import os
import random

def main():

    ligar = True
    while ligar == True:
        if os.system == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        print("┌","─"*15,"┐""\n│ Jogo da Velha │\n└","─"*15,"┘\n",sep= "")
        tabuleiro = [
            [" "," "," "],
            [" "," "," "],
            [" "," "," ",],
        ]
        jogador2 = input("Você deseja jogar com 'X' ou 'O'? ").upper().replace(" ","")
        while jogador2 != "X" and jogador2 != "O":            
            print("\nPor favor digite uma opção válida!")
            jogador2 = input("Você deseja jogar com 'X' ou 'O'? ").upper().replace(" ","")
        if jogador2 == "X": jogador1 = "O"
        else: jogador1 = "X"
        if os.system == 'nt':
            os.system("cls")
        else:
            os.system("clear")
        dificuldade = 0
        while dificuldade < 1 or dificuldade > 2:
            try:                
                dificuldade = int(input("Selecione uma dificuldade:\n\nNormal = 1\nImpossível = 2\n\nDigite: "))
                if dificuldade < 1 or dificuldade > 2: print("\nPor favor digite uma opção válida!")
            except: print("\nApenas números sao aceitos!")
        
        partida(tabuleiro,jogador1, jogador2,dificuldade)
        
        continuar = input("Deseja continuar jogando? (\033[032ms\033[m/\033[031mn\033[m): ")
        if continuar == "n":
            ligar = False
        while continuar not in "sn" or len(continuar) != 1:            
            print("\nPor favor digite uma opção válida!")
            continuar = input("Deseja continuar jogando? (\033[032ms\033[m/\033[031mn\033[m): ")
            if continuar == "n":
                ligar = False

def print_tabuleiro(tabuleiro):
    if os.system == 'nt':
            os.system("cls")
    else:
        os.system("clear")
    print("\n    A   B   C")
    print("  ╭───┬───┬───╮")
    for i in range(3):
        for j in range(3):
            if j == 0 and i == 0:
                print(f"1 │ {tabuleiro[i][j]} │ ",end="")
            elif j == 0 and i == 1:
                print(f"2 │ {tabuleiro[i][j]} │ ",end="")
            elif j == 0 and i == 2:
                print(f"3 │ {tabuleiro[i][j]} │ ",end="")
            else:
                print(f"{tabuleiro[i][j]} │ ",end="")
        print()
        if i == 2:
            print("  ╰───┴───┴───╯\n")
        else:
            print("  ├───┼───┼───┤")

def partida(tabuleiro, j1, j2,d):
    print_tabuleiro(tabuleiro)
    jogando = True
    contador = 1    
    z = random.randint(0,1)
    
    while jogando == True:
        if z == 1:
            if contador%2 == 1:
                jogador = j2
                l,c = receber_jogada(tabuleiro)
            else: 
                jogador = j1
                l,c = inteligencia(tabuleiro,j1,j2,jogador,d)
        else:
            if contador%2 == 1:
                jogador = j1
                l,c = inteligencia(tabuleiro,j1,j2,jogador,d)
            else:
                jogador = j2
                l,c = receber_jogada(tabuleiro)
        
        tabuleiro[l][c] = jogador
        resultado = verificar_resultado(tabuleiro)

        if resultado == 0:
            contador +=1
            print_tabuleiro(tabuleiro)            
        elif resultado == 1:
            print_tabuleiro(tabuleiro)
            if jogador == j1: 
                print("Que pena, você perdeu!\n")
            else:
                print("Parabéns, você ganhou!\n")
            jogando = False
        else:
            print_tabuleiro(tabuleiro)
            print("Deu velha!\n")
            jogando =  False  

def receber_jogada(tabuleiro):
    possiveis = ["1A", "1B", "1C",
                 "2A", "2B", "2C",
                 "3A", "3B", "3C"]
    recebendo_jogada = True
    while recebendo_jogada == True:
        jogada = input("Digite sua jogada (Ex: 1a): ").upper().replace(" ","")
        if jogada in possiveis:
            linha, coluna = int(jogada[0])-1 , jogada[1]
            if coluna == "A": coluna = 0
            elif coluna == "B": coluna = 1
            else: coluna = 2
            if tabuleiro[linha][coluna] == " ":
                recebendo_jogada = False
    return linha, coluna

def verificar_resultado(t):
    for i in range(3): #linhas
        if t[i][0] == t[i][1] and t[i][1] == t[i][2] and t[i][0] != " ":            
            return 1
    for i in range(3): #colunas
        if t[0][i] == t[1][i] and t[1][i] == t[2][i] and t[0][i] != " ":            
            return 1
    #diagonais
    if t[0][0] == t[1][1] and t[1][1] == t[2][2] and t[1][1] != " ":       
        return 1
    if t[0][2] == t[1][1] and t[1][1] == t[2][0] and t[1][1] != " ":       
        return 1

    velha = True
    for i in range(3):
        for j in range(3):
            if t[i][j] == " ":
                velha = False
    if velha: return 2
    return 0

if __name__ == "__main__":
    main()