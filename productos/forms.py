from django import forms

class JuegosFormulario(forms.Form):
    titulo = forms.CharField(max_length=256)
    nombre_autor = forms.CharField(max_length=256)
    apellido_autor = forms.CharField(max_length=256)
    ISBN = forms.IntegerField(required=True)

class HardwareFormulario(forms.Form):
    titulo = forms.CharField(max_length=256)
    nombre_autor = forms.CharField(max_length=256)
    genero = forms.CharField(max_length=256)