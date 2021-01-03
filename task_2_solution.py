def calculate_data_shape(X):
    return X.shape

def take_columns(X):
    return X.columns

def calculate_target_ratio(X, target_name):
    return round(X[target_name].mean(), 2)

def calculate_data_dtypes(X):
    return X.dtypes[(X.dtypes == 'float64') | (X.dtypes == 'int') | (X.dtypes == 'object')].count()

def calculate_cheap_apartment(X):
    return df[df['price_doc'] <= 1000000]['price_doc'].count()

def calculate_squad_in_cheap_apartment(X):
    return round(df[df['price_doc'] <= 1000000]['full_sq'].mean())

