from django.db import models

CATEGORY = [
    ("FR", "Fruit"),
    ("VG", "Vegetable"),
    ("ML", "Milk"),
    ("MT", "Meat"),
    ("TC", "Tea and Coffee"),
    ("FS", "Fish"),
    ("AL", "Alcohol"),
]


class Products(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=False, default="perfect product")
    price = models.FloatField()
    amount = models.PositiveIntegerField()
    delivery_date = models.DateField(auto_now_add=False)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY
    )

    def __str__(self):
        return self.name


class Vendors(models.Model):
    name = models.CharField(max_length=40)
    foundation_year = models.PositiveIntegerField()
    country = models.CharField(max_length=40)
    phone = models.CharField(max_length=40)

    def __str__(self):
        return self.name
