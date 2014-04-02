from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.utils.html import strip_tags

from .models import Student
from Schoool.models import School

class StudentCreateForm(UserCreationForm):
    error_messages = {
        'duplicate_email': "A user with that e-mail already exists.",
        'email_mismatch': "The two e-mail fields didn't match.",
    }

    username1 = forms.EmailField(label="E-mail")
    username2 = forms.EmailField(label="Confirm E-mail")
    #username1 = forms.EmailField(label="E-mail", widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    #username2 = forms.EmailField(label="Confirm E-mail", widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password Confirmation'}))
    school = forms.ModelChoiceField(queryset=School.objects.all(), empty_label="Please choose a university")
 
    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form
 
    class Meta:
        model = User
        fields = ['username1', 'username2', 'password1', 'password2', 'school']

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.save()
        user_profile = Student(user=user, school=self.cleaned_data["school"])

        if commit:
            user_profile.save()

        return user_profile

class StudentAuthForm(AuthenticationForm):
    username = forms.CharField(widget=forms.widgets.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.widgets.PasswordInput(attrs={'placeholder': 'Password'}))
 
    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form
