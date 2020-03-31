from django import forms
from .models import Prime,Sold
from django.conf import settings

class AddForm(forms.ModelForm):
    items = forms.CharField(widget=forms.TextInput(
                                 attrs={'class':'speech-input','x-webkit-speech': 'x-webkit-speech'}))
    class Meta:
        model = Prime
        fields = ('items','quantity','price',)

        widgets = {

            'items': forms.TextInput(attrs={'class': 'textinputclass'}),
            'quantity': forms.TextInput(attrs={'class': 'textinputclass'}),
            'price': forms.TextInput(attrs={'class': 'textinputclass'}),
            

        }
        labels = {
            "items":("Item"),
            "quantity":("Quantity in numbers"),
            "price":("Price with one point Value")

        }


class SoldForms(forms.ModelForm):
   
   
    Numbers_sold = forms.IntegerField(widget = forms.TextInput(attrs={'class': 'textinputclass'}))

    class Meta():
        model = Sold
        fields = ('items','quantity',)

       
        labels = {
            "items":("Item"),
            "Numbers_sold":("Numbers Sold")

        }

   