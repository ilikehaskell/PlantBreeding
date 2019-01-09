import random
import numpy as np
from scipy.stats import binom
import matplotlib.pyplot as plt
from copy import deepcopy
import json
from predict_mod import predict


file2 = open("./data/1.3.D41_efect_gene_cds.csv")
genes = file2.readlines()
headr='"gene1","gene2","is_duplicate"'


genes=[line.replace('"','').replace('\n','') for line in genes]


genz= [gene.split(';') for gene in genes[1:]]


D={}
P={}
RD={}
RP={}

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
            


def property_relevance(input_gene):

    with open('./data/data.json') as f:
        data = json.load(f)
    with open('./data/mata.json') as f:
        mata = json.load(f)

    E={}
    for date in data:
        E[date[0].strip()]=date[1].strip()

    fh = open("./data/test.csv","w")
    fh.write(headr+'\n')



    l=[len(li[1]) for li in list(P.items())]
    for date in data:
        
        try:
            fh.write('"{}","{}","{}"\n'.format(date[1],input_gene,'0'))
        except:
            continue
        
    fh.close()
    gene_from_data=[date[0] for date in data]

    prediction=predict().tolist()
    data_predict=list(zip([i for j in prediction for i in j],gene_from_data))
    data_predict.sort()

    Rez={}
    for gena in data_predict[-100:]:
        gena=gena[1]
        for p in RP[gena]:
            if p not in Rez:
                Rez[p]=1
            else:
                Rez[p]+=1
        for p in RD[gena]:
            if p not in Rez:
                Rez[p]=1
            else:
                Rez[p]+=1
    rez=[]
    for key, value in Rez.items():
        temp = [value,key]
        rez.append(temp)
    rez=[tuple(d) for d in rez]
    rez.sort()
    return rez
