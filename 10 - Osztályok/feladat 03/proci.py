class Processzor:
    def __init__(self, gyarto:str, tipus:str, orajel:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.orajel:int=orajel

    def __str__(self):
        return f"Processzor gyártó: {self.gyarto}, típusa: {self.tipus}, órajel: {self.orajel}MHz"