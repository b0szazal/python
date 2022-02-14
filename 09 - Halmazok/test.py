from typing import *

#szotar:Dict[str, int]={
 #   'alma': 222,
  #  'barack': 1321}
#szotar.__delitem__('alma')
#print (szotar)

#for item in szotar:
    #print(item)
    #print(szotar[item])

#for kulcs, ertek in szotar.items():
 #   print(kulcs, ertek)

halmaz:List[int]=[1, 2, 3, 1]
#halmaz.add(1)
print(halmaz)
sett:Set[int]=set(halmaz)
sett.add(5)
sett.update({1, 2, 4}, {8, 5, 6})
#sett.update(halmaz)
print(sett)