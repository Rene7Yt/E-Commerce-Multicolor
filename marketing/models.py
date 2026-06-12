from django.db import models

class Faq(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.TextField()
    activa = models.BooleanField(default=True)

    class Meta:
        
        db_table = 'marketing_faq'
        
    def __str__(self):
        return self.pregunta