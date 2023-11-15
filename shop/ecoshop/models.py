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
    name = models.CharField(max_length=20, verbose_name="наименование")
    description = models.CharField(max_length=100, default="perfect product", verbose_name="описание")
    price = models.FloatField(verbose_name="цена")
    amount = models.PositiveIntegerField(verbose_name="количество")
    delivery_date = models.DateField(auto_now_add=True, verbose_name="дата поставки")
    category = models.CharField(
        max_length=2,
        choices=CATEGORY,
        verbose_name="категория"
    )

    class Meta:
        verbose_name_plural = "Продукты"

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=40, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=20, null=True)
    product = models.ManyToManyField("Product")


class Passport(models.Model):
    person = models.OneToOneField("Person", on_delete=models.CASCADE)
    passport_number = models.PositiveIntegerField()
    passport_series = models.CharField(max_length=5)

    def __str__(self):
        return str(self.passport_number)


class Vendor(Person):
    inn = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Shipper(Person):
    personal_discont = models.FloatField()

    def __str__(self):
        return self.name


class Reviews(models.Model):
    title = models.CharField(max_length=40)
    descriptions = models.CharField(max_length=300, default="default review")
    author = models.CharField(max_length=40)
    review_time = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class ProductReviews(Reviews):
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class VendorReviews(Reviews):
    vendor = models.ForeignKey("Vendor", on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class ShipperReviews(Reviews):
    shipper = models.ForeignKey("Shipper", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
