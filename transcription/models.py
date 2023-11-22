from django.db import models


class Transcription(models.Model):
    text = models.CharField(max_length=255)

    class Meta:
        db_table = "transcription"
