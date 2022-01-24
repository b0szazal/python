def osszeadas(a:float, b:float)->float:
    eredmeny:float= a + b
    return eredmeny

def kivonas(a:float, b :float)->float:
    eredmeny:float= a - b
    return eredmeny

def szorzas(a:float, b : float)->float:
    eredmeny:float= a * b
    return eredmeny

def osztas(a: float, b:float)->float:
    if (b == 0):
        return 0
    
    eredmeny:float= a / b
    return eredmeny
