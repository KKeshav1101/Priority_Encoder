# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd

df = pd.read_csv("Tasks\\Tasks2.csv")


X = df.iloc[:,:-2].values
y = df.iloc[:,-2].values

import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

corpus = []

for i in range(len(X)):
  task = re.sub('[^a-zA-Z]', ' ', df.iloc[i, 4])
  task = task.lower()
  task = task.split()
  ps = PorterStemmer()
  all_stopwords = stopwords.words('english')
  task = [ps.stem(word) for word in task if word not in all_stopwords]
  task = ' '.join(task)
  corpus.append(task)



from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer(max_features=75)
embed = cv.fit_transform(corpus).toarray()


for i in range(len(df)):
  df[' brief_desc'][i] = embed[i]


df = pd.concat([df.pop(' brief_desc').apply(pd.Series), df[' task_type'], df[' hours_left'], df[' weight'], df[' completed']], axis=1)



X = df.iloc[:,:-2].values


from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer

ct = ColumnTransformer(transformers=[('encoder', OneHotEncoder(), [50])], remainder='passthrough')
# transformer: what kind of transformation and for what columns. remainder: what to do with other columns
X = np.array(ct.fit_transform(X))


from sklearn.ensemble import RandomForestRegressor
rf_reg = RandomForestRegressor(n_estimators=10, random_state=0)
rf_reg.fit(X, y)

def prep(task):
  desc= task[0]
  typ=task[1]
  hrsleft=task[2]
  ps=PorterStemmer()
  all_stopwords = stopwords.words('english')
  ntask = [ps.stem(word) for word in desc if word not in all_stopwords]
  ntask = ' '.join(ntask)
  ncorpus=[ntask]
  n_test=cv.transform(ncorpus).toarray()
  ntest_ = n_test[0]
  prep_ = [i for i in ntest_]
  prep_.append(hrsleft)
  if typ == 'Curricular':
    prep_.insert(0, 0.0)
    prep_.insert(1, 1.0)
    prep_.insert(2, 0.0)
    prep_.insert(3, 0.0)
  elif typ == 'Personal':
    prep_.insert(0, 0.0)
    prep_.insert(1, 0.0)
    prep_.insert(2, 0.0)
    prep_.insert(3, 1.0)
  elif typ == 'Co-Curricular':
    prep_.insert(0, 1.0)
    prep_.insert(1, 0.0)
    prep_.insert(2, 0.0)
    prep_.insert(3, 0.0)
  else:
    prep_.insert(0, 0.0)
    prep_.insert(1, 0.0)
    prep_.insert(2, 1.0)
    prep_.insert(3, 0.0)

  #print(prep_)
  return prep_

result = [prep(['maths homework', 'Curricular', 3])]

#print(result)

rf_reg.predict(result)

#import pickle
#file=open('pe.pkl','wb')
#pickle.dump(rf_reg,file)