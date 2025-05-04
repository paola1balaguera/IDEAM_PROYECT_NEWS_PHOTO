import graphene
from graphene_django import DjangoObjectType
from photo.models import Photo

class PhotoShema(DjangoObjectType):


    class Meta:
        model = Photo