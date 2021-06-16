from django import forms
from .models import Bride
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
Rasi_CHOICES =(
    ("1", "Mesham"),
    ("2", "Rishabam"),
    ("3", "Mithunam"),
    ("4", "Kadakam"),
    ("5", "Simmam"),
    ("6", "Kanni"),
    ("7", "Thulam"),
    ("8", "Viruchikam"),
    ("9", "Thanusu"),
    ("10", "Makaram"),
    ("10", "Kumbam"),
    ("10", "Meenam"),
)
State_Choices = (
    ("1", "Mesham"),
    ("1", "Mesham"))
class Valueform(forms.ModelForm):

    Rasi = forms.ChoiceField(choices = Rasi_CHOICES)

    class Meta:
        model = Bride
        fields = "__all__"


class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
