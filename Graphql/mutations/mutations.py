import graphene
from .create_new import CreateNews
from .update_new import UpdateNews
from .delete_new import DeleteNews
from .create_photo import CreatePhoto
from .update_photo import UpdatePhoto
from .delete_photo import DeletePhoto


class Mutation(graphene.ObjectType):

   create_new = CreateNews.Field()
   update_new = UpdateNews.Field()
   delete_new = DeleteNews.Field()
   create_photo = CreatePhoto.Field()
   update_photo = UpdatePhoto.Field()
   delete_photo = DeletePhoto.Field()
