class Videokartya:
    def __init__(self, gyarto:str, tipus:str, memoria:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.memoria:int=memoria

    def __str__(self):
        return f"Videókártya gyártó: {self.gyarto}, típusa: {self.tipus}, memória: {self.memoria}GB"