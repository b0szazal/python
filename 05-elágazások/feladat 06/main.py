print("x=")
x:int=int(input())

print("y=")
y:int=int(input())

print("z=")
z:int=int(input())

if(x > y and x > z):
    if(y > z):
        print(f"{z}, {y}, {x}")
    elif(z > y):
        print(f"{y}, {z}, {x}")
    elif(y == z):
        print(f"{y} = {z}, {x}")
elif(y > x and y > z) :
    if(x > z):
        print(f"{z}, {x}, {y}")
    elif(z > x):
        print(f"{x}, {z}, {y}")
    else:
        print(f"{x} = {z}, {y}")
elif (z > x and z > y):
    if(y > x):
        print(f"{x}, {y}, {z}")
    elif (x > y):
        print(f"{y}, {x}, {z}")
    else:
        print(f"{x} = {y}, {z}")
elif (x == y and x > z):
    print(f"{z}, {y} = {x}")
elif (x == z and x > y):
    print(f"{y}, {z} = {x}")
elif (y == z and y > x):
    print(f"{x}, {y} = {z}")
else:
    print(f"{x} = {y} = {z}")