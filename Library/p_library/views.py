from django.contrib import auth
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse_lazy
from django.views import generic

from .models import Book, Author, Publisher, Friend, CustomUser
from .forms import BookForm, AuthorForm, PublisherForm, ReaderForm, ProfileCreationForm
from allauth.socialaccount.models import SocialAccount


class BookListView(generic.ListView):
    model = Book
    template_name = 'p_library/books.html'
    context_object_name = 'books'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            context['username'] =  self.request.user.username
        return context



class BookView(generic.DetailView):
    model = Book
    template_name = 'p_library/book.html'
    context_object_name = 'book'


class BookUpdate(generic.UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'p_library/update_form.html'


class BookCreate(generic.CreateView):
    model = Book
    form_class = BookForm
    template_name = 'p_library/update_form.html'


class BookDelete(generic.DeleteView):
    model = Book
    template_name = 'p_library/book_delete.html'
    success_url = reverse_lazy('p_library:books')


class AuthorsView(generic.ListView):
    model = Author
    template_name = 'p_library/authors.html'
    context_object_name = 'authors'


class AuthorView(generic.DetailView):
    model = Author
    template_name = 'p_library/author.html'
    context_object_name = 'author'


class AuthorCreate(generic.CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'p_library/update_form.html'


class AuthorUpdate(generic.UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'p_library/update_form.html'


class AuthorDelete(generic.DeleteView):
    model = Author
    template_name = 'p_library/author_delete.html'
    success_url = reverse_lazy('p_library:authors')


class PublisherCreate(generic.CreateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'p_library/update_form.html'


class PublishersView(generic.ListView):
    model = Publisher
    template_name = 'p_library/publishers.html'
    context_object_name = 'publishers'


class PublisherView(generic.DetailView):
    model = Publisher
    template_name = 'p_library/publisher.html'
    context_object_name = 'publisher'


class PublisherUpdate(generic.UpdateView):
    model = Publisher
    form_class = PublisherForm
    template_name = 'p_library/update_form.html'


class PublisherDelete(generic.DeleteView):
    model = Publisher
    template_name = 'p_library/publisher_delete.html'
    success_url = reverse_lazy('p_library:publishers')


class ReaderCreate(generic.CreateView):
    model = Friend
    form_class = ReaderForm
    template_name = 'p_library/update_form.html'


class ReadersView(generic.ListView):
    model = Friend
    template_name = 'p_library/readers.html'
    context_object_name = 'readers'


class ReaderView(generic.DetailView):
    model = Friend
    template_name = 'p_library/reader.html'
    context_object_name = 'reader'


class ReaderUpdate(generic.UpdateView):
    model = Friend
    template_name = 'p_library/update_form.html'
    form_class = ReaderForm


class ReaderDelete(generic.DeleteView):
    model = Friend
    template_name = 'p_library/reader_delete.html'
    success_url = reverse_lazy('p_library:readers')


class RegisterUserView(generic.FormView):
    form_class = UserCreationForm
    template_name = 'p_library/register.html'
    success_url = reverse_lazy('p_library:create-profile')

    def form_valid(self, form):
        form.save()
        username=form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        auth.login(self.request, authenticate(username=username, password=raw_password))
        return super(RegisterUserView, self).form_valid(form)


class CreateUserProfileView(generic.FormView):
    form_class = ProfileCreationForm
    template_name = 'p_library/register.html'
    success_url = reverse_lazy('p_library:books')

    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        return super(CreateUserProfileView, self).form_valid(form)

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_anonymous:
            return HttpResponseRedirect('login')
        return super(CreateUserProfileView, self).dispatch(request, *args, **kwargs)
