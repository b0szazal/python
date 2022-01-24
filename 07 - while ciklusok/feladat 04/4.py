import time
import os

print("A program addig fog futni, amíg a beolvasott számok összege meghaladja 100-at.")

beovasasokszama:int=0
osszeg:int= 0
beolvasottszam:int=0
data:str=''

while(osszeg < 100):
    data= input("Kérek egy számot:")
    beovasasokszama+= 1

    if(data.replace("-", "").isnumeric()):
        beolvasottszam = int(data)
    else:
        print("Nem számot adott meg, vagy tizedesszámot.")

    osszeg+= beolvasottszam
    print(f"Eddig {beovasasokszama}-szer olvasott be számot.")
    print(f"A jelenlegi szám: {osszeg}.")
    time.sleep(3)
    os.system("cls")

print(f"{beovasasokszama} beolvasás után a végleges szám: {osszeg}.")