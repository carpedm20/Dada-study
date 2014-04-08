from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.utils import simplejson as json
from django.utils import timezone
from django import http

from .models import Event
from .forms import StudyGroupForm, EventForm
from account.forms import StudentCreateForm
from account.models import Student
from core.models import StudyGroup

from utils.func import *

########################
# Index
########################

def index(request, auth_form=None, user_form=None):
    form = StudentCreateForm(request.POST or None)
    context = RequestContext(request)

    if request.user.is_authenticated():
        current_student = get_student_from_user(request.user)

        if current_student is None:
            logout(request)
            redirect('/')
        else:
            print current_student

        # Study group for current User
        #study_group_list = current_student.studygroup_set.all()

        study_group_list = StudyGroup.objects.all()
        student_list = Student.objects.all()

        for group in study_group_list:
            if group in current_student.studygroup_set.all():
                group.isJoined = True
            else:
                group.isJoined = False

        for student in student_list:
            if student in current_student.friends.all():
                student.isFriend = True
            else:
                student.isFriend = False

        return render(request,
                      'core/home.html',
                      {'auth_form': auth_form,
                       'user_form': user_form,
                       'student_list': student_list,
                       'study_group_list' : study_group_list})

    return render_to_response('core/index.html', locals(), context_instance=context)

########################
# Calendar
########################

@login_required
def view_calendar(request, study_group_id=None):
    #form = EventForm(data=request.POST or None, user=request.user)
    template = 'core/view_calendar.html'

    return render(request, template, {})

########################
# View study group
########################

@login_required
def join_study_group(request):
    if request.method == 'POST':
        group_id = request.POST.get("group_id", "")
        group = StudyGroup.objects.get(id=group_id)

        current_student = get_student_from_user(request.user) 

        if group in current_student.studygroup_set.all():
          current_student.studygroup_set.remove(group)
        else:
          current_student.studygroup_set.add(group)

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

########################
# View study group
########################

@login_required
def view_study_group(request, unique_id):
    study_group = StudyGroup.objects.get(unique_id=unique_id)
    template = 'core/view_study_group.html'

    return render(request, template, {'study_group': study_group,  })

########################
# Create Study Group
########################

@login_required
def create_study_group(request):
    form = StudyGroupForm(data=request.POST, user=request.user)
    context = RequestContext(request)
    template = 'core/create_study_group.html'

    if request.method == "POST":
        if form.is_valid():
            group = form.save(commit=False)
            group.save()

            return redirect('/')
        else:
            return create_study_group_view(request)

    return create_study_group_view(request)

@login_required
def create_study_group_view(request):
    form = StudyGroupForm(data=request.POST or None, user=request.user)
    template = 'core/create_study_group.html'

    return render(request, template, {'form': form,  })

# Create your views here.
"""
class CreateStudyGroup(JSONResponseMixin, LoginRequiredMixin, CreateView):
    template_name = None  # JavaScript-only view
    model = Group
    form_class = StudyGroupForm

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseRedirect(reverse('core:recent-pins'))
        return super(CreateImage, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        image = form.save()

        return self.render_json_response({
            'success': {
                'id': StudyGroup.id
            }
        })

    def form_invalid(self, form):
        return self.render_json_response({'error': form.errors})
"""
