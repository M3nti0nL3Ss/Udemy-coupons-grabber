from django import forms
from django.contrib.auth import get_user_model
from comment.models import Comment

class RegisterForm(forms.Form):
    pass
class LoginForm(forms.Form):
    pass
class ContactForm(forms.Form):
    pass
class CommentForm(forms.ModelForm):

    body = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "class":"form-control",
                "placeholder":"Comment",
                "name":"comment",
                "rows":"2"}
                ),
                label="Your comment")
    class Meta:
        model = Comment
        fields = ["body"]

    def clean_bodytext(self):
        body = self.cleaned_data.get('body')
        if body:
            if not body.strip():
                raise forms.ValidationError("Error")
        return body
