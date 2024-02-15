from django.contrib import admin
from main.models import BlogpostModel,CategoryModel, AuthorModel
# Register your models here.
admin.site.register(BlogpostModel)
admin.site.register(CategoryModel)
admin.site.register(AuthorModel)