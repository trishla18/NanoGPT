from django.db import models

class ChatHistory(models.Model):
    user_id = models.CharField(max_length=256)
    topic_id = models.CharField(max_length=256)
    chat_id = models.IntegerField()
    question = models.TextField()
    response = models.TextField()

    class Meta:
        managed = False
        db_table = 'chat_history'