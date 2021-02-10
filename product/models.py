from django.db import models
from django.utils.text import slugify

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=20)
    image1 = models.ImageField(upload_to='products', null=True, blank=True)
    image2 = models.ImageField(upload_to='products', null=True, blank=True)
    image3 = models.ImageField(upload_to='products', null=True, blank=True)
    image4 = models.ImageField(upload_to='products', null=True, blank=True)
    image5 = models.ImageField(upload_to='products', null=True, blank=True)
    slug = models.SlugField(max_length=75, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    description = models.TextField()
    specification = models.TextField()
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=4.5)
    ratings_quantity = models.IntegerField(default=0)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    # Creating a unique slug for each product
    def _create_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Product.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{slug}-{num}'
            num += 1
        return unique_slug

    # Overriding save method to save the unique slug for the product
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._create_unique_slug()
        super().save(*args, **kwargs)
