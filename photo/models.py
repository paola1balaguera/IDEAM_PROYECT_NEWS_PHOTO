from django.db import models
from news.models import News

# Create your models here.

class Photo(models.Model):
    fotografia_id = models.AutoField(primary_key=True, db_column='fotografia_id')
    url_fotografia = models.CharField(null=False, max_length=800)
    coordenadas_geograficas = models.CharField(null=False, max_length=255)
    novedad = models.ForeignKey(News, db_column='novedad_id', on_delete=models.CASCADE)

    class Meta:
        db_table = 'fotografia'