from django.db import models

class Blog(models.Model): 
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    update_date = models.DateTimeField()
    body = models.TextField()
    image = models.FileField(upload_to="spblog_images/", blank=True)
