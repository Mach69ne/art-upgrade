import json
hashlisten = open("hashlist.json","r")
hashlist = hashlisten.readlines()
hashlisten.close()
mint_fist = []
for a in hashlist:
    a = a.replace('  "',"")
    a = a.replace(',','')
    a = a.replace('"','')
    a = a.replace("\n","")
    mint_fist.append(a)
mint_fist.pop(0)
mint_fist.pop(4999)
def getdata():
    for i in range(0,4999):
        mint_address = mint_fist[i]
        filename = mint_address + ".json"
        with open(filename, 'r') as d:
            data = json.load(d)
            d.close()
        with open(filename, 'w') as f:
            attributes = data['attributes']
            for k in range(0,5):
                current_att = attributes[k]
                value = current_att['value']
                #print(current_att['value'])
                current_att['value'] = value.title()
                #print(current_att['value'])
                attributes[k] = current_att
            print(attributes)
            data['attributes'] = attributes
            #print(data['attributes'])
            json.dump(data,f)
            f.close()

getdata()
