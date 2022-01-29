from django.urls import path
from candidate.views import thankyou, apply


urlpatterns = [
    path('apply', apply, name="apply-form"),
    path('thankyou', thankyou, name='thankyou-for-apply')
]