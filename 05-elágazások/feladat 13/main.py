print("x=")
x:int=int(input())

if(x >= 0 and x <= 9):
    print(f"Az {x} egyjegyű.")
elif(x <= 99 and x >= 10):
    print(f"Az {x} kétjegyű.")
elif(x >= 100 and x <= 999):
    print(f"Az {x} háromjegyű.")
elif(x < 0):
    print(f"Az {x} negatív.")
else:
    print(f"Az {x} több, mint háromjegyű.")