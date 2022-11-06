import requests

url = "http://localhost:9696/predict"

individual = {'gender': 'male',
                'family_history_with_overweight': 'yes',
                'consumption_high_caloric_food': 'yes',
                'consumption_between_meals': 'sometimes',
                'smoke': 'no',
                'calories_consumption_monitoring': 'no',
                'consumption_alcohol': 'sometimes',
                'transportation_used': 'automotive',
                'age': 33.182127,
                'consumption_vegetables': 2.0,
                'number_meals': 1.977221,
                'consumption_water': 3.0,
                'physical_activity': 1.0,
                'time_techn_devices': 0.0}

response = requests.post(url, json=individual).json()

print(response)
