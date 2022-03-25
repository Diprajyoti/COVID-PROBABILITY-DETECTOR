import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import pickle

def data_split(data, ratio):
    np.random.seed(42)
    shuffled = np.random.permutation(len(data))
    test_set_size = int(len(data) * ratio)
    test_indices = shuffled[:test_set_size]
    train_indices = shuffled[test_set_size:]
    return data.iloc[train_indices], data.iloc[test_indices]

if __name__=="__main__":
    df=pd.read_csv('data.csv')
    train, test = data_split(df, 0.2)
    X_train = train[
        [ 'bodyorjointpain', 'sorethroat', 'Fever', 'Drycough', 'chestpain', 'Headache', 'Vomitting',
         'diffbreath', 'tastesmellloss', 'Anxity']].to_numpy()
    X_test = test[
        [ 'bodyorjointpain', 'sorethroat', 'Fever', 'Drycough', 'chestpain', 'Headache', 'Vomitting',
         'diffbreath', 'tastesmellloss', 'Anxity']].to_numpy()

    Y_train = train[['Infprob']].to_numpy().reshape(80, )
    Y_test = test[['Infprob']].to_numpy().reshape(19, )

    clf = LogisticRegression()
    clf.fit(X_train, Y_train)

    file= open('connect.pkl','wb')
    pickle.dump(clf,file)
    file.close()



