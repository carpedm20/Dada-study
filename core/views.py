from django.shortcuts import render, redirect, render_to_response, RequestContext, HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .forms import StudyGroupForm
from account.forms import StudentCreateForm

def index(request, auth_form=None, user_form=None):
    form = StudentCreateForm(request.POST or None)
    context = RequestContext(request)

    if request.user.is_authenticated():
        return render(request,
                      'core/home.html',
                      {'auth_form': auth_form, 'user_form': user_form, })
    """else:
        if form.is_valid():
            # `commit=False`: before save it to database, just keep it in memory
            save_it = form.save(commit=False)
            save_it.save()

            messages.success(request, 'Thank you for joining')
            return HttpResponseRedirect('/thank-you/')"""

    return render_to_response('core/index.html', locals(), context_instance=context)

@login_required
def create_study_group(request):
    form = StudyGroupForm(request.POST or None)
    context = RequestContext(request)
    template = 'core/create_study.html'

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
    form = StudyGroupForm(request.POST or None)
    template = 'core/create_study.html'

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
