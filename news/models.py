from django.db import models

# Create your models here.

class News(models.Model):

    TIPO_CHOICES = [
        ('climatica', 'Climática'),
        ('tecnica', 'Técnica'),
        ('logistica', 'Logística'),
        ('personal', 'Personal'),
        ('ambiental', 'Ambiental'),
        ('administrativa', 'Administrativa')
    ]

    novedad_id = models.AutoField(primary_key=True, db_column='novedad_id')
    nombre = models.CharField(null=False, max_length=255)
    fecha = models.DateField( null=False)
    comentario = models.CharField(null=False, max_length=255)
    investigacion_id = models.IntegerField( null=False)
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    class Meta:
        managed = False  
        db_table = 'novedad'

