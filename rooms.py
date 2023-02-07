# know its risky but we know whats in module
from module import *

def Entre():
    NextRoom = input("du är i Entren vilket rum vill du gå till?")
    return NextRoom

def Hall():
    NextRoom = input("du är i Hallen vilket rum vill du gå till?")
    return NextRoom

def Guldtoalett():
    
    while True:
    
        Decision = Choices("Du är i Guldtoalleten, vad vill du göra?", ["gå till ett annat rum", "kolla runt"])
        
        if Decision == 0:
            
            Decision = Choices("Du tänker gå till ett annan rum, vilken?", ["gå tillbaka till hallen", "ångra dig"])

            if Decision == 0:

                return "hall"
            
            elif Decision == 1:

                break

def Slutrum():
    NextRoom = input("du är i Slutrumet vilket rum vill du gå till?")
    return NextRoom