from django.db import models
##어떤 데이터를 처리할지 class 선언

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title
    
    def summary(self):
        return self.body[:100]
# Create your models here.
