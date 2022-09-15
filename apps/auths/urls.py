from django.urls import path, include
from auths.views import (
    ContactView
)

urlpatterns = [
    path('', ContactView.as_view(), name='create_contact')
]
