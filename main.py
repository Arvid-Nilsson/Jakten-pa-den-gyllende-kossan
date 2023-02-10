import rooms as r
from module import ResetInventory
 
if __name__ == "__main__":
    ResetInventory()

    r.IntoScene()

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
        
        elif "quit" in Room:
            break