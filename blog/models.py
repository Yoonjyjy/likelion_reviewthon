from django.db import models
from django.utils import timezone

# Create your models here.

class Post(models.Model) :
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    restaurant_name = models.CharField(max_length = 200)
    text = models.TextField()
    created_date = models.DateTimeField(default = timezone.now)
    published_date = models.DateTimeField(blank = True, null = True)

    def publish(self) :
        self.published_date = timezone.now()
        self.save()

    def __str__(self) :
        return self.restaurant_name

class Comment(models.Model) :
    STAR_SCORE = (
        ('1', '★'),
        ('2', '★★'),
        ('3', '★★★'),
        ('4', '★★★★'),
        ('5', '★★★★★'),
    )
    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    nickname = models.CharField(max_length = 200)
    #score = models.IntegerField(default = 5)
    score = models.CharField(max_length = 5, choices = STAR_SCORE)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(str) :
        return self.text