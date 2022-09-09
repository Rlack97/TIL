from django import forms
from .models import Reservation

class ReservationForm(forms.Form):

    class Meta:
        model = Reservation
        fields = '__all__'



# a= forms.Form
# b= Meta