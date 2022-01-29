from django.urls import path

from job.views import JobList, JobDetailView

urlpatterns = [
    path('', JobList.as_view() , name='jobs-index'),
    path('job/<int:pk>', JobDetailView.as_view(), name='job-detail'),
]