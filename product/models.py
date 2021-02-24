from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from customer.models import Profile

# Create your models here.

CATEGORY_CHOICES = (
    ('Cosmetics_and_beauty', 'Cosmetics and Beauty'),
    ('kids_clothes', 'Kids Clothes'),
    ('men_and_women_clothes', 'Men and Women Clothes'),
    ('gadgets_accessories', 'Gadgets Accessories'),
    ('electronics', 'Electronics'),
)

class Product(models.Model):
    title = models.CharField(max_length=100)
    selling_price = models.DecimalField(max_digits=10, decimal_places=2)
    discounted_price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    image1 = models.ImageField(upload_to='products', default='default.jpg', null=True, blank=True)
    image2 = models.ImageField(upload_to='products', default='default.jpg', null=True, blank=True)
    image3 = models.ImageField(upload_to='products', default='default.jpg', null=True, blank=True)
    image4 = models.ImageField(upload_to='products', default='default.jpg', null=True, blank=True)
    image5 = models.ImageField(upload_to='products', default='default.jpg', null=True, blank=True)
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

    def specification_list(self):
        return self.specification.split('\n')

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

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10, null=True, blank=True)
    color = models.CharField(max_length=10, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.user.username

STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Shipped', 'Shipped'),
    ('Delivered', 'Delivered'),
    ('Cancelled', 'Cancelled'),
)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated_at = models.DateTimeField(auto_now_add=False, auto_now=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.user.username
