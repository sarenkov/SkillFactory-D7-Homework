from django.contrib import admin
from .models import Book, Author, Friend, Publisher, CustomUser

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Friend)
admin.site.register(Publisher)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass
