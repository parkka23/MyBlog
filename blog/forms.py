from django import forms

from .models import PostModel, Comment, Category
from django.utils.translation import gettext_lazy as _


class PostModelForm(forms.ModelForm):

    content = forms.CharField(widget=forms.Textarea(attrs={'rows': 4}), label=_('Content'))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=_("Select a category"), label=_('Category'))

    class Meta:
        model = PostModel
        fields = ('title', 'content', 'category')
        labels = {
            'title': _('Title'),

        }




class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title', 'content', 'category')
        labels = {
            'title': _('Title'),
            'content': _('Content'),
            'category': _('Category'),
        }


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        label=_('Content'), widget=forms.TextInput(attrs={'placeholder': _('Add comment here....')}))

    class Meta:
        model = Comment
        fields = ('content',)
