from candidate.forms import ApplyForm
from django.views.generic.edit import FormView
from django.shortcuts import render
from candidate.models import Candidate
from django.shortcuts import redirect


def thankyou(request):
    return render(request, 'thankyou-for-apply.html')


def apply(request):
    context = {
        'form': ApplyForm
    }
    
    if request.method == 'POST':
        form = ApplyForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_candidate = Candidate(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                position_apply=data['position_apply']
                )
            new_candidate.save()
            return redirect('thankyou-for-apply')
    return render(request, 'apply.html', context)
