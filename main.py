import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import ExtraTreesClassifier

x =[]
y =[]
t =[]

def Fill_data(x,y,t):
    doc = open("trajetoria_"".dat","r")
    doc = doc.readlines()
    docp = ""
    docl = []

    for i in range(len(doc)):
        docp+=doc[i]
        
    for i in range(len(doc)):
        docl.append(doc[i].replace('\n','').replace(' ','').split('\t'))
        
    for i in range(len(docl)):
        for d in range(len(docl[i])):
            docl[i][d] = docl[i][d].replace(',','.')
    c = 1
    

    while c<len(docl):
        
        docl[c][0] = float(docl[c][0])
        docl[c][1] = float(docl[c][1])
        docl[c][2] = float(docl[c][2])
        t.append(docl[c][0])
        x.append(docl[c][1])
        y.append(docl[c][2])
        c+=1
    return(x,y,t)

def Classifier_Data(data):
    asser = 0
    for i in range(len(data)):
        asser+=data[i]
    asser = asser/(len(data)) 
    print("-->",asser) 
    for i in range(len(data)):
        if data[i] <asser:
            data[i] = 0
        else:
            data[i] = 1    
    return data 

def DataLister(data):
    datal = []
    for i in range(len(data)):
        datal.append([])

    for i in range(len(datal)):
        datal[i].append(i)
        datal[i].append(data[i])
    return  datal
    


Fill_data(x=x,y=y,t=t)

x = Classifier_Data(x)
y = Classifier_Data(y) 
print(x,end="\n")
print(y,end="\n")
print(len(x))
x = DataLister(x)
y = DataLister(y)
print(x,end="\n")
print(y,end="\n")

x_treino, x_teste, y_treino, y_teste = train_test_split(x,y, test_size = 0.3)
try:
    modelo = ExtraTreesClassifier(n_estimators=10)
    modelo.fit(x_treino,y_treino)
    resultado = modelo.score(x_teste,y_teste)
    print("Precisão:",resultado)

except Exception as e:
    print(e)
