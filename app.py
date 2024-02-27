from flask import Flask, render_template, request
import joblib
import os

app = Flask(__name__)

#Load the model
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'model.joblib')
model = joblib.load(model_path)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #Get input from the from
    features = [
        float(request.form['Open']),
        float(request.form['High']),
        float(request.form['Low']),
        float(request.form['Adj Close']),
        float(request.form['Volume'])
    ]
    
    #Make prediction using the model
    prediction = model.predict([features])
    
    # Render the prediction on a new page
    return render_template('result.html', prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)