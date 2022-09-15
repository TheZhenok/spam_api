from django.shortcuts import render
from django.views.generic import CreateView

from auths.models import Contact
from auths.form import ContactForm
from auths.tasks import send_spam_email

# Create your views here.
class ContactView(CreateView):
    """View from create contact"""
    model = Contact
    template_name = "auths/create-contact.html"
    success_url = "/"
    form_class = ContactForm

    def form_valid(self, form):
        form.save()
        send_spam_email.delay(form.instance.email)
        return super().form_valid(form)

