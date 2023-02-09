# know its risky but we know whats in module
from module import *
   
def Entre():
    while True:
        Decision = Choices("\nDu är i entrén, vad vill du göra?", ["gå till hallen", "titta runt i rummet"])
        if Decision == 0:
            return "hall" 
        elif Decision == 1:
            Decision = Choices("\nDu väljer att titta runt i rummet, vad vill du göra?", ["gå till höger", "gå till vänster"])
            if Decision == 0:
                Decision = Choices("\nDu väljer att gå och titta till höger i entrén. På den mossiga väggen ser du något som liknar en knapp, trycker du på den?", ["trycka på den", "inte göra det, och återvända till entén"])
                if Decision == 0:
                    print("Knappen du trycker på avlöser en fallucka under sig och du faller till din död")
                    return "quit"
                elif Decision == 1: 
                    return "entre"
            elif Decision == 1:
                Decision = Choices("\nDu väljer att gå och titta till vänster i entrén. Du finner dig titta på en mossig stenvägg. Vad vill du göra?", ["undersöka det närmare", "återvända"])
                if Decision == 0:
                    print("Du tyder på väggen 'Procrastination will reign supreme' och du börjar rysa. Det är inte första gången någon besöker detta tempel. Du väljer att återvända till entren.")
                    return "entre"
                elif Decision == 1:
                    return "entre"

def Hall():
    NextRoom = input("du är i Hallen vilket rum vill du gå till?")
    return NextRoom

def Guldtoalett():
    
    while True:
    
        Decision = Choices("\nDu är i Guldtoalleten, vad vill du göra?", ["gå till ett annat rum", "kolla runt"])
        
        if Decision == 0:
            
            Decision = Choices("\nDu tänker gå till ett annan rum, vilken?", ["gå tillbaka till hallen", "ångra dig"])

            if Decision == 0:

                return "hall"
            
            elif Decision == 1:

                Decision = None

        if Decision == 1: 

            InventCheck = CheckBucket()
            
            if InventCheck == False:
                GiveBucket()
                print("\nDu plockade upp en hink!")
            else:
                print("\nDu hittade inte något nytt.")


def Slutrum():
    NextRoom = input("du är i Slutrumet vilket rum vill du gå till?")
    return NextRoom