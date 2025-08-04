from django.db import models

# Create your models here.
class Product(models.Model):
    name=models.CharField(max_length=200)
    discription=models.TextField()
    image=models.ImageField(upload_to="products/")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

def edit(self,name,discription,image):
    self.name=name 
    self.discription=discription
    self.image=image
    self.save()

def short_desc(self):
    words=self.discription.split()
    if len(words)>50:
        return ' '.join(words[:30])+"...."
    else:
        return self.discription

    