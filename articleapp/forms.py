from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField
from articleapp.models import Article
from django import forms
from django.forms import ModelForm


class ArticleCreationForm(ModelForm):
    class Meta:
        model = Article
        fields = ['name', 'preview', 'text', 'tag', 'hub', 'image']
        widgets = {
            'text': SummernoteWidget(),
        }

    def __init__(self, *args, **kwargs):
        super(ArticleCreationForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if field_name in ['name', 'preview', 'hub']:
                field.required = True
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['style'] = 'width: 1000px;'