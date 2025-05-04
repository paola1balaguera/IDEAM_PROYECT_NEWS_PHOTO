from django.db import models

# Create your models here.

class Photo(models.Model):

    fotografia_id = models.AutoField(primary_key=True, db_column='fotografia_id')
    url_fotografia = models.CharField(null=False, max_length=800)
    coordenadas_geograficas = models.CharField(null=False, max_length=255)
    novedad_id = models.IntegerField( null=False)

    class Meta:
        managed = False  
        db_table = 'fotografia'