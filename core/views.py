
from django.shortcuts import render
from django.http import HttpResponse
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from django.views.generic import View, TemplateView

class IndexView(TemplateView):

    template_name = 'index.html'

index = IndexView.as_view()

def contact(request):
    success = False
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.send_mail()
            success = True
    else:
        form = ContactForm()
    context = {
        'form': form,
        'success': success
    }
    return render(request, 'contact.html', context)
