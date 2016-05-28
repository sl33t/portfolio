from django.contrib import admin
from .models import *

admin_model = [PortfolioItem, BlogPost]

for item in admin_model:
    admin.site.register(item)