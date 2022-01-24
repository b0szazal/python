import time
import os

penz:float=None
penzdata:str=""
honapokszama:int=0

while(penz==None or penz > 50000 or penz < 10000):
    penzdata= input("Kérek egy egész számot 10 ezer és 50 ezer közt:  ")
    if(penzdata.replace("-", "").isnumeric()):
        penz= int(penzdata)
        if(penz > 50000 or penz < 10000):
            print("Rossz értéket adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

while(penz < 100000):
    penz= penz * 1.02
    honapokszama+=1

print(f"{honapokszama} hónap alatt lett a pénz legalább 100000 2%-os kamattal.")