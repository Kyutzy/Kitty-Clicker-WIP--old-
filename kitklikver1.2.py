"""
vovós - aumentam o número de gatos por segundo em 0.1x, o custo aumenta em 0.3 p/ vovó comprada - c. inicial - 10
lã - aumenta o número de gatos por segundo em 0.3x, o custo aumenta em 0.4 p/ lã comprada - c. inical - 30
whiskas - aumenta o número de gatos por clique em 1x o custo aumenta 0.6 p/whiskas comprado c. inicial - 50
ratinho - aumenta o número de gatos por segundo em 0.5x o custo aumenta em 0.8x p/ratinho comprado - c. inicial - 100
bolinha de alumínio - aumenta o número de gatos por clique em 2x o custo aumenta em 1x p/bolinha comprada - c. inicial - 1000
nariz de trouxa - aumenta o número de gatos por segundo em 4x o custo aumenta em 2x p/nariz comprado - c. inicial - 10000
"""

"""
Bônuses

1 - aumento de gatos por segundo em x777777777
2 - 
"""

import time as t 
import datetime
import keyboard as k
import os
import pickle as p
import random as r
import asyncio

vovos = 0
la = 0
whisks = 0
ratinho = 0
bola = 0
nariz = 0
gatos = 0
bonus1 = 0

pvovo = 10
pla = 30
pwhisks = 50
pratinho = 100
pbola = 1000
pnariz = 10000

bonusr = ""
letra_bonus = ""
hifen = ""



def bonus():
        
    global gatos
    global vovos
    global la
    global whisks
    global ratinho
    global bola
    global nariz
    global bonus1
    

        
    t.sleep(1)
    gatos = gatos + (vovos*0.2 + la*0.3 + ratinho*0.5 + nariz*4)

def menu():
    global bonusr
    global letra_bonus
    global hifen
    try:
        load()
    except FileNotFoundError:
        print("")
    while(1):
        print("=====================KITTY  CLICKER=====================")
        print("  Mantenha   0   Pressionado para conseguir mais gatos  ")
        print("                          {}                            ".format(gatos))
        print("                         GATOS                          ")
        print("========================================================")
        print("1 - {} Vovós                      {} Gatos                  ".format(vovos, pvovo))
        print("2 - {} Lã                         {} Gatos                  ".format(la, pla))
        print("3 - {} Whisks                     {} Gatos                  ".format(whisks, pwhisks))
        print("4 - {} Ratinhos                   {} Gatos                  ".format(ratinho, pratinho))
        print("5 - {} Bolinhas de Alumínio       {} Gatos                  ".format(bola,pbola))
        print("6 - {} Narizes                    {} Gatos                  ".format(nariz, pnariz))
        print("{} {} {}                                                     ".format(letra_bonus, hifen, bonusr))
        print("7 - Salvar                                              ")
        print("8 - Carregar                                            ")
        print("========================================================")
        
        apertou()
        bonus()
        cli()
def cli(): # essa função limpa o console para atualização dos valores
    os.system('cls' if os.name=='nt' else 'clear')

def fundosinsuficientes():
    cli()
    print("Gatos insuficientes para essa transação, continue farmando")
    t.sleep(0.3)
    menu()

def apertou(): #essa função serve para conferir o pedido do usuário
    
    enter = k.is_pressed('0')
    um = k.is_pressed('1')
    dois = k.is_pressed('2')
    tres = k.is_pressed('3')
    quatro = k.is_pressed('4')
    cinco = k.is_pressed('5')
    seis = k.is_pressed('6')
    sete = k.is_pressed('7')
    oito = k.is_pressed('8')


    chek = False
    chek1 = False
    chek2 = False
    chek3 = False
    chek4 = False
    chek5 = False
    chek6 = False
    chek7 = False
    chek8 = False

    global gatos
    global vovos
    global la
    global whisks
    global ratinho
    global bola
    global nariz

    global pgatos
    global pvovo
    global pla
    global pwhisks
    global pratinho
    global pbola
    global pnariz

    if enter == True:
        chek = True
        t.sleep(0.1)
    else:
        chek = False

    if um == True:
        chek1 = True
        t.sleep(0.1)
    else:
        chek1 = False

    if dois == True:
        chek2 = True
        t.sleep(0.1)
    else:
        chek2 = False

    if tres == True:
        chek3 = True
        t.sleep(0.1)
    else:
        chek3 = False

    if quatro == True:
        chek4 = True
        t.sleep(0.1)
    else:
        chek4 = False

    if cinco == True:
        chek5 = True
        t.sleep(0.1)
    else:
        chek5 = False

    if seis == True:
        chek6 = True
        t.sleep(0.4)
    else:
        chek6 = False
    
    if sete == True:
        chek7 = True
        t.sleep(0.4)
    else:    
        chek7 = False
    
    if oito == True:
        chek8 =  True
        t.sleep(0.4)
    else:
        chek8 = False
    if chek == True:
        gatos = gatos + 1 + whisks + (bola*2)

    if chek1 == True:
        if gatos >= pvovo:
            gatos = gatos - pvovo
            vovos = vovos + 1
            pvovo = pvovo + (pvovo*0.3)
        else:
            fundosinsuficientes()

    if chek2 == True:
        if gatos >= pla:
            gatos = gatos - pla
            la = la + 1
            pla = pla + (pla*0.4)
        else:
            fundosinsuficientes()

    if chek3 == True:
        if gatos >= pwhisks:
            gatos = gatos - pwhisks
            whisks = whisks + 1
            pwhisks = pwhisks + (pwhisks*0.6)
        else:
            fundosinsuficientes()

    if chek4 == True:
        if gatos >= pratinho:
            gatos = gatos - pratinho
            ratinho = ratinho + 1
            pratinho = pratinho + (pratinho*0.8)
        else:
            fundosinsuficientes()

    if chek5 == True:
        if gatos >= pbola:
            gatos = gatos - pbola
            bola = bola + 1
            pbola = pbola + (pbola*1)
        else:
            fundosinsuficientes()

    if chek6 == True:
        if gatos >= pnariz:
            gatos = gatos - pnariz
            nariz = nariz + 1
            pnariz = pnariz + (nariz*2.0)
        else:
            fundosinsuficientes()
    if chek7 == True:
        salva()
    if chek8 == True:
        load()

def salva():
    
    global gatos
    global vovos
    global la
    global whisks
    global ratinho
    global bola
    global nariz

    global pgatos
    global pvovo
    global pla
    global pwhisks
    global pratinho
    global pbola
    global pnariz

    with open("savegame.pkl", "wb") as b:
        p.dump(gatos, b)
        p.dump(vovos, b)
        p.dump(la, b)
        p.dump(whisks, b)
        p.dump(ratinho, b)
        p.dump(bola, b)
        p.dump(nariz, b)

        p.dump(pvovo, b)
        p.dump(pla, b)
        p.dump(pwhisks,b)
        p.dump(pratinho, b)
        p.dump(pbola, b)
        p.dump(pnariz, b)


    print("Jogo Salvo")

def load():
    
    

    global gatos
    global vovos
    global la
    global whisks
    global ratinho
    global bola
    global nariz

    global pvovo
    global pla
    global pwhisks
    global pratinho
    global pbola
    global pnariz
    
    with open("savegame.pkl", "rb") as o:
        gatos = p.load(o)
        vovos = p.load(o)
        la = p.load(o)
        whisks = p.load(o)
        ratinho = p.load(o)
        bola = p.load(o)
        nariz = p.load(o)

        pvovo = p.load(o)
        pla = p.load(o)
        pwhisks = p.load(o)
        pratinho = p.load(o)
        pbola = p.load(o)
        pnariz = p.load(o)
"""
async def tecla_bonus():
    global bonusr
    global letra_bonus
    global hifen
    global bonus1
    tempos = [1,100,300,500,600,800,1000,1200,2002,2033,2312,2562,2634,3122]
    #segundo = r.choice(tempos)
    segundo = 1
    await asyncio.sleep(segundo)
    botoes = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q", "r", "s","t","u","v","w","x","y","z"]
    letra_bonus = r.choice(botoes)
    ativadorbonus = k.is_pressed(letra_bonus)
    
    escolhaq = 1
    if escolhaq == 1:
        bonusr = "Chuva de gatos! 4x gatos por segundo"
        hifen = "-"
        bonus1 = 1
        await asyncio.sleep(9)
        bonus1 = 0
    else:
        bonus1 = 0
    menu()
"""

if __name__ == '__main__':
    menu()
