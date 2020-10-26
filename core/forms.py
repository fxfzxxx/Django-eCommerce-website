from django import forms
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget


PAYMENT_CHOICES = {
    ('S', 'Stripe'),
    ('P', 'PayPal')
}


class CheckoutForm(forms.Form):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    email_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'youremail@example.com',
        'class': 'form-control'
    }))
    street_address = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': '1234 Main St',
        'class': 'form-control'
    }))
    apartment_address = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'placeholder': 'Apartment or suite',
        'class': 'form-control'
    }))
    country = CountryField(blank_label='(select country)').formfield(widget=CountrySelectWidget(
        attrs={
            'class': 'custom-select d-block w-100',
        }
    ))
    zip = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control'
    }))
    same_billing_adress = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    save_info = forms.BooleanField(required=False, widget=forms.CheckboxInput())
    payment_option = forms.ChoiceField(widget=forms.RadioSelect, choices=PAYMENT_CHOICES)


class CouponForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Promo code',
        'aria-label': 'Recipient\'s username',
        'aria-describedby': 'basic-addon2'
    }))


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(required=False)
    save = forms.BooleanField(required=False)
    use_default = forms.BooleanField(required=False)
