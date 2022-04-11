from motorkerekpar import *
from tulajdonos import *

tulaj:Tulajdonos=Tulajdonos("C", "1999.05.31.", "egyéb", "London")
motor:Motorkerekpar=Motorkerekpar("Honda", "NT1100", "motor", 30, 250, 200, tulaj)
print(motor)