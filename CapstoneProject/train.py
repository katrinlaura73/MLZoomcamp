import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error

import tensorflow as tf
from keras.layers import Input, Dense
from keras.models import Model

import pickle

# Load data
# Because the original data must be transformed in many steps,
# I use the prepared and saved data

file = 'data_death_vacc.csv'
df = pd.read_csv(file)

# split dataset
df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# define target
y_train = (df_train['rate_14_day']).values
y_test = (df_test['rate_14_day']).values

del df_train['rate_14_day']
del df_test['rate_14_day']

# define features
features = ['firstdose_rate', 'seconddose_rate', 'doseadditional1_rate', 'doseadditional2_rate',
            'doseadditional3_rate', 'alldoses_rate', '1_Age60+']

# transform training data
scaler = StandardScaler()
scaler.fit(df_train[features])

X_train_scaled = scaler.transform(df_train[features])

# transform test data
X_test_scaled = scaler.transform(df_test[features])

# Build Neural Network

# Define Neural Network
model = tf.keras.Sequential(name="deaths_vacc")

# Define Input Layer
model.add(Dense(32, input_shape=(7,), activation='relu', name='input'))

# Define Hidden Layer
model.add(Dense(64, activation='relu', name='hidden1'))
model.add(Dense(64, activation='relu', name='hidden2'))

# Define Output Layer
model.add(Dense(1, name='output'))

# Compile model
model.compile(optimizer='rmsprop', loss='mse', metrics=['mse'])

# Train model
print('Training Neural Network to predict death rates')

model.fit(X_train_scaled, y_train, batch_size=512, epochs=500)

# Make prediciton
y_pred = model.predict(X_test_scaled)

# Calcluate sscore
rmse = round(np.sqrt(mean_squared_error(y_test, y_pred)), 3)
print(f'RMSE={rmse}')

# Save the scaler
# Save the model
output_file = 'scaler.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((scaler), f_out)

print(f'scaler is saved to {output_file}')

# Save the model
path = 'model_death_vacc.h5'
model.save(path)
print(f'model is saved to {path}')