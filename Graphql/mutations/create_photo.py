import graphene
from ..schemas.shema_news import NewsShema
from ..queries.queries import Query
from graphql import GraphQLError
from photo.models import Photo
from ..schemas.schema_photo import PhotoShema



class CreatePhoto(graphene.Mutation):
    photo = graphene.Field(PhotoShema)

    class Arguments:
        url_fotografia = graphene.String(required=True)
        coordenadas_geograficas = graphene.String(required=True)
        novedad_id = graphene.Int(required=True)

    def mutate(self, info, url_fotografia, coordenadas_geograficas, novedad_id):

        if not Photo.objects.filter(pk=novedad_id).exists():
            raise GraphQLError(f"Novedad id={novedad_id} no encontrada")

        photo = Photo.objects.create(
            url_fotografia=url_fotografia,
            coordenadas_geograficas=coordenadas_geograficas,
            novedad_id=novedad_id
        )
        return CreatePhoto(photo=photo)

