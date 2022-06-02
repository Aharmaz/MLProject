
from flask import Flask,request,jsonify
import string
import pandas as pd
import pyarabic.araby as araby
from pyarabic.araby import is_arabicrange
from farasa.stemmer import FarasaStemmer
import itertools
import random
#model = pickle.load(open('model.pkl','rb'))

app = Flask(__name__)









#@app.route('/predict',methods=['POST'])
@app.route('/')
def index():
    a="hello "
    b="world!"
    return "lah yn3l xitan"
#     return "Hello world"
@app.route('/predict',methods=['POST'])
#@app.route('/')
def predict():
    data=pd.read_json("arabicPresidentJson.json")
    # cgpa = request.form.get('cgpa')
    # iq = request.form.get('iq')
    # profile_score = request.form.get('profile_score')
    # input_query = np.array([[cgpa,iq,profile_score]])
    # result = model.predict(input_query)[0]
    # return jsonify({'placement':str(result)})
    return data.shape





if __name__ == '__main__':
    app.run(debug=True)
