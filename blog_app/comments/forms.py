from django import forms
from .models import Comment,BookComment,MovieComment

#博文评论
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']

#书评
class BookCommentForm(forms.ModelForm):
    class Meta:
        model = BookComment
        fields = ['name', 'email', 'url', 'text']
#影评
class MovieCommentForm(forms.ModelForm):
    class Meta:
        model = MovieComment
        fields = ['name', 'email', 'url', 'text']