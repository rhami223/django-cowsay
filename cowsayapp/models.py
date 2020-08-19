from django.db import models


# Create your models here.
"""
Description model:

Name (CharField)
Description (TextField)

"""

class History(models.Model):
    textline = models.CharField(max_length=80)
    

    def __str__(self):
        return self.textline
