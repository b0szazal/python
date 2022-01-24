print("x=")
x:int=int(input())

if(x >= -30 and x <= 40):
    print(f"Az {x} -30 és 40 közt van.")
elif(x < -30):
    print(f"Az {x} kisebb -30-nál.")
else:
    print(f"Az {x} nagyobb 40-nél.")