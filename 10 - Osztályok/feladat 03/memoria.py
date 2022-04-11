class Memoriakartya:
    def __init__(self, gyarto:str, tipus:str, kapacitas:int):
        super().__init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.kapacitas:int=kapacitas

    def __str__(self):
        return f"Memória gyártó: {self.gyarto}, típusa: {self.tipus}, Kapacitás: {self.kapacitas}GB"