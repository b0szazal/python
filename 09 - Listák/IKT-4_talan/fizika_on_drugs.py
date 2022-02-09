from typing import *
import time
import os
import random

baloldal:List[int]=[]
kozep:List[int]=[]
jobboldal:List[int]=[]

def hibakiiras(szoveg):
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def szambeolvasas()->int:
    eredmeny:int=None
    while (eredmeny==None or eredmeny<0):
        data:str=input("Kérem adja meg a dobások számát:  ")
        if(data.replace("-", "").isnumeric()):
            eredmeny=int(data)
            if(eredmeny<0):
                hibakiiras("Negatív számszor nem lehet dobni.")
            else:
                return eredmeny
        else:
            hibakiiras("Nem számot adott meg.")

def dobas()->int:
    eredmeny:int=random.randint(1, 20)
    return eredmeny

def kivetel(dobotszam:int, kivetel:List[int])->List[int]:
    megtalalas:int=kivetel.index(dobottszam)
    del(kivetel[megtalalas])
    return kivetel

def hozzaadas(dobotszam:int, hozzaadas:List[int])->List[int]:
    hozzaadas.append(dobottszam)
    return hozzaadas

def helyzet(bal:List[int], jobb:List[int], kozeplista:List[int], dobasszam:int):
    print(f"A jelenlegi állás {len(bal)}-{len(kozeplista)}-{len(jobb)}")
    if (dobasszam<=100):
        time.sleep(0.25)

listabetoltes:int=szambeolvasas()
for i in range(0, listabetoltes, 1):
    baloldal.append(i)

dobasokszama:int=szambeolvasas()
for j in range(0, dobasokszama, 1):
    dobottszam:int=dobas()
    if (dobottszam in baloldal):
        kivetel(dobottszam, baloldal)
        hozzaadas(dobottszam, kozep)
    elif(dobottszam in kozep):
        kivetel(dobottszam, kozep)
        hozzaadas(dobottszam, jobboldal)
    else:
        kivetel(dobottszam, jobboldal)
        hozzaadas(dobottszam, baloldal)

    helyzet(baloldal, jobboldal, kozep, dobasokszama)