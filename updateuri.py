import os
hashlisten = open("hashlist.json","r")
hashlist = hashlisten.readlines()
hashlisten.close()
mint_fist = []
for a in hashlist:
    pass
    a = a.replace('  "',"")
    a = a.replace(',','')
    a = a.replace('"','')
    a = a.replace("\n","")
    mint_fist.append(a)
mint_fist.pop(0)
mint_fist.pop(4999)


for mint in mint_fist:
    command = "metaboss update uri -a "+ mint + " -u https://raw.githubusercontent.com/Mach69ne/art-upgrade/main/"+mint+".json"
    runfile = open("command.cmd","w")
    runfile.write(command)
    runfile.close()
    os.system("command.cmd")
