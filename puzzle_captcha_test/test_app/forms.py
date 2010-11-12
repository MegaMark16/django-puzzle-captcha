from django import forms
from test_app.models import Submission
from puzzle_captcha.fields import PuzzleCaptchaField

class SubmissionForm(forms.ModelForm):
    captcha = PuzzleCaptchaField()
    class Meta:
        model = Submission

        


