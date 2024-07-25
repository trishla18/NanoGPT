from django.db import models

class CourseMaterial(models.Model):
    topic_id = models.CharField(max_length=256)
    file_location = models.TextField()

    class Meta:
        managed = False
        db_table = 'course_material'


class Faculty(models.Model):
    name = models.CharField(max_length=256)
    email = models.CharField(max_length=256)
    designation = models.CharField(max_length=256)
    about = models.TextField()
    topic_id = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'faculty'