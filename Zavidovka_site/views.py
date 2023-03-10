from django.core.mail import EmailMultiAlternatives
from django.shortcuts import render
from django.template.loader import get_template

from Zavidovka_site.forms import ContactForm
# from Zavidovka_site.models import MenuItem


def index(request):
    return render(
        request,
        'index.html'
    )


def about(request):
    return render(
        request,
        'about.html'
    )


def history(request):
    context = {}
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            context = {'success': 1}
    else:
        form = ContactForm()
    context['form'] = form
    return render(
        request,
        'history.html',
        context=context
    )


def send_message(name, email, message):
    text = get_template('message.html')
    html = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Сообщение от пользователя'
    from_email = 'vasyusha83@gmail.com.com'
    text_content = text.render(context)
    html_content = html.render(context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, ['vasyusha83@gmail.com.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()
