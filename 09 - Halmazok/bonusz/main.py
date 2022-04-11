from typing import *
import time
import os
import webbrowser

nevek:List[str]=[]
szabadnapok:List[int]=[]

def hibakiiras(szoveg:str):
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def nevbekeres()->str:
    eredmeny:str=None
    while (eredmeny==None or eredmeny.isspace() or len(eredmeny) < 3):
        eredmeny=input("Kérem adjon meg egy nevet:  ")
        if(eredmeny.isspace()):
            hibakiiras("Kérem ne csak SPACE karakterekből álljon a név.")
        elif(len(eredmeny) < 3):
            hibakiiras("Kérem legalább 3 karakterbőll álljon a név")

    return eredmeny

def szabadnapokszamanakbekerese(nev:str)->int:
    eredmeny:int=None
    while(eredmeny==None or eredmeny < 0 or eredmeny> 365):
        data:str=input(f"Kérem adja meg {nev} szabadnapjainak számát:  ")
        if(data.replace("-", "").isnumeric()):
            eredmeny=int(data)
            if(eredmeny < 0):
                hibakiiras("Negatív szabadnapszám nem lehet.")
            elif(eredmeny> 365):
                hibakiiras(f"Egy évben ennyi szabadnapja nem lehet {nev}-nek")
        else:
            hibakiiras("Nem számot adott meg.")

    return eredmeny

def nevekfeltoltese(lista:List[str]):
    hozzaadandonev:str=""
    for i in range(0, 10, 1):
        hozzaadandonev=nevbekeres()
        lista.append(hozzaadandonev)

def szabadnapokfeltoltese(lista:List[int], nev:List[str]):
    hozzaadandoszam:int=None
    for i in range(0, 10, 1):
        hozzaadandoszam=szabadnapokszamanakbekerese(nev[i])
        lista.append(hozzaadandoszam)

def kiiratas(nev:List[str], szabadnap:List[int]):
    szam:int=None
    neve:str=""
    for i in range(0, 10, 1):
        szam=szabadnap[i]
        neve=nev[i]
        print(f"{neve}-nek {szam} db szabadnapja van.")
        time.sleep(0.5)

def csokkenosorrendberakas(nev:List[str], szabadnap:List[int]):
    nevtemp:str=""
    szamtemp:int=None
    for i in range(0, len(nev)-1, 1):
        for j in range(i+1, len(nev), 1):
            if(szabadnap[i] < szabadnap[j]):
                szamtemp=szabadnap[i]
                szabadnap[i] = szabadnap[j]
                szabadnap[j]=szamtemp
                nevtemp=nev[i]
                nev[i]=nev[j]
                nev[j]=nevtemp

nevekfeltoltese(nevek)
szabadnapokfeltoltese(szabadnapok, nevek)
print("Az eredeti beolvasás szerint:")
kiiratas(nevek, szabadnapok)
csokkenosorrendberakas(nevek, szabadnapok)
print("\nA szabadnapok szerint csökkenő sorrendbe rendezve:")
kiiratas(nevek, szabadnapok)


time.sleep(10)
webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")