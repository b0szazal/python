import time
import os

kezdoertek:int=None
kezdoertekdata:str=""
vegertek:int=None
vegertekdata:str=""

while (kezdoertek == None):
    kezdoertekdata= input("Kérek egy kezdőértéket:  ")
    if (kezdoertekdata.replace("-", "").isnumeric()):
        kezdoertek= int(kezdoertekdata)
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

while (vegertek == None or vegertek <= kezdoertek):
    vegertekdata = input(f"Kérek egy végértéket (a kezdőérték {kezdoertek}):  ")
    if (vegertekdata.replace("-", "").isnumeric()):
        vegertek = int(vegertekdata)
        if (vegertek <= kezdoertek):
            print("Nem megfelelő számot adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

for i in range(vegertek, kezdoertek - 1, -1):
    print(f"{i}  ")