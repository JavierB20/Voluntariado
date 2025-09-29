from django.db import models

class Task(models.Model):
    title = models.CharField('Título', max_length=200)
    done = models.BooleanField('Completada', default=False)
    created_at = models.DateTimeField('Creada', auto_now_add=True)
    
    def __str__(self):
        return self.title
