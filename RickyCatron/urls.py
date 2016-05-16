"""RickyCatron URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static


from RickyCatron import settings
from home import views, admin_views

urlpatterns = [
    url(r'^$', views.index),

    url(r'^blog/$', views.blog, name='blog'),
    url(r'^blog/(?P<item_id>\d+)/$', views.blog_post, name='blog_post'),


    url(r'^portfolio/$', views.portfolio, name='portfolio'),
    url(r'^portfolio/(?P<item_id>\d+)/$', views.portfolio_item, name='portfolio_item'),


    url(r'^contact/$', views.contact, name='contact'),
    url(r'^send_mail/$', views.send_email, name='send_email'),

    url(r'^admin/$', admin_views.admin, name='admin'),
    url('^', include('django.contrib.auth.urls')),

    url(r'^blogChange/add/$', admin_views.add_blog_post, name='add_blog_post'),
    url(r'^blogChange/edit/(?P<item_id>\d+)/$', admin_views.update_blog_post, name='blogedit'),
    url(r'^blogChange/remove/(?P<item_id>\d+)/$', admin_views.remove_blog_post, name='remove_blog_post'),

    url(r'^portfolioChange/add/$', admin_views.add_portfolio_item, name='add_portfolio_item'),
    url(r'^portfolioChange/edit/(?P<item_id>\d+)/$', admin_views.update_portfolio_item,
      name='portfolioedit'),
    url(r'^portfolioChange/remove/(?P<item_id>\d+)/$', admin_views.remove_portfolio_item,
      name='remove_portfolio_item')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
