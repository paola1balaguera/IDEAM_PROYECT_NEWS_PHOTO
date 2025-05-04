import graphene
from graphene_django import DjangoObjectType
from news.models import News

class NewsShema(DjangoObjectType):


    class Meta:
        model = News
