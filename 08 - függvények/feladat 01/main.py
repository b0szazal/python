#fgk nevű fájl mindend részének importálása
from fgk import *
from thing import *

szam:int=None
szam1:int=None
osszeg:float=None
kulonbseg:float=None
szorzat:float=None
hanyados:float=None
        
while (szam == None):
    szam= tizedesszambeolvasas()

while (szam1 == None):
    szam1= tizedesszambeolvasas()

osszeg= osszeadas(szam , szam1)
kulonbseg= kivonas(szam, szam1)
szorzat= szorzas(szam, szam1)
hanyados= osztas(szam, szam1)

print(f"A két szám ({szam} és {szam1}) összege: {osszeg}, különbsége: {kulonbseg}, szorzata: {szorzat}, hányadosa: {hanyados}.")