import random
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
from copy import deepcopy
import json
file = open("output.csv", "r")
data = file.readlines()
file2 = open("1.3.D41_efect_gene_cds.csv")
genes = file2.readlines()
print ( sorted([len(line) for line in data])[-10000])
print (len( sorted([len(line) for line in data])[:]))

headr='"id","qid1","qid2","question1","question2","is_duplicate"'

fh = open("test.csv","w") 
fh.write(headr+'\n')
data=set(data)
data=list(data)
genes=[line.replace('"','').replace('\n','') for line in genes]
data=[line.replace('"','').replace('\n','') for line in data]

genz= [gene.split(';') for gene in genes[1:]]


D={}
P={}
RD={}
RP={}
print(genz[0][5])
for gene in genz:
    if gene[5].strip() not in P:
        P[gene[5].strip()]=[gene[0].strip()]
    else:
        P[gene[5].strip()]+=[gene[0].strip()]

    if gene[0].strip() not in RP:
        RP[gene[0].strip()]=[gene[5].strip()]
    else:
        RP[gene[0].strip()]+=[gene[5].strip()]

    for trait in gene[6:]:
        if trait.strip() not in D:
            D[trait.strip()]=[gene[0].strip()]    
        else:
            D[trait.strip()]+=[gene[0].strip()]

        if gene[0].strip() not in RD:
            RD[gene[0].strip()]=[trait.strip()]
        else:
            RD[gene[0].strip()]+=[trait.strip()]
            
print(P["signal peptidase subunit-12"])
data= [line.split(" ",1) for line in data]
data=[[line[0],line[1].split("stop")[0]] for line in data]
print(len(data))
random.shuffle(data)
print(data[0])
data,mata=deepcopy(data[:96000]),deepcopy(data[96000:])



with open('mata.json') as f:
    data = json.load(f)
print(":mu")
E={}
for date in data:
    E[date[0].strip()]=date[1].strip()

l=[len(li[1]) for li in list(P.items())]
print(sum(l) / float(len(l)))
print(len([li for li in l if li<5.0])) 
print(len([li for li in l if li<10.0]))
print(len([li for li in l if li<20.0]))
print(len([li for li in l if li<30.0]))
print(len([li for li in l if li<40.0]))
print(len([li for li in l if li<50.0])) 
print(len([li for li in l if li<60.0]))
print(len([li for li in l if li<70.0]))
print(len([li for li in l if li<80.0]))
print(len([li for li in l if li<90.0]))
print(len([li for li in l if li<100.0])) 
print(len([li for li in l if li<150.0]))
print(len([li for li in l if li<200.0]))
print(len([li for li in l if li<300.0]))
print(len([li for li in l if li<400.0]))
print(len([li for li in l]))
print("f")
for i in range(1000):
    a=random.choice([0,1])
    
    if(a==0):
        X=D
    else:
        X=P
    
    a=random.choice([0,1])
    if(a==0):
        K1,K2=random.sample(list(X.items()),2)
        if K1[0].count("probable")>0 or K1[0].count("unknown")>0 or K1[0].count("---NA---"):
            print("TRIGGERED")
            continue
        if K2[0].count("probable")>0 or K2[0].count("unknown")>0 or K2[0].count("---NA---"):
            print("TRIGGERED")
            continue
        

        K1=random.choice(K1[1])
        K2=random.choice(K2[1])
        if(set(RP[K1])&set(RP[K2]) or set(RD[K1])&set(RD[K2])):
            continue
       
        EQ="0"
    else:
        K=random.choice(list(X.items()))
        if K[0].count("unknown")>0 or K[0].count("probable")>0 or K[0].count("---NA---"):
            continue
        if(len(K[1])<2):
            continue
        else:
            K1,K2=random.sample(K[1],2)
            EQ="1"
            
    
    #print(K1,E[K1])
    try:
        fh.write('"0","1","2","{}","{}","{}"\n'.format(E[K1],E[K2],EQ))
    except:
        continue
    

fh.close()





