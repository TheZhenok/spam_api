from django.forms import ModelForm
from auths.models import Contact


class ContactForm(ModelForm):
    "Base form for contact send message"

    class Meta:
        model = Contact
        fields = '__all__'