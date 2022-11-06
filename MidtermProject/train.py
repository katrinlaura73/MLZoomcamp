# Import modules

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import roc_auc_score

import pickle

# Data Preparation
file = 'https://raw.githubusercontent.com/katrinlaura73/MLZoomcamp/main/MidtermProject/ObesityDataSet_raw_and_data_sinthetic.csv'

df = pd.read_csv(file)

# Rename and format columns to understand the meaning
df = df.rename(columns={"FAVC": "consumption_high_caloric_food",
    "FCVC": "consumption_vegetables",
    "NCP": "number_meals",
    "CAEC": "consumption_between_meals",
    "CH2O": "consumption_water",
    "CALC": "consumption_alcohol",
    "SCC": "calories_consumption_monitoring",
    "FAF": "physical_activity",
    "TUE": "time_techn_devices",
    "MTRANS": "transportation_used"})

# Format columns
df.columns = df.columns.str.lower()
for col in ['gender', 'family_history_with_overweight', 'consumption_high_caloric_food', 'consumption_between_meals', 'smoke', 'calories_consumption_monitoring', 'consumption_alcohol']:
     # make entries all to lower
    df[col] = df[col].str.lower()

# Delete all values from age higher as 50 years
df.drop(df[df['age']>50].index, inplace = True)
df = df.reset_index(drop=True)

# Replace "Always" with "Frequently" in column consumption_alcohol
df['consumption_alcohol'].replace('always', 'frequently', inplace=True)

# Replace "Bike" and 'Walking" with "Walking or Bike" in column transportation_used
df['transportation_used'].replace({'bike': 'walk_or_bike', 'walking': 'walk_or_bike', 'automobile': 'automotive', 'motorbike': 'automotive'}, inplace=True)

# Change values of target_variable nobeyesdad to numbers
df['nobeyesdad'] = df['nobeyesdad'].map({'Obesity_Type_I': 4,
                    'Obesity_Type_III': 6,
                    'Obesity_Type_II' : 5,
                    'Overweight_Level_I': 2,
                    'Normal_Weight': 1,
                    'Overweight_Level_II': 3,
                    'Insufficient_Weight':  0}).astype(int)

# Delete weight and height as features
del df['height']
del df['weight']

# Split Dataset
df_train, df_test = train_test_split(df, test_size = 0.2, random_state = 1)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

# define target
y_train = (df_train['nobeyesdad']).values
y_test = (df_test['nobeyesdad']).values

del df_train['nobeyesdad']
del df_test['nobeyesdad']

# Transform training data
train_dicts = df_train.to_dict(orient='records')
dv = DictVectorizer(sparse = False)
X_train = dv.fit_transform(train_dicts)

# Transform test data
test_dicts = df_test.to_dict(orient='records')
X_test = dv.transform(test_dicts)

# Random Forest

print('Training Random Forest model')

model = RandomForestClassifier(n_estimators=140,
                                max_depth=15,
                                min_samples_leaf=1,
                                random_state=1)
model.fit(X_train, y_train)

# make predicition
y_pred = model.predict_proba(X_test)

# Calculate Score
auc = roc_auc_score(y_test, y_pred, multi_class='ovr')

print(f'auc={auc}')

# Save the model
output_file = 'model.bin'

with open(output_file, 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f'The model is saved to {output_file}')

