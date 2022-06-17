from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.CharField(max_length=140, blank=False, null=False)
    image = models.FileField(upload_to='post_image', blank=True)

    def __str__(self):
        return self.text #whatever the text string going to be..the obj name also will be same.