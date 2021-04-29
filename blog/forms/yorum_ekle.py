from blog.models import YorumlarModel
from django import forms

class YorumEkleForm(forms.ModelForm):
    class Meta:
        model=YorumlarModel
        fields=('yorum',)