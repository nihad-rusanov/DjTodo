from django.db import models
from django.contrib.auth.models import User

TODO_STATUS = (('ACTIVE','ACTIVE'),('COMPLETED','COMPLETED'))

# Create your models here.
class Todo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name='todos')
    content = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content