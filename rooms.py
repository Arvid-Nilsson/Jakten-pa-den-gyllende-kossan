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