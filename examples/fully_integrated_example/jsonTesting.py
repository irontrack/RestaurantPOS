import json

with open('defaultSettings.json') as f: 
    data = json.load(f)
f.close()
data['Menu'].append({'subMenu':'Entrees','Buttons': []})
data['Menu'][1]['Buttons'].append({'itemName':'Tacos','cost':5.99})
data['Menu'][1]['Buttons'].append({'itemName':'Burrito','cost':6.99})
data['Menu'][1]['Buttons'].append({'itemName':'Salad','cost':5.99})

# now adding the Drinks Submenu
data['Menu'].append({'subMenu':'Drinks','Buttons': []})
data['Menu'][2]['Buttons'].append({'itemName':'Horchata','cost':2.99})
data['Menu'][2]['Buttons'].append({'itemName':'Cerveza','cost':5.99})
data['Menu'][2]['Buttons'].append({'itemName':'Jaritos','cost':1.99})

# now adding the Deserts Submenu
data['Menu'].append({'subMenu':'Desserts','Buttons': []})
data['Menu'][3]['Buttons'].append({'itemName':'Churro','cost':2.99})
data['Menu'][3]['Buttons'].append({'itemName':'Flan','cost':2.99})
data['Menu'][3]['Buttons'].append({'itemName':'Cajeta','cost':2.99})

with open('defaultSettings.json','w') as f:
    json.dump(data,f, indent = 2)
f.close()