import json

def GiveBucket():
    with open("inventory.json", "r") as f:
        data = json.load(f)

    with open("inventory.json", "w") as f:
        inventory = data["Zejd"]

        if "bucket" not in inventory:
            inventory.append("bucket")
        
        f.write(json.dumps(data))