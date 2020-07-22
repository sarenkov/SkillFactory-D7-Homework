from django.urls import path
from . import views

app_name = 'p_library'
urlpatterns = [
    path('', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>', views.BookView.as_view(), name='book'),
    path('book/<int:pk>/edit', views.BookUpdate.as_view(), name='book_edit'),
    path('book/create', views.BookCreate.as_view(), name='book_create'),
    path('book/<int:pk>/delete', views.BookDelete.as_view(), name='book_delete'),
    path('author/create', views.AuthorCreate.as_view(), name='author_create'),
    path('authors', views.AuthorsView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorView.as_view(), name='author'),
    path('author/<int:pk>/edit', views.AuthorUpdate.as_view(), name='author_edit'),
    path('author/<int:pk>/delete', views.AuthorDelete.as_view(), name='author_delete'),
    path('publisher/create', views.PublisherCreate.as_view(), name='publisher_create'),
    path('publishers', views.PublishersView.as_view(), name='publishers'),
    path('publisher/<int:pk>', views.PublisherView.as_view(), name='publisher'),
    path('publisher/<int:pk>/edit', views.PublisherUpdate.as_view(), name='publisher_edit'),
    path('publisher/<int:pk>/delete', views.PublisherDelete.as_view(), name='publisher_delete'),
    path('reader/create', views.ReaderCreate.as_view(), name='reader_create'),
    path('readers', views.ReadersView.as_view(), name='readers'),
    path('reader/<int:pk>', views.ReaderView.as_view(), name='reader'),
    path('reader/<int:pk>/edit', views.ReaderUpdate.as_view(), name='reader_edit'),
    path('reader/<int:pk>/delete', views.ReaderDelete.as_view(), name='reader_delete'),
    path('login/', views.LoginView.as_view(
        template_name = 'p_library/login.html',
    ), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('register/', views.RegisterUserView.as_view(), name='register'),
    path('create-profile', views.CreateUserProfileView.as_view(), name='create-profile'),
]
