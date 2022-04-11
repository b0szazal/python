class Tanulo:
    def __init__(self, vezeteknev:str, keresztnev:str, szuletesidatum:str):
        super().__init__()
        self.vezeteknev:str=vezeteknev
        self.keresztnev:str=keresztnev
        self.szuletesidatum:str=szuletesidatum

    def __str__(self)->str:
        return f"{self.vezeteknev} {self.keresztnev}: születési dátum: {self.szuletesidatum}"