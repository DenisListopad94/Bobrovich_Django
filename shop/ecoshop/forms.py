from django import forms
from django.forms import Textarea
from .models import Product, ShipperReviews, VendorReviews


# class ProductForm(forms.Form):
#     name = forms.CharField(label="product_name", max_length=20)
#     description = forms.CharField(label="description", max_length=100)
#     price = forms.CharField(label="price")
#     amount = forms.IntegerField(label="amount")
#     delivery_date = forms.DateField(label="delivery_date")
#     category = forms.CharField(label="category", max_length=2)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "amount", "category"]
        widgets = {
            "description": Textarea(attrs={"cols": 80, "rows": 20}),
        }


class ShipperReviewsForm(forms.ModelForm):
    class Meta:
        model = ShipperReviews
        fields = "__all__"
        widgets = {
            "descriptions": Textarea(attrs={"cols": 80, "rows": 10}),
        }


class VendorReviewsForm(forms.ModelForm):
    class Meta:
        model = VendorReviews
        fields = "__all__"
        widgets = {
            "descriptions": Textarea(attrs={"cols": 80, "rows": 10}),
        }
