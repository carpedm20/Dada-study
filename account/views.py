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
from django.shortcuts import render

from .forms import StudentCreateForm, StudentAuthForm

reverse_lazy = lambda name=None, *args: lazy(reverse, str)(name, args=args)

def sign_in(request):
    form = StudentAuthForm(request.POST or None)
    template = 'account/sign_in.html'

    if form.is_valid():
        # `commit=False`: before save it to database, just keep it in memory
        save_it = form.save(commit=False)
        save_it.save()

        messages.success(request, 'Thank you for joining')
        return HttpResponseRedirect('/thank-you/')

    return render(request, template,  {'form': form,  })

def sign_up(request):
    if request.method == 'POST':
        form = StudentCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = StudentCreateForm() 

    return render(request, "core/index.html",  {'form': form,  })

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return HttpResponseRedirect(reverse('core:recent-pins'))


def private(request):
    return TemplateResponse(request, 'users/private.html', None)
