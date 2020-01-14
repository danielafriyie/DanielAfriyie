from django.shortcuts import render
from . import models


def index(request):
    user_profile = models.MyProfile.objects.all()
    work_portfolio = models.MyWorkPortfolio.objects.all()
    context = {
        'userProfile': user_profile,
        'workPortfolio': work_portfolio
    }
    print(user_profile)
    return render(request, 'grandpa/index.html', context)
