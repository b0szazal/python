import os
import time

felhasznalopontszama:int=None
felhasznaloErdemjegye:int=None

def hibakiiras(szoveg:str):
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def pontszambekeres()->int:
    eredmeny:int=None
    while(eredmeny==None or eredmeny < 0 or eredmeny > 100):
        data:str=input("Kérek egy pontszámot(0-100ig):  ")
        if(data.replace("-", "").isnumeric()):
            eredmeny=int(data)
            if(eredmeny < 0 or eredmeny > 100):
                hibakiiras("Rossz számot adott meg!")
            else:
                return eredmeny
        else:
            hibakiiras("Nem számot adott meg!")

def pontszamvizsgalas(pontszam:int)->int :
    eredmeny:int=None
    if(pontszam < 50):
        eredmeny=1
    elif(pontszam >= 50 and pontszam < 60):
        eredmeny=2
    elif(pontszam>=60 and pontszam <70):
        eredmeny=3
    elif(pontszam>=70 and pontszam<85):
        eredmeny=4
    else:
        eredmeny=5

    return eredmeny

def kiiras(erdemjegy:int):
    print(f"Az ön érdemjegye: {erdemjegy}.")

felhasznalopontszama=pontszambekeres()
felhasznaloErdemjegye=pontszamvizsgalas(felhasznalopontszama)
kiiras(felhasznaloErdemjegye)