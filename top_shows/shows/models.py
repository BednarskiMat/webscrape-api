from django.db import models


class Show(models.Model):
    external_id = models.IntegerField(null=False)
    title = models.CharField(max_length = 100)
    desc = models.TextField(null=True)
    rating = models.CharField(max_length = 10)

    def __str___(self):
        return self.title
