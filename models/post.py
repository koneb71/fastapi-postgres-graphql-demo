from db import Model
from orator.orm import has_many


class Post(Model):
    @has_many
    def comments(self):
        from .comment import Comments

        return Comments
