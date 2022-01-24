harommalOszthatoParatlanokSzama:int=0

print("Kezdőérték=")
kezdoErtek:int=int(input())

print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek, 1):
    if (i % 3 == 0 and i % 2 == 1):
        harommalOszthatoParatlanokSzama+=1
        
print(f"{harommalOszthatoParatlanokSzama} páratlan szám osztható 3-mal.")