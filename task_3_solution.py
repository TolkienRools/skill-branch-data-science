from sklearn.model_selection import train_test_split

#1
def split_data_into_two_samples(X):
    return train_test_split(X, test_size=0.3, random_state=42)

#2
def prepare_data(x):
    key_feature = x['price_doc']

    objects = x.select_dtypes(include=['object']).columns

    filter_x = x.drop(column=['id']).drop(column=['price_doc']).dropna(axis=1)
    
    return [filter_x, key_feature]

#3
def scale_data(x, transformer):
    return transformer.fit_transform(X)







