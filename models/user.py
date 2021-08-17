from db import Model
from orator.orm import has_many


class User(Model):
    @has_many
    def posts(self):
        from .post import Post

        return Post

    @has_many
    def comments(self):
        from .comment import Comments

        return Comments
