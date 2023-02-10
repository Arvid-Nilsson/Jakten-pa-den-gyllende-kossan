import json
import os

def ResetInventory():
    """Resets file intentory.json"""

    Inventory = {"Zejd": []}
    
    with open("inventory.json", "w") as F:
        F.write(json.dumps(Inventory))


def GiveBucket():
    """Adds bucket to Zejd in inventory.json"""

    with open("inventory.json", "r") as F:
        Data = json.load(F)

    Inventory = Data["Zejd"]

    if "bucket" not in Inventory:
        Inventory.append("bucket")

    #prints modified object to inventory.json
    with open("inventory.json", "w") as F:
        F.write(json.dumps(Data))


def CheckBucket():
    """Checks if zejd has bucket in inventory.json"""

    with open("inventory.json", "r") as F:
        Data = json.load(F)
        Inventory = Data["Zejd"]

        if "bucket" in Inventory:
            return True
            
        else:
            return False

# TODO: Maybe use a CLI to take button inputs rather than typing it.
def Choices(Situation, Options):
    """Lets user pick between options. Takes two arguments a string that is used as prompt and a list of options"""

    Output = Situation
    
    for Index, N in enumerate(Options, 1):

        if Index == 1:
            Output += f"\nVill du {N} skriv {Index}?\n"
            
        else:
            Output += f"Eller vill du {N} skriv {Index}?\n"
    
    while True:
        Choice = input(Output)

        #checks if user option is a whole number
        try:
            Choice = int(Choice)

        except:
            print(f"\nInmatningen måste vara ett heltal mellan 1 och {len(Options)}, ", end="")
            continue

        #checks if user option is in range of accepted options
        if Choice in range(1, len(Options) + 1):
            os.system("clear")
            return (Choice - 1)

        else:
            print(f"\nInmatningen måste vara ett heltal mellan 1 och {len(Options)}, ", end="")
            continue

if __name__ == "__main__":
    print(Choices("testing", [8, 5, "67", "hejsan"]))