from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect

from account.forms import StudentCreateForm

def index(request):
    form = StudentCreateForm(request.POST or None)
    context = RequestContext(request)
    template = 'core/index.html'

    if form.is_valid():
        # `commit=False`: before save it to database, just keep it in memory
        save_it = form.save(commit=False)
        save_it.save()

        messages.success(request, 'Thank you for joining')
        return HttpResponseRedirect('/thank-you/')

    return render_to_response(template, locals(), context_instance=context)

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
