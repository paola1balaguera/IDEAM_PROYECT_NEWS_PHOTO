import graphene
from django.db import connections



class Query(graphene.ObjectType):


    # -----------------------------------------

    exist_id_investigation = graphene.Int()

    
    
    def resolve_exist_id_investigation(root, info, id):
        with connections['secondary'].cursor() as cursor:
            cursor.execute("SELECT 1 FROM investigacion WHERE investigacion_id = %s LIMIT 1", [id])
            return cursor.fetchone() is not None
