print("x=")
x:int=int(input())

print("y=")
y:int=int(input())

if(x > y):
    print(f"Az {x} nagyobb.")
elif(x == y):
    print(f"Az {x} és {y} egyenlő.")
else:
    print(f"Az {y} nagyobb.")