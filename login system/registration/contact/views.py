from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.template.loader import render_to_string


from .forms import ContactForm
def contactus(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('contactus.html', {
                'name': name,
                'email': email,
                'content': content,
            })

            send_mail('The contact form subject', 'This is the message', 'noreply@nakulsejwar.com', ['sejwarnakul02@gmail.com'], html_message=html)

            return redirect('contactus')
        
    else:
        form = ContactForm()

    return render (request, 'contactus.html', {
            'form': form
    })