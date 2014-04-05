from django import forms
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

from .models import Post, Board, PostTag
from core.models import StudyGroup

class BoardForm(forms.ModelForm):
    name = forms.CharField(label="Board name")
    details = forms.CharField(label="Details")

    study_group = forms.ModelChoiceField(queryset=StudyGroup.objects.all(), required=True)

    class Meta:
        model = Board
        fields = ['name', 'details', 'study_group']

    def __init__(self, user=None, *args, **kwargs):
        self._user = user
        super(BoardForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        form = super(BoardForm, self).is_valid()
        #for f, error in self.errors.iteritems():
        #    if f != '__all_':
        #        self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    def save(self, commit=True):
        if not self._user:
            return None

        baord = BoardForm(name = self.cleaned_data["name"],
                          details = self.cleaned_data["details"],
                          creator = Student.objects.get(user=self._user))
        board.save()

        study_group = self.cleaned_data["study_group"]
        study_group.board_set.add(board)
        study_group.save()

        #if commit:
        #    group.save()

        return board

class PostForm(forms.ModelForm):
    name = forms.CharField(label="Post name")
    content = forms.CharField(widget=SummernoteWidget())

    
    board = forms.ModelChoiceField(queryset=Board.objects.all(), required=True)
    post_tag = forms.ModelMultipleChoiceField(queryset=PostTag.objects.all(), required=False)
 
    class Meta:
        model = Post
        fields = ['name', 'content', 'board', 'post_tag']

    def __init__(self, user=None, *args, **kwargs):
        self._user = user
        super(PostForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        form = super(PostForm, self).is_valid()
        #for f, error in self.errors.iteritems():
        #    if f != '__all_':
        #        self.fields[f].widget.attrs.update({'class': 'error', 'value': strip_tags(error)})
        return form

    def save(self, commit=True):
        if not self._user:
            return None

        post = PostForm(name = self.cleaned_data["name"],
                        content = self.cleaned_data["content"],
                        creator = Student.objects.get(user=self._user))
        post.save()

        for tag in self.cleaned_data["tag_set"]:
            post.tag_set.add(tag)

        post.save()

        #if commit:
        #    group.save()

        return post

