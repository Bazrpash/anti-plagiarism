from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Account


def index(request):
    # template = loader.get_template('web/index.html')
    # return HttpResponse(template.render(context, request))
    context = dict()
    joined_number = Account.objects.filter(is_verified=True).count()
    context['joined_number'] = joined_number
    return render(request, 'web/index.html', context)
