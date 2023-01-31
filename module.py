import json

f = open('inventory.json')
  
data = json.load(f)
  
f.close()