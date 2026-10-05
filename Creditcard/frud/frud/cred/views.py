from django.shortcuts import render
import joblib
import os
from django.http import JsonResponse
import numpy as np
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'cred', 'models', 'fraud_detection_model.pkl')

model = joblib.load(MODEL_PATH)
# Create your views here.
def home(request):
    return render(request,'home.html') 

def cfrud(request):
    return render(request,'cfrud.html') 



def predict(request):
    if request.method == 'POST':
        data = request.post.getlist('features')

        data = np.array(data, dtype=float).reshape(1, -1)

    prediction = model.predict(data)[0]
    probability = model.predict_proba(data)[0][1]
    return JsonResponse({
    'prediction': int(prediction), 'fraud_probability': float(probability)
    }) 
