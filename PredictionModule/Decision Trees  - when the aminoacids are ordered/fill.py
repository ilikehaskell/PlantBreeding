import re

with open("out.txt") as f:
    content = f.readlines()

print(len(content))

mp = dict()

for line in content:
    t = re.findall(r'"(.*?)"', line)
    if(str(t) in mp.keys()):
        mp[str(t)] = mp[str(t)] + 1
    else:
        mp[str(t)] = 1

out = open("data.txt", "w")

for line in content:
    t = re.findall(r'"(.*?)"', line)
    if mp[str(t)] == 1 :
        out.write(line)
        out.write(line)
    elif mp[str(t)] > 1:
        out.write(line)
