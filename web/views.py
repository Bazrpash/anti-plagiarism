from django.shortcuts import render
# from django.template import loader
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account, AccountForm


def index(request, is_verified=0):
    context = dict()
    if is_verified > 0:
        context['is_verified'] = True
    joined_number = Account.objects.filter(is_verified=True).count()
    context['joined_number'] = joined_number
    return render(request, 'web/index.html', context)


def submit(request):
    context = dict()
    raw_data = request.POST
    f = AccountForm(request.POST)

    is_created = False
    joined_number = Account.objects.filter(is_verified=True).count()
    context['joined_number'] = joined_number
    obj = None
    if f.is_valid():
        obj = Account(**f.cleaned_data)
    # print(f.errors)
    # TODO do some prof. stuff here
    if obj:
        if 'uni_position' in raw_data:
            obj.is_professor = True
            if raw_data['uni_position'] == 0:
                print("injjjjjjjjjinjjjjjjjjjinjjjjjjjjjinjjjjjjjjj")
                print(Account.POSITION_CHOICES)
                obj.uni_position = Account.POSITION_CHOICES[0]
        obj.save()
        is_created = True
    context['is_created'] = is_created
    return render(request, 'web/index.html', context)


def validate(request, user_id):
    try:
        user_account = Account.objects.get(id=user_id)
    except (KeyError, Account.DoesNotExist):
        return HttpResponseRedirect(reverse('web:index'))
    if user_account.is_verified:
        return HttpResponseRedirect(reverse('web:index'))
    user_account.is_verified = True
    user_account.save()
    return HttpResponseRedirect(reverse('web:index', kwargs={'is_verified': 1}))
