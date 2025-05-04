import graphene
from ..schemas.schema_photo import PhotoShema
from ..queries.queries import Query
from graphql import GraphQLError
from photo.models import Photo
from news.models import News

class UpdatePhoto(graphene.Mutation):
    photo = graphene.Field(PhotoShema)

    class Arguments:
        fotografia_id = graphene.Int(required=True)
        url_fotografia = graphene.String()
        coordenadas_geograficas = graphene.String()
        novedad_id = graphene.Int()

    def mutate(self, info,
               fotografia_id,
               url_fotografia=None,
               coordenadas_geograficas=None,
               novedad_id=None):

        try:
            photo = Photo.objects.get(pk=fotografia_id)
        except Photo.DoesNotExist:
            raise GraphQLError(f"Photo con id={fotografia_id} no encontrada")

        if url_fotografia is not None:
            photo.url_fotografia = url_fotografia
        if coordenadas_geograficas is not None:
            photo.coordenadas_geograficas = coordenadas_geograficas
        if novedad_id is not None:
            # validar existencia de la novedad
            if not News.objects.filter(pk=novedad_id).exists():
                raise GraphQLError(f"Novedad id={novedad_id} no encontrada")
            photo.novedad_id = novedad_id

        # 3) Guardar cambios
        photo.save()
        return UpdatePhoto(photo=photo)