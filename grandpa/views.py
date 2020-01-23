from django.shortcuts import render
from . import models


def index(request):
    user_profile = models.MyProfile.objects.all().order_by('-id').first()
    work_portfolio = models.MyWorkPortfolio.objects.all().order_by('-id')
    context = {
        'userProfile': user_profile,
        'workPortfolio': work_portfolio
    }
    return render(request, 'grandpa/index.html', context)
