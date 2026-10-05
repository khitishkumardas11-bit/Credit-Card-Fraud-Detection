from django.apps import AppConfig
import joblib
import os


class AppConfig(AppConfig):
    name = 'app'

class MyappConfig(AppConfig):
    name = 'app'

    def ready(self):
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        model_path = os.path.join(BASE_DIR, 'app', 'models', 'fraud_detection_model.pkl')
        self.model = joblib.load(model_path)