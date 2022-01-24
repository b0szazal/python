print("kezdőérték:")
kezdoErtek:int=int(input())

print("Végérték:")
vegErtek:int=int(input())

sum:int=0

szorzat:int=1

for i in range(kezdoErtek, vegErtek, 1):
    sum+=i
    szorzat*= i

print(f"A {kezdoErtek} és {vegErtek} intervallum összege {sum}.")
print(f"A {kezdoErtek} és {vegErtek} intervallum szorzata {szorzat}.")