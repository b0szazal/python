#hozzaadasVagyKivonas:int=0
eredmeny:int=0
elojelValto:int=1

print("Kezdőérték=")
kezdoErtek:int=int(input())

print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    eredmeny= eredmeny + i * elojelValto
    elojelValto= elojelValto * -1

print(f"Az eredmény: {eredmeny}.")