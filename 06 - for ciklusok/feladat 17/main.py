intervallumSzamainakOsszege:int=0
intervallumSzamainakSzama:int=0

print("Kezdőérték=")
kezdoErtek:int=int(input())

print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    intervallumSzamainakSzama+=1
    intervallumSzamainakOsszege+=i

intervallumAtlaga:float=intervallumSzamainakOsszege / intervallumSzamainakSzama
print(f"Az intervallum átlaga: {intervallumAtlaga}.")