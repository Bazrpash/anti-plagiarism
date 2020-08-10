import requests

from django.shortcuts import render
from django.template import loader
from django.core.mail import send_mail
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.conf import settings
from .models import Account, AccountForm
from .tasks import new_user_signed


secret_key = settings.RECAPTCHA_SECRET_KEY


def index(request, status=-1):
    context = dict()
    if status == 0:
        context['is_error'] = True
    elif status == 1:
        context['is_created'] = True
    elif status == 2:
        context['is_verified'] = True
    joineds = Account.objects.filter(is_verified=True)
    context['student_joined_number'] = joineds.filter(is_professor=False).count()
    context['teacher_joined_number'] = joineds.filter(is_professor=True).count()
    return render(request, 'web/index.html', context)


def submit(request):
    raw_data = request.POST
    f = AccountForm(request.POST)

    if 'g-recaptcha-response' in raw_data:
        # captcha verification
        cap_data = {
            'response': raw_data['g-recaptcha-response'],
            'secret': secret_key
        }
        resp = requests.post('https://www.google.com/recaptcha/api/siteverify', data=cap_data)
        result_json = resp.json()
        if not result_json['success']:
            return HttpResponseRedirect(reverse('web:index', kwargs={'status': 0}))
    else:
        # recapta data not provided
        return HttpResponseRedirect(reverse('web:index', kwargs={'status': 0}))

    if f.is_valid():
        obj = Account(**f.cleaned_data)
    else:
        # print(f.errors)
        return HttpResponseRedirect(reverse('web:index', kwargs={'status': 0}))
    if result_json['action'] == 'studentsubmit':
        obj.is_professor = False
    else:
        obj.is_professor = True
    if 'is_visible' in raw_data:
        if int(raw_data['is_visible']) > 0:
            obj.is_visible = True
        else:
            obj.is_visible = False
    if 'is_graduated' in raw_data:
        if int(raw_data['is_graduated']) > 0:
            obj.is_graduated = True
        else:
            obj.is_graduated = False
    obj.save()

    if not settings.DEBUG:
        send_verification_email(obj.email, obj.id)

    return HttpResponseRedirect(reverse('web:index', kwargs={'status': 1}))


def validate(request, user_id):
    try:
        user_account = Account.objects.get(id=user_id)
    except (KeyError, Account.DoesNotExist):
        return HttpResponseRedirect(reverse('web:index'))
    if user_account.is_verified:
        return HttpResponseRedirect(reverse('web:index'))
    user_account.is_verified = True
    user_account.save()

    new_user_signed.delay(user_id)

    return HttpResponseRedirect(reverse('web:index', kwargs={'status': 2}))


def send_verification_email(recipient, validation_code):
    validation_link = 'https://www.iran-antiplagiarism.com/validate/' + str(validation_code)
    html_message = loader.render_to_string('web/email.html', {
        'validation_link': validation_link
    })

    send_mail(
        subject='تایید عضویت',
        message='لطفا عضویت خود را تایید نمایید.',
        html_message=html_message,
        recipient_list=[recipient],
        from_email='contact@iran-antiplagiarism.com',
        fail_silently=True
    )
