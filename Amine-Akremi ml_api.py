

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

class model_input(BaseModel):
    
    wconfid : float	
    pctid :	float

       
        
# loading the saved model
ML_prediction_model = pickle.load(open('TP4_model.sav', 'rb'))

@app.post('/ML_prediction')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    pctid = input_dictionary['pctid']
    wconfid = input_dictionary['wconfid']
	
    
    
    input_list = [pctid, wconfid]
    
    prediction = ML_prediction_model.predict([input_list])
    
    
    
    



