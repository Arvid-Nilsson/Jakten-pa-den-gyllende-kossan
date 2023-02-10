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
    
    Decision = Choices("Du kommer in till ett stort rum, väggarna så höga att du inte ser taket. Vad gör du?", ["vända och gå tillbaka till hallen", "kolla runt"])

    if Decision == 0:
        return "hall"

    while True:
        Decision = Choices("När du tittar runt ser du en höjd platform och en trappa som leder upp till platformen, du tittar ännu närmare och ser en mörk skugga uppe på platformen. Vad gör du?", ["vända tillbaka och gå till hallen", "gå upp för trappan"])    

        if Decision == 0:
            return "hall"
                
        Decision = Choices("När du går upp för trappan börjar skuggan visa sig, det är en stor ko av guld. Vad gör du?", ["vända och gå ner för trappan", "titta närmare"])

        if Decision == 0:
            Decision = Choices("Du har gått ned för trappan. Vad gör du?", ["tittar tillbaka", "går ut till hallen"])
            continue
        
        if CheckBucket() == True:
            Decision = Choices("En tanke kommer till dig, du tänker att du kan mjölka kossan. Vad gör du?", ["mjölka kossan", "låta bli och gå tillbaka ned för trappan"])

            if Decision == 1:
                Decision = Choices("Du har gått ned för trappan. Vad gör du?", ["tittar tillbaka", "går ut till hallen"])
                continue

            Decision = Choices("När du mjölkat kossan märker du att mjölken har som en dragkraft, du känner en stark vilja att dricka den. Vad gör du?", ["häll ut mjölken och springa ned för trappan", "dricka mjölken"])
            
            if Decision == 0:
                print("Du ramlar i trappan och dör, Bättre lycka nästa gång")
                return "quit"
            
            with open("ending.txt", "r") as f:
                text = f.readlines()

                for line in text:
                    print(line)

            return "quit"
                 

