from django import forms
from django.forms import fields
from .models import DefaultModel, CrispyModel,TweakModel
import datetime


class DefaultModelForm(forms.ModelForm):
    class Meta:
        model = DefaultModel
        fields = '__all__'

class CrispyModelForm(forms.ModelForm):
    dob = forms.DateField(
        label = "Enter Your Date Of Birth",
        widget=forms.SelectDateWidget(years=range(1980, datetime.date.today().year-5))    
    )

    def __init__(self, *args, **kwargs):
        super(CrispyModelForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class':'form-control my-2',
            })

    class Meta:
        model = CrispyModel
        fields = ("__all__")

class TweakModelForm(forms.ModelForm):
    class Meta:
        model = TweakModel 
        fields = '__all__'