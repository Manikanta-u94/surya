from .models import data
from django import forms



class dataForm(forms.ModelForm):

	class Meta:
		model = data


		fields = ('title','description')


