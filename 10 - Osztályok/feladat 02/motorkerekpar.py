from tulajdonos import *

class Motorkerekpar:
    def __init__(self, gyarto:str, tipus:str, kivitel:str, teljsitmeny:int, suly:int, hengerurtartalom:int, tulajdonos:Tulajdonos):
        super().__init__()
        self.gyarto:str=gyarto
        self.tipus:str=tipus
        self.kivitel:str=kivitel
        self.teljsitmeny:int=teljsitmeny
        self.suly:int=suly
        self.hengerurtartalom:int=hengerurtartalom
        self.tulajdonos:Tulajdonos=tulajdonos

    def __str__(self):
        return f"{self.gyarto}  {self.tipus}  {self.kivitel} ({self.teljsitmeny}kW)\nsúly: {self.suly} kg, hengerűrtartalom: {self.hengerurtartalom} cm3,\n{self.tulajdonos}"