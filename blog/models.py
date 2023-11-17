from django.db import models
from django.contrib.auth.models import User
class Topic(models.Model):
    name=models.CharField(max_length=200)
    date_added=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(blank=True)
    owner=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return(
            f"{self.owner}"
            f"{self.name[:30]}..."
        )
class Entry(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.TextField()
    date_added=models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name_plural='entries'
    def __str__(self):
        return f"{self.name[:50]}..."  

# Create your models here.
