from typing import *

lista:List[int]=[0, 1, 2]
#teszt
#törlés
del(lista[1])
lista.append(input("adjon egy számot  "))
#mert kell
szam:float=lista[2]
print(szam)
#rossz insert
lista.insert(45, 10)
#print(lista[45])

kiskutyak:Tuple[str]=("a", "b")
print(kiskutyak)