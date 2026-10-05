from django.apps import AppConfig
import joblib
import os

class CredConfig(AppConfig):
    name = 'cred'
    def ready(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(BASE_DIR, 'cred', 'models', 'fraud_detection_model.pkl')
        self.model = joblib.load(model_path)