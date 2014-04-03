from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Permission
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.functional import lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect

from .forms import StudentCreateForm, StudentAuthForm
from core.views import index

reverse_lazy = lambda name=None, *args: lazy(reverse, str)(name, args=args)

def sign_in(request):
    form = StudentAuthForm(data=request.POST)
    template = 'account/sign_in.html'

    if request.method == 'POST':
        if form.is_valid():
            # Success
            login(request, form.get_user())
            next_url = request.POST.get("next_url", "/")

            return redirect(next_url)
        else:
            # Failure
            return sign_in_view(request)

    return sign_in_view(request)

def sign_in_view(request):
    form = StudentAuthForm(request.POST or None)
    template = 'account/sign_in.html'

    return render(request, template, {'form': form,  })
    

def sign_up(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            # `commit=False`: before save it to database, just keep it in memory
            username = form.clean_username()
            password = form.clean_password2()
            new_user = form.save()
            user = authenticate(username=username, password=password)
            login(request, user)

            return redirect("/")
    else:
        form = StudentCreateForm() 

    return render(request, "core/index.html",  {'form': form,  })

@login_required
def sign_out(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('/')
