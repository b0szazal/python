import time
import os

szam:int=None
data:str=""

while (szam == None or szam > 9 or szam < 0):
    data= input("Kérek egy számot 0 és 9 között:")
    if(data.replace("-", "").isnumeric()):
        szam = int(data)
        if(szam != None and (szam > 9 or szam < 0)):
            print("Nem 0 és 9 közti számot adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

print(f"A szám {szam}")