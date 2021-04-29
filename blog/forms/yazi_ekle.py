from blog.models import YazilarModel
from django import forms


class YaziEkleForm(forms.ModelForm):
    class Meta:
        model=YazilarModel
        exclude=('yazar','slug')