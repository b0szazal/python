print("x=")
x:int=int(input())

if(x % 4 == 0 and x % 6 == 0):
    print(f"Az {x} osztható 4-gyel és 6-tal is.")
else:
    print(f"Az {x} nem osztható 4-gyel és 6-tal.")