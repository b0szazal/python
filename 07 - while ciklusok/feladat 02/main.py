# 1 - név nem lehet üres string     2 - egy vagy több szóköz      3 - név hossza (min 3 karakter)

import os
import time

egykiiras:int=0
nev:str=""

while (nev == ""  or nev.isspace() or len(nev) < 3):
    nev = input("Kérem a nevét:")
    egykiiras = 0
    if (nev == "" ):
        print("Nem adott meg semmit.")
        egykiiras+= 1
        time.sleep(3)
        os.system("cls")

    if (nev.isspace() and egykiiras == 0):
        print("A neve csak szóköz(ök)ből áll.")
        egykiiras+= 1
        time.sleep(3)
        os.system("cls")

    if (len(nev) < 3 and egykiiras == 0):
        print("A neve rövidebb 3 karakternél.")
        time.sleep(3)
        os.system("cls")

print(f"Üdvözlöm {nev}")