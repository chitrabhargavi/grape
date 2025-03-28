from tkinter import messagebox
from tkinter import *
from tkinter import simpledialog
import tkinter
from tkinter import filedialog
from imutils import paths
from tkinter.filedialog import askopenfilename

import numpy as np 
import pandas as pd 


from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
from sklearn.model_selection import train_test_split,KFold,cross_val_score,GridSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier, BaggingClassifier, AdaBoostClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.svm import LinearSVC

import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
import seaborn as sns
import cv2
import feature_extract


import warnings
warnings.filterwarnings('ignore')

main = tkinter.Tk()
main.title("Grape Leaf Detection")
main.geometry("1300x1200")

class test:
	def upload():
		global filename
		text.delete('1.0', END)
		filename = askopenfilename(initialdir = "Dataset")
		pathlabel.config(text=filename)
		text.insert(END,"Dataset loaded\n\n")

	def csv():
		global data
		text.delete('1.0', END)
		data=pd.read_csv(filename)
		text.insert(END,"Top Five rows of dataset\n"+str(data.head())+"\n")
		text.insert(END,"Last Five rows of dataset\n"+str(data.tail()))
		data.drop('Unnamed: 0',axis=1,inplace=True)

		
	def splitdataset():		 
	    text.delete('1.0', END)
	    print(data.columns)
	    X = data.iloc[:,:-1] 
	    Y = data.iloc[:,-1]
	    X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 7)
	    text.insert(END,"\nTrain & Test Model Generated\n\n")
	    text.insert(END,"Total Dataset Size : "+str(len(data))+"\n")
	    text.insert(END,"Split Training Size : "+str(len(X_train))+"\n")
	    text.insert(END,"Split Test Size : "+str(len(X_test))+"\n")
	    return X_train, X_test, y_train, y_test

	def MLmodels():
            global model_final
            X_train, X_test, y_train, y_test=test.splitdataset()
            text.delete('1.0', END)
            models=[]
            models.append(('SVM-Linear',LinearSVC()))
            models.append(('RandomForest',RandomForestClassifier()))
            models.append(('DecisionTree',DecisionTreeClassifier()))
            models.append(('Adaboost',AdaBoostClassifier()))
            models.append(('Bagging',BaggingClassifier()))
            results=[]
            names=[]
            predicted_values=[]
            text.insert(END,"Machine Learning Classification Models\n")
            text.insert(END,"Predicted values,Accuracy Scores and S.D values from ML Classifiers\n\n")
            for name,model in models:
                    kfold=KFold(n_splits=10,random_state=7)
                    cv_results=cross_val_score(model,X_train,y_train,cv=kfold,scoring='accuracy')
                    model.fit(X_train,y_train)
                    predicted=model.predict(X_test)

                    predicted_values.append(predicted)
                    results.append(cv_results.mean()*100)
                    names.append(name)
                    text.insert(END,"\n"+str(name)+" "+"Predicted Values on Test Data:"+str(predicted)+"\n\n")
                    text.insert(END, "%s: %f\t\t(%f)\n" %(name,cv_results.mean()*100,cv_results.std()))
                    if name == 'Bagging':
                            model_final=model
            return results
	        
	def graph():
	    results=test.MLmodels()	    
	    bars = ('SVM-Linear','RandomForest','DecisionTree','Adaboost','Bagging')
	    y_pos = np.arange(len(bars))
	    plt.bar(y_pos, results)
	    plt.xticks(y_pos, bars)
	    plt.show()

	def pred():
                global model_final
                filename = askopenfilename(initialdir = "Dataset")
                text.insert(END,"Predict File Selected\n\n")
                vector = feature_extract.featureExtraction(filename,1)
                test_data = pd.DataFrame([vector])
                               
                pred=model_final.predict(test_data)
                print(pred)
                text.insert(END,"For Image "+str(filename)+" Predicted Output is"+str(pred[0])+"\n")

font = ('times', 16, 'bold')
title = Label(main, text='Grape Leaf Detection Using Image Processing')
title.config(bg='sky blue', fg='black')  
title.config(font=font)           
title.config(height=3, width=120)       
title.place(x=0,y=5)

font1 = ('times', 14, 'bold')
upload = Button(main, text="Upload Dataset", command=test.upload)
upload.place(x=700,y=100)
upload.config(font=font1)

pathlabel = Label(main)
pathlabel.config(bg='dark orchid', fg='white')  
pathlabel.config(font=font1)
pathlabel.place(x=700,y=150)

df = Button(main, text="Reading Data ", command=test.csv)
df.place(x=700,y=200)
df.config(font=font1)

split = Button(main, text="Train_Test_Split ", command=test.splitdataset)
split.place(x=700,y=250)
split.config(font=font1)

ml= Button(main, text="All Classifiers", command=test.MLmodels)
ml.place(x=700,y=300)
ml.config(font=font1) 

graph= Button(main, text="Model Comparison", command=test.graph)
graph.place(x=700,y=350)
graph.config(font=font1)

pre= Button(main, text="Predict", command=test.pred)
pre.place(x=700,y=400)
pre.config(font=font1)

font1 = ('times', 12, 'bold')
text=Text(main,height=30,width=80)
scroll=Scrollbar(text)
text.configure(yscrollcommand=scroll.set)
text.place(x=10,y=100)
text.config(font=font1)

main.config(bg='sky blue')
main.mainloop()
