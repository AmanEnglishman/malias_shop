from django import forms
from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating',)
        widgets = {
            'rating': forms.RadioSelect(choices=[(i, f'{i}*' for i in range(6))]),
        }
