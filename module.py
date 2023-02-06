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
def Choices(Situation, Options):
    Output = Situation

    for index, n in enumerate(Options, 1):

        if index == 1:
            Output += f"\nVill du {n} skriv {index}?\n"
        
        else:
            Output += f"Eller vill du {n} skriv {index}?\n"

    choice = input(Output)

    try:
        choice = int(choice)

    except:
        ChoseAgain(Situation, Options)

    if choice in range(1, len(Options)):
        return choice
    else:
        ChoseAgain(Situation, Options)

def ChoseAgain(Situation, Options):
    print(f"\nInmatningen måste vara ett heltal mellan 1 och {len(Options)}, ", end="")
    Choices(Situation, Options)


Choices("testing", [8, 5, "67", "hejsan"])