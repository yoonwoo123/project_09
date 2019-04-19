from django.contrib import admin
from .models import Genre, Movie, Score
# Register your models here.
class GenreAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name']

admin.site.register(Genre, GenreAdmin)

class MovieAdmin(admin.ModelAdmin):
    list_display = ['pk', 'title', 'audience', 'poster_url', 'description', 'genre']

admin.site.register(Movie, MovieAdmin)

class ScoreAdmin(admin.ModelAdmin):
    list_display = ['content', 'value']

admin.site.register(Score, ScoreAdmin)