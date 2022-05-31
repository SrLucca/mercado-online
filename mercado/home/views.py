from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.


def home(request):

    promo_actives = User.objects.all()

    return render(request, 'paginas/home.html', {'promo_actives':promo_actives})