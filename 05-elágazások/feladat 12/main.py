print("x=")
x:int=int(input())

if((x >= 10 and x <= 20) or (x >= -20 and x <= -10 )):
    print(f"Az {x} 10 és 20 közt van, vagy -20 és -10 közt.")
else:
    print(f"Az {x} nincs 10 és 20, vagy -20 és -10 közt.")

