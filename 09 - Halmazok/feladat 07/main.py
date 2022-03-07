from typing import *
import random
import time
import os

halmaz:List[int]=[]
tobbszorbeirtszamok:Dict[int, int]={}
haromujszamegymasutan:int=0
ujszam:int=None

def hibakiiras(szoveg:str):
    print(szoveg)
    time.sleep(1.5)
    os.system("cls")

def szambekeres()->int:
    eredmeny:int=None
    while (eredmeny==None):
        data:str=input("Kérek egy számot amelyet még nem írt be:  ")
        if(data.replace("-", "").isnumeric()):
            eredmeny=int(data)
        else:
            hibakiiras("Nem számot adott meg")

    return eredmeny

def szotarkiiratas(szotar:Dict[int, int]):
    for key,item in szotar.items():
        print(f"{key}-et   {item+1}-szer")

while(haromujszamegymasutan<3):
    ujszam=szambekeres()
    if(halmaz.count(ujszam)==0):
        halmaz.append(ujszam)
        haromujszamegymasutan+=1
    else:
        hibakiiras("Ilyen számot már írt.")
        haromujszamegymasutan=0
        if(ujszam in tobbszorbeirtszamok.keys()):
            tobbszorbeirtszamok[ujszam]+=1
        else:
            tobbszorbeirtszamok[ujszam]=1

os.system("cls")
print(f"Gratulálok 3-szor egymás után úly számot addott meg,\nMinden beírt szám:  {halmaz}")
if (tobbszorbeirtszamok=={}):
    print("Mnden számot csak egyszer adott meg.")
else:
    print("többször beírt számok:")
    szotarkiiratas(tobbszorbeirtszamok)