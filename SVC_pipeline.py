

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.pipeline import Pipeline
from sklearn.externals import joblib
from sklearn import svm
from sklearn import tree
import numpy as np
import pandas as pd


dataset = pd.read_csv('trainData.csv')
dataset.head()

testDataset=pd.read_csv('testdata.csv')
testDataset=pd.DataFrame(testDataset)
testDataset.head()

dataset.replace({"?":np.nan},inplace=True)
dataset = dataset.apply(lambda x: x.fillna(x.value_counts().index[0]))


testDataset.replace({"?":np.nan},inplace=True)
testDataset=testDataset.apply(lambda x: x.fillna(x.value_counts().index[0]))



#convert nominal to numeric
from sklearn.preprocessing import LabelEncoder
lb_make = LabelEncoder()
l=['A1','A3','A4','A6','A8','A9','A11','A13','A15']

for i in l:
     temp = lb_make.fit_transform(dataset[i])
     dataset[i] = temp

     temp1 = lb_make.fit_transform(testDataset[i])
     testDataset[i] = temp1




feature_names = ['A1','A2','A3','A4', 'A5','A6', 'A7','A8', 'A9','A10','A11',"A12","A13",'A14','A15']
X = dataset[feature_names]
y = dataset['A16']

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size = 0.3,random_state = 42)



# Construct some pipelines

pipe_svm = Pipeline([('scl', StandardScaler()),
			('pca', PCA(n_components=2)),
			('clf', svm.SVC(random_state=42))])

]

pipe_svm.fit(X, y)

y_pred=pipe_svm.predict(testDataset)

print('\n'.join(y_pred))



