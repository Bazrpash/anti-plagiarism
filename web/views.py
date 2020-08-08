from django.shortcuts import render
# from django.template import loader
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Account, AccountForm


def index(request, status=-1):
    context = dict()
    if status == 0:
        context['is_error'] = True
    elif status == 1:
        context['is_created'] = True
    elif status == 2:
        context['is_verified'] = True
    joined_number = Account.objects.filter(is_verified=True).count()
    context['joined_number'] = joined_number
    return render(request, 'web/index.html', context)


def submit(request):
    raw_data = request.POST
    f = AccountForm(request.POST)

    obj = None
    if f.is_valid():
        obj = Account(**f.cleaned_data)
    else:
        # print(f.errors)
        return HttpResponseRedirect(reverse('web:index', kwargs={'status': 0}))
    if obj:
        if 'uni_position' in raw_data:
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
        if 'student_no' in raw_data:
            obj.is_professor = False
        obj.save()

        # TODO email validation link to user
        # validation_link = 'www.iran-antiplagiarism.com/validate/' + str(obj.id)
        # print(validation_link)

        return HttpResponseRedirect(reverse('web:index', kwargs={'status': 1}))
    else:
        return HttpResponseRedirect(reverse('web:index', kwargs={'status': 0}))


def validate(request, user_id):
    try:
        user_account = Account.objects.get(id=user_id)
    except (KeyError, Account.DoesNotExist):
        return HttpResponseRedirect(reverse('web:index'))
    if user_account.is_verified:
        return HttpResponseRedirect(reverse('web:index'))
    user_account.is_verified = True
    user_account.save()
    return HttpResponseRedirect(reverse('web:index', kwargs={'status': 2}))
