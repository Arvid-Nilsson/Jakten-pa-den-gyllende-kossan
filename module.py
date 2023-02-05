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
