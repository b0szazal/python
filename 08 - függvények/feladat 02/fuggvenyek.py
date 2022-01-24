import time
import os

def nevbekeres()->str:
    nev:str=None
    while(nev == None or nev.isspace() or len(nev) < 3):
        data:str=input("Kérem a nevét: ")
        if (data.isspace() or len(data) < 3):
            print("Túl rövid a neve (min 3 karakter), vagy csak space karakterből áll")
            time.sleep(3)
            os.system("cls")
        else:
            nev = data
            return nev

def udvozles(nev:str):
    print(f"Üdvözlöm {nev}!")