from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Room(models.Model):
    photo = models.ImageField(blank=True, upload_to='static/img/')
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    
    def __str__(self):
        return self.name
    


class Message(models.Model):
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    content  = models.TextField()
    date_add = models.DateTimeField(auto_now_add=True)



    class Meta:
        ordering = ('date_add',)