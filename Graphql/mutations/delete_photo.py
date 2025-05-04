import graphene
from ..schemas.shema_news import NewsShema
from ..queries.queries import Query
from graphql import GraphQLError
from photo.models import Photo

class DeletePhoto(graphene.Mutation):
    success = graphene.Boolean()

    class Arguments:
        fotografia_id = graphene.Int(required=True)

    def mutate(self, info, fotografia_id):
        try:
            photo = Photo.objects.get(pk=fotografia_id)
        except Photo.DoesNotExist:
            return DeletePhoto(success=False)
        photo.delete()
        return DeletePhoto(success=True)