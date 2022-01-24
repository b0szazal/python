harommalOszthatokSzama:int=0

print("Kezdőérték=")
kezdoErtek:int=int(input())

print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek, 1):
    if(i% 3 == 0):
        harommalOszthatokSzama+=1

print(f"{harommalOszthatokSzama} szám osztható 3-mal.")