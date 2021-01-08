from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

#1
def split_data_into_two_samples(X):
    return train_test_split(X, test_size=0.3, random_state=42)

#2
def prepare_data(X):
    X.drop(X.dtypes[X.dtypes == 'object'].index, axis=1, inplace=True)
    X.drop(['id'], axis=1, inplace=True)
    X.dropna(axis=1, inplace=True)
    key_feature = X.pop('price_doc')
    return X, key_feature

#3
def scale_data(X, transformer):
    scaler = transformer()
    return scaler.fit_transform(X)




