import os
import time

beolvasottszam:int=None
beolvasottdata:str=""

while (beolvasottszam == None or (beolvasottszam < 100 and beolvasottszam > -100) or beolvasottszam > 999 or beolvasottszam < -999):
    beolvasottdata= input("Kérek egy háromjegyű számot:  ")
    if(beolvasottdata.replace("-", "").isnumeric()) :
        beolvasottszam = int(beolvasottdata)
        if((beolvasottszam < 100 and beolvasottszam > -100) or beolvasottszam > 999 or beolvasottszam < -999):
            print("Nem háromjegyű számot adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

if(beolvasottszam % 7 == 0):
    print(f"A beolvasott szám ({beolvasottszam}) osztható 7-tel.")
else:
    print(f"A beolvasott szám ({beolvasottszam}) nem osztható 7-tel.")