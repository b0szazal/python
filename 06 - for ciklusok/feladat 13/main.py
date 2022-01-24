paratlanokOsszege:int=0
parosokOsszege:int=0

print("Kezdőérték=")
kezdoErtek:int=int(input())

print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek+1, 1):
    if (i % 2 == 0):
        parosokOsszege+=i
    else:
        paratlanokOsszege+=i

if (parosokOsszege > paratlanokOsszege):
    print(f"A páros számok összege ({parosokOsszege}) nagyobb a páratlan számok összegénél ({paratlanokOsszege}).")
elif(parosokOsszege < paratlanokOsszege):
    print(f"A páratlan számok összege ({paratlanokOsszege}) nagyobb a páros számok összegénél ({parosokOsszege}).")
else:
    print(f"A páros számok összege ({parosokOsszege}) egyenlő a páratlan számok összegével ({paratlanokOsszege}).")