from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RFForm
import logging

# Importar las librerias de prediccion:
import numpy as np
import joblib
import pandas as pd

# Create your views here.
class RFView(TemplateView):
    template_name = 'predicciones/rf_form.html'
    formulario = RFForm
    contexto = {
        'formulario': formulario,
        'rf_titulo' : 'Formulario para Random Forest Regression'
        }

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.contexto)
    
    def post(self, request, *args, **kwargs):
        form = self.formulario(request.POST) # Capturamos toda la data del formulario
        resultado = None

        if form.is_valid():
            # cargar el modelo
            MODEL_PATH = 'core/modelos/best_model_rl_lss.pkl'

            try:
                loaded_model = joblib.load(MODEL_PATH)
                logging.info("Modelo cargado éxitosamente")
            except Exception as e:
                logging.error(f"No se ha podido cargar el modelo de regresión Lineal: \n{e}")

            MODEL_FEATURES = [
                "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
            ]

            # preparamos los datos
            data = {
                'CRIM': form.cleaned_data['CRIM'],
                'ZN': form.cleaned_data['ZN'],
                'INDUS': form.cleaned_data['INDUS'],
                'CHAS': form.cleaned_data['CHAS'],
                'NOX': form.cleaned_data['NOX'],
                'RM': form.cleaned_data['RM'],
                'AGE': form.cleaned_data['AGE'],
                'DIS': form.cleaned_data['DIS'],
                'RAD': form.cleaned_data['RAD'],
                'TAX': form.cleaned_data['TAX'],
                'PTRATIO': form.cleaned_data['PTRATIO'],
                'B': form.cleaned_data['B'],
                'LSTAT': form.cleaned_data['LSTAT'],
            }

            # Realizar la predicción:
            input_df = pd.DataFrame([data], columns=MODEL_FEATURES)
            resultado = loaded_model.predict(input_df)[0]

        contexto = {
            'formulario': form,
            'resultado': resultado,
            'rf_titulo': 'Formulario para Regresión Lineal'
        }

        return render(request, self.template_name, contexto)
