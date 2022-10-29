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
    dean = 0
    for i in range(0,4999):
        mint_address = mint_fist[i]
        filename = mint_address + ".json"
        with open(filename, 'r') as d:
            data = json.load(d)
            d.close()
        with open(filename, 'w') as f:
          try:
            if data['attributes']:
                    attributes = data['attributes']
                    for k in range(0,5):
                        current_att = attributes[k]
                        if current_att['value']:
                            value = current_att['value']
                            #print(current_att['value'])
                            if value=="Theremal":
                                current_att['value']="Thermal"
                            #print(current_att['value'])
                            attributes[k] = current_att
                    data['attributes'] = attributes
          except:
              print(dean)
              print(filename)
              dean = dean + 1
          json.dump(data,f)
          f.close()

getdata()
