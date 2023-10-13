from flask import Flask,request,render_template,app,Response
import pickle
import numpy as np 
import pandas as pd


application = Flask(__name__)
app= application

scaler=pickle.load(open('/config/workspace/Model/standardScalar.pkl','rb'))
model=pickle.load(open("/config/workspace/Model/modelForPrediction.pkl","rb"))

#route for index page

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/predictdata",methods=['GET','POST'])
def predict_datapoint():
    result=""

    if request.method=='POST':

        Pregnancies = int(request.form.get("Pregnancies"))
        Glucose = float(request.form.get("Glucose"))
        BloodPressure = float(request.form.get("BloodPressure"))
        SkinThickness = float(request.form.get("SkinThickness"))
        Insulin = float(request.form.get("Insulin"))
        BMI = float(request.form.get("BMI"))
        DiabetesPedigreeFunction = float(request.form.get("DiabetesPedigreeFunction"))
        Age = float(request.form.get("Age"))


        new_data=scaler.transform([[DiabetesPedigreeFunction,BMI,Insulin,SkinThickness,BloodPressure,Pregnancies,Glucose,Age]])
        predict=model.predict(new_data)

        if predict[0]==1:
            result="Diabetic"
        else:
            result="Non_Diabetic"
        
        return render_template("single_prediction.html",result=result)

    else:
        return render_template("home.html")




if __name__=="__main__":
    app.run(host="0.0.0.0")