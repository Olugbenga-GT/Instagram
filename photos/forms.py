from django import forms
from photos.models import Photo


class PhotoForm(forms.ModelForm):
    class Mets:
        model = Photo
        fields = "__all__"
