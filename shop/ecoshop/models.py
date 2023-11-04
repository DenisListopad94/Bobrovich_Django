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


class Product(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, default="perfect product")
    price = models.FloatField()
    amount = models.PositiveIntegerField()
    delivery_date = models.DateField(auto_now_add=True)
    category = models.CharField(
        max_length=2,
        choices=CATEGORY
    )

    def __str__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    inn = models.PositiveIntegerField()
    product = models.ManyToManyField("Product")

    def __str__(self):
        return self.name


class Shipper(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    product = models.ManyToManyField("Product")

    def __str__(self):
        return self.name


class ReviewsProducts(models.Model):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)
    title = models.CharField(max_length=40)
    descriptions = models.CharField(max_length=300, default="default review")
    author = models.CharField(max_length=40)
    review_time = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class PassportShipper(models.Model):
    shipper = models.OneToOneField("Shipper", on_delete=models.CASCADE)
    passport_number = models.PositiveIntegerField()
    passport_series = models.CharField(max_length=5)

    def __str__(self):
        return str(self.passport_number)


class VendorRating(models.Model):
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)
    vendor_rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.vendor_rating)


class ShipperRating(models.Model):
    shipper = models.ForeignKey("Shipper", on_delete=models.CASCADE)
    shipper_rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.shipper_rating)
