f = open("hashlist.json","r")
hashes = f.read()
hashes = hashes.split('"')
counter = 0
howmany = 0
for i in hashes:
    if not counter%2==0:
        g = open(i+".json","r")
        data = g.read()
        if len(data)<500:
            print(i)
    counter = counter + 1
