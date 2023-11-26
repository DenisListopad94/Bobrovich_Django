from .models import Product, Vendor, Shipper, ProductReviews, VendorReviews, ShipperReviews, Passport, Person
from django.contrib import admin


class ProductReviewsInline(admin.TabularInline):
    model = ProductReviews


class ProductPerson_m2m_Inline(admin.StackedInline):
    model = Person.product.through


class VendorReviewsInline(admin.StackedInline):
    model = VendorReviews


class ShipperReviewsInline(admin.StackedInline):
    model = ShipperReviews


# @admin.register(Product)
# class ProductAdmin(admin.ModelAdmin):
#     pass


class PersonAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "email", "phone"]
    search_fields = ["name"]
    filter_horizontal = ["product"]


class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "amount", "category"]
    list_filter = ["category"]

    inlines = [
        ProductReviewsInline, # one to many
        ProductPerson_m2m_Inline # many to many
    ]


class VendorAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "email", "phone", "inn"]

    inlines = [
        VendorReviewsInline
    ]


class ShipperAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "email", "phone", "personal_discont"]

    inlines = [
        ShipperReviewsInline
    ]


class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ["title", "descriptions", "author", "review_time"]


class VendorReviewsAdmin(admin.ModelAdmin):
    list_display = ["title", "descriptions", "author", "review_time"]


class ShipperReviewsAdmin(admin.ModelAdmin):
    list_display = ["title", "descriptions", "author", "review_time"]


class PassportAdmin(admin.ModelAdmin):
    list_display = ["person", "passport_series", "passport_number"]


# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Vendor, VendorAdmin)
admin.site.register(Shipper, ShipperAdmin)
admin.site.register(ProductReviews, ProductReviewsAdmin)
admin.site.register(VendorReviews, VendorReviewsAdmin)
admin.site.register(ShipperReviews, ShipperReviewsAdmin)
admin.site.register(Passport, PassportAdmin)
admin.site.register(Person, PersonAdmin)
