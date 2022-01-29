from django.views.generic import ListView, DetailView
from .models import Job

class JobList(ListView):
    model = Job


class JobDetailView(DetailView):
    model = Job