import time
import os

eletkor:int=None
eletkordata:str=""

while(eletkor == None or eletkor < 0 or eletkor > 99):
    eletkordata= input("Kérem az életkorát:   ")
    if(eletkordata.replace("-", "").isnumeric()):
        eletkor= int(eletkordata)
        if (eletkor < 0 or eletkor > 99):
            print("Nem megfelelő életkort adott meg.")
            time.sleep(3)
            os.system("cls")
    else:
        print("Nem számot adott meg.")
        time.sleep(3)
        os.system("cls")

if (eletkor >= 0 and eletkor <= 6):
    print("Ön egy gyerek.")
elif (eletkor >= 7 and eletkor <= 18):
    print("Ön iskolás.")
elif (eletkor >= 19 and eletkor <= 64):
    print("Ön egy dolgozó.")
else:
    print("Ön egy nyugdíjas.")