from django import forms
from cantine.models.menu_model import MenuModel
from cantine.models.dishe_model import DishesModel

class MenuForm(forms.ModelForm):
    class Meta:
        model = MenuModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
        }
    dishe = forms.ModelChoiceField(queryset=DishesModel.objects.all(), empty_label="Choisir un plat", widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super(MenuForm, self).__init__(*args, **kwargs)
        self.fields['plat'].queryset = DishesModel.objects.all()