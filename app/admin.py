from django.contrib import admin
from .models import Chapter
from .models import Content


# Register your models here.
class ChapterAdmin(admin.ModelAdmin):
    list_display = ['chapter_name']


class ContentAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Chapter, ChapterAdmin)
admin.site.register(Content, ContentAdmin)
