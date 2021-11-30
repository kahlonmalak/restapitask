from django.contrib import admin
from .models import Article
from .models import Articles
# Register your models here.
admin.site.register(Article)
admin.site.register(Articles)