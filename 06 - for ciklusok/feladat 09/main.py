print("Kezdőérték")
kezdoErtek:int=int(input())

print("Végérték")
vegErtek:int=int(input())

if(vegErtek % 2 == 1):
    vegErtek+=1

for i in range(vegErtek, kezdoErtek, -2):
    print(i)
