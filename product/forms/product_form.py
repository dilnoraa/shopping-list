from django import forms
from ..models import Product
from django.core.exceptions import ValidationError
from PIL import Image

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "description", "category", "image")
        exclude = ("created_at", "id")

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)
