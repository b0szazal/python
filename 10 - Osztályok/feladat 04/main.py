from csoport import *

charls:Tanulo=Tanulo("Leg", "Charles", "2000. 01. 01.")
jozsi:Tanulo=Tanulo("Kis", "Józsi", "2005. 03. 15.")
thomas:Tanulo=Tanulo("Fasz", "Tamás", "1969. 04. 20.")
csoport:Csoport=Csoport("sBinners", [charls, jozsi, thomas])
print(csoport)