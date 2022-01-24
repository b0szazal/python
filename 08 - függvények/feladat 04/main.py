import time
import os

beirthomerseklet:float=None
atvaltasfajtaja:str=None
atvaltottfok:float=None

def hibakiiras(szoveg:str)->None:
    print(szoveg)
    time.sleep(3)
    os.system("cls")

def homersekletbekeres()->float:
    homerseklet:float=None
    while (homerseklet == None):
        data:str=input("Kérem adja meg a hőmérsékletet °C-ban:  ")
        if(data.replace(".", "").replace("-", "").isnumeric()):
            homerseklet= float(data)
            if(homerseklet < -273.15):
                homerseklet=None
                hibakiiras("Ilyen alacson hőmérséklet nincs.")
            else:
                return homerseklet
        else:
            hibakiiras("Nem számot adott meg.")

def atvaltasvalasztas()->str:
    eredmeny:str=None
    while(eredmeny == None):
        data:str=input("Kérem a váltás módját [F vagy K]:  ")
        if(data.capitalize() == "K" or data.capitalize() == "F"):
            eredmeny = data.capitalize()
            return eredmeny
        else:
            hibakiiras("Ilyen opció nincs!")

def atvaltas(Celsius:float, mire:str)->float:
    if(mire == "K"):
        return Celsius + 273.15
    elif (mire=="F"):
        return 9/5 * Celsius +32

def kiiras(Celsius:float, atvaltottFok:float, mertekegyseg:str):
    print(f"{Celsius}°C = {atvaltottFok}{mertekegyseg}.")

beirthomerseklet=homersekletbekeres()
atvaltasfajtaja=atvaltasvalasztas()
atvaltottfok=atvaltas(beirthomerseklet, atvaltasfajtaja)
kiiras(beirthomerseklet, atvaltottfok, atvaltasfajtaja)