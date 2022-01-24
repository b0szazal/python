print("x=")
x : float= float(input())
x+= 0.5

print("y=")
y: float= float(input())
y+= 0.7

print("z=")
z: float = float(input())

eredmeny: float= (x * y) % z 
print(f"A {x} * {y} / {z} művelet maradéka {eredmeny}.")
