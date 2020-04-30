from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model

# Create your models here.
user = get_user_model()


class LocationCategoryModel(models.Model):
    location_category = models.CharField(max_length=50)

    def __str__(self):
        return self.location_category


class PostCategory(models.Model):
    post_category = models.CharField(max_length=150)

    def __str__(self):
        return self.post_category


class PostAd(models.Model):
    # CATEGORY_CHOICE = [
    #     ('MOBILES', 'Mobiles'),
    #     ('ELECTROMICS', 'Electromics'),
    #     ('PROPERTY', 'Property'),
    #     ('SPORTS & KIDS', 'Sports & Kids'),
    #     ('HOME & LIVING', 'Home & Living'),
    #     ('VEHICLES', 'Vehicles'),
    #     ('PETS & ANIMALS', 'Pets & Animals'),
    #     ('FASHION, HEALTH & BEAUTY', 'Fashion, Health & Beauty'),
    # ]
    CONDITION_CHOICE = [
        ('NEW', 'New'),
        ('USED', 'Used'),
    ]

    # LOCATION_CHOICE = [
    #     ('DHAKA', 'Dhaka'),
    #     ('CHATTOGRAM', 'Chattogram'),
    #     ('KHULNA', 'Khulna'),
    #     ('BARISHAL', 'Barishal'),
    #     ('RAJSHAHI', 'Rajshahi'),
    #     ('RANGPUR', 'Rangpur'),
    #     ('MYMENSINGH', 'Mymensingh'),
    # ]
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICE, null=True, blank=True)
    location = models.ForeignKey(LocationCategoryModel, on_delete=models.DO_NOTHING)
    mobile = models.CharField(max_length=100, null=True, blank=True)
    price = models.CharField(max_length=20, blank=True, null=True)
    image_main = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image2 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    image3 = models.ImageField(upload_to='post_images/', blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])
