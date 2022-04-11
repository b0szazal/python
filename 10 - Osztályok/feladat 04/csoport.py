from tanulo import *
from typing import *

class Csoport:
    def __init__(self, csoportnev:str, tanulok:List[Tanulo]):
        super().__init__()
        self.csoportnev:str=csoportnev
        self.tanulok:List[Tanulo]=tanulok

    def __str__(self)->str:
        output:str= f"Csoport neve: {self.csoportnev}, tagjai : "
        for tanulo in self.tanulok:
            output+= f"\n{tanulo}"
        return output