from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

def getInput(path):
    sequences=[]
    results=[]
    for line in open(path):
        line2=line.strip()
        elements=line2.split(" ")
        sequences.append(elements[:-1])
        results.append(elements[-1])
    maximum=max([len(a) for a in sequences])
    sequences2=[a+(maximum-len(a))*['0'] for a in sequences]
    return sequences2,results

def evalClassifier(classifier,i,o,cv):
    score=cross_val_score(classifier,i,o,cv=cv)
    print(classifier)
    print('{}-fold'.format(cv))
    print('Cross val score: {}; Score average:{}\n'.format(score,score.mean()))

i,o=getInput("training.txt")
t=DecisionTreeClassifier()
t1=RandomForestClassifier(n_estimators=100)
t2=ExtraTreesClassifier(n_estimators=100)
t3=AdaBoostClassifier(n_estimators=40)
t4=GradientBoostingClassifier(n_estimators=10)
evalClassifier(t,i,o,2)
evalClassifier(t1,i,o,2)
evalClassifier(t2,i,o,2)
evalClassifier(t3,i,o,2)
evalClassifier(t4,i,o,2)


