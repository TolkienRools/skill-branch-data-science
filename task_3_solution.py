from sklearn.model_selection import train_test_split

#1
def split_data_into_two_samples(x):
    x_train, x_test = train_test_split(x, test_size=0.3, random_state=42)
    return [x_train, x_test]
#2
def prepare_data(x):
    target_vector = x['price_doc']
    objects = x.select_dtypes(include=['object']).columns
    filtered = x.drop(columns=objects).drop(columns=["id"]).drop(columns=['price_doc']).dropna(axis=1)
    return [filtered, target_vector]

#3
def scale_data(x, transformer):
    return transformer.fit_transform(x)








