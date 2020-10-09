from django.db import models
from django.conf import settings


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
    category = models.CharField(default='S', choices=CATEGORY_CHOICES, max_length=2)
    label = models.CharField(default='P', choices=LABEL_CHOICES, max_length=1)

    def __str__(self):
        return self.title


class OrderItems(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItems)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
