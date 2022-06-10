

from ast import Str
import pyttsx3
import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import time
import math  


engine = pyttsx3.init()
voice_id ='spanish-latin-am'
engine.setProperty('voice',voice_id)
rate=engine.getProperty('rate')
engine.setProperty('rate',rate-50)
hj= "escoje rapido mi cuchurumin"

print("""────────────────────██████──────────
──────────────────██▓▓▓▓▓▓██────────
────────────────██▓▓▓▓▒▒▒▒██────────
────────────────██▓▓▒▒▒▒▒▒██────────
──────────────██▓▓▓▓▒▒▒▒██──────────
──────────────██▓▓▒▒▒▒▒▒██──────────
────────────██▓▓▓▓▒▒▒▒▒▒██──────────
────────────████▒▒████▒▒██──────────
────────────██▓▓▒▒▒▒▒▒▒▒██──────────
──────────██────▒▒────▒▒██──────────
──────────████──▒▒██──▒▒██──────────
──────────██────▒▒────▒▒██──────────
──────────██▒▒▒▒▒▒▒▒▒▒▒▒██──────────
──────────████████████▒▒▒▒██────────
────────██▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒██──────
──────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒██────
────██▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██──
──██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██
██▓▓▒▒▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▒▒▒▒██
██▓▓▒▒▓▓▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒██
██▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓██
──████▐▌▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▐▌▐▌████──
────██▐▌▐▌▌▌▌▌▌▌▌▌▐▌▐▌▐▌▐▌▌▌▐▌██────
────██▌▌▐▌▐▌▌▌▐▌▌▌▌▌▐▌▌▌▌▌▌▌▌▌██────
──────██▌▌▐▌▐▌▐▌▐▌▐▌▐▌▐▌▌▌▌▌██──────
──────██▐▌▐▌▐▌████████▐▌▌▌▌▌██──────
────────██▒▒██────────██▒▒██────────
────────██████────────██████──────── """)
print("trabajo de matematica computacional")
print("                                    ")
print("       que quieres hacer bebe?   ")
print("""       
              1.mix
              2.resolver dimenciones
              3.el codigo del amor 7w7?   
              4. resolver matrices    """)

engine.say(hj)
engine.runAndWait()
la= int(input("que quieres mi cuchurrumin? "))

def corazoncito(x,y,z):
    return (x**2+(9/4)*y**2+z**2-1)**3-x**2*z**3-(9/80)*y**2*z**3

def paraelplot(fn,bbox=(-1.5,1.5)):
    xmin,xmax,ymin,ymax,zmin,zmax = bbox*3
    fig = plt.figure('PARA TI')
    ax = fig.add_subplot(111,projection = '3d')
    A = np.linspace(xmin,xmax,80)
    B = np.linspace(xmin,xmax,30)
    A1,A2 = np.meshgrid(A,A)
 
    for z in B:
        X,Y = A1,A2
        Z = fn(X,Y,z)
        cest = ax.contour(X,Y,z+Z,[z],zdir='z',colors=('r',))
 
    for y in B:
        X,Z = A1,A2
        Y = fn(X,y,Z)
        cest = ax.contour(X,Y+y,Z,[y],zdir = 'y',colors = ('red',))
 
    for x in B :
        Y,Z=A1,A2
        X = fn(x,Y,Z)
        cest = ax.contour(X+x,Y,Z,[x],zdir = 'x',colors = ('red',))
 
    ax.set_zlim3d(zmin,zmax)
    ax.set_xlim3d(xmin,xmax)
    ax.set_ylim3d(ymin,ymax)
        
    plt.show()
def codigodelamor():
    t = np.linspace(0,6.3,1000)
    x = 16*(np.sin(t))**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    plt.figure('SweetHeart')
    plt.plot(x,y,'r')
    plt.title('te amo mucho uwu',fontsize='large',color='red')
    plt.show()
 
    paraelplot(corazoncito)
def baby():
    co="te amo no lo olvides "
    print("==================================================")
    print("=       BIENVENIDO AL RESOLVEDOR DE VECTORES     =")
    print("==================================================")
    print(" 1 vector 2D")
    engine.say(co)
    engine.runAndWait()
    time.sleep(2)
    j=int(input("==>"))
    vector1=int(input("incresa el vector 1:"))
    vector2=int(input("incresa el vector 2:"))
    jh= vector1**2
    jh2= vector2**2
    jh3= jh + jh2 /1/2
    pta= math.sin(jh3)
    iu= vector1+vector2
    iu2= vector1/1/2
    iu3= vector2/1/2
    iu4= v=iu2 * iu3
    iu5= math.cos(iu4)
    if j > 0 and j==2:
       print("okey empezemos")
    if j == 1:
       print(vector1)
       print(vector2)
       
    if vector1>0 and vector2>0:
           print(pta)
           print("esta es la maginitud de ambos")

    if iu > 0:
       print(iu)
       print("esta es la maginitud vector 1")
       print(iu5)
       print("esta es la maginitud vector 2")

    else:
       print("mal joven")
       quit()

def baby1():
    print("=bienvenido que deseas hacer?=")
    print("                               ")
    print("2. resolver producto punto")
    ty='no tardes mucho nene'
    engine.say(ty)
    engine.runAndWait()
    opcion= int(input("==> "))

    if True:

        if opcion == 2:
            uwu=list(input("incresa tu numero vector p:  " ))
            uwu2=[int(jj)for jj in uwu]
            jiji=list(input("incresa tu numero vector z:  "))
            jiji2=[int(jj)for jj in jiji]
            print("=====comenzemos======")
            multi1=[jiji2[0]*uwu2[0],jiji2[1]*uwu2[1]]
            suma1=multi1[0]+multi1[1]
            multi2=[jiji2[0]*uwu2[1],jiji2[1]*uwu2[0]]
            divi=multi2[0]/1/2+multi2[1]/1/2
            total=suma1/divi
            print(suma1)
            print("-------")
            print(divi)
            print("""
                       esto es igual a |
                                     ~""")
            print(total)
            print("===paralelismo========")

def matrices():
    a=np.array([    [0,0,0],
                [0,0,0],
                [0,0,0]]) 
    print("=====fila1======")
    for m in range(1,4):
        j=int(input("numero:"))
        if m==1:
           a[0,0]=j
        if m ==2:
            a[0,1]=j
        if m == 3:
            a[0,2]=j
    print("=====fila2=====")
    for m in range(1,4):
        j=int(input("numero:"))
        if m==1:
            a[1,0]=j
        if m ==2:
            a[1,1]=j
        if m == 3:
            a[1,2]=j
    print("=====fila3========")
    for m in range(1,4):
        j=int(input("numero:"))
        if m==1:
            a[2,0]=j
        if m ==2:
            a[2,1]=j
        if m == 3:
            a[2,2]=j
    b= a[0,0]*a[1,1]*a[2,2]
    c= a[2,0]*a[1,1]*a[0,2]
    d=a[2,1]*a[1,1]*a[0,0]
    f= a[2,2]*a[1,1]*a[0,1]
    g= a[0,1]*a[1,2]*a[2,0]
    k=a[0,2]*a[1,1]*a[2,1]
    print(a)
    print("==esta es la matriz a resolver===")
    print(b)
    print(c)
    print(d)
    print(f)
    print(g)
    print(k)
    bf=b+c+d-d-f-g+k
    print("el determinarte es: ")
    print(bf)
    print("el ejercicio  RESOLVER")
   
while la>0:
    
    if la == 1:
        baby1()
    if la == 3:
        codigodelamor()
    if la == 2:
        baby()
    if la == 4:
        matrices()
    la = 0
    

