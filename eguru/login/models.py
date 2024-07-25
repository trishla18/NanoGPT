from django.db import models

class Users(models.Model):
    email = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    created_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'users'
