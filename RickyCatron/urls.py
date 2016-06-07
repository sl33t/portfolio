from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin

from RickyCatron import settings
from home import views

urlpatterns = [
                  url(r'^$', views.index, name="index"),

    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<item_id>\d+)/$', views.blog_post, name='blog_post'),


    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^portfolio/(?P<item_id>\d+)/$',
        views.portfolio_item, name='portfolio_item'),


    url(r'^contact/$', views.contact, name='contact'),
    url(r'^send_mail/$', views.send_email, name='send_email'),

    url(r'^admin/', admin.site.urls),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT
           ) + static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT
                      )
