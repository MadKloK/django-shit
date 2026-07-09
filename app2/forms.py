from django.forms import ModelForm
from captcha.fields import CaptchaField
from app2.models import Comment


class CommentForm(ModelForm):
    captcha = CaptchaField()

    class Meta:
        model = Comment
        fields = ['name', 'email', 'subject', 'message']
