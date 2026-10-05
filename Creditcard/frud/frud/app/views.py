from django.shortcuts import render

# Create your views here.
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODEL_PATH = os.path.join(BASE_DIR, 'app', 'models', 'fraud_detection_model.pkl')

model = joblib.load(MODEL_PATH)
# from django.http import JsonResponse
# import numpy as np

# def predict_view(request):
#     if request.method == 'POST':
#         data = request.POST.getlist('features')  
#         data = np.array(data, dtype=float).reshape(1, -1)

#         prediction = model.predict(data)[0]
#         probability = model.predict_proba(data)[0][1]

#         return JsonResponse({
#             'prediction': int(prediction),
#             'fraud_probability': float(probability)
#         })


from django.apps import apps
import numpy as np
from django.http import JsonResponse

def predict_view(request):
    model = apps.get_app_config('app').model

    data = request.POST.getlist('features')
    data = np.array(data, dtype=float).reshape(1, -1)

    pred = model.predict(data)[0]
    prob = model.predict_proba(data)[0][1]

    return JsonResponse({
        'prediction': int(pred),
        'fraud_probability': float(prob)
    })

# sklearn==1.3

# from tensorflow.keras.models import load_model
# model = load_model('model.h5')

# python manage.py shell

# from myapp.views import model
# model.predict([[1000, 0.5, 3]])

features = [2500, 1, 0.75, 3, 120]
import requests

url = "http://127.0.0.1:8000/predict/"
data = {
    'features': [2500, 1, 0.75, 3, 120]
}
r = requests.post(url, data=data)
print(r.json())

features: 2500
features: 1
features: 0.75
features: 3
features: 120

{
  "prediction": 1,
  "fraud_probability": 0.87
}

model.n_features_in_
print(model.n_features_in_)

