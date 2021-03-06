from django.db.models import CharField, TextField, Model
from django.db.models.fields import URLField

from stdimage import StdImageField


class PortfolioItem(Model):
    main_image_url = StdImageField(blank=True,
                                   variations={'xl': (1200, 1200), 'large': (800, 800), 'medium': (500, 500)})
    title = CharField(max_length=100)
    url = URLField()
    description = TextField()
    examples1 = StdImageField(blank=True, variations={'xl': (1200, 1200), 'medium': (500, 500)})
    examples2 = StdImageField(blank=True, variations={'xl': (1200, 1200), 'medium': (500, 500)})
    examples3 = StdImageField(blank=True, variations={'xl': (1200, 1200), 'medium': (500, 500)})

    def __unicode__(self):
        return u'{0}'.format(self.title)
