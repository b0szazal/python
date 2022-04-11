class Tulajdonos:
    def __init__(self, nev:str, szuletesidatum:str, nem:str, szuletesihely:str):
        super().__init__()
        self.nev:str=nev
        self.szuletesidatum:str=szuletesidatum
        self.nem:str=nem
        self.szuletesihely:str=szuletesihely
        
    def __str__(self):
        return f"Tulajdonos: {self.nev}, nem: {self.nem} születési dátum: {self.szuletesidatum}, Születési helye: {self.szuletesihely}"