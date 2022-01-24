print("x=")
x:int=int(input())

if(x % 2 == 0):
    print(f"Az {x} páros.")
else:
    print(f"Az {x} páratlan.")

if(x < 0):
    print(f"Az {x} negatív.")
elif(x > 0):
    print(f"Az {x} pozitív.")
else:
    print(f"Az {x} se nem pozitív se nem negatív.")     *ez nem fontos

if(x % 5 == 0):
    print(f"Az {x} osztható 5-tel.")
else:
    print(f"Az {x} nem osztható 5-tel.")