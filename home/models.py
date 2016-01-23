from django.db.models import CharField, TextField, Model, ImageField


class PortfolioItem(Model):
    main_image_url = ImageField()
    title = CharField(max_length=100)
    description = TextField()
    examples1 = ImageField(default=None)
    examples2 = ImageField(default=None)
    examples3 = ImageField(default=None)


class BlogPost(Model):
    main_image_url = ImageField()
    title = CharField(max_length=100)
    post = TextField()
