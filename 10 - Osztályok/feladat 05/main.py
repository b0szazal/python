from roplabdacsapat import *

szekhely:Levelezesicim=Levelezesicim("Szeged", "Csongrád", 6941, "Jóska u.", "13-20")
hetfo:Jatekos=Jatekos("Hétfő", "Helga", 15, "szélső ütő")
kedd:Jatekos=Jatekos("Kedd", "Ko", 69, "fogadó")
szerda:Jatekos=Jatekos("Szerda", "Szimp", 42, "támadó")
csutortok:Jatekos=Jatekos("Csütörtökk", "Csumi", 56, "feladó")
pentek:Jatekos=Jatekos("Péntek", "Péntek", 13, "center")
szombat:Jatekos=Jatekos("Szombat", "Simp", 87, "négyes ütő")
vasarnap:Jatekos=Jatekos("Vasárnap", "Vas", 5, "alma")
csapat:Roplabdacsapat=Roplabdacsapat("Józsik", [hetfo, kedd, szerda, csutortok, pentek, szombat, vasarnap], szekhely)
print(csapat)