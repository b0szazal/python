print("x=")
x:int=int(input())

print("y=")
y:int=int(input())

print("z=")
z:int=int(input())

if(x % y == 0 and x % z == 0):
    print(f"Az {y} és {z} is osztója {x}-nek.")
elif(x % y == 0):
    print(f"Csak az {y} osztója {x}-nek.")
elif(x % z == 0):
    print(f"Csak az {z} osztója {x}-nek.")
else:
    print(f"Az {y} és a {z} nem osztója {x}-nek.")
