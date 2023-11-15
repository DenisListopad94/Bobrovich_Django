from .models import Product, Vendor, Shipper, ProductReviews, VendorReviews, ShipperReviews, Passport
from django.contrib import admin

# Register your models here.
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Shipper)
admin.site.register(ProductReviews)
admin.site.register(VendorReviews)
admin.site.register(ShipperReviews)
admin.site.register(Passport)
