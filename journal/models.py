from django.db import models

# Create your models here.
class Entry(models.Model):
    game_title = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)
    entry_subject = models.CharField(max_length=100)
    entry = models.TextField()
    
    def __str__(self):
        return self.game_title


