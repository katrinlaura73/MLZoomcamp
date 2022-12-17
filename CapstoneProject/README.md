# Capstone project ML Zoomcamp 2022: Prediction of death rates in dependency of vaccination rates in Germany
## Description of problem and data
In this project I examined the problem, if you can predict the death rates in Germany given the vaccination rates.

To answer the question I found two datasets on the homepage of the European Centre for Disease Prevention and Control under the link https://www.ecdc.europa.eu/en/covid-19/data.  
You can find the datasat in my github repository also: 
Death dates: 'https://raw.githubusercontent.com/katrinlaura73/MLZoomcamp/main/CapstoneProject/data%20(1).csv
Vaccination data:  (only wegetable because it is to big for github: ) https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/csv/data.csv

All data is © ECDC [2005-2022]

### Description of data about death rates

The description of the data can be seen also under: https://www.ecdc.europa.eu/sites/default/files/documents/Variable_Dictionary_VaccineTracker-7-october-2022.pdf

The data presented in the Vaccine Tracker are submitted by European Union/European Economic Area (EU/EEA) countries to ECDC through The European Surveillance
System (TESSy) once every two weeks on Tuesdays. EU/EEA countries report aggregated data on the number of vaccine doses distributed by manufacturers to the country,
the number of first, second, additional and unspecified doses administered to adults (18+), adolescent and children (<18) overall, by age groups and in specific 
target groups, such as healthcare workers (HCWs) and in residents in longterm care facilities (LTCFs). Doses are also reported by vaccine product. 
The downloadable data files contain the data on the COVID-19 vaccine rollout mentioned above and each row contains the corresponding data for a certain week 
and country. The files are updated once every two weeks on Thursdays. Data are subject to retrospective corrections; corrected datasets are released as soon 
as processing of updated national data has been completed. You may use the data in line with ECDC’s copyright policy.



### Description of project
In the project I first cleaned the data.

Then I tested different classification methods:

Polynomial Regression, but Linear Regression turned out to have better performance.
Random Forest Regressor
Neural Network Regression
I searched the best parameters for the models and compared them. For comparison I used the metric RMSE.

The best model turned out to be a Neural Network.

## Description of files in Github Repository
- Data: ObesityDataSet_raw_and_data_sinthetic.csv

- Jupyter Notebook: notebook.ipynb with
  - Data preparation and data clearning
  - EDA, feature importance analysis
  - Model selection process and parameter tuning

- Script: train.py - in here the final model is build

- scaler.bin: Standard scaler to normalize the data
- model bin: The final model and Dict Vecotrizer are saved by pickle to model.boin

- predict.py. contains
  - Loading the model
  - Serving it via a web service via flask
  - Pipenv and Pipenv.lock: to build a evironment via Pipenv

- Dockerfile: for running the service

  - test_predict.py: to test the dockerfilde

## Description on how to use the model

- Build the docker image: docker build -t test:latest .

- Run the docker image: docker run -it -p 9696:9696 test:latest

- Test the docker impage: python test_predict.py

If you want to test another set of vaccination_rates than given in test_predict use the following structure:

vacc_rates = vacc_rates = {"firstdose_rate": {"0": number},
            "seconddose_rate": {"0": number},
            "doseadditional1_rate": {"0": number},
            "doseadditional2_rate": {"0": number},
            "doseadditional3_rate": {"0": number},
            "alldoses_rate": {"0": number},
            "1_Age60+": {"0": nuber}}

