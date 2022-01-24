print("a=")
a: float=float(input())

print("b=")
b: float=float(input())

print("c=")
c: float= float(input())

print("d=")
d: float= float(input())

osszeg: float= a + b
kulonbseg: float = c - d
eredmeny: float= osszeg / kulonbseg
print(f"A ({a} + {b}) / ({c} - {d}) = {eredmeny}")