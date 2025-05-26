from django.forms import ModelForm, CharField, TextInput, ModelChoiceField
from .models import Tag, Quote, Author


class TagForm(ModelForm):

    name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())

    class Meta:
        model = Tag
        fields = ['name']


class QuoteForm(ModelForm):

    name = CharField(min_length=5, max_length=50, required=True, widget=TextInput())
    author = ModelChoiceField(queryset=Author.objects.all(), required=True)

    class Meta:
        model = Quote
        fields = ['name', 'author']
        exclude = ['tags']


class AuthorForm(ModelForm):

    full_name = CharField(min_length=3, max_length=25, required=True, widget=TextInput())
    description = CharField(required=True, widget=TextInput())

    class Meta:
        model = Author
        fields = ['full_name', 'description']