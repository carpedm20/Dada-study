from django import forms
from django.utils.html import strip_tags

from .models import StudyGroup, Tag
from account.models import Student

class StudyGroupForm(forms.ModelForm):
    name = forms.CharField(label="Group name")
    details = forms.CharField(label="Details")

    user_set = forms.ModelMultipleChoiceField(queryset=Student.objects.all())
    tag_set = forms.ModelMultipleChoiceField(queryset=Tag.objects.all())
 
    def is_valid(self):
        form = super(StudyGroupForm, self).is_valid()
        for f, error in self.errors.iteritems():
            if f != '__all_':
                self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form
 
    class Meta:
        model = StudyGroup
        fields = ['name', 'details', 'user_set', 'tag_set']

    def save(self, commit=True):
        group = StudyGroup(name = self.cleaned_data["name"],
                           details = self.cleaned_data["details"],
                           user_set = self.cleaned_data["user_set"],
                           tag_set = self.cleaned_data["tag_set"])

        if commit:
            group.save()

        return user_profile
