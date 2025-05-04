import graphene
from ..schemas.shema_news import NewsShema
from ..queries.queries import Query
from graphql import GraphQLError
from news.models import News

class DeleteNews(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        novedad_id = graphene.Int(required=True)

    def mutate(self, info, novedad_id):
        try:
            nov = News.objects.get(pk=novedad_id)
        except News.DoesNotExist:
            return DeleteNews(success=False)
        nov.delete()
        return DeleteNews(success=True)