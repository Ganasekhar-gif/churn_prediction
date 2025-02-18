from flask import Flask, render_template, request
import joblib
import numpy as np

app = Flask(__name__, template_folder="template")

# Load the trained model
model = joblib.load("churn_model.joblib")

@app.route('/')
def home():
    return render_template('web.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Print form data to debug
        print("Received Form Data:", request.form)  # <-- Debugging Step

        # Get input values from form
        features = [
            request.form.get('SeniorCitizen', type=float),
            request.form.get('Partner', type=float),
            request.form.get('Dependents', type=float),
            request.form.get('tenure', type=float),
            request.form.get('PaperlessBilling', type=float),
            request.form.get('MonthlyCharges', type=float),
            request.form.get('TotalCharges', type=float),
            request.form.get('FiberOptic', type=float),
            request.form.get('NoService', type=float),
            request.form.get('Tenure_MonthlyCharges', type=float),
            request.form.get('AvgChargesPerMonth', type=float),
            request.form.get('Contract_Duration', type=float)
        ]

        # Print features list to debug
        print("Extracted Features:", features)  # <-- Debugging Step

        # Check if all features are received
        if None in features:
            return render_template('web.html', prediction="Error: Missing input fields")

        # Convert to numpy array
        input_array = np.array([features]).reshape(1, -1)

        # Predict churn
        prediction = model.predict(input_array)[0]
        result = "Churn" if prediction == 1 else "No Churn"

        return render_template('web.html', prediction=result)

    except Exception as e:
        print("Error:", str(e))  # <-- Debugging Step
        return render_template('web.html', prediction=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
