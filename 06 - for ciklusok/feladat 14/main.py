ottelOszthatokOsszege:int=0
hettelOszthatokOsszege:int=0

print("Kezdőérték=")
kezdoErtek:int=int(input())

print("Végérték=")
vegErtek:int=int(input())

for i in range(kezdoErtek, vegErtek, 1):
    if (i % 5 == 0 and i % 7 == 0):
        ottelOszthatokOsszege+=i
        hettelOszthatokOsszege+=i
    elif(i % 5 == 0) :
        ottelOszthatokOsszege+=i
    elif (i % 7 == 0):
        hettelOszthatokOsszege+=i
    else:
        pass

if( ottelOszthatokOsszege == hettelOszthatokOsszege):
    print(f"A héttel oszthatók összege ({hettelOszthatokOsszege}) egyenlő az öttel oszthatók összegével ({ottelOszthatokOsszege}). ")
elif (ottelOszthatokOsszege > hettelOszthatokOsszege):
    print(f"A öttel oszthatók összege ({ottelOszthatokOsszege}) egyenlő az héttel oszthatók összegével ({hettelOszthatokOsszege}).")
else:
    print(f"A héttel oszthatók összege ({hettelOszthatokOsszege}) egyenlő az öttel oszthatók összegével ({ottelOszthatokOsszege}).")