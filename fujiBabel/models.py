from django.db import models

# Create your models here.

class Bibliotheque(models.Model):
    mangas_id = models.IntegerField()
    notified = models.BooleanField(default=True)
    add_date = models.DateTimeField(auto_now_add=True)

class ChapitreLu(models.Model):
    mangas_id = models.ForeignKey(Bibliotheque, on_delete=models.CASCADE)
    chapter_id = models.IntegerField()
    date_read = models.DateTimeField(auto_now_add=True)
