from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone


LABEL_CHOICES = (
    ('P', ' primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport wear'),
    ('OW', 'Outwear')
)


class Item(models.Model):
    title = models.CharField(max_length=100)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    category = models.CharField(default='S', choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(default='P', choices=LABEL_CHOICES, max_length=1)
    slug = models.SlugField(default='test_product')
    description = models.TextField(default='Welcome to Myshop!')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("core:product", kwargs={"slug": self.slug})

    def get_add_to_cart_url(self):
        return reverse("core:add_to_cart", kwargs={"slug": self.slug})

    def get_remove_from_cart_url(self):
        return reverse("core:remove_from_cart", kwargs={"slug": self.slug})


class OrderItems(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE, blank=True, null=True)
    ordered = models.BooleanField(default=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.item.title}"


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItems)
    ordered_date = models.DateTimeField(default=timezone.now)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
