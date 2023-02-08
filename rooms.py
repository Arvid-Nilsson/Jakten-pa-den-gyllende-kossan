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
    
    Decision = Choices("Du kommer in till ett stort rum, väggarna så höga att du inte ser taket. Vad gör du?", ["vända och går tillbaka till hallen", "kolla runt"])

    if Decision == 0:
        return "hall"

    Decision = Choices("När du tittar runt ser du en höjd platform och en trappa som leder upp till platformen, du tittar ännu närmare och ser en mörk skugga uppe på platformen. Vad gör du?", ["vända tillbaka och gå till hallen", "gå upp för trappan"])    

    if Decision == 0:
        return "hall"
