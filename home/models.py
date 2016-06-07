from django.db.models import CharField, TextField, Model

from stdimage import StdImageField


class PortfolioItem(Model):
    main_image_url = StdImageField(blank=True, variations={'large': (800, 800), 'medium': (500, 500)})
    title = CharField(max_length=100)
    description = TextField()
    examples1 = StdImageField(blank=True, variations={'large': (500, 500)})
    examples2 = StdImageField(blank=True, variations={'large': (500, 500)})
    examples3 = StdImageField(blank=True, variations={'large': (500, 500)})


class BlogPost(Model):
    title = CharField(max_length=100)
    post = TextField()
