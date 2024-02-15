from django.db import models

class CategoryModel(models.Model):
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=255)

    def __str__(self):
       return self.title

class AuthorModel(models.Model):
    name = models.CharField(max_length=128)
    bio = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True)
    email = models.EmailField()

    def __str__(self):
       return self.name

class BlogpostModel(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey(AuthorModel, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
       return self.title



# TODO:
    #create author and category models
    #update temp with django temp
    #homepage, category, posts using bootstrap





