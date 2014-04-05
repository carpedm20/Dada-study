from django import forms
from django.utils.html import strip_tags

from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import StudyGroup, Event, Tag
from account.models import Student

class StudyGroupForm(forms.ModelForm):
    name = forms.CharField(label="Group name")
    details = forms.CharField(label="Details")

    user_set = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
    tag_set = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False)
 
    class Meta:
        model = StudyGroup
        fields = ['name', 'details', 'user_set', 'tag_set']

    def __init__(self, user=None, *args, **kwargs):
        self._user = user
        super(StudyGroupForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        form = super(StudyGroupForm, self).is_valid()
        #for f, error in self.errors.iteritems():
        #    if f != '__all_':
        #        self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form
 
    def save(self, commit=True):
        if not self._user:
            return None

        group = StudyGroup(name = self.cleaned_data["name"],
                           details = self.cleaned_data["details"])
        group.save()

        for user in self.cleaned_data["user_set"]:
            group.user_set.add(user)

        print self._user
        group.user_set.add(Student.objects.get(user=self._user))

        for tag in self.cleaned_data["tag_set"]:
            group.tag_set.add(tag)
            
        #if commit:
        #    group.save()

        return group

class EventForm(forms.ModelForm):
    name = forms.CharField(label="Event name")
    details = forms.CharField(label="Details")

    start = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))
    end = forms.DateField(widget=forms.TextInput(attrs={'class':'datepicker'}))

    allDay = forms.BooleanField(required=True)

    studyGroup = forms.ModelChoiceField(queryset=StudyGroup.objects.all(), empty_label="Choose your study group")
 
    class Meta:
        model = StudyGroup
        fields = ['name', 'details', 'start', 'end', 'allDay', 'studyGroup']

    def __init__(self, user=None, *args, **kwargs):
        self._user = user
        super(EventForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        form = super(EventForm, self).is_valid()
        #for f, error in self.errors.iteritems():
        #    if f != '__all_':
        #        self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    def save(self, commit=True):
        if not self._user:
            return None

        event = Event(name = self.cleaned_data["name"],
                      details = self.cleaned_data["details"],
                      start = self.cleaned_data["start"],
                      end = self.cleaned_data["end"],
                      creator = Student.objects.get(user=self._user))

        #event.start = self.cleaned_data["start"]
        #event.end = end = self.cleaned_data["end"]
        #event.creator = self._user

        event.save()

        studyGroup = self.cleaned_data["studyGroup"]
        studyGroup.event_set.add(event)

        #if commit:
        #    event.save()

        return event


