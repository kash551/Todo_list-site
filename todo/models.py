from django.db import models
from django.utils import timezone

STATUS = ((0, "Incomplete"), (1, "Complete"))

class UserProfile(models.Model):
    """
    Model to represent extended auth User Class to add additional
    profile information.
    """
    user_id = models.IntegerField(unique=True)  # Changed to models.IntegerField
    username = models.CharField(max_length=30, unique=True)
    max_spoons = models.PositiveIntegerField(blank=True, default=12)  # Changed to models.PositiveIntegerField

    def __str__(self):
        return f"Profile for {self.username}"

class Todo(models.Model):
    title = models.CharField(max_length=100, unique=True)
    details = models.TextField()
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)  # Added ForeignKey here
    spoons_required = models.IntegerField()  # Changed to models.IntegerField
    date = models.DateTimeField(default=timezone.now)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return self.title