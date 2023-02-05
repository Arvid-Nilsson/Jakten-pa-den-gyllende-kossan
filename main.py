import rooms as r
from module import ResetInventory
 
ResetInventory()

Room = "Entre"

while True:
    Room = Room.lower()
    if "entre" in Room:
        Room = r.Entre()
    elif "hall" in Room:
        Room = r.Hall()
    elif "guldtoalett" in Room:
        Room =r.Guldtoalett()
    elif "slutrum" in Room:
        Room = r.Slutrum()