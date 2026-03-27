from django.contrib import admin

from .models import Author, Book, BookInstance, Genre, Language


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fieldsets = (
        ('General Information', {
            'fields': ('first_name', 'last_name'),
        }),
        ('Dates', {
            'fields': (('date_of_birth', 'date_of_death'),),
        }),
    )


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'due_back')
    list_filter = ('book', 'status', 'due_back')


admin.site.register(Genre)
admin.site.register(Language)
