from typing import *
import random

honapok:Tuple[str]=(
 "Január",
 "Február",
 "Március",
 "Április",
 "Május",
 "Június",
 "Július",
 "Augusztus",
 "Szeptember",
 "Október",
  "November",
 "December")
fizetesek:List[int]=[]
osszeg:int=None
adozas:float=None
egeszsegugyiresz:float=None
nyugdijhozzajarulas:float=None

def halmazkitoltes()->List[int]:
    lista:List[int]=[]
    for i in range(0, 12, 1):
        generaltszam:int=random.randint(200, 10000)
        lista.append(generaltszam)

    return lista

def kiiras(lista:List[int], tuple:Tuple[str]):
    for index in range(0, 12, 1):
        print(f"{tuple[index]}: {lista[index]} ezer Ft.")

def osszege(lista:List[int])->int:
    eredmeny:int=0
    for item in lista:
        eredmeny+=item
        
    return eredmeny

def szja(halmazosszeg:int)->float:
    szjaminden:float=halmazosszeg * 0.335
    egeszsegugy:float=szjaminden * 0.45
    nyugdij:float=szjaminden * 0.55
    return szjaminden, egeszsegugy, nyugdij

fizetesek=halmazkitoltes()
print("A havi bruttó fizetés: ")
kiiras(fizetesek, honapok)
osszeg=osszege(fizetesek)
print(f"Összesen: {osszeg} ezer Ft")
adozas, egeszsegugyiresz, nyugdijhozzajarulas=szja(osszeg)
print(f"Ebből {adozas} ezer Ft SZJA-t fizet ({egeszsegugyiresz} ezer egészségügyi hozzájárulást és {nyugdijhozzajarulas} nyugdíjalapot).")