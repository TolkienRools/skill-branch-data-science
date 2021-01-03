def calculate_data_shape(X):
    return X.shape

def take_columns(X):
    return X.columns

def calculate_target_ratio(X, target_name):
    return round(X[target_name].mean(), 2)