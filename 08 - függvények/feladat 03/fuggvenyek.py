import time
import os
import datetime

def nevbekeres()->str:
    nev:str=None
    while(nev==None or len(nev)<3 or nev.isspace()):
        data:str=input("kérem a nevét:")
        if (len(data)<3 or data.isspace()):
            print("Túl rövid nevet adott meg vagy csak Space karakterekből áll.")
            time.sleep(3)
            os.system("cls")
        else:
            nev = data
            return nev
    
def szuletesievbekeres() -> int:
    szuletesiev:int=None
    ma:datetime=datetime.datetime.now() #mai dátum
    jelenlegiev:int=int(ma.strftime("%Y")) #jelenlegi év
    while(szuletesiev == None):
        data:str=input("Kérem a születési évét:  ")
        if (data.replace("-", "").isnumeric()):
            szuletesiev= int(data)
            if (szuletesiev >= jelenlegiev):
                szuletesiev = None
                print("A születési éve nem lehet nagyobb a jelenlegi évnél.(még meg se született)")
                time.sleep(3)
                os.system("cls")
            else:
                return szuletesiev
        else:
            print("Nem számot adott meg")
            time.sleep(3)
            os.system("cls")

def eletkorkiszamitas(szuletesiev:int)->int:
    ma:datetime=datetime.datetime.now()
    jelenlegiev:int=int(ma.strftime("%Y"))
    eletkor:int= jelenlegiev - szuletesiev 
    return eletkor

def kiiratas(nev:str, eletkor:int):
    print(f"{nev} ön az idén {eletkor} éves.")