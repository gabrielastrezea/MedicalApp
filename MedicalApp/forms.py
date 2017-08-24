from django import forms
from django.contrib.auth.models import User


class MedicineForm(forms.Form):
    name = forms.CharField(widget=forms.widgets.TextInput,
                           required=True, max_length=256)


class LoginForm(forms.Form):
    username = forms.CharField(label="Username")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)


class DoctorForm(forms.Form):
    user = forms.ChoiceField(choices=[('', "Unassigned user")], required=False)
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={'class': 'hidden'}))
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "hidden"}))
    first_name = forms.CharField(label="First Name")
    last_name = forms.CharField(label="Last Name")
    phone = forms.DecimalField(label="Phone Number")
    email = forms.EmailField(label="E-mail Address")
    cnp = forms.DecimalField(label="CNP")

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)

        self.fields['user'].choices += (
            [
                (user.pk, user)
                for user in
                User.objects.filter(patient__isnull=True, doctor__isnull=True)
            ]
        )


class PrescriptionForm(forms.Form):
    patient = forms.ChoiceField(choices=[('', "Patient")])
    medicine = forms.ChoiceField(choices=[('', "Medicine")])
    total_quantity = forms.DecimalField(label="Quantity")

