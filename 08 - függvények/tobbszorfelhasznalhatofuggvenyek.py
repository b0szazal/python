def nevbekeres()->str:
    nev:str=None
    while(nev == None or nev.isspace() or len(nev) < 3):
        data:str=input("Kérem a nevét: ")
        if (data.isspace() or len(data) < 3):
            print("Túl rövid a neve (min 3 karakter), vagy csak space karakterből áll")
            time.sleep(3)
            os.system("cls")
        else:
            nev = data
            return nev

def szambeolvasas()->int:
    szam:int=None
    data=input(f"Kérek egy számot:  ")
    if(data.replace("-", "").isnumeric()):
        szam=int(data)
        return szam
    else:
        print("Nem számot adott meg!")