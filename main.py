""" Importing the Dependencies """

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json



app = FastAPI()


origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)


""" Base Model for the Input """

class model_input (BaseModel):
    Pregnancies: int
    Glucose: int
    BloodPressure: int
    SkinThickness: int
    Insulin: int
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int


""" Loading the Model """

diabetes_model = pickle.load(open('diabetes.sav', 'rb'))


@app.post('/predict')

def diabetes_pred(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)


    Pregnancies = input_dictionary['Pregnancies']
    Glucose = input_dictionary['Glucose']
    BloodPressure = input_dictionary['BloodPressure']
    SkinThickness = input_dictionary['SkinThickness']
    Insulin = input_dictionary['Insulin']
    BMI = input_dictionary['BMI']
    DiabetesPedigreeFunction = input_dictionary['DiabetesPedigreeFunction']
    Age = input_dictionary['Age']

    input_list = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 1:
        return {"Prediction": "Diabetic"}
    
    else:
        return {"Prediction": "Not Diabetic"}