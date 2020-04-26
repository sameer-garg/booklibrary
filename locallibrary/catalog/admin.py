from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance

admin.site.register(Genre)
#admin.site.register(BookInstance)
#admin.site.register(Book)
# admin.site.register(Author)
# Define the admin class
class BooksInline(admin.TabularInline):
    model = Book
    extra = 0
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    inlines = [BooksInline]
    # Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)
# Register the Admin classes for Book using the decorator
class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]
admin.site.register(Book, BookAdmin)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('BookDetails', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
    # Register the admin class with the associated model
admin.site.register(BookInstance, BookInstanceAdmin)


