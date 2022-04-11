class Negyzet:
    def __init__(self, a:float=0):
        super().__init__()
        self.a:float=a
    
    def terulet(self)->float:
        return self.a * self.a

    def kerulet(self)->float:
        return 4 * self.a

negyzet:Negyzet=Negyzet(10)
terulet:float=negyzet.terulet()
print(negyzet.a, terulet)