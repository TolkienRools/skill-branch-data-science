import numpy as np

#1
def calculate_data_shape(X):
    return X.shape

#2
def take_columns(X):
    return X.columns

#3
def calculate_target_ratio(X, target_name):
    return round(X[target_name].mean(), 2)

#4
def calculate_data_dtypes(X):
    return [X.dtypes[(X.dtypes == 'float64') | (X.dtypes == 'int64')].count(),  X.dtypes[X.dtypes == 'object'].count()]

#5
def calculate_cheap_apartment(X):
    return X[X['price_doc'] <= 1000000]['price_doc'].count()

#6
def calculate_squad_in_cheap_apartment(X):
    return round(X[X['price_doc'] <= 1000000]['full_sq'].mean())

#7 -- 
def calculate_mean_price_in_new_housing(X):
    return int(X[(X['num_room'] == 3) & (X['build_year'] <= 2010)]['price_doc'].mean())


#8
def calculate_mean_squared_by_num_rooms(X):
    return X.groupby(['num_room'])['full_sq'].mean().round(2)

#9 -- 
def calculate_squared_stats_by_material(X):
    return X.groupby('material')['full_sq'].aggregate([np.amax, np.amin]).round(2)

#10 -- 
def calculate_crosstab(X):
    return X.pivot_table('price_doc', index=('sub_area'), columns=['product_type'], fill_value=0).round(2)

