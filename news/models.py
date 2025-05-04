from django.db import models

# Create your models here.

class News(models.Model):

    novedad_id = models.AutoField(primary_key=True, db_column='novedad_id')
    nombre = models.CharField(null=False, max_length=255)
    fecha = models.DateField( null=False)
    comentario = models.CharField(null=False, max_length=255)
    investigacion_id = models.IntegerField( null=False)

    class Meta:
        managed = False  
        db_table = 'novedad'

