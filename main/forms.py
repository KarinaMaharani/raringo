from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags

class ProductEntryForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price", "description", "tags", "ratings", "image_url"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_price(self):
        price = self.cleaned_data["price"]
        return strip_tags(price)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)

    def clean_tags(self):
        tags = self.cleaned_data["tags"]
        return strip_tags(tags)
    
    def clean_ratings(self):
        ratings = self.cleaned_data["ratings"]
        return strip_tags(ratings)
    
    def clean_image_url(self):
        image_url = self.cleaned_data["image_url"]
        return strip_tags(image_url)