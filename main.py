import random
matriz = [[' ',' ',' '],[' ',' ',' '],[' ',' ',' ']]

def tabuleiro(matriz):
    for item in range(3):
        print(f' {matriz[item][0]} | {matriz[item][1]} | {matriz[item][2]} ')
        if item <= 1:
            print("---+---+---")


def jogada_humano(matriz):
    while True:
        linha = int(input('Digite a linha que deseja jogar: ')) - 1
        while 0 > linha or linha > 2:
            linha = int(input('LOCAL INVÁLIDO. Digite a linha que deseja jogar: ')) - 1
            
        coluna = int(input('Digite a coluna que deseja jogar: ')) - 1
        while 0 > coluna or coluna > 2:
            coluna = int(input('LOCAL INVÁLIDO. Digite a coluna que deseja jogar: ')) - 1
            
        if matriz[linha][coluna] == ' ':
            matriz[linha][coluna] = 'X'
            break
        else:
            print('Posição já ocupada')
            continue


def jogada_pc(matriz):
    while True:
        linha_computador = random.randint(0,2)
        print(f'Linha escolhida pelo computador: {linha_computador+1}')
        
        coluna_computador = random.randint(0,2)
        print(f'Coluna escolhida pelo computador: {coluna_computador+1}')

        if matriz[linha_computador][coluna_computador] == ' ':
            matriz[linha_computador][coluna_computador] = 'O'
            print(f'Computador jogou na linha {linha_computador + 1} na coluna {coluna_computador + 1}')
            break
        else:
            print('Posição escolhida pelo computador já está ocupada.')
            continue
    

def verificador_do_vencedor(matriz):
    for linha in matriz:
        if linha [0] == linha[1] == linha[2] and linha[0] != ' ':
            if linha[0] == 'X':
                print('Jogador venceu')
            else:
                print('Computador venceu')
            return True
    
    for coluna in range(3):
        if matriz[0][coluna] == matriz[1][coluna] == matriz[2][coluna] and matriz[0][coluna] != ' ':
            if matriz[0][coluna] == 'X':
                print('Jogador venceu')
            else:
                print('Computador venceu')
            return True
    
    # verificador da diagonal esquerda
    if matriz[0][0] == matriz[1][1] == matriz[2][2] and matriz[0][0] != ' ':
        if matriz[0][0] == 'X':
            print('Jogador venceu')
        else:
            print('Computador venceu')
        return True
    
    #verificador da diagonal direita
    if matriz[0][2] == matriz[1][1] == matriz[2][0] and matriz[0][2] != ' ':
        if matriz[0][2] == 'X':
            print('Jogador venceu')
        else:
            print('Computador venceu')
        return True

    return False
        

def main():
    print('Vamos começar!')
    contador = 0
    primeiro_jogador = random.randint(0,1)

    tabuleiro(matriz)

    while contador < 9:
        if (contador % 2 == 0 and primeiro_jogador == 0) or (contador % 2 == 1 and primeiro_jogador == 1):
            jogada_pc(matriz)
        else:
            jogada_humano(matriz)
        
        tabuleiro(matriz)
        if verificador_do_vencedor(matriz):
            break
        contador += 1

    if contador == 9 and not verificador_do_vencedor(matriz):
        print('Empate!')

main()
