from django.db import models
from django.utils import timezone

STATUS = ((0, "Incomplete"), (1, "Complete"))
<<<<<<< HEAD
 
class To_Do(models.Model):
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    user_id = user_profile.user_id
    username = user_profile.username
    spoons_required = IntegerField() 
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)
=======
>>>>>>> e9ed442c774747244f216f26bd6654863a2293d1

class UserProfile(models.Model):
    """
    Model to represent extended auth User Class to add additional
    profile information.
    """
    user_id = models.IntegerField(unique=True)  # Changed to models.IntegerField
    username = models.CharField(max_length=30, unique=True)
    max_spoons = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return f"Profile for {self.username}"

class ToDo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Added ForeignKey here
    spoons_required = models.IntegerField()  # Changed to models.IntegerField
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title