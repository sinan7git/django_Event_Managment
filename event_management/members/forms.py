from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


BIRTH_YEAR_CHOICES = ['1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003', '2004', '2005', '2006', '2007',]


class RegisterUserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    customer_name = forms.CharField(max_length=50,widget=forms.TextInput(attrs={'class': 'form-control'}))
    dob = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    address = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    
    class Meta:
        model = User
        fields = ('username', 'customer_name', 'email','dob','address' ,'password1', 'password2',)
        
        
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class' ] = 'form-control'
        self.fields['password1'].widget.attrs['class' ] = 'form-control'
        self.fields['password2'].widget.attrs['class' ] = 'form-control'
        

        