import graphene
from django.db import connections
from news.models import News
from photo.models import Photo
from ..schemas.shema_news import NewsShema
from ..schemas.schema_photo import PhotoShema
from django.db.models import Count
from graphene.types.generic import GenericScalar
from django.db.models.functions import TruncDate


class Query(graphene.ObjectType):


    # -----------------------------------------

    # exist_id_investigation = graphene.Int()
    all_news = graphene.List(NewsShema)
    all_photos = graphene.List(PhotoShema)
    news_for_id_investigation = GenericScalar(id_investigation=graphene.Int(required=True))
    calculate_active_days = graphene.Field(NewsShema,id_investigation=graphene.Int(required=True))



    
    
    # def resolve_exist_id_investigation(root, info, id):
    #     with connections['secondary'].cursor() as cursor:
    #         cursor.execute("SELECT 1 FROM investigacion WHERE investigacion_id = %s LIMIT 1", [id])
    #         return cursor.fetchone() is not None

    def resolve_all_news(root,info):

        return News.objects.all()
    
    def resolve_all_photos(root, info):

        return Photo.objects.all()
    
    def resolve_news_for_id_investigation(root, info, id_investigation):

        novedades = News.objects.filter(investigacion_id=id_investigation)

        # (1,) 
        #flat quita la tupla y permanece una lista plana 
        ids_novedades = list(novedades.values_list('novedad_id', flat=True))
        
        fotos = Photo.objects.filter(novedad_id__in=ids_novedades)

        novedades_con_foto_ids = (
            fotos.values_list('novedad_id', flat=True).distinct()
        )
        novedades_con_foto_ids = set(novedades_con_foto_ids)
        con_foto = len(novedades_con_foto_ids)

        total = len(ids_novedades)
        porcentaje = (con_foto / total) * 100 if total > 0 else 0

        


        return {
            "total_novedades": total,
            "con_foto": con_foto,
            "porcentaje": porcentaje
        }


    def resolve_calculate_active_days(root, info, id_investigation):
        
        # Obtener las fechas únicas en que se registraron novedades para una investigación
        queryset = News.objects.filter(investigacion_id=id_investigation)

        # Truncar la fecha (quitar la hora) y seleccionar solo las fechas distintas
        fechas_unicas = queryset.annotate(
            fecha_sin_hora=TruncDate('fecha')
        ).values_list('fecha_sin_hora', flat=True).distinct()

        # Convertir las fechas a string formato ISO (YYYY-MM-DD)
        fechas_formateadas = [fecha.isoformat() for fecha in fechas_unicas]

        return fechas_formateadas