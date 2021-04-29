from blog.models import KategoriModel
from django import template

register=template.Library()

@register.simple_tag
def kategori_list():
    kategoriler=KategoriModel.objects.all()
    return kategoriler