import random

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404

from test_app.models import Submission
from test_app.forms import SubmissionForm

def show_form(request):
    form = SubmissionForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse('Thank you for your feedback!')
    return render_to_response('test_app/test_form.html', { 'form': form, }, context_instance=RequestContext(request))

