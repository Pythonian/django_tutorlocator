from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Tutor, Student


# class TutorSignUpForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     address = forms.CharField(max_length=200)
#     about = forms.CharField(widget=forms.Textarea)
#     phone_number = forms.CharField(max_length=11)
#     company_name = forms.CharField(max_length=50)
#     image = forms.ImageField()
#     state = forms.CharField(max_length=10)
#     government_id = forms.FileField()
#     cac_file = forms.FileField()

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.visible_fields():
#             field.field.widget.attrs['class'] = 'form-control'
#             field.field.help_text = None

#     class Meta(UserCreationForm.Meta):
#         model = User
#         fields = ['company_name', 'address', 'image', 'about',
#                   'state', 'government_id', 'cac_file', 'phone_number',
#                   'password1', 'password2', 'email', 'username']

#     @transaction.atomic
#     def save(self):
#         user = super().save(commit=False)
#         user.is_vendor = True
#         user.save()
#         user.refresh_from_db()
#         user.vendor.about = self.cleaned_data.get('about')
#         user.vendor.email = self.cleaned_data.get('email')
#         user.vendor.phone_number = self.cleaned_data.get('phone_number')
#         user.vendor.cac_file = self.cleaned_data.get('cac_file')
#         user.vendor.government_id = self.cleaned_data.get('government_id')
#         user.vendor.company_name = self.cleaned_data.get('company_name')
#         user.vendor.image = self.cleaned_data.get('image')
#         user.vendor.address = self.cleaned_data.get('address')
#         user.vendor.state = self.cleaned_data.get('state')
#         user.save()
#         return user


class StudentSignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    phone_number = forms.CharField(required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.help_text = None

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['email', 'password1', 'password2',
                  'first_name', 'last_name', 'phone_number']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                "A user with that email already exists.")
        return email

# class UserForm(forms.ModelForm):

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.visible_fields():
#             field.field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']


# class CustomerForm(forms.ModelForm):

#     class Meta:
#         model = Customer
#         fields = ['phone_number', 'address', 'image']


# class VendorForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         for field in self.visible_fields():
#             field.field.widget.attrs['class'] = 'form-control'

#     class Meta:
#         model = Vendor
#         fields = ['company_name', 'address', 'image', 'about',
#                   'state', 'government_id', 'cac_file', 'phone_number']
