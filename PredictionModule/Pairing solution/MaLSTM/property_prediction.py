
from datac import property_relevance
import json
with open('./data/mata.json') as f:
    mata = json.load(f)
x=[]
for i in range(1):
    x+=[property_relevance(mata[i][1])]

