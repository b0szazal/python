import time
import os 
import random

parosszam:int=None
parosdata:str=""
parostavolsaga:int=0
parososneggyeloszthatok:int=0
paratlanszam:int=None
paratlandata:str=""
paratlantavolsaga:int=0
paratlanosneggyeloszthatok:int=0
atlag:int=0


while(parosszam == None or parosszam % 2 == 1):
    parosdata= input("Kérek egy páros számot:  ")
    if (parosdata.replace("-", "").isnumeric()):
        parosszam= int(parosdata)
        if (parosszam % 2 == 1):
            print("Páratlan számot adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

while (paratlanszam == None or paratlanszam <= parosszam or paratlanszam % 2 == 0):
    paratlandata= input(f"Kérek egy páratan számot amely nagyobb az előzőnél ({parosszam}):  ")
    if (paratlandata.replace("-", "").isnumeric()):
        paratlanszam= int(paratlandata)
        if (paratlanszam <= parosszam or paratlanszam % 2 == 0):
            print(f"Nem páratlan számot adott meg / Nem {parosszam}-nál nagyobb számot adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

rng:int=random.randint(parosszam, paratlanszam)
print(f"A gép generált egy {parosszam} és {paratlanszam} közti számot ami {rng}.")
time.sleep(3)

for i in range(parosszam, rng+1, 1):
    parostavolsaga+=1
    if (i % 4 == 0):
        parososneggyeloszthatok+=1

for j in range(rng, paratlanszam+1, 1):
    paratlantavolsaga+=1
    if (j % 4 == 0):
        paratlanosneggyeloszthatok+=1

if (paratlantavolsaga == parostavolsaga):
    print(f"A két szám egyenlő távolságra van {rng}-től.")
elif(paratlantavolsaga < parostavolsaga):
    print(f"{paratlanszam} közelebb van {rng}-hez, mint {parosszam}")
else:
    print(f"{parosszam} közelebb van {rng}-hez, mint {paratlanszam}")

atlag = (parosszam + paratlanszam) / 2
print(f"A két szám átlaga {atlag}.")
print(f"{parosszam} és {rng} közt {parososneggyeloszthatok} szám osztható 4-gyel.")
print(f"{rng} és {paratlanszam} közt {paratlanosneggyeloszthatok} szám osztható 4-gyel.")