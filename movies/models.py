from django.db import models
# Create your models here.
from django.conf import settings

class Genre(models.Model):
    name = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.name}'
        
class Movie(models.Model):
    title = models.CharField(max_length=30)
    audience = models.IntegerField()
    poster_url = models.TextField()
    description = models.TextField()
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    score_users = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Score', related_name='score_movies')

class Score(models.Model):
    content = models.CharField(max_length=140)
    value = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    class Meta: # 메타 정보 : 일관성있는 정보 -> 모든 클래스에는 메타정보를 담을 수 있다.
        ordering = ['-value'] # 원래 pk값 순서로 갖고오나 이렇게 설정하면 value의 내림차순('-')으로 갖고옴
        