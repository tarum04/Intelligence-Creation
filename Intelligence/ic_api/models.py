from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class ReceivedData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    data = models.JSONField()
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'id']

    def __str__(self):
        return f"Data from {self.user.username} at {self.timestamp}"