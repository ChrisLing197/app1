from django import forms
from django.contrib.auth.forms import UserCreationForm
from system import models

#Form for an Admin Registration Form
class AdminRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    date_of_birth = forms.DateField()
    phone_number = forms.CharField()
    mail_address = forms.CharField(widget=forms.Textarea)
    role = forms.ChoiceField(
            choices = models.Registration.ROLE_TYPE_CHOICES
            )

    #Meta and save overwrite default user creation form to include email, first name, and last name
    class Meta:
        model = models.User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    #Meta and save overwrite default user creation form to include email, first name, and last name
    def save(self, commit=True):
        user = super(AdminRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        reg = models.Registration()
        reg.date_of_birth = self.cleaned_data['date_of_birth']
        reg.phone_number = self.cleaned_data['phone_number']
        reg.mail_address = self.cleaned_data['mail_address']
        reg.role = self.cleaned_data['role']

        if commit:
            user.save()
            reg.user = user
            reg.save()
        return user
    
#Form for a Patient Registration Form
class MyRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    date_of_birth = forms.DateField()
    phone_number = forms.CharField()
    mail_address = forms.CharField(widget=forms.Textarea)

    ChOI=(
        ('BU','Buyer'),
        ('SE','Seller')
    )

    role = forms.ChoiceField(choices=ChOI,required=True)

    #Meta and save overwrite default user creation form to include email, first name, and last name
    class Meta:
        model = models.User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')

    #Meta and save overwrite default user creation form to include email, first name, and last name
    def save(self, commit=True):
        user = super(MyRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        reg = models.Registration()
        reg.date_of_birth = self.cleaned_data['date_of_birth']
        reg.phone_number = self.cleaned_data['phone_number']
        reg.mail_address = self.cleaned_data['mail_address']

        if commit:
            user.save()
            
        reg.user = user
        if commit:
            reg.save()
        return user

#Form for a Patient Registration Form
class Cart(UserCreationForm):
    timestamp=forms.CharField(max_length=30)

    #Meta and save overwrite default user creation form to include email, first name, and last name
    class Meta:
        model = models.Cart
        fields =('name','description','condition','price','quantity')

    def save(self, commit=True):
        user = super(Cart, self).save(commit=False)
        self.object=form.save(commit=False)
        self.object.buyer=User
        self.object.save()
        return super(edit.ModelFormMixin,self).form_valid(form)
