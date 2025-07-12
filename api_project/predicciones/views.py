from django.shortcuts import render
from django.views.generic import TemplateView
from .forms import RFForm
import logging

# Importar librerías necesarias para el manejo de datos y carga del modelo
import numpy as np
import joblib
import pandas as pd

class RFView(TemplateView):
    """
    Vista basada en clase para renderizar y procesar un formulario 
    de predicción con un modelo de regresión lineal.

    Atributos:
    ----------
    template_name : str
        Ruta del template HTML que se utilizará para mostrar el formulario.
    formulario : Form
        Clase del formulario que contiene los campos requeridos para la predicción.
    """

    template_name = 'predicciones/rf_form.html'
    formulario = RFForm

    def get(self, request, *args, **kwargs):
        """
        Método para manejar solicitudes GET y renderizar el formulario vacío.

        Parámetros:
        -----------
        request : HttpRequest
            Objeto de la solicitud HTTP.

        Retorna:
        --------
        HttpResponse : Renderizado del template con el formulario.
        """
        contexto = {
            'formulario': self.formulario(),
            'rf_titulo': 'Formulario para Random Forest Regression'
        }
        return render(request, self.template_name, contexto)

    def post(self, request, *args, **kwargs):
        """
        Método para manejar solicitudes POST, validar el formulario,
        cargar el modelo de regresión y generar una predicción.

        Parámetros:
        -----------
        request : HttpRequest
            Objeto de la solicitud HTTP con los datos del formulario.

        Retorna:
        --------
        HttpResponse : Renderizado del template con el resultado de la predicción.
        """
        # Capturar la información enviada en el formulario
        form = self.formulario(request.POST)
        resultado = None  # Variable para almacenar el resultado de la predicción

        if form.is_valid():
            # Ruta al modelo previamente entrenado
            MODEL_PATH = 'core/modelos/best_model_rl_lss.pkl'

            try:
                # Cargar el modelo usando joblib
                loaded_model = joblib.load(MODEL_PATH)
                logging.info("Modelo cargado éxitosamente")
            except Exception as e:
                # Registrar errores si el modelo no se carga correctamente
                logging.error(f"No se ha podido cargar el modelo de regresión Lineal: \n{e}")

            # Orden de características esperadas por el modelo
            MODEL_FEATURES = [
                "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE",
                "DIS", "RAD", "TAX", "PTRATIO", "B", "LSTAT"
            ]

            # Crear diccionario con los datos procesados del formulario
            data = {feature: form.cleaned_data[feature] for feature in MODEL_FEATURES}

            # Convertir los datos en un DataFrame para la predicción
            input_df = pd.DataFrame([data], columns=MODEL_FEATURES)

            # Generar la predicción usando el modelo
            resultado = loaded_model.predict(input_df)[0]

        # Preparar el contexto para el template incluyendo el resultado
        contexto = {
            'formulario': form,
            'resultado': resultado,
            'rf_titulo': 'Formulario para Regresión Lineal'
        }

        # Renderizar la plantilla con el resultado
        return render(request, self.template_name, contexto)
