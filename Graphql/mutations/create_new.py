import graphene
from ..schemas.shema_news import NewsShema
from ..queries.queries import Query
from graphql import GraphQLError
from news.models import News

class CreateNews(graphene.Mutation):
    news = graphene.Field(NewsShema)

    class Arguments:
        nombre = graphene.String(required=True)
        fecha  = graphene.types.datetime.Date(required=True)
        comentario = graphene.String(required=True)
        investigacion_id = graphene.Int(required=True)

    def mutate(self, info, nombre, fecha, comentario, investigacion_id):


        investigation = Query.resolve_exist_id_investigation(None,None,investigacion_id)


        if not investigation:
            raise GraphQLError(f"Investigación id={investigacion_id} no encontrada")

        nov = News.objects.create(
            nombre=nombre,
            fecha=fecha,
            comentario=comentario,
            investigacion_id=investigacion_id,
        )
        return CreateNews(news=nov)
