# translation.py
from modeltranslation.translator import translator, TranslationOptions
from .models import Post

class PostTranslationOptions(TranslationOptions):
    fields = ('title', 'content')  # Fields to translate

translator.register(Post, PostTranslationOptions)
