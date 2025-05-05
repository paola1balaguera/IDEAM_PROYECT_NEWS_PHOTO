import graphene
from django.db import connections
from news.models import News
from photo.models import Photo
# from ...news.models import News
# from ...photo.models import Photo
from ..schemas.shema_news import NewsShema
from ..schemas.schema_photo import PhotoShema



class Query(graphene.ObjectType):


    # -----------------------------------------

    exist_id_investigation = graphene.Int()
    all_news = graphene.List(NewsShema)
    all_photos = graphene.List(PhotoShema)


    
    
    def resolve_exist_id_investigation(root, info, id):
        with connections['secondary'].cursor() as cursor:
            cursor.execute("SELECT 1 FROM investigacion WHERE investigacion_id = %s LIMIT 1", [id])
            return cursor.fetchone() is not None

    def resolve_all_news(root,info):

        return News.objects.all()
    
    def resolve_all_photos(root, info):

        return Photo.objects.all()