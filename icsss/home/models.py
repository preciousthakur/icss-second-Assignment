from django.db import models


class Details(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.EmailField()
    inquiry = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

