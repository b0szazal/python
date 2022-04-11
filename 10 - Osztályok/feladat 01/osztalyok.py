import math

class Teglalap:
    def __init__(self, a:float=0, b:float=0):
        super().__init__()
        self.a:float=a
        self.b:float=b

    def __str__(self)->str:
        return f"A téglalapban a={self.a}, b={self.b}\nterülete: {self.terulet()}, kerülete: {self.kerulet()}"

    def terulet(self)->float:
        return self.a * self.b

    def kerulet(self)->float:
        return 2 * (self.a + self.b)

class Kor:
    def __init__(self, sugar:float=0):
        super().__init__()
        self.sugar:float=sugar

    def __str__(self)->str:
        return f"A körnek r={self.sugar}\nterülete: {self.terulet()}, kerülete: {self.kerulet()}"

    def kerulet(self)->float:
        return 2 * self.sugar * math.pi
    
    def terulet(self)->float:
        return self.sugar*self.sugar * math.pi / 2

class Szabalyosharomszog:
    def __init__(self, a:float=0):
        super().__init__()
        self.a:float=a

    def __str__(self)->str:
        return f"A szabályos háromszögnek a={self.a}\nterülete: {self.terulet()}, kerülete: {self.kerulet()}"

    def kerulet(self)->float:
        return 3*self.a

    def terulet(self)->float:
        magassag:float= math.sqrt(self.a * self.a - self.a/2 * self.a/2)
        return self.a * magassag / 2

class Derekszoguharomszog:
    def __init__(self, befogo1:float=0, befogo:float=0, atfogo:float=0):
        super().__init__()
        self.befogo:float=befogo
        self.befogo1:float=befogo1
        self.atfogo:float=atfogo

    def __str__(self)->str:
        return f"A derékszögű háromszögnek egyik befogója={self.befogo}, másik={self.befogo1}, átfogója={self.atfogo}\nterülete: {self.terulet()}, kerülete: {self.kerulet()}"

    def kerulet(self)->float:
        return self.befogo + self.befogo1 + self.atfogo

    def terulet(self)->float:
        return self.befogo * self.befogo1

class Egyenloszeruharomszog:
    def __init__(self, szarak:float=0, alap:float=0):
        super().__init__()
        self.szarak:float=szarak
        self.alap:float=alap

    def __str__(self)->str:
        return f"Az egyenlő szárú háromszögnek alapja={self.alap}, szárai={self.szarak}\nterülete: {self.terulet()}, kerülete: {self.kerulet()}"

    def kerulet(self)->float:
        return 2*self.szarak + self.alap

    def terulet(self)->float:
        magassag:float=math.sqrt(self.szarak * self.szarak - self.alap/2 * self.alap/2)
        return self.alap * magassag / 2