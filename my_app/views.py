from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    username = request.user.username

    context = {
        'username': username,
    }

    return render(request, 'index.html', context)
