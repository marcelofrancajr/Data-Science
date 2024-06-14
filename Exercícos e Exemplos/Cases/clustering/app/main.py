import pickle
import pandas as pd
from flask import Flask, request

app = Flask(__name__)

with open('models/kmeans.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict_cluster', methods=['POST'])
def index():
    data_json = request.get_json()['data']
    df_input = pd.DataFrame(data_json)
    output = model.predict(df_input).tolist()
    return output

if __name__ == '__main__':
    app.run()