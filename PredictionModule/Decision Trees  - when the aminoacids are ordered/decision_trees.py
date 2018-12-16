from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier
import pickle

def getInput(path):
    sequences=[]
    results=[]
    for line in open(path):
        line2=line.strip()
        elements=line2.split(" ")
        if elements.count("stop")==1:
            index=elements.index("stop")
            sequences.append(elements[1:index])
            results.append(" ".join(elements[index+1:]))
    maximum=max([len(a) for a in sequences])
    for a in sequences:
        a[len(a):]=(maximum-len(a))*['0']
    return sequences,results

def evalClassifier(classifier,i,o,cv):
    score=cross_val_score(classifier,i,o,cv=cv)
    print(classifier)
    print('{}-fold'.format(cv))
    print('Cross val score: {}; Score average:{}\n'.format(score,score.mean()))

"""
#Write to file only when training a new classifier  

i,o=getInput("data.txt")

classifier=ExtraTreesClassifier(n_estimators=20)
classifier=classifier.fit(i,o)

with open('classifier.pkl', 'wb') as f:
    pickle.dump(classifier, f)
"""

with open('classifier.pkl', 'rb') as f:
    classifier=pickle.load(f)

"""
t=DecisionTreeClassifier()
t1=RandomForestClassifier(n_estimators=20)
t2=ExtraTreesClassifier(n_estimators=20)
t3=AdaBoostClassifier(n_estimators=40)
evalClassifier(t,i,o,2)
evalClassifier(t1,i,o,2)
evalClassifier(t2,i,o,2)
evalClassifier(t3,i,o,2)
"""

