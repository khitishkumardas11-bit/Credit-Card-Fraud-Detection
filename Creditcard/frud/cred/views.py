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
    return render(request, 'home.html')


def cfrud(request):
    return render(request, 'cfrud.html')


def login(request):
    return render(request, 'login.html')


def predict(request):
    if request.method == 'POST':
        values = request.POST.getlist('features')

        if not values:
            values = []
            for index in range(1, 11):
                value = request.POST.get(f'f{index}')
                if value is not None:
                    values.append(value)

        if not values:
            return JsonResponse({'error': 'No feature values provided.'}, status=400)

        expected_features = getattr(model, 'n_features_in_', 30)
        if len(values) < expected_features:
            values = values + ['0'] * (expected_features - len(values))
        elif len(values) > expected_features:
            values = values[:expected_features]

        data = np.array(values, dtype=float).reshape(1, -1)
        prediction = model.predict(data)[0]
        probability = model.predict_proba(data)[0][1]
        return JsonResponse({
            'prediction': int(prediction),
            'fraud_probability': float(probability),
        })
    return JsonResponse({'error': 'Only POST requests are supported.'}, status=405)


def logout(request):
    return render(request, 'logout.html')
