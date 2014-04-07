from django.shortcuts import render

from .models import Event

########################
# Event
########################

@login_required
def create_event(request):
    form = EventForm(data=request.POST or None, user=request.user)
    context = RequestContext(request)
    template = 'core/create_event.html'

    if request.method == "POST":
        if form.is_valid():
            group = form.save(commit=False)
            group.save()

            return redirect('/')
        else:
            return create_event_view(request)

    return create_event_view(request)

@login_required
def create_event_view(request):
    form = EventForm(data=request.POST or None, user=request.user)
    template = 'core/create_event.html'

    return render(request, template, {'form': form,  })

########################
# Calendar
########################

@login_required
def view_calendar(request):
    #form = EventForm(data=request.POST or None, user=request.user)
    template = 'core/view_calendar.html'

    return render(request, template, {})

@login_required
def get_event_as_json(request): 
    # Get all events - Not yet completed 
    events = Event.objects.all()

    # Create the fullcalendar json events list 
    event_list = []

    for event in events: 
        # It retrieves dates in the correct time horaire 
        event_start = event.start.astimezone(timezone.get_default_timezone()) 
        event_end = event.end.astimezone(timezone.get_default_timezone())

        # It was decided that if the event starts at midnight is a 
        # on the event day 
        if event_start.hour == 0 and event_start.minute == 0: 
            Allday = True 
        else: 
            Allday = False

        #if not event.is_cancelled : 
        event_list.append ({ 
                    'id':  event.id , 
                    'start':  event_start.strftime ( '%Y-%m- %d %H:%M:%S' ), 
                    'end':  event_end.strftime ( '%Y-%m- %d %H:%M:%S' ), 
                    'title':  event.name, 
                    'allDay': True 
                    })

    if len(event_list)  ==  0 : 
        raise http.Http404 
    else : 
        return http.HttpResponse(json.dumps(event_list), content_type = 'application/json' )
