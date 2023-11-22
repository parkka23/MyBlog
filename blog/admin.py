from django.contrib import admin
from .models import PostModel, Comment, Category


# Register your models here.


class PostModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_created')


admin.site.register(PostModel, PostModelAdmin)
admin.site.register(Comment)
# admin.site.register(Category)
#
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     pass
