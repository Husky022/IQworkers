from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from articleapp.models import Article

# Register your models here.


class ArticleAdmin(SummernoteModelAdmin):
    summernote_fields = ('text',)


admin.site.register(Article, ArticleAdmin)
