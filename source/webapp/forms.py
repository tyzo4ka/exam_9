from django.forms import forms
from webapp.views import Photography, Comments


class PhotoCommentsForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['text', "comments_author", "created_date"]
