from curses.ascii import US
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2']

    # def __init__(self, *args, **kwargs):
    #     super(MyUserCreationForm, self).__init__(*args, **kwargs)
    #     self.fields.widget.attrs.update({'class': 'form-control'})

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'name', 'username', 'email', 'bio']
