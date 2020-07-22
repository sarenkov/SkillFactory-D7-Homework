from allauth.socialaccount.models import SocialAccount
from django import forms
from django.forms import CharField, Textarea

from .models import Book, Author, Publisher, Friend, CustomUser


class BookForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput)
    description = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Author
        fields = '__all__'


class PublisherForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    city = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Publisher
        fields = '__all__'


class ReaderForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.TextInput)

    class Meta:
        model = Friend
        fields = '__all__'


class ProfileCreationForm(forms.ModelForm):
    
    class Meta:
        model = SocialAccount
        fields = ['extra_data']

