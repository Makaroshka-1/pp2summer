import json

file = open("sample-data.json")
data = json.load(file)

output = "Interface Status\n================================================================================\n"
output += "DN                                                 Description           Speed    MTU  \n"
output += "-------------------------------------------------- --------------------  ------  ------\n"

for item in data['imdata']:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes['dn']
    descr = attributes.get('descr', '')
    speed = attributes.get('speed', 'inherit')
    mtu = attributes.get('mtu', '')

    output += f"{dn:50} {descr:20} {speed:7} {mtu:6}\n"

print(output)
