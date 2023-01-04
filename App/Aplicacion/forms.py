from django import forms

class EntradaForm(forms.Form):
    file = forms.FileField()
    #textarea = forms.CharField(widget=forms.Textarea(attrs={"rows":20, "cols":60}))

class EntradaFecha(forms.Form):
    fecha = forms.CharField(label = "fname")

