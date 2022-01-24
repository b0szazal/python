import time
import os

szam:int=None
minimalisszam:int=None
data:str=""
kikotes:str=""

def szambeolvasas()->int:
    data=input(f"Kérek egy számot{kikotes}:  ")
    if(data.replace("-", "").isnumeric()):
        return int(data)
    else:
        return None

while(szam == None):
    szam= szambeolvasas()
    if (szam == None):
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

print(szam)

kikotes = " ami legelább 20"
while(minimalisszam == None or minimalisszam < 20):
    minimalisszam = szambeolvasas()
    if (minimalisszam == None):
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")
    elif(minimalisszam < 20):
        print("Nem megfelelő számot adott meg.")
        time.sleep(3)
        os.system("cls")

print(minimalisszam)