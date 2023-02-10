# know its risky but we know whats in module
from module import *
import time
   
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
    
    while True:
        
        Decision = Choices("\nDu befinner dig i hallen, vad gör du?", ["Gå till höger rum", "Gå till vänster rum"])

        if Decision == 0:
            
            return "guldtoalett"
        
        if Decision == 1:
            
            Decision = Choices("\nDu står vid dörren till det nya rummet, vad gör du nu?", ["Öppna dörren", "ångra val"])

            if Decision == 0:

                return "slutrum"
            
            elif Decision == 1:

                Decision = None

    
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
                    time.sleep(2)
                    print(line)

            return "quit"

def IntoScene():
    with open("introscene.txt", "r") as f:
                text = f.readlines()

                for line in text:
                    time.sleep(2)
                    print(line)