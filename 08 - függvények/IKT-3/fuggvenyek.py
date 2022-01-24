import re
import time
import os
from typing import Dict

def emailcimbeolvasas()->str:
    emailRe=re.compile(r"^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$")
    email:str=None
    while email == None:
        data:str=input("Kérem írja be az e-mail címét:  ")
        if(re.fullmatch(emailRe, data)):
            email= data
            return email
        else:
            print("Ilyen e-mail cím nem létezik.")
            time.sleep(3)
            os.system("cls")

def jelszobeolvasas()->str:
    jelszoRe=re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{8,}$")
    jelszo:str=None
    while jelszo == None:
        data=input("Kérem írja be a jelszavát:  ")
        if(re.fullmatch(jelszoRe, data)):
            jelszo = data
            return jelszo
        else:
            print("A jelszónak: \n - min. 8 karakterből kell hogy álljon \n - kell hogy legyen benne kis- és nagybetű \n - kell hogy legyen benn szám.")
            time.sleep(3)
            os.system("cls")

def isUserExists(email:str, password:str)->bool:
    users:Dict[str,str]={
        'zalan.szasz06@gmail.com': 'Password123',
        'hetfo@test.com': 'Testjelszo1',
        'kedd@test.com': 'Testjelszo2',
        'szerda@test.com': 'Testjelszo3',
        'csutortok@test.com': 'Testjelszo4',
        'pentek@test.com': 'Testjelszo5',
        'szombat@test.com': 'Testjelszo6',
        'vasarnap@test.com': 'Testjelszo7',
    }
    isExists:bool=((email, password) in users.items())
    return isExists

def hozzaferesmegadasa(hozzaferesadasa:bool):
    if(hozzaferesadasa == True):
        print("Sikeres bejelentkezés a rendszerbe!")
    else:
        print("A rendszerhez való hozzáférés megtagadva!")