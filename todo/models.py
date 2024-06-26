from django.db import models
from django.utils import timezone
 
 STATUS = ((0, "Incomplete"), (1, "Complete"))
 
class To_do(models.Model):
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    user_id = user_profile.user_id
    username = user_profile.username
    spoons_required = IntegerField() 
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

 
    def __str__(self):
        return self.title

class user_profile(models.Model):
    user_id = IntegerField()
    username = models.CharField(max_length=30, unique=True)
    max_spoons = IntegerField()