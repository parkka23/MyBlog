from modeltranslation.translator import register, TranslationOptions
from .models import Category, PostModel
from modeltranslation.admin import TranslationAdmin
from django.contrib import admin

@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)  # Add other fields you want to translate here

@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}

