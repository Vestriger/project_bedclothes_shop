from django import forms


PRODUCT_VALUE_CHOICES = [(i, str(i)) for i in range(1, 5)]


class CartAddProductForm(forms.Form):
    value = forms.TypedChoiceField(choices=PRODUCT_VALUE_CHOICES, coerce=int)
    update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)