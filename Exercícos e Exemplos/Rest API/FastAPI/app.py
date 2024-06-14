import pickle
import uvicorn
import pandas as pd
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

# Inicia API
app = FastAPI()

# Carrega modelo
with open('models/model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Cria página inicial
@app.get('/')
def home():
    return 'Welcome to the Medical Insurance Prediction App!'

# Classifica custo (consumo do modelo)
@app.get('/predict')
def predict(age: int, bmi: float, children: int, smoker: str='no'):
    df_input = pd.DataFrame([dict(age=age, bmi=bmi, children=children, smoker=smoker)])
    output = model.predict(df_input)[0]
    return output

class Customer(BaseModel):
    age: int
    bmi: float
    children: int
    smoker: str
    class Config:
        schema_extra = {
            'example': {
                'age': 20,
                'bmi': 30.4,
                'children': 1,
                'smoker': 'no'
            }
        }

@app.post('/predict_with_json')
def predict(data: Customer):
    df_input = pd.DataFrame([data.dict()])
    output = model.predict(df_input)[0]
    return output

class CustomerList(BaseModel):
    data: List[Customer]

@app.post('/mult_predict_with_json')
def predict(data: CustomerList):
    df_input = pd.DataFrame(data.dict()['data'])
    output = model.predict(df_input).tolist()
    return output

# Executa API
if __name__ == '__main__':
    uvicorn.run(app)
