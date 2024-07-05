import pandas_datareader as pdr
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, LSTM

# Data Collection
key = "835f62051ab4b6531a3c468624176f1b6f43b77c"

try:
    # Fetch data from Tiingo
    df = pdr.get_data_tiingo('AAPL', api_key=key, start='2017-01-01', end='2022-01-01')

    # Ensure data is in DataFrame format
    if isinstance(df, pd.DataFrame):
        # Data Preprocessing
        df1 = df.reset_index()['close']
        scaler = MinMaxScaler(feature_range=(0, 1))
        df1 = scaler.fit_transform(np.array(df1).reshape(-1, 1))

        # Prepare Data for LSTM
        def create_dataset(dataset, time_step=1):
            dataX, dataY = [], []
            for i in range(len(dataset)-time_step-1):
                a = dataset[i:(i+time_step), 0]
                dataX.append(a)
                dataY.append(dataset[i + time_step, 0])
            return np.array(dataX), np.array(dataY)

        time_step = 100
        X_train, y_train = create_dataset(df1, time_step)
        X_train = X_train.reshape(X_train.shape[0], X_train.shape[1], 1)

        # Build LSTM Model
        model = Sequential()
        model.add(LSTM(50, return_sequences=True, input_shape=(100, 1)))
        model.add(LSTM(50, return_sequences=True))
        model.add(LSTM(50))
        model.add(Dense(1))
        model.compile(loss='mean_squared_error', optimizer='adam')

        # Train LSTM Model
        model.fit(X_train, y_train, epochs=100, batch_size=64, verbose=1)

        # Generate Predictions
        x_input = df1[-100:].reshape(1, -1)
        temp_input = list(x_input[0])
        lst_output = []
        i = 0
        while i < 30:
            if len(temp_input) > 100:
                x_input = np.array(temp_input[1:])
                x_input = x_input.reshape(1, -1, 1)
                yhat = model.predict(x_input, verbose=0)
                temp_input.extend(yhat[0].tolist())
                temp_input = temp_input[1:]
                lst_output.extend(yhat.tolist())
                i += 1
            else:
                x_input = x_input.reshape(1, -1, 1)
                yhat = model.predict(x_input, verbose=0)
                temp_input.extend(yhat[0].tolist())
                lst_output.extend(yhat.tolist())
                i += 1

        # Print Predictions
        print("Predicted Stock Prices:")
        print(lst_output)
    else:
        print("Error: Data not retrieved in DataFrame format")

except Exception as e:
    print("An error occurred during data retrieval:", e)
