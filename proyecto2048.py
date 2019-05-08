#Entradas:
#Salidas:
#Restricciones:

import os
clear = lambda : os.system('cls')
import pygame, sys, random
from pygame.locals import *
from random import randint, uniform,random
import time
import math

sys.path.append("")
tempo=[3000]
WINDOW_WIDTH = 2
WINDOW_HEIGHT = 2
posicionesI=[]
posicionesJ=[]
leaderboard = []
score=[0]
nombre=[0]
matriz=[[0,0,0,0],
                    [1024,1024,0,0],
                    [0,0,0,0],
                    [0,0,0,0]]
base=[8]


def main(Mprincipal):
    Msecundaria=Mprincipal
    pygame.init()
    DISPLAY_SURF = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption('2048')
    pintar(Mprincipal)
    while (True):        
        time.sleep(0.1)
        tempo[0]-=1
        if(tempo[0]<=0):
            perdio(2)
        #if(keyboard.is_pressed('ctrl+shift+x')):
         #   break
        
        #if(keyboard.is_pressed('ctrl+shift+r')):
         #   Mprincipal=nueva(Mprincipal)            
         #   vaciarPocisiones()
         #   print(Mprincipal)
        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()
            if(tempo[0]<=0):
                perdio(2)
            elif event.type == KEYUP:
                
            
        #elif(keyboard.is_pressed('flecha izquierda')):            
           # arrow_press(Mprincipal,"izq",0,4)
           # mover(Mprincipal,"izq",0,len(posicionesI))            
            #print(posicionesI,posicionesJ)
           # vaciarPocisiones()
           # pintar(Mprincipal)
                if event.key in (K_LEFT, K_a):            
                    arrow_press(Mprincipal,"izq",0,4)
                    mover(Mprincipal,"izq",0,len(posicionesI))            
                    #print(posicionesI,posicionesJ)
                    vaciarPocisiones()
                    pintar(Mprincipal)
 
            
        #if(keyboard.is_pressed('flecha derecha')):
           # arrow_press(Mprincipal,"der",0,4)
           # mover(Mprincipal,"der",0,len(posicionesI))
           # vaciarPocisiones()
            #print(posicionesI,posicionesJ)
            #print(Mprincipal)
           # pintar(Mprincipal)
            #printTable(Mprincipal,0)
                elif event.key in (K_RIGHT, K_d):
                   arrow_press(Mprincipal,"der",0,4)
                   mover(Mprincipal,"der",0,len(posicionesI))
                   vaciarPocisiones()
                   pintar(Mprincipal)

            
        #elif(keyboard.is_pressed('flecha arriba')):         
           # arrow_press(Mprincipal,"up",1,4)            
            #print(posicionesI,posicionesJ)
           # mover(Mprincipal,"up",0,len(posicionesI))
           # vaciarPocisiones()
           # pintar(Mprincipal)
                elif event.key in (K_UP, K_w):        
                   arrow_press(Mprincipal,"up",1,4)            
                    #print(posicionesI,posicionesJ)
                   mover(Mprincipal,"up",0,len(posicionesI))
                   vaciarPocisiones()
                   pintar(Mprincipal)
                   
            
        #elif(keyboard.is_pressed('flecha abajo')):            
           # arrow_press(Mprincipal,"down",0,3)            
            #print(posicionesI,posicionesJ)
           # mover(Mprincipal,"down",0,len(posicionesI))
           # vaciarPocisiones()
           # pintar(Mprincipal)
                elif event.key in (K_DOWN, K_s):            
                   arrow_press(Mprincipal,"down",0,3)            
                    #print(posicionesI,posicionesJ)
                   mover(Mprincipal,"down",0,len(posicionesI))
                   vaciarPocisiones()
                   pintar(Mprincipal)

                   
                if NOpuede_jugar(Mprincipal,0,0):
                    perdio(1)
                time.sleep(0.1)
                tempo[0]-=2.5

def perdio(x):
    nuevo_score()
    imprimir_mayor()
    
    if(x==2):
        print("Se te acabo el tiempo\n")
    print("Has perdido\n")
    print(nombre[0]+"= "+str(score[0]))
    pygame.quit()
    sys.exit()


def gano():
    nuevo_score()
    imprimir_mayor()
    print("Has ganado")
    print(nombre[0]+"= "+str(score[0]))
    pygame.quit()
    sys.exit()
    




def arrow_press(Mprincipal,direc,i,stop_point):
    if(i!=stop_point):
        auxArrow(Mprincipal,i,0,direc,3)
        arrow_press(Mprincipal,direc,i+1,stop_point)
    

#def auxArrow(Mprincipal,i,j,direc):
  #  if(Mprincipal[i][j]!=0):
    #    ocupado=vecinoLleno(Mprincipal,i,j,direc)
      #  if(ocupado==1):
        #    if(vecinoIgual(Mprincipal,i,j,direc)):
          #      agregarPosi(i,j)
       # elif(ocupado==2):
       #     agregarPosi(i,j)
    #if(j<3):
      #  auxArrow(Mprincipal,i,j+1,direc)    

def auxArrow(Mprincipal,i,j,direc,stop_point):
    if(direc == "der" and j < stop_point):
        if(Mprincipal[i][j] != 0):
            agregarPosi(i,j)
            
        auxArrow(Mprincipal,i,j+1,direc,stop_point)

        
    elif(direc == "izq" and j < stop_point):
        if(Mprincipal[i][stop_point] != 0):
            agregarPosi(i,stop_point)
            
        auxArrow(Mprincipal,i,j,direc,stop_point-1)

        
    elif(direc == "down" and j < stop_point+1):
        if(Mprincipal[i][j] != 0):
            agregarPosi(i,j)
            
        auxArrow(Mprincipal,i,j+1,direc,stop_point)

        
    elif(direc == "up" and j < stop_point+1):
        if(Mprincipal[i][j] != 0):
            agregarPosi(i,j)
            
        auxArrow(Mprincipal,i,j+1,direc,stop_point)




def agregarPosi(i,j):
    posicionesI.append(i)
    posicionesJ.append(j)



def mover(Mprincipal,direc,i,largo):
    if(i != largo and direc == "up"):
        movedor(Mprincipal,posicionesI[i],posicionesJ[i],direc)
        mover(Mprincipal,direc,i+1,largo)
        
    elif(i!=largo):
        movedor(Mprincipal,posicionesI[largo-1],posicionesJ[largo-1],direc)
        mover(Mprincipal,direc,i,largo-1)

    
#def movedor(Mprincipal,i,j,direc):
  #  if(direc=="der"):
    #    if(j!=3):
      #      if(Mprincipal[i][j+1]==Mprincipal[i][j]):
        #        Mprincipal[i][j+1]=Mprincipal[i][j]*2
       #     else:
         #       Mprincipal[i][j+1]=Mprincipal[i][j]
          #  Mprincipal[i][j]=0
    
def movedor(Mprincipal,i,j,direc):
    if(direc == "der"):
        if(j!=3):
            puedeMover = vecinoLleno(Mprincipal,i,j,direc)
            if(puedeMover):
                if(Mprincipal[i][j+1]==Mprincipal[i][j]):
                    Mprincipal[i][j+1]=Mprincipal[i][j]*2
                    acumular(Mprincipal[i][j]*2)
                    
                else:
                    Mprincipal[i][j+1]=Mprincipal[i][j]
                Mprincipal[i][j]=0
                movedor(Mprincipal,i,j+1,direc)
                
    if(direc == "izq"):
        if(j!=0):
            puedeMover = vecinoLleno(Mprincipal,i,j,direc)
            if(puedeMover):
                if(Mprincipal[i][j-1]==Mprincipal[i][j]):
                    Mprincipal[i][j-1]=Mprincipal[i][j]*2
                    acumular(Mprincipal[i][j]*2)
                    
                else:
                    Mprincipal[i][j-1]=Mprincipal[i][j]
                Mprincipal[i][j]=0
                movedor(Mprincipal,i,j-1,direc)
                
    if(direc == "down"):
        if(i!=3):
            puedeMover = vecinoLleno(Mprincipal,i,j,direc)
            if(puedeMover):
                if(Mprincipal[i+1][j]==Mprincipal[i][j]):
                    Mprincipal[i+1][j]=Mprincipal[i][j]*2
                    acumular(Mprincipal[i][j]*2)
                    
                else:
                    Mprincipal[i+1][j]=Mprincipal[i][j]
                Mprincipal[i][j]=0
                movedor(Mprincipal,i+1,j,direc)
                
    if(direc == "up"):
        if(i!=0):
            puedeMover = vecinoLleno(Mprincipal,i,j,direc)
            if(puedeMover):
                if(Mprincipal[i-1][j]==Mprincipal[i][j]):
                    Mprincipal[i-1][j]=Mprincipal[i][j]*2
                    acumular(Mprincipal[i][j]*2)
                    
                else:
                    Mprincipal[i-1][j]=Mprincipal[i][j]
                Mprincipal[i][j]=0
                movedor(Mprincipal,i-1,j,direc)


#def vecinoLleno(Mprincipal,i,j,direc):
  #  print("Check")
   # if(direc=="der"):
    #    if(j==3):
      #      return 0
        #elif(Mprincipal[i][j+1]!=0):
          #  return 1
        #else:
          #  return 2



def vecinoLleno(Mprincipal,i,j,direc):
    if(direc=="der"):
        if(Mprincipal[i][j+1]!=0):
            return vecinoIgual(Mprincipal,i,j,direc)
        else:
            return True

    elif(direc=="izq"):
        if(Mprincipal[i][j-1]!=0):
            return vecinoIgual(Mprincipal,i,j,direc)
        else:
            return True
        
    elif(direc=="down"):
        if(Mprincipal[i+1][j]!=0):
            return vecinoIgual(Mprincipal,i,j,direc)
        else:
            return True
        
    elif(direc=="up"):
        if(Mprincipal[i-1][j]!=0):
            return vecinoIgual(Mprincipal,i,j,direc)
        else:
            return True

def pintar(Mprincipal):
    print('\n'*32)
    randomDos(Mprincipal)
    printTable(Mprincipal,0)
    print("Puntaje: ",score[0])

def acumular(x):
    score[0]=score[0]+x    
    if(x==2048):
        gano()


def vecinoIgual(Mprincipal,i,j,direc):
    if(direc=="der"):
        if(Mprincipal[i][j+1]==Mprincipal[i][j]):
            return True
        else:
            return False
        
    if(direc=="izq"):
        if(Mprincipal[i][j-1]==Mprincipal[i][j]):
            return True
        else:
            return False
        
    if(direc=="down"):
        if(Mprincipal[i+1][j]==Mprincipal[i][j]):
            return True
        else:
            return False
        
    if(direc=="up"):
        if(Mprincipal[i-1][j]==Mprincipal[i][j]):
            return True
        else:
            return False


def randomDos(Mprincipal):
    x=randint(0,3)
    y=randint(0,3)
    #x=0
    #y=0
    if(Mprincipal[x][y]==0):
        Mprincipal[x][y]=2
    elif(0 in Mprincipal[0] or 0 in Mprincipal[1] or
        0 in Mprincipal[2] or 0 in Mprincipal[3]):
        randomDos(Mprincipal)


def NOpuede_jugar(Mprincipal,i,j):
    if(i==4):
        return True
    if(j==4):
        return NOpuede_jugar(Mprincipal,i+1,0)
    if(i!=0):
        if(Mprincipal[i-1][j] == Mprincipal[i][j] or Mprincipal[i-1][j] == 0):
            return False
    if(i!=3):
        if(Mprincipal[i+1][j]==Mprincipal[i][j] or Mprincipal[i+1][j] == 0):
            return False
    if(j!=0):
        if(Mprincipal[i][j-1]==Mprincipal[i][j] or Mprincipal[i][j-1] == 0):
            return False
    if(j!=3):
        if(Mprincipal[i][j+1]==Mprincipal[i][j] or Mprincipal[i][j+1] == 0):
            return False
    return NOpuede_jugar(Mprincipal,i,j+1)
        
    
    
    

def nueva(Mprincipal):    
    Mprincipal=[[0,0,0,0],
                       [0,0,0,0], 
                       [0,0,0,0],
                       [0,0,0,0]]
    randomDos(Mprincipal)
    return Mprincipal


def vaciarPocisiones():  
    posicionesI.clear()
    posicionesJ.clear()
    

def printTable(Mprincipal,i):
    if(i!=4):
        linea=auxPT(Mprincipal[i],0)
        print(linea)
        printTable(Mprincipal,i+1)

    

def auxPT(fila,i):
    if(i==4):
        return ""
    if(base[0] == 10):
        linea=str(fila[i] )+"\t"+ auxPT(fila,i+1)

    elif(base[0] == 2):        
        linea=camb_bin(fila[i]) + "\t" + auxPT(fila,i+1)

    elif(base[0] == 8):        
        linea=camb_oct(fila[i]) + "\t" + auxPT(fila,i+1)

    elif(base[0] == 16):        
        linea=camb_hexa(fila[i]) + "\t" + auxPT(fila,i+1)
    return linea



def camb_bin(x):
    #print(x)
    if(x/2 < 1):
        if(x/2==1):
            return str(math.floor(x/2))+str(x%2)
        else:
            return str(x%2)
    else:
        if(x%2==0):
            return camb_bin(math.floor(x/2))+str(x%2)
        else:
            return camb_bin(math.floor(x/2))+str(x%2)



def camb_oct(x):
    #print(x)
    if(x/8 < 7):
        if(x/8>=1):
            return str(math.floor(x/8))+str(x%8)
        else:
            return str(x%8)
    else:
        if(x%8==0):
            return camb_oct(math.floor(x/8))+str(x%8)
        else:
            return camb_oct(math.floor(x/8))+str(x%8)




def camb_hexa(x):
    #print(x)
    ele=letras(x%16)
    if(x/16 < 7):
        if(x/16>=1):
            return str(math.floor(x/16))+ele
        else:
            return ele
    else:
        if(x%16==0):
            return camb_hexa(math.floor(x/16))+ele
        else:
            return camb_hexa(math.floor(x/16))+ele



def letras(x):
    if(x==10):
        return "A"
    elif(x==11):
        return "B"
    elif(x==12):
        return "C"
    elif(x==13):
        return "D"
    elif(x==14):
        return "E"
    elif(x==15):
        return "F"
    else:
        return str(x)




def login():
    nombre[0]=input("\n\nIngrese su nombre de usuario: ")
    if(len(nombre[0])!=3):
        print("El nombre debe de poseer exatamente 3 caracteres")
        login()
    else:
        f=open("scores.txt","r")
        x = f.readlines()
        for i in x:
            if nombre[0] in i:
                print("\n\n\Este nomre ya existe en el leaderboard\nPor favor digite uno nuevo")
                f.close()
                login()
                break
        f.close()


                
def nuevo_score():
    f=open("scores.txt","r")
    x = f.readlines()
    if(len(x)<1):
        f.close()
        d=open("scores.txt","w")
        d.write(nombre[0]+"= "+str(score[0]))
        d.close
    else:
        y=None
        #print(x)
        j=0
        for i in x:
            y= i.split("= ")
            y=y[1].split("\n")
            #print(y)
            print(score[0])
            if(score[0]>int(y[0])):
                    print(score[0],y[0])
                    #print(x)
                    if(len(x)<10):
                        agregar_score(j,x,len(x))
                    else:
                        agregar_score(j,x,len(x))
                    
                    break
            elif(i==x[len(x)-1] and len(x)<10):
                #print("adios"+x[len(x)-1])
                x[len(x)-1]=x[len(x)-1]+"\n"
                #print(x)
                x.append(nombre[0]+"= "+str(score[0]))
                modificar_Scores_txt(x)
                break
            j+=1
        f.close()


def agregar_score(j,x,largo):
    jaux=j
    if largo<10:
        x.append(x[largo-1])
    for i in x[j:largo-1]:
        x[j+1]=i
        j+=1
    x[jaux]=nombre[0]+"= "+str(score[0])+"\n"
    modificar_Scores_txt(x)



def modificar_Scores_txt(x):
    d=open("scores.txt","w")
    for i in x:
        d.write(i)
    d.close



def imprimir_mayor():
    print("\n"*32)
    print("---------Leaderboard---------")
    f=open("scores.txt","r")
    x=f.readlines()
    leaderboard = x
    for i in x:
        print (i)
    f.close()


def escoger_base():
    print("\n"*32)
    print("1.Decimal\n2.Octal\n3.Hexadecimal\n4.Binario")
    selec=int(input("\nEscoja la base en la que desea jugar: "))
    if(selec == 1):
        base[0] = 10
        
    elif(selec == 2):
        base[0] = 8

    elif(selec == 3):
        base[0] = 16

    elif(selec == 4):
        base[0] = 2
    

if __name__ == '__main__':
    imprimir_mayor()
    login()
    escoger_base()
    main(matriz)

