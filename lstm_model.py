import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

data = np.array([50,60,70,80,90,100,110,120])

X=[]
y=[]

for i in range(len(data)-3):
    X.append(data[i:i+3])
    y.append(data[i+3])

X=np.array(X)
y=np.array(y)

X=X.reshape((X.shape[0],X.shape[1],1))

model=Sequential()
model.add(LSTM(50,input_shape=(3,1)))
model.add(Dense(1))

model.compile(loss='mse',optimizer='adam')
model.fit(X,y,epochs=50,verbose=0)

def predict_lstm():
    last=np.array([100,110,120])
    last=last.reshape((1,3,1))
    pred=model.predict(last)
    return float(pred[0][0])
