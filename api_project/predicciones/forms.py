from django import forms


# Crear el formulario necesario para la predicción:

class RFForm(forms.Form):
    CRIM = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    ZN = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    INDUS = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    CHAS = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    NOX = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    RM = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    AGE = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    DIS = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    RAD = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    TAX = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    PTRATIO = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    B = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))
    LSTAT = forms.FloatField(required = True,widget=forms.NumberInput(attrs={'class':'form-control'}))