class Levelezesicim:
    def __init__(self, telepules:str, megye:str, iranyitoszam:int, kozterulet:str, szam:str):
        super().__init__()
        self.telepules:str=telepules
        self.megye:str=megye
        self.iranyitoszam:int=iranyitoszam
        self.kozterulet:str=kozterulet
        self.szam:str=szam

    def __str__(self)->str:
        return f"{self.megye} megye : {self.iranyitoszam}, {self.telepules} {self.kozterulet} {self.szam}"