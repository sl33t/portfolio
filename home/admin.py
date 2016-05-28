from django.contrib import admin
from home.models import PortfolioItem, BlogPost

admin_model = [PortfolioItem, BlogPost]

for item in admin_model:
    admin.site.register(item)
