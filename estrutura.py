import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time


# o x aumenta de 20 em 20 e o y é 49-valor da range
POSICAO_Y = random.randrange(10,25,5)
POSICAO_X = 28

#Define a posição da bolinha
if (POSICAO_Y == 10):
    BOLINHA = [[POSICAO_Y+23, 15]] #10,20,15
elif (POSICAO_Y == 15):
    BOLINHA = [[POSICAO_Y+13, 15]]
elif (POSICAO_Y == 20):
    BOLINHA = [[POSICAO_Y+3, 15]]

def telacheia():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMIZE = 3
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_MAXIMIZE)

def main(stdscr):
    telacheia()
    
    curses.curs_set(0)
    stdscr.nodelay(1)
    stdscr.timeout(100)

    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3,sw-3]]
    win = curses.newwin(box[0][0], box[0][1], box[1][0], box[1][1])
    rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])
    
    #-------------------------COLUNAS E POSICAO INICIAL DA BOLA E PERSONAGEM---------------------------------

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    COR1 = curses.color_pair(1)
    text = 'O'

    PERSONAGEM_1_POSICAO = []
    for a in range(5):
        y = BOLINHA[0][0]
        x = BOLINHA[0][1]-9+a
        stdscr.addstr(y, x, "O") #+"\n"+"()"+"\n"+"| |"
        PERSONAGEM_1_POSICAO.insert(a, [y,x])


    SUPERFICIE_PREDIOS = []

    #Define a posição, altura e largura das colunas
    for i in range(1):
        for y in range(POSICAO_Y):
            for x in range(POSICAO_X):
                c = int(25)*int(i)
                alt = y+46-POSICAO_Y
                larg = x+4+c
                stdscr.addstr(alt, larg ,text ,COR1)
                mapear_y= 0
                mapear_x= 0
                SUPERFICIE_PREDIOS.insert(y, [alt, larg]) 

                #stdscr.addstr(y+47-posicao_y,x+25+c, '')
    
    for i in range(6):
        POSICAO_Y2 = random.randrange(10,25,5) 
        for y in range(POSICAO_Y2):
            for x in range(POSICAO_X):
                d = int(25)*int(i)+25
                alt = y+46-POSICAO_Y2
                larg = x+4+d
                stdscr.addstr(alt, larg, text, COR1)
                SUPERFICIE_PREDIOS.insert(y+POSICAO_Y, [alt, larg])

                #stdscr.addstr(y+47-posicao_y,x+25+c, '')

    for i in range(1):
        POSICAO_Y3 = random.randrange(10,25,5)
        for y in range(POSICAO_Y3):
            for x in range(28):
                a = int(25)*int(i)+175
                alt = y+46-POSICAO_Y3
                larg = x+4+a
                stdscr.addstr(alt, larg , text, COR1)
                SUPERFICIE_PREDIOS.insert(y+POSICAO_Y2, [alt, larg])


    if (POSICAO_Y3 == 10):
        BOLINHA2 = [[POSICAO_Y3+23, 200]] #10,20,15
    elif (POSICAO_Y3 == 15):
        BOLINHA2 = [[POSICAO_Y3+13, 200]]
    elif (POSICAO_Y3 == 20):
        BOLINHA2 = [[POSICAO_Y3+3, 200]]

    stdscr.addstr(BOLINHA2[0][0], BOLINHA2[0][1]-5, "OOOOOOO")
    PERSONAGEM_2_POSICAO = [BOLINHA2[0][0], BOLINHA2[0][1]-5]

    #--------------------------------TEXTBOX------------------------------
    curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_WHITE)
    COR = curses.color_pair(2)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    COR3 = curses.color_pair(3)

    JOGADOR = ["player_1", "player_2"]
    CONTADOR = 0
    PERDEU = 0

    while True:
        stdscr.addstr(1, 2, "Velocidade: ", COR3)
        stdscr.addstr(5, 2, "Angulo: ", COR3)

        editwin = curses.newwin(1, 20, 3, 3)
        stdscr.refresh()

        boxedit = Textbox(editwin)
        boxedit.edit()

        editwin2 = curses.newwin(1, 20, 8, 3)
        stdscr.refresh()

        boxedit2 = Textbox(editwin2)
        boxedit2.edit()

        velocidade = int(boxedit.gather())
        angulo = int(boxedit2.gather())
        gravidade = 9.8
        tempo = math.ceil((velocidade*velocidade)/2*gravidade)

        seno = math.sin(angulo)

        if seno < 0:
            seno = -math.sin(angulo)

        altura_maxima = math.ceil((velocidade*velocidade)/2*gravidade)
        alcance = math.ceil(((velocidade*velocidade*seno*2)/gravidade))
        metade_alcance = math.ceil(alcance/2)

        px= BOLINHA[0][1] # 15 + 1 // 16, 17, 18, 19
        py= BOLINHA[0][0] # 23 - 1 // 22,

        px2= BOLINHA2[0][1]-9
        py2= BOLINHA2[0][0]

        if JOGADOR[CONTADOR] == JOGADOR[0]:
            PERDEU_P = 0
            for y in range(metade_alcance):
                alt = py-y
                larg = px+y

                if alt > 0:
                    stdscr.addstr(alt, larg, 'oo', COR)
                    stdscr.refresh()
                    time.sleep(0.2)
                    stdscr.addstr(alt, larg, '  ')
                elif alt <= 0:
                    pass

                #for y in range(alcance):
                #    stdscr.addstr(py, px+y, 'F')
            for y in range(metade_alcance+10):
                alt = py+y-metade_alcance
                larg = px+y+metade_alcance
            
                if alt > 0:
                    if larg < box[1][1]:
                        stdscr.addstr(alt, larg, 'FF',COR)
                        stdscr.refresh()
                        time.sleep(0.2)
                        stdscr.addstr(alt, larg, '  ')
                elif alt <= 0:
                    if larg >= box[1][1]:
                        pass

                for c in range(len(SUPERFICIE_PREDIOS)):
                    ff = SUPERFICIE_PREDIOS[c]
                    if [alt, larg] == ff:
                        PERDEU_P = 1
                       

                for c in range(len(PERSONAGEM_1_POSICAO)):
                    a = PERSONAGEM_1_POSICAO[c]
                    if [alt, larg] == a:
                        stdscr.clear()
                        stdscr.addstr(sh-3, sw-3, 'GAME OVER',COR3)   
                        stdscr.refresh()
                        PERDEU_P = 1

                if PERDEU_P == 1:
                    break

            CONTADOR = 1

        elif JOGADOR[CONTADOR] == JOGADOR[1]:
            PERDEU = 0
            for y in range(metade_alcance):
                alt = py2-y
                larg = px2-y

                if alt > 0:
                    stdscr.addstr(alt, larg, 'oo', COR)
                    stdscr.refresh()
                    time.sleep(0.2)
                    stdscr.addstr(alt, larg, '  ')
                elif alt <= 0:
                    pass

                #for y in range(alcance):
                #    stdscr.addstr(py, px+y, 'F')
            for y in range(metade_alcance+10):
                alt = py2+y-metade_alcance
                larg = px2-y-metade_alcance
            
                if alt > 0:
                    if larg > box[0][1]:
                        stdscr.addstr(alt, larg, 'FF',COR)
                        stdscr.refresh()
                        time.sleep(0.2)
                        stdscr.addstr(alt, larg, '  ')
                elif alt <= 0:
                    if larg <= box[0][1]:
                        pass         

                for c in range(len(SUPERFICIE_PREDIOS)):
                    ff = SUPERFICIE_PREDIOS[c]
                    if [alt, larg] == ff:
                        PERDEU = 1
                       

                for c in range(len(PERSONAGEM_1_POSICAO)):
                    a = PERSONAGEM_1_POSICAO[c]
                    if [alt, larg] == a:
                        stdscr.clear()
                        stdscr.addstr(sh-3, sw-3, 'GAME OVER',COR3)   
                        stdscr.refresh()
                        PERDEU = 1

                if PERDEU == 1:
                    break

            CONTADOR = 0



        #----------------------------------------------------------------
        

        stdscr.getch()


    #--------------------------------------------------------------------
    stdscr.getch()

curses.wrapper(main)