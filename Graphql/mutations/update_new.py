import graphene
from ..schemas.shema_news import NewsShema
from ..queries.queries import Query
from graphql import GraphQLError
from news.models import News

class UpdateNews(graphene.Mutation):
    news = graphene.Field(NewsShema)

    class Arguments:
        novedad_id = graphene.Int(required=True)
        nombre = graphene.String()
        fecha = graphene.types.datetime.Date()
        comentario = graphene.String()
        investigacion_id = graphene.Int()

    def mutate(self, info, novedad_id, nombre=None, fecha=None, comentario=None, investigacion_id=None):
        try:
            nov = News.objects.get(pk=novedad_id)



        except News.DoesNotExist:
            raise GraphQLError(f"Novedad con id={novedad_id} no encontrada")

        if nombre is not None:
            nov.nombre = nombre
        if fecha is not None:
            nov.fecha = fecha
        if comentario is not None:
            nov.comentario = comentario
        if investigacion_id is not None:

            if not Query.resolve_exist_id_investigation(None,None, investigacion_id):
                raise GraphQLError(f"Investigación id={investigacion_id} no encontrada")
            nov.investigacion_id = investigacion_id

        nov.save()
        return UpdateNews(news=nov)