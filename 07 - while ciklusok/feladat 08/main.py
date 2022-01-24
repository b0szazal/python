import time
import os

beolvasottszam:int=None
beolvasottdata:str=""

while(beolvasottszam == None or beolvasottszam < 1 or beolvasottszam > 6):
    print("1 - almalé \t 2 - őszilé \t 3 - tea \n4 - Red Bull \t 5 - Hell \t 6 - ropi")
    beolvasottdata= input("Kérem írja be a választott termék számát:  ")
    if(beolvasottdata.replace("-", "").isnumeric()):
        beolvasottszam= int(beolvasottdata)
        if(beolvasottszam < 1 or beolvasottszam > 6):
            print("Ilyen számmal ellátott termék nincs az automatában.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Számot kell megadni.")
        time.sleep(3)
        os.system("cls")

if(beolvasottszam == 1):
    print("Tessék az almaleve.")
elif(beolvasottszam == 2):
    print("Tessék az őszileve.")
elif(beolvasottszam == 3):
    print("Tessék a teája.")
elif(beolvasottszam == 4):
    print("Tessék a Red Bull.")
elif(beolvasottszam == 5):
    print("Tessék a Hell.")
elif(beolvasottszam == 6):
    print("Tessék a ropija.")