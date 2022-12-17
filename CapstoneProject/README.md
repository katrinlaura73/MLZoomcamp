# Capstone project ML Zoomcamp 2022: Prediction of death rates in dependency of vaccination rates in Germany
## Description of problem and data
In this project I examined the problem, if you can predict the death rates in Germany given the vaccination rates.

To answer the question I found two datasets on the homepage of the European Centre for Disease Prevention and Control under the link https://www.ecdc.europa.eu/en/covid-19/data.  

You can find the datasat in my github repository also: 
- Death dates: 'https://raw.githubusercontent.com/katrinlaura73/MLZoomcamp/main/CapstoneProject/data%20(1).csv
- Vaccination data:  (only wegetable because it is to big for github: ) https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/csv/data.csv

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

#### Data dictionary

|Variable |Definition|Code|
|:-----|:----:|----:|
|YearWeekISO | Date when the vaccine wasreceived/administered. Only weeks are allowed (e.g. “2021-W01”). | yyyy-Www |
| ReportingCountry | ISO 3166-1-alpha-2 | two-letter code |
| Denominator Population | denominators for target groups (total population and age- specific population obtained from Eurostat/UN).Denominators reported by countries for TargetGroup = “HCW” and TargetGroup = “LTCF”. | Numeric |
| NumberDosesReceived |Number of vaccine doses distributed by the manufacturers to the country during the reporting week.| Numeric|
|NumberDosesExported |Number of vaccine doses donated or sold by the country during the reporting week.| Numeric |
| FirstDose | Number of first dose vaccine administered to individuals during the reporting week. | Numeric |
| FirstDoseRefused | Number of individuals refusing the first vaccine dose. |Numeric |
| SecondDose | Number of second dose vaccine administered to individuals during the reporting week. | Numeric |
|DoseAdditional1| Number of first additional vaccine doses administered after a complete standard primary course to individuals during the reporting week.| Numeric |
| DoseAdditional2 | Number of second additional vaccine doses administered after a complete standard primary course to individuals during the reporting week.| Numeric |
| DoseAdditional3 | Number of third additional vaccine doses administered after a complete standard primary course to individuals during the reporting week.|Numeric|
| DoseUnk | Number of doses administered during the reporting week where the type of dose was not specified (i.e. it is not known whether it was a first or second dose).| Numeric |
| Region| As a minimum data should be reported at national level (Region = country code). |Country/NUTS1 or 2/GAUL1/Country specific |
| TargetGroup | Target group for vaccination. | e. .g. ALL = Overall adults (18+), Age<18 = Overall adolescents and children (0-17 years old), 1_Age<60 = adults below 60 years of age and above 17, 1_Age60+ = adults 60 years and over|
| Vaccine name | Name of vaccine. Additional vaccines will be added on approval or as requested. | e.g AZ = AstraZeneca - for more information see Link above
| Population |  Age-specific population for the country |Numeric|

### Description of vaccination data
The downloadable data file contains information for EU/EEA countries on the 14-day notification
rate of newly reported COVID-19 cases per 100 000 population and the 14-day notification rate of
reported deaths per million population by day and country. Each row contains the corresponding
data for a certain day per country. The file is updated weekly on Thursdays. You may use the data in
line with ECDC’s copyright policy.
For updated data on non-EU/EEA countries please refer to the World Health Organization (WHO)
data on COVID-19 and the WHO Weekly Epidemiological and Weekly Operational Updates page.

#### Source

For EU/EEA countries, data submitted by Member States to The European Surveillance System
(TESSy) are the primary source for weekly COVID-19 data on cases and deaths. If data is unavailable for
a country, it might be supplemented with data published by ministries of health or national public
health institutes (official websites, official twitter accounts or official Facebook accounts) which is
collected on a weekly basis. More information is available at https://www.ecdc.europa.eu/en/covid19/data-collection.

#### Interpretation of COVID-19 data

TThe 14-day notification rate of newly reported COVID-19 cases in EU/EEA countries is based on data
submitted by Member States to The European Surveillance System (TESSy). This is supplemented by
data collected by the ECDC Epidemic Intelligence (EI) team from various sources, and is affected by
local testing strategies, laboratory capacities and the effectiveness of surveillance systems. Comparing
the epidemiological situations regarding COVID-19 between countries should therefore not be based
on these rates alone. However, at the individual country level, this indicator may be useful for
monitoring the national situation over time.
Testing policies and the number of tests performed per 100 000 persons vary markedly across the
EU/EEA and presumably even more so among Third countries. More extensive testing will inevitably
lead to more cases being detected.
The 14-day notification rate of new COVID-19 cases should be used in combination with other factors
including testing policies, number of tests performed, test positivity, excess mortality and rates of
hospital and intensive care unit (ICU) admissions, when analysing the epidemiological situation in a
country. Most of these indicators are presented for EU/EEA Member States in the Country Overview
report. Even when using several indicators in combination, comparisons between countries should be
done with caution and relevant epidemiological expertise.

#### Data dictionary

|Variable  (as of 20200623) |Definition|Code|
|:-----|:----:|----:|
|Country | |String |
|country_code |3-letter ISO country code  | |
|continent| |String |
|population | Eurostat |Numeric |
|indicator |cases / deaths |String |
|weekly_count | |Numeric |
|year_week | |yyyy-Www|
|rate_14_day| 14-day notification rate of reported COVID-19 cases per 100 000 population OR 14-day notification rate of reported deaths per 1 000 000 population|  Numeric |
|cumulativ_count | |Numeric |
|source |The European Surveillance System (TESSy),Alt. Epidemic Intelligence, national weekly data, https://www.ecdc.europa.eu/en/covid-19/data-collection | String|

## Description of project
In the project I first cleaned the data.

Then I tested different classification methods:

Polynomial Regression, but Linear Regression turned out to have better performance.
Random Forest Regressor
Neural Network Regression
I searched the best parameters for the models and compared them. For comparison I used the metric RMSE.

The best model turned out to be a Neural Network.

## Description of files in Github Repository
- Data: 
  -- Death rates: 'data_death.csv'
  -- vaccination rates see under: https://opendata.ecdc.europa.eu/covid19/vaccine_tracker/csv/data.csv (file was to big for github)
  -- prepared data for direct use in train.py: data_death_vacc.csv


- Jupyter Notebook: notebook.ipynb with
  - Data preparation and data clearning
  - EDA, feature importance analysis
  - Model selection process and parameter tuning

- Script: train.py - in here the final model is build

- scaler.bin: Standard scaler to normalize the data - saved by pickle to scaler.bin
- model_death_vacc.h5: The final model saved by tensorflow.save() to model_death_vacc.h5

- predict.py. contains
  - Loading the model and scaler
  - Serving it via a web service via flask
  - Pipenv and Pipenv.lock: to build a evironment via Pipenv

- Dockerfile: for running the service

  - test_predict.py: to test the dockerfile

## Description on how to use the model

- Build the docker image: docker build -t test:latest .

- Run the docker image: docker run -it -p 9696:9696 test:latest

- Test the docker impage: python test_predict.py

If you want to test another set of vaccination_rates than given in test_predict use the following structure:

vacc_rates = {"firstdose_rate": {"0": number},

            "seconddose_rate": {"0": number},
            
            "doseadditional1_rate": {"0": number},
            
            "doseadditional2_rate": {"0": number},
            
            "doseadditional3_rate": {"0": number},
            
            "alldoses_rate": {"0": number},
            
            "1_Age60+": {"0": nuber}}

