from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load the model
loaded_model = joblib.load("../models/lightgbm_model.pkl")

# Render the main page
@app.route('/')
def index():
    return render_template('index.html')

# Handle the form submission
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get the form data
        no_of_beds = float(request.form['no_of_beds'])
        no_of_baths = float(request.form['no_of_baths'])
        area = float(request.form['area'])

        # Create a DataFrame with the new data
        new_data = pd.DataFrame({
            'No. Beds': [no_of_beds],
            'No. Baths': [no_of_baths],
            'Area': [area],
            'Type_n': [0],  # Assuming Type_n is a categorical feature
            'Region_n': [3],  # Assuming Region_n is a categorical feature
            'Sub-region_n': [432]  # Assuming Sub-region_n is a categorical feature
        })

        # Make predictions using the loaded model
        predictions = loaded_model.predict(new_data)

        # Display the result on the prediction page
        return render_template('prediction.html', prediction=predictions[0])

if __name__ == '__main__':
    app.run(debug=True)
