#why

szamok:int=None
almak:str=""

def akarmi()->int:
  alma:str="alma"
  szam:int=15
  return szam, alma

almak, szamok=akarmi()
print(szamok)
print(almak)