import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

df = pd.read_csv("climate_dataset.csv")

X = df[['CO2','O2','Temperature']]
y_aqi = df['AQI']

# AQI Category
def categorize(aqi):
    if aqi < 80:
        return 0
    elif aqi < 120:
        return 1
    else:
        return 2

y_cat = df['AQI'].apply(categorize)

linear_model = LinearRegression()
linear_model.fit(X,y_aqi)

logistic_model = LogisticRegression()
logistic_model.fit(X,y_cat)

knn_model = KNeighborsClassifier(n_neighbors=3)
knn_model.fit(X,y_cat)

def predict_all(co2,o2,temp):

    X_input = [[co2,o2,temp]]

    aqi = linear_model.predict(X_input)[0]
    category = logistic_model.predict(X_input)[0]
    knn = knn_model.predict(X_input)[0]

    return aqi,category,knn
