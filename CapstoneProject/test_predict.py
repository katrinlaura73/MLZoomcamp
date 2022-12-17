import requests

url = "http://localhost:9696/predict"

vacc_rates = {"firstdose_rate": {"0": 5186.565321},
            "seconddose_rate": {"0": 13293.447032},
            "doseadditional1_rate": {"0": 58860.683967},
            "doseadditional2_rate": {"0": 72.647438},
            "doseadditional3_rate": {"0": 15.453063},
            "alldoses_rate": {"0": 77428.796821},
            "1_Age60+": {"0": 12466.233101}}



response = requests.post(url, json=vacc_rates).json()

print(response)
