import random
import os
from django.db import models

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext

# Create your models here.
def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 2323232)
    name, ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    #final_filename = '{new_filename}{ext}'.format(new_filename=new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename=new_filename,
        final_filename=final_filename
    )


class ProductManager(models.Manager):
    def get_by_id(self, id):
        qs = self.get_queryset().filter(id=id)    # Product.objects == self.get_queryset()
        if qs.count() == 1:
            return qs.first()
        return None


class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=225)
    price = models.DecimalField(decimal_places=2, max_digits=12, default=0.92)
    image = models.ImageField(upload_to=upload_image_path, null=True, blank=True)

    objects = ProductManager()

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
