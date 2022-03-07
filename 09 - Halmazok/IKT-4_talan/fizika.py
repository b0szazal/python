#Van 1-6-ig egy-egy számozott kör egy dobozban, és van egy üres dobozunk.
#amikor dobunk egy dobókockával egy számot akkor az a szám a másik dobozba kerül
#a dobások számát a felhasználótól kérjük be vagy random számmal generáljuk le
#a dobások után kiírassuk ki a helyzeteket

from typing import *
import time
import os
import random

baloldal:List[int]=[1, 2, 3, 4, 5, 6]
jobboldal:List[int]=[]
hatnulla:int=0
otegy:int=0
negyketto:int=0
haromharom:int=0
kettonegy:int=0
egyot:int=0
nullahat:int=0

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
    eredmeny:int=random.randint(1, 6)
    return eredmeny

def kivetel(dobotszam:int, kivetel:List[int])->List[int]:
    megtalalas:int=kivetel.index(dobottszam)
    del(kivetel[megtalalas])
    return kivetel

def hozzaadas(dobotszam:int, hozzaadas:List[int])->List[int]:
    hozzaadas.append(dobottszam)
    return hozzaadas

def helyzet(bal:List[int], jobb:List[int]):
    print(f"A jelenlegi állás {len(bal)}-{len(jobb)}")
    time.sleep(0.25)

dobasokszama:int=szambeolvasas()
for i in range(0, dobasokszama, 1):
    dobottszam:int=dobas()
    if (dobottszam in baloldal):
        kivetel(dobottszam, baloldal)
        hozzaadas(dobottszam, jobboldal)
    else:
        kivetel(dobottszam, jobboldal)
        hozzaadas(dobottszam, baloldal)

    if (len(baloldal)==6):
        hatnulla+=1
    elif(len(baloldal)==5):
        otegy+=1
    elif(len(baloldal)==4):
        negyketto+=1
    elif(len(baloldal)==3):
        haromharom+=1
    elif(len(baloldal)==2):
        kettonegy+=1
    elif(len(baloldal)==1):
        egyot+=1
    else:
        nullahat+=1

    if(dobasokszama<=100):
        helyzet(baloldal, jobboldal)

print(f"Összesítés \n 6-0: {hatnulla} \n 5-1: {otegy} \n 4-2: {negyketto} \n 3-3: {haromharom} \n 2-4: {kettonegy} \n 1-5: {egyot} \n 0-6: {nullahat}")