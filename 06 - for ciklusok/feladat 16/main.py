paratlanEsParosSzamokAtlaga:float=0
paratlanokOsszege:int=0
parosokOsszege:int=0

print("Kezdőérték=")
kezdoErtek:int=int(input())

print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek, 1):
    if (i % 2 == 0):
        parosokOsszege+=i
    else:
        paratlanokOsszege+=i

paratlanEsParosSzamokAtlaga= (paratlanokOsszege + parosokOsszege)/2


print(f"Az intervallum átlaga átlaga: {paratlanEsParosSzamokAtlaga}.")