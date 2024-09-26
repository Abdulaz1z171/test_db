from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Post

# Register your models here.



class PostAdmin(TranslationAdmin):
    pass

admin.site.register(Post, PostAdmin)
