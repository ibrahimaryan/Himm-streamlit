# import all the app dependencies
import pandas as pd
import numpy as np
import sklearn
import streamlit as st
import joblib
import matplotlib
from IPython import get_ipython
from PIL import Image

# load the encoder and model object
model = joblib.load("rta_model_deploy3.joblib")
encoder = joblib.load("ordinal_encoder2.joblib")

st.set_option('deprecation.showPyplotGlobalUse', False)

# 1: serious injury, 2: Slight injury, 0: Fatal Injury

st.set_page_config(page_title="Accident Severity Prediction App",
        page_icon="🚧", layout="wide")

#creating option list for dropdown menu
options_day = ['Sunday', "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
options_age = ['18-30', '31-50', 'Over 51', 'Unknown', 'Under 18']

# number of vehicle involved: range of 1 to 7
# number of casualties: range of 1 to 8
# hour of the day: range of 0 to 23

options_types_collision = ['Vehicle with vehicle collision','Collision with roadside objects',
              'Collision with pedestrians','Rollover','Collision with animals',
              'Unknown','Collision with roadside-parked vehicles','Fall from vehicles',
              'Other','With Train']

options_sex = ['Male','Female','Unknown']

options_education_level = ['Junior high school','Elementary school','High school',
              'Unknown','Above high school','Writing & reading','Illiterate']

options_services_year = ['Unknown','2-5yrs','Above 10yr','5-10yrs','1-2yr','Below 1yr']

options_acc_area = ['Other', 'Office areas', 'Residential areas', ' Church areas',
    ' Industrial areas', 'School areas', ' Recreational areas',
    ' Outside rural areas', ' Hospital areas', ' Market areas',
    'Rural village areas', 'Unknown', 'Rural village areasOffice areas',
    'Recreational areas']

# features list
features = ['Number_of_vehicles_involved','Number_of_casualties','Hour_of_Day','Type_of_collision','Age_band_of_driver','Sex_of_driver',
    'Educational_level','Service_year_of_vehicle','Day_of_week','Area_accident_occured']

a,b,c = st.columns([0.2,0.6,0.2])
with b:
 st.image("banner-picture.jpeg", use_column_width=True)


# description about the project and code files       
st.subheader("🧾Description:")
st.text("""This data set is collected from Addis Ababa Sub-city police departments for master's research work. 
The data set has been prepared from manual records of road traffic accidents of the year 2017-20. 
All the sensitive information has been excluded during data encoding and finally it has 32 features and 12316 instances of the accident.
Then it is preprocessed and for identification of major causes of the accident by analyzing it using different machine learning classification algorithms.
""")

st.markdown("Source of the dataset: [Click Here](https://www.narcis.nl/dataset/RecordID/oai%3Aeasy.dans.knaw.nl%3Aeasy-dataset%3A191591)")

st.subheader("🧭 Problem Statement:")
st.text("""The target feature is Accident_severity which is a multi-class variable. 
The task is to classify this variable based on the other 31 features step-by-step by going through each day's task. 
The metric for evaluation will be f1-score
""")

st.markdown("Please find GitHub repository link of project: [Click Here](https://github.com/avikumart/Road-Traffic-Severity-Classification-Project)")          
  
# run the main function        
if __name__ == '__main__':
  main()