from sklearn.model_selection import train_test_split

def split_data_into_two_samples(X):
    return train_test_split(X, test_size=0.3, random_state=42)