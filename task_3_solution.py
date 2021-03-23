from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
import pandas as pd


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

#4
def prepare_data_for_model(x, transformer):
    x_train, y_train = prepare_data(x)
    scaled_x = scale_data(x_train, transformer)
    x_train_scaled = pd.DataFrame(scaled_x, columns=x_train.columns)
    return [x_train_scaled, y_train]

#5
def fit_first_linear_model(x_train, y_train):
    x_train_s = scale_data(x_train, StandardScaler())
    clr = LinearRegression()
    clr.fit(x_train_s, y_train)
    return clr

#6
def fit_first_linear_model_2(x_train, y_train):
    x_train_s = scale_data(x_train, MinMaxScaler())
    clr = LinearRegression()
    clr.fit(x_train_s, y_train)
    return clr

#7
def evaluate_model(linreg, x_pred, y_true):
    y_pred = linreg.predict(x_pred)
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    return [round(mse, 2), round(mae, 2), round(r2, 2)]

#8
def calculate_model_weights(model, features):
    df = pd.DataFrame({
        'features': features,
        'weights': model.coef_
    })
    
    df.sort_values(by=["weights"])

    return df










