import pandas as pd 
import numpy as np
from sklearn.linear_model import LogisticRegression


# training data
def dataSplit(data,ratio):
        shffled = np.random.permutation(len(data))
        testSize = int(len(data) * ratio)
        test_indices = shffled[:testSize]
        train_indices = shffled[testSize:]
        return data.iloc[train_indices],data.iloc[test_indices]

# predicting legends taking features as inputs
def predict():
    df = pd.read_csv('files/data.csv')
    train, test = dataSplit(df,0.2)
    # print(train)
    
    X_train = train[['fever','bodyPain','age','diffBreath','runnyNose']].to_numpy()
    X_test = test[['fever','bodyPain','age','diffBreath','runnyNose']].to_numpy()
    
    Y_train = train[['infectionProb']].to_numpy().reshape(4560,)
    Y_test = test[['infectionProb']].to_numpy().reshape(1139,)
    
    clf = LogisticRegression()
    clf.fit(X_train,Y_train)
    
    # infProb = clf.predict_proba([[100,1,22,-1,0]])
    return clf
