from django.contrib import admin
from .models import Article
from .models import Articles
from .models import Generic_new
# Register your models here.
admin.site.register(Article)
admin.site.register(Articles)
admin.site.register(Generic_new)
