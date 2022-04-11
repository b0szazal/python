from proci import *
from videokartya import *
from merevlemez import *
from memoria import *
from szamitogep import *

proc:Processzor=Processzor("Intel", "464", 1800)
videokari:Videokartya=Videokartya("asd", "Gforce", 16)
hdd:Merevlemez=Merevlemez("idk", "45a", 1024)
memory:Memoriakartya=Memoriakartya("stillidk", "asd12", 16)
szmito:Szamitogep=Szamitogep(proc, videokari, hdd, memory)
print(szmito)