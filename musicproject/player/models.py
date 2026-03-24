from django.db import models

# Create your models here.


from django.db import models

class Song(models.Model):
    title = models.CharField(max_length=200)
    audio = models.FileField(upload_to='songs/')
    cover = models.ImageField(upload_to='covers/')

    def __str__(self):
        return self.title