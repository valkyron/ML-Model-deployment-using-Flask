import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler
# from flask_restful import Api, Resource
import joblib

app = Flask(__name__)
model = joblib.load("knn.joblib")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/visualize')
def visualize():
    return render_template('visualize.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''

    if request.method == "POST":
        projectpath = request.form
        print("pinku")
        print(projectpath)
        
        list = []
        for i in projectpath:
            list.append(float(projectpath[i]))

        result = model.predict([list])
        print(result[0])

    #return render_template('predict.html')
    return render_template('predict.html', prediction_text='Species found: {}'.format(result[0]))

if __name__ == "__main__":
    app.run(debug=True)