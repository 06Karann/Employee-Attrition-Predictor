from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Updated model load
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        
        age = float(request.form['Age'])
        monthly_income = float(request.form['MonthlyIncome'])
        distance = float(request.form['DistanceFromHome'])
        overtime = int(request.form['Overtime']) # 1 for Yes, 0 for No
        marital_status = request.form['MaritalStatus'] # 'Single', 'Married', or 'Divorced'
        
        # One-hot encoding mapping 
        marital_single = 1 if marital_status == 'Single' else 0
        marital_married = 1 if marital_status == 'Married' else 0
        
        # Features array
        features = np.array([[age, monthly_income, distance, overtime, marital_single, marital_married]])
        
        # Prediction
        prediction = model.predict(features)
        result = "High Risk: Employee might leave!" if prediction[0] == 1 else "Low Risk: Employee will likely stay."
        
        return render_template('index.html', prediction_text=result)
    except Exception as e:
        return render_template('index.html', prediction_text=f"Error: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)
