from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from users.models import Profile, Buyer
from product.models import Product


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # by default dont have an email so we added it by itself

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['category', 'image', 'title', 'description', 'price']


class BuyerRegisterForm(UserRegisterForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class BuyerUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = Buyer
        fields = ['image']








