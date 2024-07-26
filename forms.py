from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['shop_name', 'shop_zone', 'shop_location', 'complaint_type', 'phone_number']

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number.isdigit() or len(phone_number) != 10:
            raise forms.ValidationError("Phone number must be 10 digits long.")
        return phone_number