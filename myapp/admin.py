from django.contrib import admin
from .models import Author, Book

# Admin class for Author model
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name','id')  # Display fields in the list view
    search_fields = ('name',)  # Add a search box for the 'name' field
    list_filter = ('birth_date',)  # Filter authors by birth date

# Admin class for Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')  # Display fields in the list view
    list_filter = ('author', 'published_date')  # Add filter by author and published date
    search_fields = ('title', 'author__name')  # Add a search box for 'title' and 'author name'
    date_hierarchy = 'published_date'  # Date hierarchy for easy navigation by published date
    autocomplete_fields = ['author'] 