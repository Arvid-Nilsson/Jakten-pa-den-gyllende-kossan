import json

def ResetInventory():
    inventory = {"Zejd": []}
    
    with open("inventory.json", "w") as f:
        f.write(json.dumps(inventory))


def GiveBucket():
    with open("inventory.json", "r") as f:
        data = json.load(f)

    inventory = data["Zejd"]

    if "bucket" not in inventory:
        inventory.append("bucket")

    with open("inventory.json", "w") as f:
        f.write(json.dumps(data))


def CheckBucket():
    with open("inventory.json", "r") as f:
        data = json.load(f)
        inventory = data["Zejd"]

        if "bucket" in inventory:
            return True
        else:
            return False

#TODO: Maybe use a CLI to take button inputs rather than typing it.
def Choices(Situation, Choices):
    
    print(Situation)

    ChoicesAmount = len(Choices)

    print(f"Du har {ChoicesAmount} val")

    for index, n in enumerate(Choices):

        if index == 0:
            print(f"Vill du {n}?\n")
        
        else:
            print(f"Eller vill du {n}?\n")


Choices("testing", [8, 5, "67", "hejsan"])