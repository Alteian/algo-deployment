#!/usr/bin/env python
# coding: utf-8

# # Loading of the data

# In[1]:


import pandas as pd
data = pd.read_csv('/code/src/algo/data/F1_training.csv').set_index('Driver')


# # Data preparation

# In[2]:


X = data[['Race_Entries', 'Race_Starts', 'Pole_Positions', 'Race_Wins', 'Fastest_Laps']].copy()
X.loc[:, 'Races_to_Wins'] = X['Race_Wins'] / X['Race_Entries']
X.loc[:, 'Races_to_Poles']  = X['Pole_Positions'] / X['Race_Entries']
X = X.drop(columns=['Race_Wins', 'Race_Entries', 'Pole_Positions'])
y = (data['Championships'] > 0) * 1


# # Test train split

# In[3]:


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"""
Shape of training dataset: {X_train.shape}
Shape of testing dataset: {X_test.shape}

# of champions in train: {y_train.sum()}
# of champions in test: {y_test.sum()}
""")


# # Model fitting

# In[4]:


from sklearn.linear_model import LogisticRegression
clf = LogisticRegression(random_state=0).fit(X_train, y_train)


# # Model evaluation

# In[5]:


from sklearn.metrics import confusion_matrix
y_pred = clf.predict(X_test)
confusion_matrix(y_pred=y_pred, y_true=y_test)


# We can observe that the model misspecified one of the champions to not be champion and vice versa.

# # Export to pickle

# In[6]:


import pickle
with open('/code/src/algo/model.pickle', 'wb') as f:
    pickle.dump(clf, f)

