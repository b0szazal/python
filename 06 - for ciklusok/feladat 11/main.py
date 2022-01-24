sum:int=0
szorzat:int=1

print("Kezdőérték:")
kezdoErtek:int=int(input())

print("Végérték:")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek, 1):
    if (i % 2 == 0):
        sum+= i
    else:
        szorzat*=i

print(f"Páros számok összege = {sum}.")
print(f"Páratlan számok szorzata = {szorzat}.")