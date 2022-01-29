from django import forms
from job.models import Job


class ApplyForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    position_apply = forms.ModelChoiceField(Job.objects.all())
    resume_file = forms.FileField()
