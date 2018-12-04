from sklearn.model_selection import cross_val_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import GradientBoostingClassifier

def getInput(path):
    aminoacid_quantities=[]
    proteins=[]
    for line in open(path):
        line2=line.strip()
        elements=line2.split(" ",21)
        gene=elements[0]
        aminoacid_quantities.append(list(map(int,elements[1:21])))
        proteins.append(elements[21])
    return (aminoacid_quantities,proteins)

def getInstances(path):
    instances=[]
    for line in open(path):
        line2=line.strip()
        elements=line2.split(" ")
        gene=elements[0]
        instances.append(list(map(int,elements[1:])))
    return instances

def evalClassifier(classifier,i,o,split):
    score=cross_val_score(classifier,i,o,cv=split)
    print(type(classifier).__name__)
    print('{}-split'.format(split))
    print('Cross val score: {}; Score average:{}\n'.format(score,score.mean()))

i,o=getInput("training.txt")
t=DecisionTreeClassifier()
t1=RandomForestClassifier(n_estimators=10)
t2=ExtraTreesClassifier(n_estimators=10)
t3=AdaBoostClassifier(n_estimators=100)
t4=GradientBoostingClassifier(n_estimators=100)
evalClassifier(t,i,o,4)
evalClassifier(t1,i,o,4)
evalClassifier(t2,i,o,4)
evalClassifier(t3,i,o,4)
evalClassifier(t4,i,o,4)
instances=getInstances("instances.txt")
t=t.fit(i,o)
print(t.predict(instances))
t1=t1.fit(i,o)
print(t1.predict(instances))
t2=t2.fit(i,o)
print(t2.predict(instances))
t3.fit(i,o)
print(t3.predict(instances))
t4=t4.fit(i,o)
print(t4.predict(instances))
