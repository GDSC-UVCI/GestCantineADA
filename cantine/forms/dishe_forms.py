from django import forms
from cantine.models.dishe_model import DishesModel

class DishesForm(forms.ModelForm):
    class Meta:
        model = DishesModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'menu': forms.Select(attrs={'class': 'form-control'}),
        }