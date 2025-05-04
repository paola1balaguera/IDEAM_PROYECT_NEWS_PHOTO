import graphene
from .mutations.mutations import Mutation
from .queries.queries import Query

# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")

schema = graphene.Schema(query=Query, mutation=Mutation)