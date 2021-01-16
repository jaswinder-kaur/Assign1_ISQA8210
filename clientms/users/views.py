from django.urls import reverse_lazy
from django.views import generic

from .forms import CustomUserCreationForm
from django.core.mail import send_mail
from django.conf import settings

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

