from .models import Product, Vendor, Shipper, ReviewsProducts, PassportShipper, VendorRating, ShipperRating
from django.contrib import admin

# Register your models here.
admin.site.register(Product)
admin.site.register(Vendor)
admin.site.register(Shipper)
admin.site.register(ReviewsProducts)
admin.site.register(PassportShipper)
admin.site.register(VendorRating)
admin.site.register(ShipperRating)
