from django.db import models
from django.contrib.auth import get_user_model
from computer.models import Computer
User = get_user_model()

class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings', on_delete=models.CASCADE)
    computer = models.ForeignKey(Computer, related_name='ratings', on_delete=models.CASCADE)
    value = models.IntegerField(choices=[(1,1), (2,2), (3,3), (4,4), (5,5)])