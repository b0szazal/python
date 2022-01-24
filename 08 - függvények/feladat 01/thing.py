import os

def tizedesszambeolvasas()->float:
    data=input(f"Kérek egy számot:  ")
    if(data.replace("-", "").replace(".", "").isnumeric()):
        return float(data)
    else:
        print("Nem számot adott meg.")