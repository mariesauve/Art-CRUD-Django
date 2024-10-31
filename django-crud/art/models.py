from django.db import models


class Art(models.Model):
    name = models.CharField(max_length=50)
    value = models.IntegerField(choices=[(i, str(i)) for i in range(1, 7)])

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-value']

        
