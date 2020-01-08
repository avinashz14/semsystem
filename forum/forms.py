from django import forms
from forum.models import Bang

class Rev(forms.ModelForm):
	class Meta:
		model = Bang
		fields =(
			'name',
			'category',
			'location',
			'title',
			'rating',
			'review',
		)

class Edi(forms.ModelForm):
	class Meta:
		model = Bang
		fields =(
			'name',
			'category',
			'location',
			'title',
			'rating',
			'review',
		)