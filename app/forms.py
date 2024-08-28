from django import forms

from app.models.yandex_disk import Resource


class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = ['name', 'public_key', 'public_url', 'owner']
