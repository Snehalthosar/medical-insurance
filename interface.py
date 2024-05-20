from flask import Flask, request, jsonify, render_template
from utils import  MedicalInsurence
import config

app = Flask(__name__)

@app.route('/medical_insurance')
def home1():

    return render_template('medical_insurence.html')


@app.route("/predict_charges", methods = ['GET', 'POST'])
def predicted_charges():

    if request.method == 'GET':
        data = request.args.get
        print("Data: ", data)
        age      = int(data('age'))
        gender   = data('gender')
        bmi      = int(data('bmi'))
        children = int(data('children'))
        smoker   = data('smoker')
        region   = data('region')

        obj = MedicalInsurence(age,gender,bmi,children,smoker,region)
        pred_price = obj.get_predicted_price()
    
        return render_template('medical_insurence.html', prediction = pred_price)

    elif request.method == 'POST':
         data = request.form
         print("Data: ", data)
         age      = data['age']
         gender   = data['gender']
         bmi      = data['bmi']
         children = data['children']
         smoker   = data['smoker']
         region   = data['region']

         obj = MedicalInsurence(age,gender,bmi,children,smoker,region)
         pred_price = obj.get_predicted_price()


         return render_template('medical_insurence.html', prediction = pred_price)

    return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = config.PORT_NUMBER)