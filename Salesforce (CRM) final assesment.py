import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN,LSTM,GRU,Dense,Dropout,Conv1D, GlobalAveragePooling1D
from neuralforecast import NeuralForecast
from neuralforecast.models import PatchTST, TimesNet

df=pd.read_csv("Salesforce (CRM) From 2004 To Dec-2024.csv")
print(df.head(5))
print(df.info())
df["Date"]=pd.to_datetime(df["Date"])
df=df.sort_values("Date")
df=df.dropna()
print(df.describe())

plt.figure(figsize=(12,5))
sns.lineplot(data=df,x="Date",y="Close")
plt.title("Salesforce stock closing price")
plt.xlabel("Date")
plt.ylabel("Close")
plt.show()

plt.figure(figsize=(8,6))
sns.heatmap(df[["Open","High","Low","Close","Volume"]].corr(),annot=True,cmap="coolwarm")
plt.title("Relation between Stock Features")
plt.show()

Data=df[["Close"]].values
print(Data.shape)

scaled=MinMaxScaler(feature_range=(0,1))
scaled_data=scaled.fit_transform(Data)
print(scaled_data[:6])

Train_Size=int(len(scaled_data)*0.8)
Train_Data=scaled_data[:Train_Size]
Test_Data=scaled_data[Train_Size:]
print(f"Train Size: {round((len(Train_Data)/len(scaled_data))*100)}%")
print(f"Test Size: {round((len(Test_Data)/len(scaled_data))*100)}%")

def create_sequences(data,Time_steps=60):
 X=[]
 Y=[]
 for i in range(Time_steps,len(data)):
   X.append(scaled_data[i-Time_steps:i])
   Y.append(scaled_data[i,0])
 return np.array(X),np.array(Y)

X_Train,Y_Train=create_sequences(Train_Data,60)
X_Test,Y_Test=create_sequences(Test_Data,60)
print("X_Train:",X_Train.shape)
print("Y_Train",Y_Train.shape)
print("X_Test:",X_Test.shape)
print("Y_Test",Y_Test.shape)

RNN_Model=Sequential([SimpleRNN(50,return_sequences=True,input_shape=(X_Train.shape[1],1)),SimpleRNN(50),Dense(1)])
LSTM_Model=Sequential([LSTM(50,return_sequences=True,input_shape=(X_Train.shape[1],1)),LSTM(50),Dense(1)])
GRU_Model=Sequential([GRU(50,return_sequences=True,input_shape=(X_Train.shape[1],1)),GRU(50), Dense(1)])
PatchTST_Model=Sequential([Conv1D(64,kernel_size=4,activation="relu",input_shape=(X_Train.shape[1], 1)),Conv1D(64,kernel_size=4,activation="relu"),GlobalAveragePooling1D(),Dense(50, activation="relu"),Dense(1)])
TimesNet_Model=Sequential([Conv1D(64,kernel_size=3,padding="same",activation="relu",input_shape=(X_Train.shape[1], 1)), Conv1D(64,kernel_size=5,padding="same",activation="relu"),Conv1D(64,kernel_size=7,padding="same",activation="relu"),GlobalAveragePooling1D(),Dense(50, activation="relu"), Dense(1)])

RNN_Model.compile(optimizer="adam",loss="mean_squared_error")
LSTM_Model.compile(optimizer="adam",loss="mean_squared_error")
GRU_Model.compile(optimizer="adam",loss="mean_squared_error")
PatchTST_Model.compile(optimizer="adam",loss="mean_squared_error")
TimesNet_Model.compile(optimizer="adam",loss="mean_squared_error")

RNN_Model.fit(X_Train,Y_Train,epochs=20,batch_size=32)
LSTM_Model.fit(X_Train,Y_Train,epochs=20,batch_size=32)
GRU_Model.fit(X_Train,Y_Train,epochs=20,batch_size=32)
PatchTST_Model.fit(X_Train,Y_Train,epochs=20,batch_size=32)
TimesNet_Model.fit(X_Train,Y_Train,epochs=20,batch_size=32)

Rnn_predict=RNN_Model.predict(X_Test)
Lstm_predict=LSTM_Model.predict(X_Test)
gru_predict=GRU_Model.predict(X_Test)
patchtst_predict=PatchTST_Model.predict(X_Test)
timesnet_predict=TimesNet_Model.predict(X_Test)


Rnn_predict=scaled.inverse_transform(Rnn_predict)
Lstm_predict=scaled.inverse_transform(Lstm_predict)
gru_predict=scaled.inverse_transform(gru_predict)
patchtst_predict=scaled.inverse_transform(patchtst_predict)
timesnet_predict=scaled.inverse_transform(timesnet_predict)
Y_test_actual=scaled.inverse_transform(Y_Test.reshape(-1,1))

print("RNN")
print("MAE :",mean_absolute_error(Y_test_actual,Rnn_predict))
print("RMSE :",np.sqrt(mean_squared_error(Y_test_actual,Rnn_predict)))
print("R2 :",r2_score(Y_test_actual,Rnn_predict))

print("\nLSTM")
print("MAE :",mean_absolute_error(Y_test_actual,Lstm_predict))
print("RMSE :",np.sqrt(mean_squared_error(Y_test_actual,Lstm_predict)))
print("R2 :",r2_score(Y_test_actual,Lstm_predict))

print("\nGRU")
print("MAE :",mean_absolute_error(Y_test_actual,gru_predict))
print("RMSE :",np.sqrt(mean_squared_error(Y_test_actual,gru_predict)))
print("R2 :",r2_score(Y_test_actual,gru_predict))

print("\nPatchTST")
print("MAE :",mean_absolute_error(Y_test_actual,patchtst_predict))
print("RMSE :",np.sqrt(mean_squared_error(Y_test_actual,patchtst_predict)))
print("R2 :",r2_score(Y_test_actual,patchtst_predict))

print("\nTimesNet")
print("MAE :",mean_absolute_error(Y_test_actual,timesnet_predict))
print("RMSE :",np.sqrt(mean_squared_error(Y_test_actual,timesnet_predict)))
print("R2 :",r2_score(Y_test_actual,timesnet_predict))

plt.figure(figsize=(12,5))
plt.plot(Y_test_actual,label="Actual")
plt.plot(Rnn_predict,label="RNN")
plt.plot(Lstm_predict,label="LSTM")
plt.plot(gru_predict,label="GRU")
plt.plot(patchtst_predict,label="PatchTST")
plt.plot(timesnet_predict,label="TimesNet")

plt.title("Salesforce Actual Price Vs Predicted Price")
plt.xlabel("Days")
plt.ylabel("Closing Price")
plt.legend()
plt.show()

Last_60_Days=scaled_data[-60:]
Input_Data=Last_60_Days.reshape(1,60,1)

Next_RNN=RNN_Model.predict(Input_Data)
Next_LSTM=LSTM_Model.predict(Input_Data)
Next_GRU=GRU_Model.predict(Input_Data)
Next_PatchTST=PatchTST_Model.predict(Input_Data)
Next_TimesNet=TimesNet_Model.predict(Input_Data)

Next_RNN=scaled.inverse_transform(Next_RNN)[0][0]
Next_LSTM=scaled.inverse_transform(Next_LSTM)[0][0]
Next_GRU=scaled.inverse_transform(Next_GRU)[0][0]
Next_PatchTST=scaled.inverse_transform(Next_PatchTST)[0][0]
Next_TimesNet=scaled.inverse_transform(Next_TimesNet)[0][0]

print("RNN Next Price is :",Next_RNN)
print("LSTM Next Price is :",Next_LSTM)
print("GRU Next Price is :",Next_GRU)
print("PatchTST Next Price is :",Next_PatchTST)
print("TimesNet Next Price is :",Next_TimesNet)

Current_Price=df["Close"].iloc[-1]
print("Current Price is :",Current_Price)

Average_prediction=(Next_RNN+Next_LSTM+Next_GRU+Next_PatchTST+Next_TimesNet)/5
print("Average Prediction is :",Average_prediction)

Change=((Average_prediction-Current_Price)/Current_Price)*100
print("Expected Change is :",round(Change,2),"%")


