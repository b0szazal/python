from levelezesicim import *
from jatekos import *
from typing import *

class Roplabdacsapat:
    def __init__(self, csapatnev:str, jatekosok:List[Jatekos], szekhely:Levelezesicim):
        super().__init__()
        self.csapatnev:str=csapatnev
        self.jatekosok:List[Jatekos]=jatekosok
        self.szekhely:Levelezesicim=szekhely

    def __str__(self)->str:
        szoveg:str=f"{self.csapatnev}:\nSzékhely: {self.szekhely}"
        for jatekos in self.jatekosok:
            szoveg+=f"\n{jatekos}"

        return szoveg