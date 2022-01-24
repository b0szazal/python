#csomagok importálása
import os
#import keyboard
import time

#változók definiálása

#a szám amit be kell olvasni
#kezdőrértéke None, mivel a while ciklusban ki lehet ezt használni, vagyis a ciklust mindaddig futtatjuk, még a változónak nem lesz számértéke
number:int= None
#segéd változó, a beolvasott értéket fogja tárolni
data:str=""

#while ciklus ami addig fut amig a number változó nem kap számértéket, értéke nem None lesz
while (number == None):
    #beolvasás a konzolról és a beolvasott értéket eétároljuk a data-ba
    data = input("Kérem a számot: ")
    #megvizsgáljuk, hogy a beolvasott érték (string) számra alakítható e
    #mindegy, higy ez a szám int vagy int típusú
    #isdigit() -> bool típusú változót ad visza
    if (data.isdigit()):
        #ha az isdigit() fg igaz akkor a számot írt fel a felhasználó, amit BIZTOS át tudunk számmá alakítani
        number = int(data)
    # ha  az isdigit hamis akkor a felhasználó nem számot írt be, number változó értéke None marad, így a while ciklus ismétlődni fog
    else:
        print("\n Nem számot adott meg!")
        #a programot futtató szálat (thred) elaltatjuk 3 másodpercre
        time.sleep(3)
        # 3 sec
        # letöröljük a képernyőt
        os.system("cls")
        

        #print("\n A folytatáshoz nyomja meg az ENTER billentyűt.")
        #egy végtelen while ciklust írunk, mivel arra fogunk várni, hogy a felhasználó lenyomja a kért billentyűt (ENTER)
        #while True:
        #figyeljük, hogy a felhasználó kenyomta e az ENTER gombot
            #if(keyboard.is_pressed('enter')):
    # letöröljük a képernyőt
                #os.system("cls")
    #kilépünk a belső (végtelen) while ciklusból
                #break

#kiírjuk a beolvasott számot
print(f"A beolvasott szám {number}")