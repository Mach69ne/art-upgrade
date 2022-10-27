import os
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
    global mint_fist
    for i in range(1,5):
        mint_address = mint_fist[i]
        filename = mint_address + ".json"

        command = "metaboss decode mint --account "+ mint_address
        runfile = open("command.cmd","w")
        runfile.write(command)
        runfile.close()
        os.system("command.cmd")
getdata()
