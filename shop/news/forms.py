from .models import Articles
from django. forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
     class Meta:
         model = Articles
         fields = ['title', 'anons', 'full_text', 'date']

         widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Articles name'
            }),
             'anons': TextInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'Articles anons'
             }),
             'date': DateTimeInput(attrs={
                 'class': 'form-control',
                 'placeholder': 'date of publication'
             }),
             'full_text': Textarea(attrs={
                 'class': 'form-control',
                 'placeholder': 'Articles text'
             })
         }