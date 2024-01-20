from django.shortcuts import render
from django.http import HttpResponse
import joblib
import pandas as pd

# Load the model
loaded_model = joblib.load("../models/lightgbm_model.pkl")

def index(request):
    return render(request, 'predictor/index.html')

def predict(request):
    if request.method == 'POST':
        # Get the form data
        no_of_beds = float(request.POST['no_of_beds'])
        no_of_baths = float(request.POST['no_of_baths'])
        area = float(request.POST['area'])

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
        return render(request, 'predictor/prediction.html', {'prediction': predictions[0]})
    else:
        return HttpResponse("Invalid request")

