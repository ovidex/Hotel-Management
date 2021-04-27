from django import forms
from .models import Room
class AvailabilityForm(forms.Form):

    room_category=forms.ChoiceField(choices=Room.ROOM_CATEGORIES,required=True)
    check_in=forms.DateTimeField(required=True,input_formats=["%Y-%m-%d",])
    check_out=forms.DateTimeField(required=True,input_formats=["%Y-%m-%d",])
