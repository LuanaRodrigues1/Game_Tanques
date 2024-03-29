import curses
import ctypes
import random
from curses.textpad import Textbox, rectangle
from random import shuffle, randrange
import math
import time
import menu

# o x aumenta de 20 em 20 e o y é 49-valor da range
POSICAO_Y = random.randrange(10,25,5)
POSICAO_X = [28, 20, 15]

#Define a posição da bolinha
if (POSICAO_Y == 10):
    BOLINHA = [[POSICAO_Y+23, 15]] 
elif (POSICAO_Y == 15):
    BOLINHA = [[POSICAO_Y+13, 15]]
elif (POSICAO_Y == 20):
    BOLINHA = [[POSICAO_Y+3, 15]]

def main_cenario_facil(stdscr):
    stdscr.clear()
    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3,sw-3]]
    win = curses.newwin(box[0][0], box[0][1], box[1][0], box[1][1])
    rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    COR1 = curses.color_pair(1)
    curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_BLUE)
    COR7 = curses.color_pair(7)
    curses.init_pair(8, curses.COLOR_RED, curses.COLOR_RED)
    COR8 = curses.color_pair(8)
    text = 'O'

    PERSONAGEM_1_POSICAO = []
    for a in range(5):
        y = BOLINHA[0][0]+1
        x = BOLINHA[0][1]-9+a
        stdscr.addstr(y, x, "O", COR8) 
        PERSONAGEM_1_POSICAO.insert(a, [y,x])
    for a in range(7):
        y = BOLINHA[0][0]+2
        x = BOLINHA[0][1]-10+a
        stdscr.addstr(y, x, "O", COR8) 
        PERSONAGEM_1_POSICAO.insert(a+5, [y,x])
    y_canhao1 = BOLINHA[0][0]
    x_canhao1 = BOLINHA[0][1]-4
    stdscr.addstr(y_canhao1, x_canhao1, "O", COR8) 
    PERSONAGEM_1_POSICAO.insert(12, [y_canhao1,x_canhao1])
    y_canhao2 = BOLINHA[0][0]-1
    x_canhao2 = BOLINHA[0][1]-3
    stdscr.addstr(y_canhao2, x_canhao2, "O", COR8) 
    PERSONAGEM_1_POSICAO.insert(13, [y_canhao2,x_canhao2])

    SUPERFICIE_PREDIOS = []

    #Define a posição, altura e largura das colunas
    for i in range(1):
        for y in range(POSICAO_Y):
            for x in range(POSICAO_X[0]):
                c = int(25)*int(i)
                alt = y+46-POSICAO_Y
                larg = x+4+c
                stdscr.addstr(alt, larg ,text ,COR1)
                mapear_y= 0
                mapear_x= 0
                SUPERFICIE_PREDIOS.insert(y, [alt, larg]) 

    
    for i in range(6):
        POSICAO_Y2 = random.randrange(10,25,5) 
        for y in range(POSICAO_Y2):
            for x in range(POSICAO_X[0]):
                d = int(25)*int(i)+25
                alt = y+46-POSICAO_Y2
                larg = x+4+d
                stdscr.addstr(alt, larg, text, COR1)
                SUPERFICIE_PREDIOS.insert(y+POSICAO_Y, [alt, larg])


    for i in range(1):
        POSICAO_Y3 = random.randrange(10,25,5)
        for y in range(POSICAO_Y3):
            for x in range(POSICAO_X[0]):
                a = int(25)*int(i)+175
                alt = y+46-POSICAO_Y3
                larg = x+4+a
                stdscr.addstr(alt, larg , text, COR1)
                SUPERFICIE_PREDIOS.insert(y+POSICAO_Y2, [alt, larg])


    if (POSICAO_Y3 == 10):
        BOLINHA2 = [[POSICAO_Y3+23, 200]] 
    elif (POSICAO_Y3 == 15):
        BOLINHA2 = [[POSICAO_Y3+13, 200]]
    elif (POSICAO_Y3 == 20):
        BOLINHA2 = [[POSICAO_Y3+3, 200]]

    PERSONAGEM_2_POSICAO = []
    for a in range(5):
        y = BOLINHA2[0][0]+1
        x = BOLINHA2[0][1]-5+a
        stdscr.addstr(y, x, "O", COR7) 
        PERSONAGEM_2_POSICAO.insert(a, [y,x])
    for a in range(7):
        y = BOLINHA2[0][0]+2
        x = BOLINHA2[0][1]-6+a
        stdscr.addstr(y, x, "O", COR7) 
        PERSONAGEM_2_POSICAO.insert(a+5, [y,x])
    y_canhao1 = BOLINHA2[0][0]
    x_canhao1 = BOLINHA2[0][1]-6
    stdscr.addstr(y_canhao1, x_canhao1, "O", COR7) 
    PERSONAGEM_2_POSICAO.insert(12, [y_canhao1,x_canhao1])
    y_canhao2 = BOLINHA2[0][0]-1
    x_canhao2 = BOLINHA2[0][1]-7
    stdscr.addstr(y_canhao2, x_canhao2, "O", COR7) 
    PERSONAGEM_2_POSICAO.insert(13, [y_canhao2,x_canhao2])
    

    return PERSONAGEM_1_POSICAO,SUPERFICIE_PREDIOS,PERSONAGEM_2_POSICAO,BOLINHA,BOLINHA2, box


def main_cenario_medio(stdscr):
    stdscr.clear()
    sh, sw = stdscr.getmaxyx()
    box = [[3,3], [sh-3,sw-3]]
    win = curses.newwin(box[0][0], box[0][1], box[1][0], box[1][1])
    rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_YELLOW)
    COR1 = curses.color_pair(1)
    curses.init_pair(7, curses.COLOR_BLUE, curses.COLOR_BLUE)
    COR7 = curses.color_pair(7)
    curses.init_pair(8, curses.COLOR_RED, curses.COLOR_RED)
    COR8 = curses.color_pair(8)
    text = 'O'

    PERSONAGEM_1_POSICAO = []
    for a in range(5):
        y = BOLINHA[0][0]+1
        x = BOLINHA[0][1]-9+a
        stdscr.addstr(y, x, "O", COR8) 
        PERSONAGEM_1_POSICAO.insert(a, [y,x])
    for a in range(7):
        y = BOLINHA[0][0]+2
        x = BOLINHA[0][1]-10+a
        stdscr.addstr(y, x, "O", COR8) 
        PERSONAGEM_1_POSICAO.insert(a+5, [y,x])
    y_canhao1 = BOLINHA[0][0]
    x_canhao1 = BOLINHA[0][1]-4
    stdscr.addstr(y_canhao1, x_canhao1, "O", COR8) 
    PERSONAGEM_1_POSICAO.insert(12, [y_canhao1,x_canhao1])
    y_canhao2 = BOLINHA[0][0]-1
    x_canhao2 = BOLINHA[0][1]-3
    stdscr.addstr(y_canhao2, x_canhao2, "O", COR8) 
    PERSONAGEM_1_POSICAO.insert(13, [y_canhao2,x_canhao2])

    SUPERFICIE_PREDIOS = []

    #Define a posição, altura e largura das colunas
    for i in range(1):
        for y in range(POSICAO_Y):
            for x in range(POSICAO_X[1]):
                alt = y+46-POSICAO_Y
                larg = x+4
                stdscr.addstr(alt, larg ,text ,COR1)
                mapear_y= 0
                mapear_x= 0
                SUPERFICIE_PREDIOS.insert(y, [alt, larg]) 

    
    for i in range(9):
        POSICAO_Y2 = random.randrange(10,20,2) 
        for y in range(POSICAO_Y2):
            for x in range(POSICAO_X[1]):
                d = int(18)*int(i)+18
                alt = y+46-POSICAO_Y2
                larg = x+4+d
                stdscr.addstr(alt, larg, text, COR1)
                SUPERFICIE_PREDIOS.insert(y+POSICAO_Y, [alt, larg])

    for i in range(1):
        POSICAO_Y3 = random.randrange(10,25,5)
        for y in range(POSICAO_Y3):
            for x in range(POSICAO_X[1]):
                alt = y+46-POSICAO_Y3
                larg = x+4+162+20
                stdscr.addstr(alt, larg , text, COR1)
                SUPERFICIE_PREDIOS.insert(y+POSICAO_Y2, [alt, larg])


    if (POSICAO_Y3 == 10):
        BOLINHA2 = [[POSICAO_Y3+23, 200]] 
    elif (POSICAO_Y3 == 15):
        BOLINHA2 = [[POSICAO_Y3+13, 200]]
    elif (POSICAO_Y3 == 20):
        BOLINHA2 = [[POSICAO_Y3+3, 200]]

    PERSONAGEM_2_POSICAO = []
    for a in range(5):
        y = BOLINHA2[0][0]+1
        x = BOLINHA2[0][1]-5+a
        stdscr.addstr(y, x, "O", COR7) 
        PERSONAGEM_2_POSICAO.insert(a, [y,x])
    for a in range(7):
        y = BOLINHA2[0][0]+2
        x = BOLINHA2[0][1]-6+a
        stdscr.addstr(y, x, "O", COR7) 
        PERSONAGEM_2_POSICAO.insert(a+5, [y,x])
    y_canhao1 = BOLINHA2[0][0]
    x_canhao1 = BOLINHA2[0][1]-6
    stdscr.addstr(y_canhao1, x_canhao1, "O", COR7) 
    PERSONAGEM_2_POSICAO.insert(12, [y_canhao1,x_canhao1])
    y_canhao2 = BOLINHA2[0][0]-1
    x_canhao2 = BOLINHA2[0][1]-7
    stdscr.addstr(y_canhao2, x_canhao2, "O", COR7) 
    PERSONAGEM_2_POSICAO.insert(13, [y_canhao2,x_canhao2])

    return PERSONAGEM_1_POSICAO,SUPERFICIE_PREDIOS,PERSONAGEM_2_POSICAO,BOLINHA,BOLINHA2, box

