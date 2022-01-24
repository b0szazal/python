import time
import os

beolvasottszam:int=None
beolvasottdata:str=""
otteloszthatokoosszege:int=0
tizeneggyeloszthatokszama:int=0

while(beolvasottszam == None or beolvasottszam < 0 or beolvasottszam > 99):
    beolvasottdata= input("Kérek egy max. kétjegyű pozitív számot:  ")
    if (beolvasottdata.replace("-", "").isnumeric()):
        beolvasottszam= int(beolvasottdata)
        if (beolvasottszam < 0 or beolvasottszam > 99):
            print("Nem megfelelő számot adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

print("Ezek a páros számok:")

for i in range(0, beolvasottszam+1, 1):
    if (i % 2 == 0):
        print(f"{i}", end="  ")

    if (i % 5 == 0):
        otteloszthatokoosszege+= i

    if (i % 11 == 0):
        tizeneggyeloszthatokszama+= 1

print(f"\nAz öttel osztható számok összege {otteloszthatokoosszege}")
print(f"{tizeneggyeloszthatokszama} szám osztható 11-el.")
print("Ezek a számok 7-tel osztva 3-at adnak maradékul:")

for j in range(0, beolvasottszam+1, 1):
    if (j % 7 == 3):
        print(f"{j}", end="  ")