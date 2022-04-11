class Merevlemez:
    def __init__(self, gyarto:str, tipus:str, meret:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.meret:int=meret

    def __str__(self):
        return f"Tárhely gyártó: {self.gyarto}, típusa: {self.tipus}, méret: {self.meret}GB"