import json

with open('defaultSettings.json') as f: 
    data = json.load(f)
f.close()
data['Menu'].append({'subMenu':'Entrees','Buttons': []})
data['Menu'][1]['Buttons'].append({'itemName':'Tacos','cost':3.99})
data['Menu'][1]['Buttons'].append({'itemName':'Burrito','cost':3.99})
data['Menu'][1]['Buttons'].append({'itemName':'Salad','cost':3.99})

with open('outPut.json','w') as f:
    json.dump(data,f, indent = 2)
f.close()