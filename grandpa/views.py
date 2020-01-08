from django.shortcuts import render
from . import models


def index(request):
    user_profile = models.UserProfile.objects.all()
    work_portfolio = models.WorkPortfolio.objects.all()
    context = {
        'userProfile': user_profile,
        'workPortfolio': work_portfolio
    }
    return render(request, 'grandpa/index.html', context)
