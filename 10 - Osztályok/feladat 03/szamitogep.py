from proci import *
from videokartya import *
from merevlemez import *
from memoria import *

class Szamitogep:
    def __init__(self, proci:Processzor, videokartya:Videokartya, merevlemez:Merevlemez, memoria:Memoriakartya):
        super().__init__()
        self.proci:Processzor=proci
        self.videokartya:Videokartya=videokartya
        self.merevlemez:Merevlemez=merevlemez
        self.memoria:Memoriakartya=memoria

    def __str__(self):
        return f"Számítógép részei:\n{self.proci}\n{self.memoria}\n{self.merevlemez}\n{self.videokartya} "