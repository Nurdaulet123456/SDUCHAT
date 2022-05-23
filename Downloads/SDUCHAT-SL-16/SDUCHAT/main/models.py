from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class People(models.Model):
    username = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)



    def __str__(self):
        return self.username + ' ' + self.lastname



class Message(models.Model):
    to_user = models.CharField(max_length=200, verbose_name='to User', null=True)
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    subject = models.CharField(max_length=200, verbose_name='Subject', null=True)
    message = models.TextField(max_length=500, default="", verbose_name="Message")
    date = models.DateTimeField(default=datetime.today())

    def __str__(self):
        return self.message

    def get_date(self):
        time = datetime.today()
        if self.date.day == time.day:
            if self.date.hour + 1 == time.hour or self.date.hour == time.hour:
                return str(abs(time.minute - self.date.minute)) + " minutes ago"
            return str(time.hour - self.date.hour) + " hours ago"
        else:
            if self.date.month == time.month:
                return str(time.day - self.date.day) + " days ago"
            else:
                if self.date.year == time.year:
                    return str(time.month - self.date.month) + " months ago"
        return self.date


class ChatModel(models.Model):
    sender = models.CharField(max_length=100, default=None)
    message = models.TextField(null=True, blank=True)
    thread_name = models.CharField(null=True, blank=True, max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.message
    

    
class Starred(models.Model):
    user = models.ManyToManyField(User)
    star = models.IntegerField()